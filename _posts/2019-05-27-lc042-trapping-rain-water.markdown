---
layout: post
title: "042: Trapping Rain Water"
date: "2019-05-27 14:51:34 -0700"
categories: [leetcode]
mathjax: true
---

<p>Given <em>n</em> non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.</p>

<!--more-->

<p><img src="https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png" style="width: 412px; height: 161px;" /><br />
<small>The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. <strong>Thanks Marcos</strong> for contributing this image!</small></p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [0,1,0,2,1,0,1,3,2,1,2,1]
<strong>Output:</strong> 6</pre>

# Solutions

While this problem is solvable in O(n) one-pass and O(1) space ( I would add on to this later ), the more practical solution for an interview answer would probably be the stack solution.

## Stack

The basic idea is, whenever we enter a supposed-water-area, we push its location to a stack.  When that area is then "sealed off" by the other wall, we pop it from the stack and add the volume to the total water, and effectively **fill up** the holes in each level.

```python
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        p0 = 0
        cur_h = height[p0]
        s = []
        total = 0
        while p0<len(height):
            if len(s)==0 or height[p0] <= height[s[-1]] :
                s.append(p0)
                p0+=1
            else:
                block = s.pop()
                if not s:
                    trapped = 0
                else:
                    trapped_h = ( min(height[p0],height[s[-1]]) - height[block] )
                    trapped_w = ( p0 - s[-1] - 1)
                    trapped = trapped_h * trapped_w
                total += trapped
        return total
```


