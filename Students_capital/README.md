# Student capital

## Introduction
<p>
This command-line interface (CLI) application helps students maximize their capital by buying, fixing, and reselling laptops during the summer break.
The application allows users to specify the number of laptops to buy, the initial capital, and the gains and prices of each laptop. It then calculates the maximum amount of money that can be made by buying the specified number of laptops with the given initial capital.
</p>

## Efficiency Analysis
**Storage:** 
The algorithm uses additional memory to store the list of laptops, which is O(K), where K is the number of laptops available.

- **Creating the List of Laptops:** 
  - Creating the list of laptops involves iterating through the gains and prices arrays once, resulting in a time complexity of O(K), where K is the number of laptops available.
- **Heapification:** 
  - Converting the list into a max heap using `heapify` takes O(K) time.
- **Iterating through Laptops:** 
  - The main loop iterates through the laptops once, or until N laptops are bought. In the worst case, it iterates through all K laptops, resulting in a time complexity of O(KlogK) for popping each laptop from the heap.
- **Overall Time Complexity:** 
  - The overall time complexity is dominated by the sorting step, which is O(KlogK).

## Usage
To use the program, enter data (main.py) .
To run the program : <code>python3 main.py</code>
Also is possible to run unit tests: <code>python3 test.py</code>

## Duration of solving the task
- The task was completely solved in 46 minutes. 
    - Study the teory: 8 minutes
    - Implementation: 38 minutes

## Conclusion
The Laptop Reselling CLI Application provides a convenient tool for students looking to maximize their capital during the summer break by buying, fixing, and reselling laptops. By inputting the number of laptops to consider, initial capital, gains array, and prices array, users can efficiently determine the maximum amount of money they can earn after buying a specified number of laptops with the given initial capital.

The application employs an efficient algorithm utilizing the heapq module in Python to optimize the selection of laptops with the highest gains while considering budget constraints. 