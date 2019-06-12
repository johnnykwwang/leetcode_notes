---
layout: post
title: "417: Pacific Atlantic Water Flow"
date: "2019-06-11 21:08:49 -0700"
categories: [leetcode]
---

<p>Given an <code>m x n</code> matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.</p>

<p>Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.</p>

<p>Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.</p>

<!--more-->

<p><b>Note:</b><br />
<ol>
<li>The order of returned grid coordinates does not matter.</li>
<li>Both <i>m</i> and <i>n</i> are less than 150.</li>
</ol>
</p>
<p><b>Example:</b>
<pre>
Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
</pre>
</p>

# Solutions

This is another 2D-grid traversal problem.  From our experiences dealing with this kind of problem, BFS-by-layer is an easier approach.  So the approach is :

1. Compute the reachable water for Pacific, via tracing back the water flow.  Starting from ocean, finding blocks with larger or equal height.  Record the reachable blocks.
2. Do the same for Atlantic.
3. Compute intersection of their reachable blocks.

```python
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []
        h, w = len(matrix), len(matrix[0])
        self.h, self.w = h, w
        pac_starts = set([ (0,x) for x in range(w) ] + [(y,0) for y in range(h)])
        atl_starts = set([ (h-1,x) for x in range(w) ] + [(y,w-1) for y in range(h)])
        
        return self.reachable(matrix, pac_starts, set(pac_starts), 'pac') & self.reachable(matrix, atl_starts, set(atl_starts), 'atl')
    
    def reachable(self, matrix, layer, visited, direction):
        while layer:
            new_layer = []
            for y,x in layer:
                neighbors = [ (y+1,x), (y,x+1), (y, x-1), (y-1,x) ]
                for ny,nx in neighbors:
                    if 0<=ny<self.h and 0<=nx<self.w and matrix[ny][nx] >= matrix[y][x] and (ny,nx) not in visited:
                        new_layer.append( (ny,nx) )
                        visited.add( (ny,nx) )
            layer = new_layer
        return visited
```
