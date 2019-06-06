---
layout: post
title: "297: Serialize and Deserialize Binary Tree"
date: "2019-06-05 21:19:03 -0700"
categories: [leetcode]
---

<p>Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.</p>

<p>Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.</p>

<!--more-->

<p><strong>Example:&nbsp;</strong></p>

<pre>
You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as <code>&quot;[1,2,3,null,null,4,5]&quot;</code>
</pre>

<p><strong>Clarification:</strong> The above format is the same as <a href="/faq/#binary-tree">how LeetCode serializes a binary tree</a>. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.</p>

<p><strong>Note:&nbsp;</strong>Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.</p>

# Solutions

This is a very open-ended problem with many solution. 

## The Leetcode Encoding via Layered BFS

This is the encoding that this problem suggests.  By examining the example, we can see that this is a BFS-approach.  

So for serialize, what we do is:

* Traverse the tree via BFS, allowing append `None` into the layer queue.
  * Whenever the whole layer is None, we drop this layer ( happens only at last layer )
* Change to comma-separated string, with `None` being just `'None'`

Then for deserialize, we can imagine that we're still traversing a tree, but we need to **pave our way** down:
* Start at root, traverse layer-by-layer
* For every node in a layer, grab 2 elements from the serialized data and make them `TreeNodes` if they're not `None`.
  * Append the newly-created node into next layer-queue.

```python
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        layer = [root]
        ret = []
        next_layer_all_none = True
        while layer:
            new_layer = []
            layer_ret = []
            for n in layer:
                if n:
                    next_layer_all_none = False
                    layer_ret.append(n.val)
                    new_layer.append(n.left)
                    new_layer.append(n.right)
                else:
                    layer_ret.append(None)
            if not next_layer_all_none:
                ret.extend(layer_ret)
                next_layer_all_none = True
            layer = new_layer

        return ",".join([str(r) for r in ret])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data)==0:
            return None

        data = data.split(',')
        root = TreeNode(data[0])
        i = 1
        layer = [root]

        while layer:
            new_layer = []
            for n in layer:
                if n:
                    left = self.node(data[i]) if i<len(data) else None
                    right = self.node(data[i+1]) if i+1<len(data) else None
                    n.left, n.right = left, right
                    new_layer.extend([n.left,n.right])
                    i+=2
            layer = new_layer
        return root

    def node(self, data):
        if data=='None':
            return None
        else:
            return TreeNode(data)
```


