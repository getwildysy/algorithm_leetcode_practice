from typing import List, Optional


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0        # 目前連續 0 的數量
        zero_blocks = []  # 用來存每一段 0 的長度
       # 核心技巧：在前後各補一個 0，把邊界問題變成中間問題
        # 這樣無論是 [0,0,1] 還是 [1,0,0]，都會被當作中間有連續 0 的情況處理
        padded_flowerbed = [0] + flowerbed + [0]
        for num in padded_flowerbed:
            if num == 0:
                count += 1
            else:
                # 遇到 1 了，檢查剛才累積了幾個 0
                if count > 0:
                    zero_blocks.append(count)  # 紀錄長度
                count = 0  # 重要：歸零！

  # 迴圈結束後，如果陣列結尾是 0，因為沒觸發到儲存count的區塊，所以要補做最後一次結算
        if count > 0:
            zero_blocks.append(count)
  # 連續0的數量假設為k，能種植花的數量為 k-1//2

        can_place = [(k-1)//2 for k in zero_blocks]

        if n <= sum(can_place):
            return (True)
        else:
            return (False)

    # return []


# ==========================================
# 本機測試區 (Local Test Bench)
# ==========================================
if __name__ == "__main__":
    # 實例化解答類別
    sol = Solution()
    flowerbed = [1, 0, 0, 0, 1, 0, 0, 1]
    # 定義測試資料：(輸入資料, 預期結果)
    print(sol.canPlaceFlowers(flowerbed, 5))
