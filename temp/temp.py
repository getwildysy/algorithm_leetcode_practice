class Solution:
    def findMaxAverage(self, nums, k):
        total, max, avg = 0, 0, 0
        total = sum(nums[:k])
        if len(nums) == k:
            max = total

        else:
            for i in range(1, len(nums)-k+1):
                total = total-nums[i-1]+nums[i+k-1]
                if total >= max:
                    max = total
        avg = max / k
        print(avg)


if __name__ == '__main__':
    s = Solution()
    nums = [9, 7, 3, 5, 6, 2, 0, 8, 1, 9]
    s.findMaxAverage(nums, 6)
