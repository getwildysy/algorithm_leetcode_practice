from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_1, nums_2 = [], []

        for i in range(len(nums)):
            if nums[i] != 0:
                nums_1.append(nums[i])
            else:
                nums_2.append(nums[i])
        
        # 使用切片賦值 (Slice Assignment) 來修改原始 List
        nums[:] = nums_1 + nums_2

if __name__ == "__main__":
    solution = Solution()
    test_nums = [0, 1, 0, 3, 12]
    print(f"Before: {test_nums}")
    solution.moveZeroes(test_nums)
    print(f"After:  {test_nums}")
