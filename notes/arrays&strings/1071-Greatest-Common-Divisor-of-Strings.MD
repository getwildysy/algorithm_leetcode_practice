# 題目名稱

Merge Strings Alternately

## 題目類型

## 題目摘要

https://leetcode.com/problems/greatest-common-divisor-of-strings/description/

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"

Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"

Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"

Output: ""

Example 4:

Input: str1 = "AAAAAB", str2 = "AAA"

Output: ""

## 我的解題思路

1.想到最原先的方法是將兩個字串合併，然後找出＂最小重複單元＂，但是這個想法錯誤，題目是要找出「最大」公因單元。測資失敗。（２０２５１２１６）。 2.正確解法為
(1) 如果有最大公因字串，則 str1+str2 一定會等於 str2+str1，不等於的話直接回傳""。

(2)接下來可以用:
(i) 暴力法:
先找出兩個字串中哪個字數最少(base)，然後看另一個字串的字數是不是 base 的整數倍，如果不是的話，則移除 base 的最後一個字元當成新 base，繼續搜尋，如果是的話，看目前的 str1 跟 str2 是不是 base 的整數倍，是的話，將 base 乘以長度被整除的除數，並檢查產生的字串數否等於 str。

    (ii)gcd法

## 程式碼

[解法:link](../../problems/leetcode/1071-Greatest-Common-Divisor-of-Strings.py)

解法:

一、最簡方法:

```python
import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 1. 檢查拼接是否相等
        if (str1 + str2) != (str2 + str1):
            return ""

        # 2. 利用 math.gcd 計算最大公因數長度
        # 注意：math.gcd 是 Python 3 的標準庫函數
        gcd_length = math.gcd(len(str1), len(str2))

        # 3. 回傳該長度的前綴字串
        return str1[:gcd_length]
```

二、暴力法:

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def valid(k):
            if len1 % k or len2 % k:
                return False
            n1, n2 = len1 // k, len2 // k
            base = str1[:k]
            return str1 == n1 * base and str2 == n2 * base

        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]
        return ""

```
