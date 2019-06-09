---
layout: post
title: "079: Word Search"
date: "2019-06-09 13:36:18 -0700"
categories: [leetcode]
---


<p>Given a 2D board and a word, find if the word exists in the grid.</p>

<p>The word can be constructed from letters of sequentially adjacent cell, where &quot;adjacent&quot; cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.</p>

<!--more-->

<p><strong>Example:</strong></p>

<pre>
board =
[
  [&#39;A&#39;,&#39;B&#39;,&#39;C&#39;,&#39;E&#39;],
  [&#39;S&#39;,&#39;F&#39;,&#39;C&#39;,&#39;S&#39;],
  [&#39;A&#39;,&#39;D&#39;,&#39;E&#39;,&#39;E&#39;]
]

Given word = &quot;<strong>ABCCED</strong>&quot;, return <strong>true</strong>.
Given word = &quot;<strong>SEE</strong>&quot;, return <strong>true</strong>.
Given word = &quot;<strong>ABCB</strong>&quot;, return <strong>false</strong>.
</pre>

# Solutions

This is another 2D-map style DFS problem that requires recording the path taken.  Here, the point is to not traverse to the path that already taken.  So we have 2 approaches:
* Maintain a set of coordinates that the current traversal already taken
* Along the traversal, change the board to `None`.  After exploring, change it back.

We choose the second method because of lower memory usage.  Then it's just a simple recursive DFS:

```python
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        h,w = len(board), len(board[0])
        self.h, self.w = h, w

        for y in range(h):
            for x in range(w):
                if self.dfs(board,y,x,word,0):
                    return True

    def dfs(self, board,y, x, word, i):
        if board[y][x] == word[i]:
            if i==len(word)-1:
                return True
            board[y][x] = None
            for ny,nx in [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]:
                if ny>=0 and nx>=0 and ny<self.h and nx<self.w:
                    r = self.dfs(board, ny,nx, word, i+1)
                    if r:
                        board[y][x] = word[i]
                        return True
            board[y][x] = word[i]
        return False
```

