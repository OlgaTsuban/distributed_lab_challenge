# Hitler crawler

## Introduction
<p>
You may know a joke that says each dialog will end with a discussion about Hitler. Let’s check it on Wikipedia. You should create a program that receives a Wikipedia article and scans it for other Wikipedia links, opens them, and scans for links until it finds the link to the Hitler Wikipedia page.
</p>

## Efficiency Analysis
**Storage:** 
The program uses sets to store visited URLs, ensuring that each URL is visited only once.
For faster search was used parallelism(Threads)

## Time Complexity
The time complexity depends on the number of hops required to find the Hitler page. In the worst case, where the page is not found within 6 hops, the time complexity can be considered linear with respect to the number of links visited.


## Memory Storage
The memory storage requirements are primarily determined by the number of URLs visited and the depth of the search. As the program progresses, it accumulates visited URLs in memory until the search is complete.


## Usage
To use the program, simply run it and provide a Wikipedia URL to start the search from.
To run the program : <code>python3 main.py</code>

## Duration of solving the task
- The task was completely solved in 2 hours and 56 minutes. </p>
    - Study the teory: 1 hour and 58 minutes
    - Implementation: 58 minutes

## Conclusion
This program provides a straightforward solution to the task of searching for the Wikipedia page on Adolf Hitler. By efficiently traversing Wikipedia articles and following links, it can find the desired page within a reasonable number of hops.