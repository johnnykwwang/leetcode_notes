---
layout: post
title: "200: Number of Islands"
date: "2019-05-21 13:11:18 -0400"
categories: [leetcode]
---

<p>Given a 2d grid map of <code>&#39;1&#39;</code>s (land) and <code>&#39;0&#39;</code>s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.</p>

<!--more-->

<p><b>Example 1:</b></p>

<pre>
<strong>Input:</strong>
11110
11010
11000
00000

<strong>Output:</strong>&nbsp;1
</pre>

<p><b>Example 2:</b></p>

<pre>
<strong>Input:</strong>
11000
11000
00100
00011

<strong>Output: </strong>3
</pre>

# Solutions

This problem is solvable via either BFS and DFS.  Basically, the idea is to traverse the whole map, and when we encounter any part of the island, we **greedily** find the connecting parts of this island and remove it from the map.

## BFS & DFS (Iterative)

Writing a separate BFS/DFS function just makes the code more readable.  Code is almost identical for BFS/DFS.  Changing `deque` to `[]` and `popleft()` to `pop()` and it's DFS.

```python
from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        total = 0

        if not grid or not grid[0]:
            return 0

        m_y, n_x = len(grid), len(grid[0])

        for y in range(m_y):
            for x in range(n_x):
                if grid[y][x]=='1':
                    self.bfs(grid, x, y)
                    total += 1
        return total

    def bfs(self, grid, x, y):
        q = deque([(x,y)])
        while q:
            x,y = q.popleft()
            if grid[y][x] == '1':
                grid[y][x] = '0'
                if len(grid[y])>=x+2:
                    q.append( (x+1, y) )
                if len(grid)>=y+2:
                    q.append( (x, y+1) )
                if x-1>=0:
                    q.append( (x-1, y))
                if y-1>=0:
                    q.append( (x, y-1))
```

