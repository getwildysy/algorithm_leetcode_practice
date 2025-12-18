class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow = slow+1
        print(nums)


if __name__ == '__main__':
    s = Solution()
    list_a = [0, 1, 0, 3, 12]
    s.moveZeroes(list_a)
