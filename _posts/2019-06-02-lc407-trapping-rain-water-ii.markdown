---
layout: post
title: "407: Trapping Rain Water II"
date: "2019-06-02 21:00:37 -0700"
categories: [leetcode]
---

<p>Given an <code>m x n</code> matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.</p>
<p><img src="https://assets.leetcode.com/uploads/2018/10/13/rainwater_empty.png" style="width: 100%; max-width: 500px;" /></p>

<!--more-->

<p><b>Note:</b></p>

<p>Both <i>m</i> and <i>n</i> are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.</p>

<p><b>Example:</b></p>

<pre>
Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.
</pre>


<p>The above image represents the elevation map <code>[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]</code> before the rain.</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/13/rainwater_fill.png" style="width: 100%; max-width: 500px;" /></p>

<p>After the rain, water is trapped between the blocks. The total volume of water trapped is 4.</p>

# Solutions

This is the kind of problem that I don't think will be reasonable to come up with optimal solution and a bug-free code during an interview.  But still, we can learn a lot of techniques from this problem.

The general idea is, the height of water above a certain cell can hold, is determined by the minimum of the surround "border cells".  

So we can solve this problem by :

1. Initialize a priority queue with all the border cells.  This queue pops the minimum height cell every time. 
2. In each iteration, pop a cell and let it **flow** to each neighbor, and determine if the water fills up in the neighbor cell. If it does flow, the water becomes solid and can be viewed as another **border cell** that can block water, so we push it to the queue.
3. Repeat this process until no more **border cells**.

```python

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0
        h, w = len(heightMap), len(heightMap[0])

        import heapq
        heap = []
        visited = [[False] * w for _ in range(h)]

        for i in range(h):
            for j in range(w):
                if i==0 or j==0 or i==h-1 or j==w-1:
                    heapq.heappush(heap, ( heightMap[i][j],i,j )  )
                    visited[i][j] = True

        total = 0

        while heap:
            height, i, j = heapq.heappop(heap)
            for ni, nj in [ (i+1,j), (i-1,j), (i,j+1), (i,j-1) ]:
                if 0 <= ni < h and 0<= nj < w and not visited[ni][nj]:
                    total += max(0, height - heightMap[ni][nj])
                    new_h = max(heightMap[ni][nj], height)
                    heapq.heappush(heap, ( new_h , ni,nj )   )
                    visited[ni][nj] = True
        return total
```


