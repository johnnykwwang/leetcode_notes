---
layout: post
title: "003: Longest Substring Without Repeating Characters"
date: "2019-05-20 20:22:41 -0400"
categories: [leetcode]
---

<p>Given a string, find the length of the <b>longest substring</b> without repeating characters.</p>

<!--more-->

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">&quot;abcabcbb&quot;</span>
<strong>Output: </strong><span id="example-output-1">3
<strong>Explanation:</strong></span> The answer is <code>&quot;abc&quot;</code>, with the length of 3.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">&quot;bbbbb&quot;</span>
<strong>Output: </strong><span id="example-output-2">1
</span><span id="example-output-1"><strong>Explanation: </strong>T</span>he answer is <code>&quot;b&quot;</code>, with the length of 1.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">&quot;pwwkew&quot;</span>
<strong>Output: </strong><span id="example-output-3">3
</span><span id="example-output-1"><strong>Explanation: </strong></span>The answer is <code>&quot;wke&quot;</code>, with the length of 3.
             Note that the answer must be a <b>substring</b>, <code>&quot;pwke&quot;</code> is a <i>subsequence</i> and not a substring.
</pre>
</div>
</div>
</div>

# Solutions

This is the classic **Same-direction** type of two-pointer problem.  The idea is that at any moment, we have two pointers `i`,`j` each scanning thru the string.

* Start at i=0, j=1
* while i is within range,
  * While the condition ( No duplicate character ) holds, advance `j`.
  * If breaking the condition, advance `i`.
  * Deal with necessary data handling.

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j = 0, 1
        
        if len(s)<=1:
            return len(s)
        
        counts = set([s[i]])
        max_len = 0
        
        while i < len(s):
            while j < len(s) and s[j] not in counts:
                counts.add(s[j])
                j+=1
                
            max_len = max(max_len, j-i)
            
            counts.remove(s[i])
            i = i + 1
            
        return max_len
```
