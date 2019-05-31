---
layout: post
title: "Best Time to Buy and Sell Stock (121, 122, 123)"
date: "2019-05-30 21:02:37 -0700"
---

There are 3 very similar problems we can cover together.

<!--more-->

# 121. Best Time to Buy and Sell Stock

<p>Say you have an array for which the <em>i</em><sup>th</sup> element is the price of a given stock on day <em>i</em>.</p>

<p>If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.</p>

<p>Note that you cannot sell a stock before you buy one.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [7,1,5,3,6,4]
<strong>Output:</strong> 5
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
&nbsp;            Not 7-1 = 6, as selling price needs to be larger than buying price.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transaction is done, i.e. max profit = 0.
</pre>

## Solutions

This is very straightforward.  The maximum profit is the lowest price **we've seen so far** and the highest price that comes after the lowest price.  So in each iteration, we keep update the lowest price and the highest profit we can gain.

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0
        lowest = prices[0]
        max_profit = 0

        for p in prices:
            lowest = min(lowest, p)
            max_profit = max(max_profit, p-lowest)

        return max_profit
```

---

# 122: Best Time to Buy and Sell Stock II

<p>Say you have an array for which the <em>i</em><sup>th</sup> element is the price of a given stock on day <em>i</em>.</p>

<p>Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).</p>

<p><strong>Note:</strong> You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [7,1,5,3,6,4]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
&nbsp;            Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [1,2,3,4,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
&nbsp;            Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
&nbsp;            engaging multiple transactions at the same time. You must sell before buying again.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transaction is done, i.e. max profit = 0.</pre>

## Solutions

This is actually just greedy search.  Whenever a price drop, we sell before it drops.  When the price is rising we keep the stock at hand.

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        holding = None
        holding_buy_price = None
        profit = 0
        for p in prices:
            if holding is None:
                holding_buy_price = p
                holding = p
                continue
            if p>holding:
                #dont sell
                holding = p
            else:
                #sell
                profit += max(holding-holding_buy_price,0)
                holding_buy_price, holding = p, p
        if holding:
            profit += holding-holding_buy_price
        return profit
```

---

# 123: Best Time to Buy and Sell Stock III

<p>Say you have an array for which the <em>i</em><sup>th</sup> element is the price of a given stock on day <em>i</em>.</p>

<p>Design an algorithm to find the maximum profit. You may complete at most <em>two</em> transactions.</p>

<p><strong>Note:&nbsp;</strong>You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [3,3,5,0,0,3,1,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
&nbsp;            Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [1,2,3,4,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
&nbsp;            Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
&nbsp;            engaging multiple transactions at the same time. You must sell before buying again.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transaction is done, i.e. max profit = 0.</pre>

## Solutions

I personally think this is the hardest one to understand.  The approach to this is use a simple two-pass.  

* In the first pass, we calculate a `F[i]` which is the maximum profit we can get in each day with only 1 transation.
* In the second pass, we work backward, but still calculate the maximum profit we can gain if we do transation after day i.  This gives us `B[i]`
* Combine them via `Total[i]=F[i-1]+B[i]` because we need to avoid selling first stock and buying second stock on the same day.

We can see the example below:
![image](https://user-images.githubusercontent.com/13166286/58681212-57fe8180-8320-11e9-8640-412c0ee68c68.png){:.ctr-img}


```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        max_total_profit = 0
        min_price_so_far = 2**32
        first_buy_profit = [0] * len(prices)

        for i, p in enumerate(prices):
            # print min_price_so_far
            min_price_so_far = min(p, min_price_so_far)
            max_total_profit = max(max_total_profit, p-min_price_so_far)
            first_buy_profit[i] = max_total_profit

        max_price_so_far = - (2**32)
        print first_buy_profit
        for i,p in enumerate(prices[1:][::-1]):
            _i = len(prices)-i-1
            max_price_so_far = max(max_price_so_far, p)
            max_total_profit = max( max_total_profit, max_price_so_far - p + first_buy_profit[_i-1] )
        return max_total_profit
```




