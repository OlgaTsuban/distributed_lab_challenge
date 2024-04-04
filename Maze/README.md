# Maze Implementation
## Introduction
<p>This console program generates 2D mazes with various types of cells, including entrance, exit, road, wall.</p>

## Usage
<p>To use the maze generator, simply run the console program and provide the size of the maze as input. The program will then generate a maze and display it in the console. </p>

## Cell Types
<ul>
<li>Entrance: There is only one entrance, which must be located on some outer side of the maze.</li>
<li>Exit: There is only one exit, which must be located on some outer side of the maze.</li>
<li>Road: A cell that the player can pass through.</li>
<li>Wall: A cell that the player cannot pass through.</li>
</ul>

## Implementation Details
<ul>
  <li>
    <strong>Creation algorithm:</strong>
    <ul>
      <li>
        The maze is represented as a 2D grid filled with ones and zeros, where:

        <ul>
          <li><code>1 represents a wall (impassable)</code> </li>
          <li><code>0 represents a road (passable).</code> </li>
        </ul>
        depth-first search (DFS) algorithm
      </li>
      <li>
        Algorithm : <code>Delete in Dictionary:</code> <code>time complexity of DFS is O(V + E)</code></li>.
      </li>
    </ul>
  </li>
  <li>
    <strong>Searching Algorithm:</strong> 
    I use BFS algorithm to find the shortest path<code>Time complexity is O(V + E)</code>.
  </li>
  
</ul>

## Visualization

  <li>Uses Matplotlib's <code>imshow</code> function to display the maze grid and way to the finish in colors.</li>

## Duration of solving the task
- The task was completely solved in 5 hours and 40 minutes. </p>
    - Study the teory: 2 hours and 20 minutes
    - Implementation: 3 hours 30 minutes
