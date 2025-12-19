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
        print(max_sum / k)


if __name__ == '__main__':
    s = Solution()
    nums = [9, 7, 3, 5, 6, 2, 0, 8, 1, 9]
    s.findMaxAverage(nums, 6)
