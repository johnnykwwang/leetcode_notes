---
layout: post
title: "Breath-First-Search Compilation"
date: "2019-05-21 13:56:37 -0400"
---

All BFS-related problems are extremely similar.  Here we would go through several problems at once and then give some general techniques.

<!--more-->

# [279. Perfect Squares](https://leetcode.com/problems/perfect-squares/description/)

<p>Given a positive integer <i>n</i>, find the least number of perfect square numbers (for example, <code>1, 4, 9, 16, ...</code>) which sum to <i>n</i>.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> <i>n</i> = <code>12</code>
<b>Output:</b> 3 
<strong>Explanation: </strong><code>12 = 4 + 4 + 4.</code></pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> <i>n</i> = <code>13</code>
<b>Output:</b> 2
<strong>Explanation: </strong><code>13 = 4 + 9.</code></pre>

## Solutions

This is solvable via **BFS-by-layer**.  The way to do BFS by layer is that we dont maintain a global queue, we generate the queue for the next layer during the iteration of the current layer.  Some key points to notice:

* Trim Condition 
* Stop Condition
* Next Layer Generation

```python
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return n
        sq_list = []
        i=0
        while i*i <= n:
            sq_list.append(i*i)
            i+=1

        count = 0
        layer = [n]
        while layer:
            count+=1
            next_layer = []

            for x in layer:
                for y in sq_list:
                    if x==y:
                        return count
                    elif x<y:
                        break
                    else:
                        next_layer.append(x-y)
            layer = next_layer

        return count
```




