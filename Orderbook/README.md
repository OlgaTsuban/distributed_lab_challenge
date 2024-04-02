# Order Book Implementation
## Introduction
<p>This project implements an order book for trading two assets: USD (quote asset) and UAH (base asset). Users can place orders to buy or sell UAH at specified prices in USD. The order book matches buy and sell orders based on their prices, allowing users to execute trades when a price match occurs.</p>

## Functionality
<ul>
<li>Order Placement: Users can place orders to buy or sell UAH. Each order specifies the user ID, amount of UAH, price in USD, and the side (buy or sell).</li>
<li>Order Matching: The order book matches buy and sell orders based on their prices. When the price of a sell order is less than or equal to the price of a buy order, a trade is executed.</li>
<li>Efficiency: The implementation uses data structures and algorithms optimized for efficiency, ensuring fast order matching even with a large number of orders. </li>
</ul>

## Implementation Details
<ul>
  <li>
    <strong>Data Structures:</strong>
    <ul>
      <li>
        The order book utilizes dictionaries to store buy and sell orders, with prices serving as keys. This allows for efficient access and manipulation of orders based on their prices.
        <ul>
          <li><code>Insert and delete in dictionaries:</code> <code>O(1)</code> on average, but can be <code>O(n)</code> in worst-case scenarios.</li>
          <li><code>Accessing elements in a Dictionary:</code> <code>O(1)</code></li>
          <li><code>Delete in Dictionary:</code> <code>O(1)</code></li>
        </ul>
      </li>
      <li>
        Additionally, heaps are employed to maintain the order of prices for efficient price matching and sorting.
        <ul>
          <li><code>Insert and delete in heaps:</code> <code>O(log n)</code></li>
          <li><code>Heapsort:</code> <code>O(n log n)</code></li>
        </ul>
      </li>
    </ul>
  </li>
  <li>
    <strong>Order Matching Algorithm:</strong> 
    The order book matches orders using a priority queue-based algorithm, which has a time complexity of <code>O(n log n)</code> for matching orders, where <em>n</em> is the number of orders in the order book.
  </li>
  <li>
    <strong>Validation:</strong> 
    Orders are validated to ensure that the amount and price are non-negative and that the side is either 0 (buy) or 1 (sell). This validation helps maintain the integrity of the order book data.
  </li>
</ul>

## Efficiency and Complexity Analysis
<p><strong>Time Complexity:</strong></p>
<ul>
  <li>Placing an order: <code>O(log n)</code>, where <em>n</em> is the number of orders in the order book.</li>
  <li>Matching orders: <code>O(n log n)</code>, where <em>n</em> is the number of orders in the order book.</li>
</ul>
<p><strong>Space Complexity:</strong></p>
<p><code>O(n)</code>, where <em>n</em> is the number of orders in the order book. This space is primarily used to store the order book data structures.</p>

## Duration of solving the task
- The task was completely solved in 2 hours and 56 minutes. </p>
    - Study the teory: 1 hour and 58 minutes
    - Implementation: 58 minutes