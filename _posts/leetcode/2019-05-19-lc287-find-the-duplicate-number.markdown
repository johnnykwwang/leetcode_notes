---
layout: post
title: "287: Find the Duplicate Number"
date: "2019-05-19 18:17:34 -0400"
categories: [leetcode]
---


<p>Given an array <i>nums</i> containing <i>n</i> + 1 integers where each integer is between 1 and <i>n</i> (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.</p>

<!--more-->

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> <code>[1,3,4,2,2]</code>
<b>Output:</b> 2
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> [3,1,3,4,2]
<b>Output:</b> 3</pre>

<p><b>Note:</b></p>

<ol>
	<li>You <b>must not</b> modify the array (assume the array is read only).</li>
	<li>You must use only constant, <i>O</i>(1) extra space.</li>
	<li>Your runtime complexity should be less than <em>O</em>(<em>n</em><sup>2</sup>).</li>
	<li>There is only one duplicate number in the array, but it could be repeated more than once.</li>
</ol>

# Solutions

## Binary Search

The idea is that when we do binary search, we count the elements of the array that are less than **mid** ( as in index, not `nums[mid]`.  For example, say we have `[1,3,4,2,2]`, we can set `start=1` and `end=5`.  Now when `mid=3`, we calculate the occurance of elements than are <= 3 which is 4.  If no duplicate in the range 0~mid, this count should be <= 3.  Therefore we know that the duplicated element must be in range 0~mid.

```python
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 1, len(nums)

        while start+1 < end:

            mid = start + (end-start)//2

            lower_than_mid = len([ n for n in nums if n<=mid])
            if lower_than_mid > mid:
                end = mid
            else:
                start = mid

        lower_than_start = len([n for n in nums if n<=start])
        if lower_than_start > start:
            return start
        else:
            return end
```

## Cycle Detection in Linked List

We can think of the list as a list of pointers.  Consider points labeled 0, 1, ... n, and each of the nums[i] indicates there's an edge from i to nums[i].  Duplicating element means that multiple point has an edge towards the duplicated element.  This is the same scenario as having a circle in the linked list, since we need at least two element in the linked list to point at the same element to form a circle.

This is a classic algorithm that detects the **Starting Point** of a cycle in a linked list.  When the fast reaches the slow, the rest of the cycle that slow needs to travel is the same as the origin to the start of cycle.

The math is as follows:

![image](https://user-images.githubusercontent.com/13166286/57989267-51415600-7a66-11e9-9861-3cae9e04dcae.png){:.w80.ctr-img}

Therefore we can write the fast-slow algorithm as:

```python
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast, slow = 0, 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break

        # detected, find the origin of breach.
        slow = 0
        while slow!=fast:
            slow, fast = nums[slow], nums[fast]
        return slow
```

---

# Related Problems

## [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/description/)

we use the same technique to find the node where the cycle begins.

```python
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow = head, head
        meet = None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast==slow:
                meet = slow
                break
        if meet is None:
            return None
        
        fast, slow = head, meet
        while fast != slow:
            fast, slow = fast.next, slow.next
            
        return slow
```

## [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)

Also the same kind of two-pointer in linked list problem.  In this problem, we:

1. Give the fast pointer a n-node lead
2. Then traverse the list with the slow pointer at the same speed.
3. When reaching the end, the slow pointer would be at node right before the node we're deleting.

```python
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
        
        if fast is None:
            head = head.next
            return head
        
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return head
```
