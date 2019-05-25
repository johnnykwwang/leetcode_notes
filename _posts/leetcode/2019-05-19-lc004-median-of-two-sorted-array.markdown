---
layout: post
title: "004: Median of Two Sorted Arrays"
date: "2019-05-19 15:47:17 -0400"
categories: [leetcode]
#tags: [hardproblem,median,binarysearch]
---

<p>There are two sorted arrays <b>nums1</b> and <b>nums2</b> of size m and n respectively.</p>

<p>Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).</p>

<p>You may assume <strong>nums1</strong> and <strong>nums2</strong>&nbsp;cannot be both empty.</p>

<!--more-->

<p><b>Example 1:</b></p>

<pre>
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
</pre>

<p><b>Example 2:</b></p>

<pre>
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
</pre>

# Solutions

Our first #HardProblem of the season!

The most naive way is of course, merging the two sorted array ( Time: O(m+n) ) and then find the median.

Here we would do something smarter:

## Find k-th 

We first define a recursive structure `kth(a,b,k)` that finds the k-th element in the combined array of a and b.  a,b are sorted.

then the problem becomes just handling odd/even case.

So the point is how we calculate the kth element of sorted arrays a,b.

consider a, b's median ma and mb and their index ia and ib.  

If k > ia+ib, that means k is larger than the median of the combined array.  Also, in the combined array, if mb is smaller, then anything on the left of mb we dont need to consider.  Since we can only guarantee b[:ib+1] are on the left of mb, we eliminate this part.

```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a,b = nums1, nums2
        l = len(nums1)+len(nums2)
        if l & 1:
            return self.kth(a,b,l//2)
        else:
            return (self.kth(a,b,l//2-1) + self.kth(a,b,l//2)) / 2.

    def kth(self,a,b,k):
        if len(a)==0:
            return b[k]
        if len(b)==0:
            return a[k]

        ia, ib = len(a)//2, len(b)//2
        ma, mb = a[ia], b[ib]

        if ia+ib < k:
            if ma > mb:
                return self.kth(a,b[ib+1:],k-ib-1)
            else:
                return self.kth(a[ia+1:],b,k-ia-1)
        else:
            if ma > mb:
                return self.kth(a[:ia],b,k)
            else:
                return self.kth(a,b[:ib],k)
```


# Techniques

## Edge Case Handling
In this problem we experienced fair amount of edge case handling.  Especially in calculating median.  I should do a full list of median-related problems just to practice this.

