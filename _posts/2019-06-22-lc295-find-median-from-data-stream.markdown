---
layout: post
title: "295: Find Median from Data Stream"
date: "2019-06-22 17:08:53 -0700"
categories: [leetcode]
---

<p>Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.</p>
For example,

<p><code>[2,3,4]</code>, the median is <code>3</code></p>

<p><code>[2,3]</code>, the median is <code>(2 + 3) / 2 = 2.5</code></p>

<p>Design a data structure that supports the following two operations:</p>

<ul>
	<li>void addNum(int num) - Add a integer number from the data stream to the data structure.</li>
	<li>double findMedian() - Return the median of all elements so far.</li>
</ul>

<!--more-->

<p><strong>Example:</strong></p>

<pre>
addNum(1)
addNum(2)
findMedian() -&gt; 1.5
addNum(3)
findMedian() -&gt; 2
</pre>

<p>&nbsp;</p>

<p><strong>Follow up:</strong></p>

<ol>
	<li>If all integer numbers from the stream are between 0&nbsp;and 100, how would you optimize it?</li>
	<li>If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?</li>
</ol>

# Solutions

This is a classic problem to understand the heap data structure.  In this problem, we can keep two heaps, called `left_heap` and `right_heap`, such that:

* `left_heap` is a **max-heap**, aka the `left_heap[0]` would be the max element among all.
* `right_heap` is a **min-heap**.
* When there's odd number of elements, `left_heap[0]` is the median.
* When there's even number of elements, the average of `left_heap[0]` and `right_heap[0]` is the median.

In this sense, we only need to design what happens when we insert a new element.

* When both heap empty, new element goes to left.
* When heaps have same number of elements:
  * If it's smaller than `left_heap[0]`, add it to left.
  * If it's larger or equal to `left_heap[0]`, add it to right.  This would break our constraints, so we pop one elements from right to compensate the `left_heap` to keep the number of elements in check.
* When heaps have different number of elements, aka left has one more elments:
  * If it's smaller than `left_heap[0]`, add it to left and pop one to right, to keep the `left_heap` only one more element than `right_heap`.
  * If it's bigger than `left_heap[0]`, then just add it to right.

```python
class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left_heap = []
        self.right_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.left_heap)==0 and len(self.right_heap)==0:
            heapq.heappush(self.left_heap, -num)

        elif len(self.left_heap)==len(self.right_heap):

            if -self.left_heap[0] > num:
                heapq.heappush(self.left_heap, -num)
            else:
                heapq.heappush(self.right_heap, num)
                right_pop = heapq.heappop(self.right_heap)
                heapq.heappush(self.left_heap,-right_pop)

        else:
            if -self.left_heap[0] > num:
                heapq.heappush(self.left_heap, -num)
                left_pop = - heapq.heappop(self.left_heap)
                heapq.heappush(self.right_heap,left_pop)
            else:
                heapq.heappush(self.right_heap, num)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.left_heap)!=len(self.right_heap):
            return float(-self.left_heap[0])
        else:
            return (-self.left_heap[0] + self.right_heap[0]) / 2.
```
