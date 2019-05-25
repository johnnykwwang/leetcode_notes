---
layout: post
title: "EPI Chapter 4.1~4.5: Bits-Manipulation"
date: "2019-05-24 23:14:09 -0400"
mathjax: true
---

This is a note from the book "Elements of Programming Interviews in Python"

Covering Topics: **Bits Manipulation**

<!--more-->

# Bits Manipulation

Bitwise operations are one of the weirdest topics in coding problems.  If not prepared, these all seems like sorcery.

## List of Techniques and Concepts

If you're too lazy to read through, here is the summary:

| **Operation** | **What you'll get** |
| `x & 1`     | `x`'s last bit  |
| `x >> 1`    | `x/2`, or `x` right-shifted by 1 bit |
|`x & (x-1)`  |  `x` with its rightmost `1` erased. |
|`x & ~(x-1)` | get only the rightmost `1` of `x`  |

| **Concepts** | 
| Don't think of bits as list of integers, think of them as a **row of switches** |
| Think of a **XOR** b  as flipping a at where b is set to `1`|

## Intro: Counting Bits

*Problem: Write a program to count the number of bits that are set to `1` in an unsigned integer*

Naive Solution: 

```python
def count_bits(x):
    c = 0
    while x:
        c += x & 1
        x >>= 1
    return c
```

Time: $O(n)$ where $n$ is # of bits of the input.

How can we do better?

Introducing bits sorcery #1: `x & (x-1)` equals `x` with its rightmost `1` erased.

We can use this and rewrite as:

```python
def count_bits(x):
    c = 0
    while x:
        x &= (x-1)
        c += 1
    return c
```

This becomes $O(k)$ where $k$ is # of bits that are set to 1 in the input.

---

## Example: Parity

*Problem: Given an unsigned integer `x`, if the # of set bits are old, the parity is `1`, else it's `0`.  Write a program to output the parity of `x`.*

### Brute Force
Iterate through every bit of `x`

```python
def parity(x):
    p = 0
    while x:
        p ^= x & 1
        x >>= 1
    return p
```

### Apply the x & (x-1) trick 
Iterate through every set bit of `x`

```python
def parity(x):
    p = 0
    while x:
        x &= (x-1)
        p ^= 1
    return p
```

Now, say we not only want to compute the parity of a single integer, but **a lot of** unsighed 64-bit integers.

How can we do better?

### Utilize Pre-Computed Parity

First, we know that since we'll have a lot of integers to calculate parity, we can store some of the parity results.

But storing all `2^64` parity results seems too many.  How about we store the results of all 16-bits ?

By splitting every integers with 64 bits into 4 16-bit block, we can then XOR their parity to get the answer.

```python
def parity(x, pre_computed):
    mask_size = 16
    mask = 0xFFFF
    return pre_computed[ (x >> 3 * mask_size) ] ^
           pre_computed[ (x >> 2 * mask_size) & mask ] ^
           pre_computed[ (x >> 1 * mask_size) & mask ] ^
           pre_computed[ x & mask ] 
```

### Utilize XOR 

Now, think of parity in this way:  `11010111` has a parity of 0, we can split it to `1101` and `0111`.  Now, if we XOR these two blocks, we get `1010`, which has the same parity.  

The intuitive explaination is, **think of XORing two things as cancelling out the same bits**, so if the corresponding bits are both `0` or `1`, we can just set it to zero, since in the parity scenario it doesn't matter if the count of `1` is `4` or `2`.

So we can repetitively shrink down the length by factor of 2, which gives us a complexity of $O(log(n))$, where n is the word size of the integer.

```python
def parity(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1
```

---

## Practices

Write the following programs using bits-manipulation and in $O(1)$ time.

* *Right Propagation: Given `x`, return the integer that flips all of the zeros at the right of the rightmost `1`*
    * For example if x is `01010000`, return `01011111`

```python
def right_propagate(x):

    x_without_right_bit = x & (x-1)
    right_bit = x & ~(x-1)
    right_propogate = ( right_bit << 1 ) - 1

    return x_without_right_bit + right_propogate
```

* *Test Power of 2: Given `x`, return if the integer is a power of `2`, like `64`, `256`, ...*

```python
def test_if_power_of_2(x):
    return x&(x-1) == 0
```

---

## Example: Swap Bits

*Problem: Given an unsigned integer `x`, bit positions `i` and `j`, swap the bits of `x` in `i` and `j` and return the integer after swapping.*

Here, the naive way would be to use bitmask to extract i-th and j-th bit and swap them, but here we can consider a few things:

1. Consider bits as switches, if bit at `i` and at `j` are the same value, we don't even need to switch.
2. When we need to switch, it's just flipping their values, can be done using XOR.

Therefore we have our $O(1)$ way to swap bits, independent of word size.

```python
def swap_bits(x,i,j):
    if ( ( x>>i ) & 1 ) ^ ( ( x>>j ) & 1 ):
        # Need to swap.
        xor_mask = ( 1 << i ) | ( 1 << j ) 
        x ^= xor_mask
    return x
```


## Example: Reverse Bits

*Problem: Given an unsigned 64-bit integer `x`, reverse its bit and output the result integer.*

*Problem ( Follow-Up ): What if there are a lot of integers?*

This is kind of merging the concepts in swap bits and parity.  If we only need to do 1 integer, we can just swap 32 times.

But if we will need to do a lot of integers, we can use the same split-and-cache technique.  For every 16-bit block, we store each of these block's reverse.

```python
def reverse_bits(x, precomputed_reverse):
    mask_size = 16
    mask = 0xFFFF 
    # x = [ p4 p3 p2 p1 ]
    p1 =  precomputed_reverse[ x & mask ] << 3 * mask_size
    p2 =  precomputed_reverse[ (x >> mask_size) & mask ] << 2 * mask_size
    p3 =  precomputed_reverse[ (x >> 2*mask_size) & mask ] << 1 * mask_size
    p4 =  precomputed_reverse[ (x >> 3*mask_size) & mask ]
    return p1 | p2 | p3 | p4
```









