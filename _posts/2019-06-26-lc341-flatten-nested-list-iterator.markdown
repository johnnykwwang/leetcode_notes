---
layout: post
title: "341: Flatten Nested List Iterator"
date: "2019-06-26 21:17:02 -0700"
categories: [leetcode]
---

<p>Given a nested list of integers, implement an iterator to flatten it.</p>

<p>Each element is either an integer, or a list -- whose elements may also be integers or other lists.</p>

<!--more-->

<p><strong>Example 1:</strong></p>

<div>
<pre>
<strong>Input: </strong><span id="example-input-1-1">[[1,1],2,[1,1]]</span>
<strong>Output: </strong><span id="example-output-1">[1,1,2,1,1]
</span><strong>Explanation: </strong>By calling <i>next</i> repeatedly until <i>hasNext</i> returns false,
&nbsp;            the order of elements returned by <i>next</i> should be: <code>[1,1,2,1,1]</code>.</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,[4,[6]]]</span>
<strong>Output: </strong><span id="example-output-2">[1,4,6]
</span><strong>Explanation: </strong>By calling <i>next</i> repeatedly until <i>hasNext</i> returns false,
&nbsp;            the order of elements returned by <i>next</i> should be: <code>[1,4,6]</code>.
</pre>
</div>
</div>

# Solutions

To initialize, we just put all items into a stack, reversing it so that the first item is at the top of stack.
For the `next()` function and `hasNext()` function, we do:
* First, check if the top item is an integer item.  If not, we recursively dive deeper, saving all trace in the stack.
  * If no items are left in stack, `hasNext()` will return False
* Then we just simply pop the top item, which we just confirmed is an integer.

In this problem I learned a few more techniques:

* Originally I followed almost the same approach as [173. Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/description/), but later found out that I can separate some work in different functions, making it more clear.
* When thinking about processing stack, don't think 'linearly' -- think about if this operation can be expressed in a single while loop, instead of multiple layers of loops doing identical things.

```python
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:-1] + top.getList()[::-1]
        return False
```
