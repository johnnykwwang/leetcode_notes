---
layout: post
title: "133: Clone Graph"
date: "2019-05-22 20:46:34 -0400"
categories: [leetcode]
---


<p>Given&nbsp;a reference of a node in a&nbsp;<strong><a href="https://en.wikipedia.org/wiki/Connectivity_(graph_theory)#Connected_graph" target="_blank">connected</a></strong>&nbsp;undirected graph, return a <a href="https://en.wikipedia.org/wiki/Object_copying#Deep_copy" target="_blank"><strong>deep copy</strong></a> (clone) of the graph. Each node in the graph contains a val (<code>int</code>) and a list (<code>List[Node]</code>) of its neighbors.</p>
<!--more-->

<p><strong>Example:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/02/19/113_sample.png" style="width: 200px; height: 149px;" /></p>

<pre>
<strong>Input:
</strong>{&quot;$id&quot;:&quot;1&quot;,&quot;neighbors&quot;:[{&quot;$id&quot;:&quot;2&quot;,&quot;neighbors&quot;:[{&quot;$ref&quot;:&quot;1&quot;},{&quot;$id&quot;:&quot;3&quot;,&quot;neighbors&quot;:[{&quot;$ref&quot;:&quot;2&quot;},{&quot;$id&quot;:&quot;4&quot;,&quot;neighbors&quot;:[{&quot;$ref&quot;:&quot;3&quot;},{&quot;$ref&quot;:&quot;1&quot;}],&quot;val&quot;:4}],&quot;val&quot;:3}],&quot;val&quot;:2},{&quot;$ref&quot;:&quot;4&quot;}],&quot;val&quot;:1}

<strong>Explanation:</strong>
Node 1&#39;s value is 1, and it has two neighbors: Node 2 and 4.
Node 2&#39;s value is 2, and it has two neighbors: Node 1 and 3.
Node 3&#39;s value is 3, and it has two neighbors: Node 2 and 4.
Node 4&#39;s value is 4, and it has two neighbors: Node 1 and 3.
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li>The number of nodes will be between 1 and 100.</li>
	<li>The undirected&nbsp;graph is a <a href="https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)#Simple_graph" target="_blank">simple graph</a>,&nbsp;which means no repeated edges and no self-loops in the graph.</li>
	<li>Since the graph is undirected, if node <em>p</em>&nbsp;has node <em>q</em>&nbsp;as&nbsp;neighbor, then node <em>q</em>&nbsp;must have node <em>p</em>&nbsp;as neighbor too.</li>
	<li>You must return the <strong>copy of the given node</strong> as a reference to the cloned graph.</li>
</ol>

# Solutions

Intuitively speaking, as long as we can successfully traverse the graph, we can clone this graph.  Therefore, we still need to try using both BFS and DFS to solve this.

## BFS

In BFS, the way to traverse a graph is:

1. Starting at a queue with 1 node, an empty set of visited nodes.
2. while queue not empty, pop 1 node from queue
  * for every **unvisited** neightbor, add it to queue

Knowing this, we can clone the graph by:

1. Starting at a queue with 1 node, an empty set of visited nodes.
  * make a copy of the starting node
2. while queue not empty, pop 1 node from queue
  * for every **unvisited** neightbor, add it to queue, make a copy of it, and connect the new copy to new neighbor.

```python
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        q = collections.deque([node])

        new_node = Node(node.val,[])
        visited = {node:new_node}

        while q:
            cur = q.popleft()

            for neighbor in cur.neighbors:
                if neighbor not in visited:
                    q.append(neighbor)
                    new_neighbor = Node(neighbor.val,[])
                    visited[neighbor] = new_neighbor
                    visited[cur].neighbors.append(new_neighbor)
                else:
                    visited[cur].neighbors.append( visited[neighbor] )

        return visited[node]
```

Keep in mind that when doing this kind of graph-traversing BFS, consider:

* Should you operate on the neighbor **before** or **during** traversing to that node?
  * In this problem, it's easier to copy node when first 'seeing' the node as someone's neighbor.
* How to avoid 2-pass BFS by maneuvering the traversal carefully?















