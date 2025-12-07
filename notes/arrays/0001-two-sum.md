# 題目名稱

Two Sum

## 題目類型

Array/ Hash Map

## 題目摘要

https://leetcode.com/problems/two-sum/description/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

## 我的解題思路

起先我先暴力使用暴力搜尋，但是耗掉的時間太多，複雜度是 logn^2
接下來是看到提示可以使用 hash 表，複雜度可以降到 logn，但是要考慮到 hash 表內，有重複元素而且是答案的處理方式。

## 程式碼

[解法:link](../../problems/leetcode/0001-two-sum.py)

解法一: 暴力搜尋法

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]+nums[j] == target:
                    return [i, j]
```

解法二: 使用 hash 表

```python
        l = len(nums)
        hash_map = {}

        # 建 hash map
        for i, num in enumerate(nums):
            if num not in hash_map:
                hash_map[num] = []
            hash_map[num].append(i)

        # 找答案
        for i in range(l):
            diff = target - nums[i]

            # 情況 1：diff == nums[i] → 需要至少兩個 index
            if diff == nums[i]:
                if len(hash_map[diff]) >= 2:
                    # 找到另一個 index
                    for idx in hash_map[diff]:
                        if idx != i:
                            return [i, idx]

            # 情況 2：diff != nums[i]
            elif diff in hash_map:
                return [i, hash_map[diff][0]]

        return []

```
