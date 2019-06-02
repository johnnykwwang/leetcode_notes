---
layout: post
title: "124: Binary Tree Maximum Path Sum"
date: "2019-06-01 17:10:50 -0700"
categories: [leetcode]
---

<p>Given a <strong>non-empty</strong> binary tree, find the maximum path sum.</p>

<p>For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain <strong>at least one node</strong> and does not need to go through the root.</p>

<!--more-->

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [1,2,3]

       <strong>1</strong>
      <strong>/ \</strong>
     <strong>2</strong>   <strong>3</strong>

<strong>Output:</strong> 6
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [-10,9,20,null,null,15,7]

&nbsp;  -10
&nbsp; &nbsp;/ \
&nbsp; 9 &nbsp;<strong>20</strong>
&nbsp; &nbsp; <strong>/ &nbsp;\</strong>
&nbsp; &nbsp;<strong>15 &nbsp; 7</strong>

<strong>Output:</strong> 42
</pre>

## Solutions

This is a hard problem with a very simple solution.  The spirit behind this problem is to correctly identify **how to recursively traverse a graph** and update a global maximum.

So the way we can do recurive is, we define a `maxPath()` function that calculates the maximum sum **below** the given `root`.  But along the recursive calls, we also examine the sum that takes both the left and right of the current node, and updates the global maximum.

```python

class Solution(object):

    cur_max = - (2**64)

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPath(root)
        return self.cur_max

    def maxPath(self, root):
        if not root:
            return None
        l = self.maxPath(root.left)
        r = self.maxPath(root.right)
        l = 0 if l is None else (l if l>0 else 0)
        r = 0 if r is None else (r if r>0 else 0)
        self.cur_max = max( l+root.val+r, self.cur_max )
        return max(l,r) + root.val

```


