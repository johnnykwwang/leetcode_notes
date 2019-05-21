---
layout: post
title: "234: Palindrome Linked List"
categories: [leetcode]
date: "2019-05-20 22:42:08 -0400"
mathjax: True
---

<p>Given a singly linked list, determine if it is a palindrome.</p>

<!--more-->

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 1-&gt;2
<strong>Output:</strong> false</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 1-&gt;2-&gt;2-&gt;1
<strong>Output:</strong> true</pre>

<p><b>Follow up:</b><br />
Could you do it in O(n) time and O(1) space?</p>

# Solutions

This is an extremely interesting problem.  Although the easier solution, putting every value into a list and detect palindrome from the list, is very easy, the hardest part is to implement it in $ O(n) $ time and $ O(1) $ space.

The big picture is as follows:

1. First, use fast-slow algorithm to find the mid-point of the linked-list
  * This would generate two cases, with minor differences going into second step.
2. Then, reverse the second half of the linked list.
3. Finally, Go through first half and second half one-by-one to check if they're identical

Let's just see the code:
```python

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast,slow = head, head
        
        if head is None or head.next is None:
            return True
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #slow is the midpoint
        if fast is None: # case: 1->2->[2]->1
            dum = None
            prev, cur, nex = dum, slow, slow.next
        else: # case: 1->[2]->1
            slow2 = slow.next
            dum = None
            prev, cur, nex = dum, slow2, slow2.next
            
        # reverse the part starting from slow or next of slow, depending on case
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex

        # detect palindrome
        first, second = head, prev
        while first!=slow and second!=None:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True
```
