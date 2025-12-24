# 題目名稱

Can Place Flowers

## 題目類型

Array

## 題目摘要

https://leetcode.com/problems/can-place-flowers/description/

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

## 我的解題思路

1. 我的想法是(如解法 1)掃描一次陣列中有幾個連續的 0，將數字存入一個陣列 ZERO_COUNT[]，才能種下一朵。
2. 因為首位或最終位置是 0 可能會掃不到，所以需要在首尾補上 0，讓首位跟最終位置如果是 00，也可以種。
3. 連續幾個 0 能種 N 棵，會有個公式 n= [(K-1)/2]，
4. Ai 的解法是用貪婪演算法 (Greedy Algorithm)，只要連續看到三個空位或邊界，就直接種下一朵花。
5. 要在索引 i 的位置種花，必須同時滿足以下三個條件：

(1). 該位置本身是空的：flowerbed[i] == 0

(2). 左邊是空的（或是起點）：i == 0 或 flowerbed[i - 1] == 0

(3). 右邊是空的（或是終點）：i == len(flowerbed) - 1 或 flowerbed[i + 1] == 0

## 程式碼

[解法:link](../../problems/leetcode/2215-Find-the-Difference-of-Two-Arrays.py)

(一)、 自己的解法

```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        count = 0        # 目前連續 0 的數量
        zero_blocks = []  # 用來存每一段 0 的長度

        padded_flowerbed = [0] + flowerbed + [0]
        for num in padded_flowerbed:
            if num == 0:
                count += 1
            else:
                # 遇到 1 了，檢查剛才累積了幾個 0
                if count > 0:
                    zero_blocks.append(count)  # 紀錄長度
                count = 0  # 重要：歸零！

  # 迴圈結束後，如果陣列結尾是 0，因為沒觸發到儲存count的區塊，所以要補做最後一次結算
        if count > 0:
            zero_blocks.append(count)
  # 連續0的數量假設為k，能種植花的數量為 k-1//2

        can_place = [(k-1)//2 for k in zero_blocks]

        if n <= sum(can_place):
            return (True)
        else:
            return (False)

```

(二)、 google gemini 解法

```python
def canPlaceFlowers(flowerbed, n):
    count = 0
    length = len(flowerbed)

    for i in range(length):
        # 檢查當前位置是否為 0
        if flowerbed[i] == 0:
            # 判斷左邊是否符合條件 (如果是索引 0，視為左邊有空位)
            prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
            # 判斷右邊是否符合條件 (如果是最後一個索引，視為右邊有空位)
            next_empty = (i == length - 1) or (flowerbed[i + 1] == 0)

            if prev_empty and next_empty:
                # 種花！
                flowerbed[i] = 1
                count += 1

                # 如果已經種夠了，提早結束
                if count >= n:
                    return True

    return count >= n
```
