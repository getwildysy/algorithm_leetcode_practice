# 題目名稱

Find the Difference of Two Arrays

## 題目類型

Hash \_table

## 題目摘要

https://leetcode.com/problems/find-the-difference-of-two-arrays/description/

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]

Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].

For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not
present in nums1. Therefore, answer[1] = [4,6].

Example 2:

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].

## 我的解題思路

1. 先將兩個 nums 建立 hash table，有兩種建立方式(1)字典形式 (2)集合形式。
2. 使用字典要注意需要將值當成 key，value 隨便設定都行(不會用到)
3. 依據建立的形式，搜尋的方式會不同，要注意重複的數字。

## 程式碼

[解法:link](../../problems/leetcode/2215-Find-the-Difference-of-Two-Arrays.py)

(一)、 使用字典

```python
    def findDifference(self, nums1, nums2):

        hash_nums1, hash_nums2 = {},  {}
        answer1, answer2 = [], []
        # 建 hash map，用nums的值當作字典的鍵，字典的值為True,(或是任何東西都可以，不會用到)
        hash_nums1 = {val: True for val in nums1}
        hash_nums2 = {val: True for val in nums2}

        for key in nums1:
            if key not in hash_nums2:
                answer1.append(key)
        for key in nums2:
            if key not in hash_nums1:
                answer2.append(key)

        print([answer1, answer2])


```

(二)、 使用集合

```python
def findDifference(self, nums1, nums2):
        # 將列表轉為集合，自動去重，且查詢時間複雜度為 O(1)
        set1 = set(nums1)
        set2 = set(nums2)

        # 使用集合運算的「差集」
        ans1 = list(set1 - set2)
        ans2 = list(set2 - set1)

        return [ans1, ans2]
```
