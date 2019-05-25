---
layout: post
title: "011: Container With Most Water"
date: "2019-05-20 19:17:29 -0400"
categories: [leetcode]
---

<p>Given <i>n</i> non-negative integers <i>a<sub>1</sub></i>, <i>a<sub>2</sub></i>, ..., <i>a<sub>n&nbsp;</sub></i>, where each represents a point at coordinate (<i>i</i>, <i>a<sub>i</sub></i>). <i>n</i> vertical lines are drawn such that the two endpoints of line <i>i</i> is at (<i>i</i>, <i>a<sub>i</sub></i>) and (<i>i</i>, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.</p>

<!--more-->

<p><strong>Note:&nbsp;</strong>You may not slant the container and <i>n</i> is at least 2.</p>

<p>&nbsp;</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg" style="width: 600px; height: 287px;" /></p>

<p><small>The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain&nbsp;is 49. </small></p>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [1,8,6,2,5,4,8,3,7]
<strong>Output:</strong> 49</pre>

# Solutions

This is an application of the two-pointer algorithm.  The most important thing about two-pointer related problems is **when should you move the pointers**.

In this problem, say we have two pointers L and R starting from left and right:

* When `height[L]` > `height[R]`, then this amount is the best since all (L+1, R), (L+2,R)... would be less than (L,R) since the height is determined by `height[R]`.

* So in our loop, we move R when `height[L]` > `height[R]`, else move L.

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        i, j = 0, len(height)-1
        cur = min( height[i], height[j] ) * (j-i)

        while i<j:
            if height[j] >= height[i]:
                cur = max(cur, height[i]*(j-i))
                i = i+1
            else:
                cur = max(cur, height[j]*(j-i))
                j = j-1
        return cur
```
