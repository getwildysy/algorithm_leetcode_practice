# 題目名稱

     Maximum Average Subarray I

## 題目類型

Sliding Window

## 題目摘要

https://leetcode.com/problems/maximum-average-subarray-i/

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000

## 我的解題思路

    使用滑動視窗，先設定max=sum[:k]，然後用for迴圈踢掉舊的，加入新的，如果值比max大，則取代max。

## 程式碼

[解法:link](../../problems/leetcode/0643-Maximum-Average-Subarray.py)

```python
class Solution:
    def findMaxAverage(self, nums, k):
        # 1. 先計算第一個視窗的和
        current_sum = sum(nums[:k])
        # 2. 將最大值初始化為第一個視窗的和（解決全負數問題）
        max_sum = current_sum

        # 3. 從索引 k 開始滑動到結尾
        for i in range(k, len(nums)):
            # 滑動視窗：加上新元素 nums[i]，減去舊元素 nums[i-k]
            current_sum = current_sum + nums[i] - nums[i-k]
            # 更新最大值
            if current_sum > max_sum:
                max_sum = current_sum

        # 4. 最後再除以 k 得到平均值
        return (max_sum / k)
```
