---
layout: post
title: "130: Surrounded Regions"
date: "2019-05-23 18:47:10 -0400"
categories: [leetcode]
---

<p>Given a 2D board containing <code>&#39;X&#39;</code> and <code>&#39;O&#39;</code> (<strong>the letter O</strong>), capture all regions surrounded by <code>&#39;X&#39;</code>.</p>

<p>A region is captured by flipping all <code>&#39;O&#39;</code>s into <code>&#39;X&#39;</code>s in that surrounded region.</p>

<!--more-->

<p><strong>Example:</strong></p>

<pre>
X X X X
X O O X
X X O X
X O X X
</pre>

<p>After running your function, the board should be:</p>

<pre>
X X X X
X X X X
X X X X
X O X X
</pre>

<p><strong>Explanation:</strong></p>

<p>Surrounded regions shouldn&rsquo;t be on the border, which means that any <code>&#39;O&#39;</code>&nbsp;on the border of the board are not flipped to <code>&#39;X&#39;</code>. Any <code>&#39;O&#39;</code>&nbsp;that is not on the border and it is not connected to an <code>&#39;O&#39;</code>&nbsp;on the border will be flipped to <code>&#39;X&#39;</code>. Two cells are connected if they are adjacent cells connected horizontally or vertically.</p>

# Solutions

In this problem, we basically:

1. Traverse all the `O`-components connecting to a boarder, and flip it to `B`
2. Flip every `B` to `O` and everything else to `X`

```python
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        if board == [] :
            return
        h, w = len(board), len(board[0])

        border = [ (0,x) for x in range(w) ] + \
                 [ (h-1,x) for x in range(w) ] + \
                 [ (y,0) for y in range(h) ] + \
                 [ (y,w-1) for y in range(h) ]

        border = set(border)

        for y,x in border:
            if board[y][x] == 'O':
                self.flip_components(board,y,x)

        for y in range(h):
            for x in range(w):
                if board[y][x] == 'B':
                    board[y][x] = 'O'
                else:
                    board[y][x] = 'X'

    def flip_components(self, board, y,x):
        h, w = len(board), len(board[0])
        q = collections.deque([(y,x)])
        while q:
            ny, nx = q.popleft()
            board[ny][nx] = 'B'
            if ny-1>=0 and (ny-1,nx) and board[ny-1][nx] == 'O':
                q.append((ny-1,nx))
            if ny+1<h and (ny+1,nx) and board[ny+1][nx] == 'O':
                q.append((ny+1,nx))
            if nx-1>=0 and (ny,nx-1) and board[ny][nx-1] == 'O':
                q.append((ny,nx-1))
            if nx+1<w and (ny,nx+1) and board[ny][nx+1] == 'O':
                q.append((ny,nx+1))
```

# Techniques in 2D-map Related Problems 

1. When creating new data structure to store information, think about **storing it on the 2D-map itself.**
  * In this problem, we can store the intermediate `B` token directly in the map, just remember to flip it back.
2. When doing operations on whole map, think about **equivalent sequence of operations**.
  * In this problem, we can also flip the inside-`O`s directly, but if the map consists mostly `O`s connecting to the border, this operation would waste a lot of time.


