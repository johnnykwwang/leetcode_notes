---
layout: post
title: "394: Decode String"
date: "2019-06-06 22:08:48 -0700"
categories: [leetcode]
---


<p>
Given an encoded string, return it's decoded string.
</p>
<p>
The encoding rule is: <code>k[encoded_string]</code>, where the <i>encoded_string</i> inside the square brackets is being repeated exactly <i>k</i> times. Note that <i>k</i> is guaranteed to be a positive integer.</p>

<!--more-->

<p>
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.</p>

<p>Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, <i>k</i>. For example, there won't be input like <code>3a</code> or <code>2[4]</code>.
</p>

<p><b>Examples:</b>
<pre>
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
</pre>
</p>
# Solutions

This is not exactly trivial to solve using DFS.  But it is very obvious that it involves some very subtle stack operations.  Here we try to implement in such way that requires no recursion, just to practice using stacks.

The logic is as follows:

We maintain a stack in the process.
* When we encounter numbers, we parse it ( if next digit is still number, previous parsed numbers needs to times 10)
* When we got `[`, we push the number and a `[` to the stack.
* When we got ']', we start popping everything until we find a corresponding `[`, then multiply by the next pop(), which is the associated number.  Push the resulting string back to stack.
* When we got alphabets, just push it to stack.

Finally, we just join the whole stack to form the resulting string.

```python
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        i = 0
        nums_c = [ str(d) for d in [0,1,2,3,4,5,6,7,8,9] ]
        cur_count = 0
        res = ""
        buf = []

        while i<len(s):
            c = s[i]
            if c in nums_c:
                if cur_count!=0:
                    cur_count *= 10
                cur_count += int(c)

            elif c == '[':
                buf.append(cur_count)
                cur_count = 0
                buf.append('[')

            elif c == ']':
                k = buf.pop()
                comb = []
                while k!='[':
                    comb += [k]
                    k = buf.pop()

                buf.append("".join(comb[::-1]) * buf.pop())

            else:
                buf.append(c)

            i+=1

        return ("".join(buf))
```
