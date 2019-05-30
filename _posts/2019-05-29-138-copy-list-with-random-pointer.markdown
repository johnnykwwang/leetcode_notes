---
layout: post
title: "138: Copy List with Random Pointer"
categories: [leetcode]
---

<p>A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.</p>

<p>Return a <a href="https://en.wikipedia.org/wiki/Object_copying#Deep_copy" target="_blank"><strong>deep copy</strong></a> of the list.</p>

<!--more-->

<p><strong>Example 1:</strong></p>

<p><strong><img alt="" src="https://discuss.leetcode.com/uploads/files/1470150906153-2yxeznm.png" style="width: 375px; height: 129px;" /></strong></p>

<pre>
<strong>Input:
</strong><span id="example-input-1-1">{&quot;$id&quot;:&quot;1&quot;,&quot;next&quot;:{&quot;$id&quot;:&quot;2&quot;,&quot;next&quot;:null,&quot;random&quot;:{&quot;$ref&quot;:&quot;2&quot;},&quot;val&quot;:2},&quot;random&quot;:{&quot;$ref&quot;:&quot;2&quot;},&quot;val&quot;:1}
</span>
<b>Explanation:
</b>Node 1&#39;s value is 1, both of its next and random pointer points to Node 2.
Node 2&#39;s value is 2, its next pointer points to null and its random pointer points to itself.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li>You must return the <strong>copy of the given head</strong>&nbsp;as a reference to the cloned list.</li>
</ol>

# Solutions

## Using Hash(Dict):

The easy way to approach this problem is to use a hash that maps every original node to the cloned node.  Then after 1 pass that creates all the nodes, the second pass would connect the random pointers.

```python
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        n = head
        old2new = {None: None}
        last_new = None
        while n:
            c_n = Node(n.val,None,None)
            if last_new:
                last_new.next = c_n
            old2new[n] = c_n
            n = n.next
            last_new = c_n
        n = head
        while n:
            c_n = old2new[n]
            # c_n.next = old2new[n.next]
            c_n.random = old2new[n.random]
            n = n.next
            
        return old2new[head]
```

## Without Extra Space:

The way to solve this problem without extra space is kind of tricky.  I am not sure if this is a practical approach in an interview, but the thought process might help.

The way to achieve O(1) space is as follows:
1. First Pass: Create cloned node and link it such that it's the `.next` of the original node.
    * For example, ` 1 -> 2 -> 3` would become ` 1 -> 1' -> 2 -> 2' -> 3 -> 3'` 
2. Second Pass: Loop through the original nodes and `node.next.random = node.random.next`
3. Third Pass: Retrieve the cloned nodes.

```python
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        # First Pass
        h = head
        while h:
            clone = Node(h.val,None,None)
            orig_next = h.next
            h.next = clone
            clone.next = orig_next
            h = orig_next

        # Second Pass
        h = head
        while h:
            if h.random and h.next:
                h.next.random = h.random.next
            h = h.next.next

        # Third Pass
        h = head
        cloned_head = h.next
        while h:
            orig = h
            orig_next = h.next.next if h.next else None
            cloned = h.next
            h.next = orig_next

            if cloned.next:
                cloned.next = cloned.next.next
            else:
                cloned.next = None

            h = orig_next

        return cloned_head
```



