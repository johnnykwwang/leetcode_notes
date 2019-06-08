---
layout: post
title: "039: Combination Sum"
date: "2019-06-07 22:37:32 -0700"
categories: [leetcode]
---

<p>Given a <strong>set</strong> of candidate numbers (<code>candidates</code>) <strong>(without duplicates)</strong> and a target number (<code>target</code>), find all unique combinations in <code>candidates</code>&nbsp;where the candidate numbers sums to <code>target</code>.</p>

<p>The <strong>same</strong> repeated number may be chosen from <code>candidates</code>&nbsp;unlimited number of times.</p>

<!--more-->

<p><strong>Note:</strong></p>

<ul>
	<li>All numbers (including <code>target</code>) will be positive integers.</li>
	<li>The solution set must not contain duplicate combinations.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> candidates = <code>[2,3,6,7], </code>target = <code>7</code>,
<strong>A solution set is:</strong>
[
  [7],
  [2,2,3]
]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2,3,5]<code>, </code>target = 8,
<strong>A solution set is:</strong>
[
&nbsp; [2,2,2,2],
&nbsp; [2,3,3],
&nbsp; [3,5]
]
</pre>

# Solutions

This is a classic combination problem.  The way to first understand this is, we can think of traversing a tree, each node with all the candidates as children.  So  by traversing down, whenever we found a path that sums to `target`, we can return that path.

```python
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.ans = []
        self.dfs([], 0, 0, candidates, target)
        return self.ans
        
    def dfs(self, path, cur_sum, i, candidates, target):
        if cur_sum > target:
            return
        if cur_sum == target:
            self.ans.append(path)
            return
        for j, c in enumerate(candidates[i:]):
            self.dfs(path+[c], cur_sum+c, i+j, candidates,target)
```

