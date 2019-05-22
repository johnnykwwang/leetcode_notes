---
layout: post
title: "127: Word Ladder && 126: Word Ladder II"
date: "2019-05-22 17:42:55 -0400"
categories: [leetcode]
---

<p>Given two words (<em>beginWord</em> and <em>endWord</em>), and a dictionary&#39;s word list, find the length of shortest transformation sequence from <em>beginWord</em> to <em>endWord</em>, such that:</p>

<ol>
	<li>Only one letter can be changed at a time.</li>
	<li>Each transformed word must exist in the word list. Note that <em>beginWord</em> is <em>not</em> a transformed word.</li>
</ol>

<!--more-->

<p><strong>Note:</strong></p>

<ul>
	<li>Return 0 if there is no such transformation sequence.</li>
	<li>All words have the same length.</li>
	<li>All words contain only lowercase alphabetic characters.</li>
	<li>You may assume no duplicates in the word list.</li>
	<li>You may assume <em>beginWord</em> and <em>endWord</em> are non-empty and are not the same.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong>
beginWord = &quot;hit&quot;,
endWord = &quot;cog&quot;,
wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;,&quot;cog&quot;]

<strong>Output: </strong>5

<strong>Explanation:</strong> As one shortest transformation is &quot;hit&quot; -&gt; &quot;hot&quot; -&gt; &quot;dot&quot; -&gt; &quot;dog&quot; -&gt; &quot;cog&quot;,
return its length 5.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong>
beginWord = &quot;hit&quot;
endWord = &quot;cog&quot;
wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;]

<strong>Output:</strong>&nbsp;0

<strong>Explanation:</strong>&nbsp;The endWord &quot;cog&quot; is not in wordList, therefore no possible<strong>&nbsp;</strong>transformation.
</pre>

<ul>
</ul>

# Solutions

Word Ladder is a classic back-tracking & BFS related problem that is solvable by multiple techniques.  Here we try to approach with BFS.

The idea is:

* for every word in the wordList and the beginWord, create a list of word that is only 1-character off from them.
* do BFS starting on the beginWord, building next layer via the one-off list.

```python
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        wordList.add(beginWord)

        if endWord not in wordList:
            return 0

        word_list_one_off = {}

        for w in wordList:
            word_list_one_off[w] = set()
            for i in range(len(w)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_w = w[:i] + c + w[i+1:]
                    if new_w in wordList and c != w[i]:
                        word_list_one_off[w].add(new_w)

        layer = set([beginWord])
        depth = 0

        while layer:
            new_layer = set()
            depth+=1
            for word in layer:
                if word == endWord:
                    return depth
                new_layer |= (word_list_one_off[word])
            layer = new_layer
        return 0
```

Here we did not check if the loop goes indefinitely.  In the next problem we would fix this.

---

# Extended Version: Word Ladder II

<p>Given two words (<em>beginWord</em> and <em>endWord</em>), and a dictionary&#39;s word list, find all shortest transformation sequence(s) from <em>beginWord</em> to <em>endWord</em>, such that:</p>

<ol>
	<li>Only one letter can be changed at a time</li>
	<li>Each transformed word must exist in the word list. Note that <em>beginWord</em> is <em>not</em> a transformed word.</li>
</ol>

<p><strong>Note:</strong></p>

<ul>
	<li>Return an empty list if there is no such transformation sequence.</li>
	<li>All words have the same length.</li>
	<li>All words contain only lowercase alphabetic characters.</li>
	<li>You may assume no duplicates in the word list.</li>
	<li>You may assume <em>beginWord</em> and <em>endWord</em> are non-empty and are not the same.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong>
beginWord = &quot;hit&quot;,
endWord = &quot;cog&quot;,
wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;,&quot;cog&quot;]

<strong>Output:</strong>
[
  [&quot;hit&quot;,&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;cog&quot;],
&nbsp; [&quot;hit&quot;,&quot;hot&quot;,&quot;lot&quot;,&quot;log&quot;,&quot;cog&quot;]
]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong>
beginWord = &quot;hit&quot;
endWord = &quot;cog&quot;
wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;]

<strong>Output: </strong>[]

<strong>Explanation:</strong>&nbsp;The endWord &quot;cog&quot; is not in wordList, therefore no possible<strong>&nbsp;</strong>transformation.
</pre>

<ul>
</ul>

## Solutions:

Here we only care about the BFS part.  The process of building the one-off list is the same.

The idea is that we want to not only store the current word, but also the path it took.

Therefore, we change the set to a hash, key being the current word in the layer and value being the paths it took to get to this word.

```python
        layer = {}
        layer[beginWord] = [[beginWord]]
        ans = []

        while layer:
            new_layer = collections.defaultdict(list)
            for word in layer:
                if word == endWord:
                    ans.extend( [seq for seq in layer[word]] )
                for next_w in word_list_one_off[word] :
                    if next_w in wordList:
                        new_layer[next_w] += [seq + [next_w] for seq in layer[word]]

            wordList -= set(new_layer.keys())
            layer = new_layer
        return ans
```

