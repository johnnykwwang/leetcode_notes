---
layout: post
title: "236: Lowest Common Ancestor of a Binary Tree"
date: "2019-06-04 19:57:25 -0700"
categories: [leetcode]
---

<p>Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.</p>

<!--more-->

<p>According to the <a href="https://en.wikipedia.org/wiki/Lowest_common_ancestor" target="_blank">definition of LCA on Wikipedia</a>: &ldquo;The lowest common ancestor is defined between two nodes p&nbsp;and q&nbsp;as the lowest node in T that has both p&nbsp;and q&nbsp;as descendants (where we allow <b>a node to be a descendant of itself</b>).&rdquo;</p>

<p>Given the following binary tree:&nbsp; root =&nbsp;[3,5,1,6,2,0,8,null,null,7,4]</p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarytree.png" style="width: 200px; height: 190px;" />
<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
<strong>Output:</strong> 3
<strong>Explanation: </strong>The LCA of nodes <code>5</code> and <code>1</code> is <code>3.</code>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
<strong>Output:</strong> 5
<strong>Explanation: </strong>The LCA of nodes <code>5</code> and <code>4</code> is <code>5</code>, since a node can be a descendant of itself according to the LCA definition.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>All of the nodes&#39; values will be unique.</li>
	<li>p and q are different and both values will&nbsp;exist in the binary tree.</li>
</ul>

# Solutions

This is a classic tree traversal problem that requires some detailed condition-checking.  Our algorithm goes like:

When DFS-ing the tree, we check how many target nodes `p` or `q` are in each subtree or is the root itself.
  * If there's 2 in left or 2 in right, then that subtree is passing the LCA up, so just return.
  * If it happens to be one each, or one plus root being another, then this root is the LCA.
  * Else just return the number of target target nodes we found.

```python
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        n, _ = self.dfs(root,p, q)
        return n
    
    def dfs(self, root, p, q):
        if not root:
            return None, 0
        
        l_n, l = self.dfs(root.left, p, q)
        r_n, r = self.dfs(root.right, p, q)
        
        c = 1 if (root==p) or (root==q) else 0
        
        if l==2 or r==2:
            return (l_n,2) if l==2 else (r_n,2)
        elif l+c==2 or r+c==2 or l+r==2:
            return root, 2     
        
        return None, c+l+r
```

---

# Related Problem: [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/)

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

## Solution:

This is even easier than the Binary Tree case, becuase the node is ordered in such way, it makes the traversal and finding much  easier.  We can eliminate a subtree everytime using the relation between `root.val`, `p.val` and `q.val`.

```python
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
    
        if p>q:
            p,q = q,p
                        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p,  q)
        
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
```





