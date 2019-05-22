---
layout: post
title: "101: Symmetric Tree"
date: "2019-05-22 00:09:13 -0400"
categories: [leetcode]
---

<p>Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).</p>

<!--more-->

<p>For example, this binary tree <code>[1,2,2,3,4,4,3]</code> is symmetric:</p>

<pre>
    1
   / \
  2   2
 / \ / \
3  4 4  3
</pre>


<p>But the following <code>[1,2,2,null,3,null,3]</code> is not:</p>

<pre>
    1
   / \
  2   2
   \   \
   3    3
</pre>


<p><b>Note:</b><br />
Bonus points if you could solve it both recursively and iteratively.</p>

# Solutions

## BFS
This problem is solvable via simply BFS-by-level, storing each level's value and see if the value is identical from left and right.

```python
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        level = [root]
        while level:
            next_level = []
            level_val = [ node.val if node else None for node in level]
            if level_val != level_val[::-1]:
                return False
            for node in level:
                if node:
                    next_level.append(node.left)
                    next_level.append(node.right)

            level = next_level
        return True
```

## DFS( Recursive )

This is also very easily solved by recursive DFS.  Notice that in order for any tree in a node to be symmetric, it means that:

* `node.left.val` equals `node.right.val`
* `node.left.right` tree is symmetric to `node.right.left` tree
* `node.right.left` tree is symmetric to `node.left.right` tree

```python
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isSym(root.left, root.right)

    def isSym(self, r1, r2):
        if r1 and r2:
            return r1.val == r2.val and self.isSym(r1.left,r2.right) and self.isSym(r1.right,r2.left)
        elif r1 is None and r2 is None:
                return True
        else:
            return False
```



