from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

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


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))  # Expected: [0, 1]
    print(s.twoSum([3, 2, 4], 6))       # Expected: [1, 2]
    print(s.twoSum([3, 3], 6))          # Expected: [0, 1]
    # s.twoSum([3, 1, 4, 3], 6)          # Expected: [0, 1]
    # s.twoSum([3, 2, 4], 6)
