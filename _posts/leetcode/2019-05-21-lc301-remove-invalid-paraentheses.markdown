---
layout: post
title: "301: Remove Invalid Parentheses"
date: "2019-05-21 17:05:01 -0400"
categories: [leetcode]
---

<p>Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.</p>

<!--more-->

<p><strong>Note:</strong>&nbsp;The input string may contain letters other than the parentheses <code>(</code> and <code>)</code>.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> &quot;()())()&quot;
<b>Output:</b> [&quot;()()()&quot;, &quot;(())()&quot;]
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> &quot;(a)())()&quot;
<b>Output:</b> [&quot;(a)()()&quot;, &quot;(a())()&quot;]
</pre>

<p><b>Example 3:</b></p>

<pre>
<b>Input:</b> &quot;)(&quot;
<b>Output: </b>[&quot;&quot;]
</pre>

# Solutions

Another #hardproblem!  This is an application of the **BFS-By-Layer**.  Basically, we generate the next layer by trying to remove a `(` or `)` from the current string.

```python
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        layer = set([s])
        ans = []
        end_this_layer = False
        while layer:
            next_layer = set()
            for s in layer:
                left_count, right_count = 0, 0
                if self.check(s):
                    ans.append(s)
                    end_this_layer = True
                    continue
                for c in s:
                    if c=='(':
                        left_count += 1
                    elif c==')':
                        right_count += 1
                for i,c in enumerate(s):
                    sym = '(' if left_count>= right_count else ')'
                    if c==sym:
                        new_s = list(s)
                        new_s[i] = ''
                        next_layer.add(''.join(new_s))
            if end_this_layer:
                break
            layer = next_layer
        return ans
    def check(self,s):
        left_count = 0
        for c in s:
            if c=='(':
                left_count += 1
            elif c==')':
                left_count -= 1
            if left_count < 0:
                return False
                return left_count==0
```





