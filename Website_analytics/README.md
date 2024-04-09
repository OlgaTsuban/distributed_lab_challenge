# Website analytics Implementation
## Introduction
<p>The provided solution is designed to efficiently find users who visited some pages on both days and those who visited different pages on both days based on the data from two CSV files representing user activities. The solution ensures efficient storage and execution time by utilizing dictionaries to represent user-page mappings and sets for fast intersection and difference operations.</p>

## Efficiency Analysis

**Storage:** The script uses dictionaries to store user-page data, which provides efficient access to user information based on user IDs. Sets are used to store page IDs, ensuring uniqueness and efficient intersection and difference operations.

## Time Complexity
- Reading CSV files: O(N), where N is the number of entries in each CSV file.
- Processing data: O(N), where N is the number of entries in the combined data from both days.
- Finding users who visited some pages on both days: O(M), where M is the number of common users between the two days.
- Finding users who visited different pages on both days: O(M), where M is the number of common users between the two days.

## Memory Storage
1. **Data Storage:** The data is stored in dictionaries and sets, which have efficient lookup and insertion operations.
2. **Optimized Operations:** The solution optimizes memory usage by using sets to store unique page visits for each user, reducing redundancy and improving efficiency.

## Usage
run funtion : <code>
<strong>Command:</strong> python3 main.py
if __name__ == '__main__':
    find_users('day1.csv', 'day2.csv')
</code>

## Duration of solving the task
- The task was completely solved in 1 hour and 23 minutes. </p>
    - Study the teory: 39 minutes
    - Implementation: 44 minutes

## Conclusion
The solution efficiently processes and analyzes user activity data from two CSV files, ensuring optimal storage and execution time. By leveraging dictionaries and sets, the solution minimizes redundant computations and efficiently identifies users meeting the specified criteria. Overall, the solution is well-optimized and suitable for handling large datasets with minimal resource consumption.