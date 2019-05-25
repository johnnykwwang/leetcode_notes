---
layout: post
title: "033: Search in Rotated Sorted Array"
date: "2019-05-19 17:21:55 -0400"
categories: [leetcode]
---

<p>Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.</p>

<p>(i.e., <code>[0,1,2,4,5,6,7]</code> might become <code>[4,5,6,7,0,1,2]</code>).</p>

<p>You are given a target value to search. If found in the array return its index, otherwise return <code>-1</code>.</p>

<p>You may assume no duplicate exists in the array.</p>

<p>Your algorithm&#39;s runtime complexity must be in the order of&nbsp;<em>O</em>(log&nbsp;<em>n</em>).</p>

<!--more-->

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [<code>4,5,6,7,0,1,2]</code>, target = 0
<strong>Output:</strong> 4
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [<code>4,5,6,7,0,1,2]</code>, target = 3
<strong>Output:</strong> -1</pre>

# Solutions

## Binary Search (Explicit)

Here I marked this solution **explicit** because in this kind of problem with multiple conditions, I like to lay out every possible scenario more clearly.  It might results in more code but it's more expressive.

In this problem, we can use a binary search with the following twist:

First, we determine if the midpoint is in the first ascend or in the second ascent.

In either case, we also try to determine if the target belongs to that part of the ascent.  If it does, we use normal binary search on that segment.  If not, we move mid to try finding the other ascend.

```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        start = 0
        end = len(nums)-1

        if len(nums)==0:
            return -1
        if nums[start]==target:
            return start
        if nums[end]==target:
            return end

        while start+1 < end:
            mid = start + (end-start)//2
            #must be the format of: start < mid < end

            if nums[mid]==target:
                return mid

            if nums[mid]<nums[-1]: # mid in second ascend
                if target < nums[-1]: # target in second ascend
                    if nums[mid] > target:
                        end = mid
                    else:
                        start = mid
                else: # target not in second ascend, move mid to find first ascend
                    end = mid
            else:
                if target>nums[0]: # target in first ascend
                    if nums[mid]>target:
                        end = mid
                    else:
                        start = mid
                else: # target not in first ascend, move mid to find second ascend
                    start=mid

        return -1
```

# Techniques

## Binary Search 

In binary search, the most convenient way is like:

```
start, end = 0, len(something)
while start + 1 < end:
    mid = start + (end - start) / 2
    if mid....
        start = mid
    else...
        end = mid
```

This is more useful than setting `start<end` because it ensures `start`,`mid`,`end` are 3 different elements.

Notice that if using this kind of binary search, we might need to add edge cases such as when length is 0,1 or 2.

# Related Problems

## [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)

This problem is easier than searching specific element.  Code as follows.  Worth noting that sometimes it's important to add edge case handling at the end of the binary search.  The `start` and `end` pointer after binary search would be adjacent, so we can compare them somehow to output an edge case answer.

```python
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums)-1
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return min(nums[0],nums[1])

        while start+1 < end:

            mid = start + (end-start)//2

            if nums[start] > nums[mid] and nums[mid] < nums[end] and start+1==mid:
                return nums[mid]
            if nums[mid] < nums[-1]:
                end = mid
            else:
                start = mid

        return min(nums[start],nums[end]) # edge case
```
