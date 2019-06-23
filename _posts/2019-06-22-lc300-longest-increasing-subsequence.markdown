---
layout: post
title: "300: Longest Increasing Subsequence"
date: "2019-06-22 16:45:33 -0700"
categories: [leetcode]
---


<p>Given an unsorted array of integers, find the length of longest increasing subsequence.</p>

<!--more-->
<p><b>Example:</b></p>

<pre>
<b>Input:</b> <code>[10,9,2,5,3,7,101,18]
</code><b>Output: </b>4
<strong>Explanation: </strong>The longest increasing subsequence is <code>[2,3,7,101]</code>, therefore the length is <code>4</code>. </pre>

<p><strong>Note: </strong></p>

<ul>
	<li>There may be more than one LIS combination, it is only necessary for you to return the length.</li>
	<li>Your algorithm should run in O(<i>n<sup>2</sup></i>) complexity.</li>
</ul>

<p><b>Follow up:</b> Could you improve it to O(<i>n</i> log <i>n</i>) time complexity?</p>

# Solutions

From now on we'll see a lot of this subsequence / subarray / supersequence type of thing.  First, we need to recognize:

* What is subsequence?
* What technique can be used?

In this problem, we can first maintain a stack that is the current longest subsequence, and gradually update it.

The trick is, when we meet a number that is **lower than last of stack**, we can just change the corresponding closest element in the stack to this value, so that from now on the sequence would kind of **consider** this number so that we won't miss any number later that are slightly larger than this number.

The way we locate this number is of course, binary search.

```python
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        s = [nums[0]]
        max_len = 1
        for n in nums[1:]:
            if s[-1]<n:
                s.append(n)
            else:
                idx = self.find_idx(s,n)
                s[idx] = n
            max_len = max(max_len,len(s))
        return max_len

    def find_idx(self, s, n):
        low, high = 0, len(s)-1
        while low+1 < high:
            mid = low + (high-low)//2
            if s[mid]<n:
                low = mid
            else:
                high = mid
        if s[low]==n:
            return low
        return low if n<s[low] else high
```

---

# Related Problem: [354. Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/description/)

<p>You have a number of envelopes with widths and heights given as a pair of integers <code>(w, h)</code>. One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.</p>

<p>What is the maximum number of envelopes can you Russian doll? (put one inside other)</p>

<p><b>Note:</b><br />
Rotation is not allowed.</p>

<p><strong>Example:</strong></p>

<div>
<pre>
<strong>Input: </strong><span id="example-input-1-1">[[5,4],[6,4],[6,7],[2,3]]</span>
<strong>Output: </strong><span id="example-output-1">3
<strong>Explanation: T</strong></span>he maximum number of envelopes you can Russian doll is <code>3</code> ([2,3] =&gt; [5,4] =&gt; [6,7]).
</pre>
</div>

## Solutions

This problem looks just like the LIS problem.  But the problem is, we now have two sequence to handle.  This creates a lot of different states while comparing: both larger, both smaller, both equal, one larger,...

So in order to handle this problem more elegant, we consider this problem in a broad sense.  For example, for `[[5,4],[6,4],[6,7],[2,3]]`, we first sort it via width.  Now it's `[[2,3],[5,4],[6,4],[6,7]]`.  now if we traverse all items, we have 2\*2 scenarios:

* The item's width is larger than the last item in stack:
  * But height is not --> don't put it in stack. [ Achievable ]
  * Height is also larger, so we can put it to stack. [ Achievable ] 

* The item's width is equal to the last item in stack.
  * If the height is larger, then we should not change it to stack because it limits further iteration
  * If the height is smaller, then we maybe should put it to stack.

In this analysis, we can see that the problem is in second case.  Therefore, we can do the following: **Sort the array first by weight, then reversely by height.  Then do LIS on height.**

This way, we ensure that when the width is equal, we consider the larger height first, then gradually update the height to the smallest value possible, while keeping the widths increasing.

```python
import functools
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if len(envelopes) == 0:
            return 0
        envelopes = sorted(list(set([ (h,w) for h,w in envelopes ])), key=functools.cmp_to_key(self.cmp)) 
        envelopes = [ w for _,w in envelopes ]
        s = [envelopes[0]]
        max_len = 1
        for n in envelopes[1:]:
            if s[-1]<n:
                s.append(n)
            else:
                idx = self.find_idx(s,n)
                s[idx] = n
            max_len = max(max_len,len(s))
        return max_len
    
    def cmp(self,a,b):
        if a[0]<b[0]:
            return -1
        elif a[0]>b[0]:
            return 1
        else:
            if a[1]<b[1]:
                return 1
            elif a[1]>b[1]:
                return -1
            return 0
    
    def find_idx(self, s, n):
        low, high = 0, len(s)-1
        while low+1 < high:
            mid = low + (high-low)//2
            if s[mid]<n:
                low = mid
            else:
                high = mid
        if s[low]==n:
            return low
        return low if n<s[low] else high
```
        

