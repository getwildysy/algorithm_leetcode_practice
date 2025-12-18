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
        nums = nums_1+nums_2
