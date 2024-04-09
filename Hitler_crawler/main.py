import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin
import threading

# -------------------------------Without parallelism-------------------------------
def get_links(url:str):
    """
    Function to retrieve all links (URLs) from a given webpage URL.
    Parameters:
    - url: The URL of the webpage to retrieve links from.
    Returns:
    - A list of URLs found on the webpage, filtered to include only Wikipedia links.
        Each URL is converted to an absolute URL using urljoin.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', href=True)
    return [urljoin(url, link['href']) for link in links if is_wikipedia_link(link['href'])]

def is_wikipedia_link(link):
    """
    The is_wikipedia_link function checks if a link is a valid Wikipedia article.
        It does this by checking that the link starts with /wiki/ and doesn't start with any of the following:
            - /wiki/File:
            - /wiki/Template:
            - /wiki/Category: 
            - /wiki/Special: 
            - /wiki/Help: 
            - wiki/Portal:/    
        Or end with '.svg' and '.png'
    Parameters link: Check if the link is a wikipedia link
    Returns: True if the link is a wikipedia article, and false otherwise
    """
    return link.startswith('/wiki/') and not link.startswith('/wiki/File:') and not link.startswith('/wiki/Template:') \
           and not link.startswith('/wiki/Category:') and not link.startswith('/wiki/Special:') \
           and not link.startswith('/wiki/Help:') and not link.startswith('/wiki/Portal:') \
           and not link.startswith('/wiki/Wikipedia:') and not link.startswith('/wiki/Template_talk:')\
           and not link.endswith('.svg') and not link.endswith('.png') 

def match_hitler_link(link:str, basic_link:str, current_link:str)->bool:
    """
    The match_hitler_link function takes in a link, the basic_link and current_link.
    It checks if the link ends with /wiki/Adolf_Hitler. If it does, then it prints out 
    the full path to that page and returns True. Otherwise, it returns False.
    
    :param link: Check if the link ends with &quot;/wiki/adolf_hitler&quot;
    :param basic_link: Store the basic link of wikipedia
    :param current_link: Store the current link
    :return: True if the link ends with /wiki/adolf_hitler, and false otherwise
    """
    if link.endswith('/wiki/Adolf_Hitler'):
            print(f"Hitler page found at: {basic_link} + {current_link} + {link}")
            return True
    return False


def search_hitler_page(start_url, max_hops=6):
    """
    The search_hitler_page function takes a starting URL and an optional maximum number of hops.
    It then searches for the first page that contains /wiki/Adolf_Hitler; (case-insensitive).
    If it finds such a page, it returns its URL. If not, it returns None.
    
    :param start_url: Set the starting point for the search
    :param max_hops: Limit the number of links we can follow before giving up
    :return: None
    """
    visited = set()
    visited.add(start_url)
    urls_to_visit = [(start_url, 0)]

    while urls_to_visit:
        current_url, hops = urls_to_visit.pop(0)
        print("Current URL:", current_url)
        print(" hops:", hops)
        if hops > max_hops:
            print("Hitler not found within {} hops.".format(max_hops))
            return

        links = get_links(current_url) 
        for link in links:
            if link not in visited:
                if match_hitler_link(link, start_url,current_url):
                    return
                
                visited.add(link)
                hops += 1 
                urls_to_visit.append((link, hops))
    print("Hitler not found.")

# -------------------------------Using the parallelism-------------------------------

stop_flag = threading.Event() # flag to indicate a stop event for a thread
def process_link(link:str, basic_link:str, current_link:str, visited:list):
    """
    The process_link function takes in a link, the basic_link (the original url), 
    the current_link (the page we are currently on), and a list of visited links. 
    It checks if the stop flag is set, and if it is not then it checks to see if the link has been visited before. 
    If it hasn't been visited before then we check to see if this link matches our hitler url. If so, we set our stop flag and return True; otherwise, we add this new link to our list of visited links.
    
    :param link: Store the link that is being processed
    :param basic_link: Determine if the link is a relative or absolute path
    :param current_link: Keep track of the current link that is being processed
    :param visited: Store all the links that have been visited
    :return: True if the link is a hitler link, false otherwise
    """
    if stop_flag.is_set():
        return
    if link not in visited:
        if match_hitler_link(link, basic_link, current_link):
            stop_flag.set()
            return True 
        visited.add(link)
        return True

def search_hitler_page_thread(start_url, max_hops=6):
    """
    The search_hitler_page_thread function takes a starting URL and an optional max_hops parameter.
    It then searches the page at that URL for links to other pages, and visits those pages in turn.
    If it finds a link to the Wikipedia page on Adolf Hitler within 6 hops
    For more efficient search use the threads.
    :param start_url: Determine if the link is a relative or absolute url
    :param max_hops: Limit the number of links to follow
    :return: None
    """
    visited = set()
    visited.add(start_url)
    urls_to_visit = [(start_url, 0)]

    with ThreadPoolExecutor(max_workers=5) as executor: 
        while urls_to_visit:
            current_url, hops = urls_to_visit.pop(0)
            print("Current URL:", current_url)
            print(" hops:", hops)
            if hops > max_hops:
                print("Hitler not found within {} hops.".format(max_hops))
                return

            links = get_links(current_url)
            for link in links:
                if executor.submit(process_link, link, start_url, current_url, visited):
                    hops += 1
                    urls_to_visit.append((link, hops ))
                    if stop_flag.is_set():
                            return
                
    print("Hitler not found.")

if __name__ == "__main__":
    # Test link with result: https://en.wikipedia.org/wiki/Nazi_Germany
    # Test link without result: https://en.wikipedia.org/wiki/Apple_Watch

    start_url = input("Enter the Wikipedia URL to start from: ") 
    #search_hitler_page(start_url) # search without threads
    search_hitler_page_thread(start_url) # search with threads
