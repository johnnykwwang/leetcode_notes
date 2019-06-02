---
layout: post
title: "463: Island Perimeter"
date: "2019-06-01 19:29:35 -0700"
categories: [leetcode]
---


<p>You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.</p>

<p>Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).</p>

<p>The island doesn&#39;t have &quot;lakes&quot; (water inside that isn&#39;t connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don&#39;t exceed 100. Determine the perimeter of the island.</p>

<!--more-->

<p><b>Example:</b></p>

<pre>
<strong>Input:</strong>
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

<strong>Output:</strong> 16

<strong>Explanation:</strong> The perimeter is the 16 yellow stripes in the image below:

<img src="https://assets.leetcode.com/uploads/2018/10/12/island.png" style="width: 221px; height: 213px;" />
</pre>

# Solutions

This is another 2D-map traversal problem.  The key to this problem is to be very careful when determining how to add next node to the queue.  Basically, we can either:
* First determine the neighbor's condition then add to queue
* Or, add to queue regardless and then check condition

In this implementation, I think it's more expressive to use the first method.  So the **BFS** would look like:

1. Find the island
2. Add 4 edges when found a block
3. Minus 2 edges when found a connecting block.

```python
from collections import deque

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        total = 0

        if not grid or not grid[0]:
            return 0

        m_y, n_x = len(grid), len(grid[0])

        for y in range(m_y):
            for x in range(n_x):
                if grid[y][x]==1:
                    return self.bfs(grid, x, y)
        return total

    def bfs(self, grid, x, y):
        q = deque([(x,y)])
        area = 0
        while q:
            x,y = q.popleft()
            if grid[y][x] == 1:
                grid[y][x] = -1
                area += 4
                if len(grid[y])>=x+2:
                    if grid[y][x+1] == 1:
                        q.append( (x+1, y) )
                    elif grid[y][x+1] == -1:
                        area -=2
                if len(grid)>=y+2:
                    if grid[y+1][x] == 1:
                        q.append( (x, y+1) )
                    elif grid[y+1][x] == -1:
                        area -=2
                if x-1>=0:
                    if grid[y][x-1] == 1:
                        q.append( (x-1, y))
                    elif grid[y][x-1] == -1:
                        area -=2
                if y-1>=0:
                    if grid[y-1][x] == 1:
                        q.append( (x, y-1))
                    elif grid[y-1][x] == -1:
                        area -=2

        return area
```



