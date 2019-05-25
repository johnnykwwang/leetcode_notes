---
layout: post
title: "207: Course Schedule"
date: "2019-05-22 22:56:39 -0400"
categories: [leetcode]
---

<p>There are a total of <i>n</i> courses you have to take, labeled from <code>0</code> to <code>n-1</code>.</p>

<p>Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: <code>[0,1]</code></p>

<p>Given the total number of courses and a list of prerequisite <b>pairs</b>, is it possible for you to finish all courses?</p>

<!--more-->

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 2, [[1,0]]
<strong>Output: </strong>true
<strong>Explanation:</strong>&nbsp;There are a total of 2 courses to take.
&nbsp;            To take course 1 you should have finished course 0. So it is possible.</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 2, [[1,0],[0,1]]
<strong>Output: </strong>false
<strong>Explanation:</strong>&nbsp;There are a total of 2 courses to take.
&nbsp;            To take course 1 you should have finished course 0, and to take course 0 you should
&nbsp;            also have finished course 1. So it is impossible.
</pre>

<p><b>Note:</b></p>

<ol>
	<li>The input prerequisites is a graph represented by <b>a list of edges</b>, not adjacency matrices. Read more about <a href="https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs" target="_blank">how a graph is represented</a>.</li>
	<li>You may assume that there are no duplicate edges in the input prerequisites.</li>
</ol>

# Solutions

Classic topological sort problem!  For topological sorting with BFS, the general steps are:

* Calculate the in-degree of nodes
* set initial queue as nodes with 0 in-degree
* while queue nonempty, pop a node 
  * find all outgoing edges from the node, remove all edges and decrement all nodes indegree
  * if in this process, any nodes' in-degree becomes 0, add to queue

In this problem, we only need to know if the topological sort exists.  We can do this by keeping a record of the sorting and compare its length to the total number of nodes.

```python
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        indeg = { i:0 for i in range(numCourses) }
        out = { i:[] for i in range(numCourses) }

        for a,b in prerequisites: # b-->a
            indeg[a] += 1
            out[b].append(a)

        q = collections.deque([a for a in indeg.keys() if indeg[a]==0 ])
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for out_node in out[node]:
                indeg[out_node]-=1
                if indeg[out_node]==0:
                    q.append(out_node)

        return if len(ans)==numCourses
```

Changing the last line to `return ans if len(ans)==numCourses else []` would give the answer to [210. Course Schedule II
](https://leetcode.com/problems/course-schedule-ii/description/), which is asking to give any valid topological sorting.


