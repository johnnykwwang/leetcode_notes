---
layout: post
title: "914: Random Point in Non-overlapping Rectangles"
date: "2019-06-18 19:27:48 -0700"
categories: [leetcode]
---


<p>Given a list of <strong>non-overlapping</strong>&nbsp;axis-aligned rectangles <code>rects</code>, write a function <code>pick</code> which randomly and uniformily picks an <strong>integer point</strong> in the space&nbsp;covered by the rectangles.</p>

<!--more-->

<p>Note:</p>

<ol>
	<li>An <strong>integer point</strong>&nbsp;is a point that has integer coordinates.&nbsp;</li>
	<li>A point&nbsp;on the perimeter&nbsp;of a rectangle is&nbsp;<strong>included</strong> in the space covered by the rectangles.&nbsp;</li>
	<li><code>i</code>th rectangle = <code>rects[i]</code> =&nbsp;<code>[x1,y1,x2,y2]</code>, where <code>[x1, y1]</code>&nbsp;are the integer coordinates of the bottom-left corner, and <code>[x2, y2]</code>&nbsp;are the integer coordinates of the top-right corner.</li>
	<li>length and width of each rectangle does not exceed <code>2000</code>.</li>
	<li><code>1 &lt;= rects.length&nbsp;&lt;= 100</code></li>
	<li><code>pick</code> return a point as an array of integer coordinates&nbsp;<code>[p_x, p_y]</code></li>
	<li><code>pick</code> is called at most <code>10000</code>&nbsp;times.</li>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:
</strong><span id="example-input-1-1">[&quot;Solution&quot;,&quot;pick&quot;,&quot;pick&quot;,&quot;pick&quot;]
</span><span id="example-input-1-2">[[[[1,1,5,5]]],[],[],[]]</span>
<strong>Output:
</strong><span id="example-output-1">[null,[4,1],[4,1],[3,3]]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:
</strong><span id="example-input-2-1">[&quot;Solution&quot;,&quot;pick&quot;,&quot;pick&quot;,&quot;pick&quot;,&quot;pick&quot;,&quot;pick&quot;]
</span><span id="example-input-2-2">[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]</span>
<strong>Output:
</strong><span id="example-output-2">[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]</span></pre>
</div>

<div>
<p><strong>Explanation of Input Syntax:</strong></p>

<p>The input is two lists:&nbsp;the subroutines called&nbsp;and their&nbsp;arguments.&nbsp;<code>Solution</code>&#39;s&nbsp;constructor has one argument, the array of rectangles <code>rects</code>. <code>pick</code>&nbsp;has no arguments.&nbsp;Arguments&nbsp;are&nbsp;always wrapped with a list, even if there aren&#39;t any.</p>
</div>
</div>

<div>
<div>&nbsp;</div>
</div>

# Solutions

This is a very interesting problem.  My approach is to first calculate the "weight" of each rectangles, to determine how much probability to land in every rectangle.  Then once decided the rectangle, we can just randomly choose a point from it.

Problem is, in order to use the weights to decide which rectangle to choose, we need some sort of range for our random number generator.  For example, if there's two rectangles with area `4` and `1`, then we define a random variable `0 <= r < 1`, So our **bounds** will be: 

* If `0 <= r < 0.8`, choose from the first
* If `0.8 <= r < 1`, choose from the second

and so on.  To avoid all kinds of binary search problems, I just over-complicate this boundary calculation and include left and right bound.

```python
class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.A = [ abs((x2-x1+1)*(y2-y1+1)) for x1,y1,x2,y2 in rects ]

        s = sum(self.A)
        self.A = [ a/float(s) for a in self.A ]
        su = 0.
        i = 0
        while i<len(self.A):
            a = self.A[i]
            self.A[i] = (su, su+a)
            su += a
            i+=1

    def find_A_by_val(self, val):
        low = 0
        high = len(self.A)-1

        while low+1<high:
            mid = low + (high-low)//2
            l,r = self.A[mid]
            if l<=val<r:
                return mid
            elif r<=val:
                low = mid
            else:
                high = mid
        l,r = self.A[high]
        if l<=val<r:
            return high
        return low

    def pick(self):
        """
        :rtype: List[int]
        """
        r = random.random()
        idx = self.find_A_by_val(r)
        x1, y1, x2, y2 = self.rects[idx]
        x = random.choice( range(x1,x2+1) )
        y = random.choice( range(y1,y2+1) )
        return [x,y]
```


