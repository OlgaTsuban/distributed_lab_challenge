import csv

def read_file(filename:str) -> list:
    """
    Read a CSV file and return a list of lists.
    Args:
    - filename (str): The name of the CSV file to be read.
    Returns:
    - data: A list of lists representing the data in the CSV file.
    """
    data = []
    with open(filename, 'r') as f:
        csv_reader = csv.reader(f, delimiter=';')
        header = next(csv_reader)
        for row in csv_reader:
            data.append(row)
    print(f"header {header}")
    return data

def process_data(file_list:list) -> dict:
    """
    Process the data from the input file list and generate a dictionary representing
    the pages visited by each user.
    Args:
    - file_list (list): A list of tuples representing the data from the CSV files.
                        Each tuple contains user_id, product_id, and timestamp.
    Returns:
    - dict: A dictionary where keys are user IDs and values are sets containing
            the product IDs visited by each user.
    """
    pages = {}
    for user_id, product_id, _ in file_list:
        pages.setdefault(user_id, set()).add(product_id)
    return pages


def some_pages_on_both_days(data1: dict, data2: dict) -> None:
    """
    Print the users who visited some pages on both days.
    Args:
    - data1 (dict): Dictionary representing pages visited by users on the first day.
    - data2 (dict): Dictionary representing pages visited by users on the second day.
    Returns:
    - None
    """
    common_user_ids = set(data1.keys()) & set(data2.keys())
    for user_id in common_user_ids:
        common_pages = data1[user_id] & data2[user_id]
        if common_pages:
            print(f"User {user_id} visited the following pages on both days: {common_pages}")


def different_pages_on_both_days(data1:dict, data2:dict) -> set:
    """
    Find users who visited different pages on both days.
    Args:
    - data1 (dict): Dictionary representing pages visited by users on the first day.
    - data2 (dict): Dictionary representing pages visited by users on the second day.
    Returns:
    - set: Set of user IDs who visited different pages on both days.
    """
    users = set(data1.keys()) & set(data2.keys()) 

    different_pages_users = set()
    for user_id in users:
        if data2[user_id] - data1[user_id]:
            different_pages_users.add(user_id)

    return different_pages_users


def find_users(data1:str, data2:str) -> None:
    """
    Find users who visited some pages on 2 days and those who visited different pages on 2 days.
    Args:
    - data1 (str): File path for the CSV file representing pages visited by users on the first day.
    - data2 (str): File path for the CSV file representing pages visited by users on the second day.
    Returns:
    - None
    """
    day1 = read_file(data1)
    day2 = read_file(data2)
    print("--------------Visited some pages on both days--------------")
    some_pages_on_both_days(process_data(day1), process_data(day2))

    print("--------------Visited different pages on both days---------")
    print(different_pages_on_both_days(process_data(day1), process_data(day2)))



if __name__ == '__main__':
    find_users('day1.csv', 'day2.csv')
    