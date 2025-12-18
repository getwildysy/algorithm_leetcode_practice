# 題目名稱

Merge Strings Alternately

## 題目類型

Two Pointers
String

## 題目摘要

https://leetcode.com/problems/merge-strings-alternately/description/

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1: a b c
word2: p q r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1: a b
word2: p q r s
merged: a p b q r s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1: a b c d
word2: p q
merged: a p b q c d

## 我的解題思路

## 程式碼

[解法:link](../../problems/leetcode/1768-Merge-Strings-Alternately.py)

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        n1 = len(word1)
        n2 = len(word2)
        i = 0
        while i < n1 or i < n2:
            if i < n1:
                merged.append(word1[i])
            if i < n2:
                merged.append(word2[i])
            i = i+1
        return "".join(merged)


```
