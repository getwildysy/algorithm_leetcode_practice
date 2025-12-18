# 題目名稱

Move Zeroes

## 題目類型

Two Pointers

## 題目摘要

https://leetcode.com/problems/move-zeroes/description

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

## 我的解題思路

1. 遍歷兩個數字串列，將值 !=0 的寫在 list_1；值==0 的寫在 list_2
   接下來將兩個串列合併，但是空間複雜度會太大，寫法較差。
2. 正規寫法，訂兩個指標 fast(i)、slow(j)，j 代表找到 0 之後，目前最後一個 0 的指標。
   用 i 搜尋串列，
   如果 list[i] != 0 ，則 swap (list[i],list[j]),j+1,如果 list[i]==0，j 不動。

## 程式碼

[解法:link](../../problems/leetcode/283-Move-Zeroes.MD.py)

解法１：較慢，不推薦。

```python
class CorrectSolution:
    def moveZeroes(self, nums: List[int]) -> None:
        nums_1, nums_2 = [], []
        for i in range(len(nums)):
            if nums[i] != 0:
                nums_1.append(nums[i])
            else:
                nums_2.append(nums[i])
        # 正確寫法：使用切片 [:] 賦值，會將資料填入「原本的記憶體位置」
        nums[:] = nums_1 + nums_2

```

解法２：空間複雜度較小，推薦

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow = slow+1

```
