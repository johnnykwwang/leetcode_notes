---
layout: post
title: "410: Split Array Largest Sum"
date: "2019-06-16 17:20:23 -0700"
categories: [leetcode]
---

<p>Given an array which consists of non-negative integers and an integer <i>m</i>, you can split the array into <i>m</i> non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these <i>m</i> subarrays.
</p>

<!--more-->

<p><b>Note:</b><br />
If <i>n</i> is the length of array, assume the following constraints are satisfied:
<ul>
<li>1 &le; <i>n</i> &le; 1000</li>
<li>1 &le; <i>m</i> &le; min(50, <i>n</i>)</li>
</ul>
</p>

<p><b>Examples: </b>
<pre>
Input:
<b>nums</b> = [7,2,5,10,8]
<b>m</b> = 2

Output:
18

Explanation:
There are four ways to split <b>nums</b> into two subarrays.
The best way is to split it into <b>[7,2,5]</b> and <b>[10,8]</b>,
where the largest sum among the two subarrays is only 18.
</pre>
</p>

# Solutions

This is an interesting variation of the binary search.  The key here is knowing that we can use **binary search on values** instead of typical binary search on array index.  Here, to perform a binary search on value, we need to identify:

1. What's the range of the answer?
* This is easy.  According to the problem, the minimum cut must contain at least one element, so `minimum=min(nums)`.  As for maximum, we can just be lazy and set `maximum=sum(nums)`
2. How to check if a value is legal or not?
* We can take a `O(n)` time to actually perform the cutting on the given val, aka if the array can be partitioned such that every partition sum <= the given value, and it takes less than `m` partitions to do that.

Having all these, it becomes a very trivial binary search, just remember to check the boundary condition on the `low` and `high`.

```python
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """

        # ans range
        low = min(nums)
        high = sum(nums)

        # binary search on the ans range
        while low + 1 < high:
            mid = (low+high)//2
            print mid
            if self.check_split_valid(nums, m, mid):
                high = mid
            else:
                low = mid

        # edge case test
        if self.check_split_valid(nums,m,low):
            return low
        else:
            return high

    def check_split_valid(self, nums, m, val):
        parts = 0
        cur = 0
        for n in nums:
            if n>val:
                return False
            if cur+n <= val:
                cur+=n
            else:
                parts+=1
                cur=n
        return cur<=val and parts+1<=m
```


