from typing import List, Optional


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result1 = [x + extraCandies for x in candies]
        result2 = [x >= max_candies for x in result1]

        return (result2)


# ==========================================
# 本機測試區 (Local Test Bench)
# ==========================================
if __name__ == "__main__":
    # 實例化解答類別
    sol = Solution()

    # 定義測試資料：(輸入資料, 預期結果)
    print(sol.kidsWithCandies([4, 2, 1, 1, 2], 1))
