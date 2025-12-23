import sys
import os

# ==========================================
# 題目編號：(例如 a001)
# 題目名稱：
# ==========================================


def solve():
    """
    主要邏輯寫在這裡
    """
    # 使用 sys.stdin.read().split() 可以一次讀入所有內容並按空白/換行切分
    # 或者使用 sys.stdin 進行逐行讀取
    for line in sys.stdin:
        try:
            # 範例1：讀取一行內的多個整數
            data = list(map(int, line.split()))
            # 範例2:通用，包含文字的話
            # data = list(line.split())

            if not data:
                break

            # --- 邏輯開始 ---
            print(f"讀取到的內容: {data}")

            # --- 邏輯結束 ---

        except EOFError:
            break


if __name__ == "__main__":
    # --- 本機測試功能 ---
    # 如果資料夾內有 input.txt，則自動讀取該檔案作為輸入
    # 這樣你在練習時，只需把測資貼在 input.txt，直接執行即可
    if os.path.exists('input.txt'):
        sys.stdin = open('input.txt', 'r', encoding='utf-8')
        print(f"--- [Local Test Mode: Reading from input.txt] ---")

    solve()
