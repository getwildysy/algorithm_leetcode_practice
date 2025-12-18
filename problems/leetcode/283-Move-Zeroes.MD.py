from typing import List

class WrongSolution:
    def moveZeroes(self, nums: List[int]) -> None:
        nums_1, nums_2 = [], []
        for i in range(len(nums)):
            if nums[i] != 0:
                nums_1.append(nums[i])
            else:
                nums_2.append(nums[i])
        # 這是你原本的寫法：這只會讓 nums 變數指向一個新的記憶體位置
        # 外部原本傳進來的那個 List 不會被改變
        nums = nums_1 + nums_2 

class CorrectSolution:
    def moveZeroes(self, nums: List[int]) -> None:
        nums_1, nums_2 = [], []
        for i in range(len(nums)):
            if nums[i] != 0:
                nums_1.append(nums[i])
            else:
                nums_2.append(nums[i])
        # 正確寫法：使用切片 [:] 賦值，會將資料填入「原本的記憶體位置」
        nums[:] = nums_1 + nums_2

# 模擬 LeetCode 的檢查機制
def test_leetcode():
    # 測試原本的寫法
    wrong = WrongSolution()
    test_data = [0, 1, 0, 3, 12]
    print(f"原本資料: {test_data}")
    wrong.moveZeroes(test_data)
    print(f"原本寫法執行後 (LeetCode 看到的結果): {test_data}")
    if test_data == [0, 1, 0, 3, 12]:
        print("-> 失敗！資料沒有變動.\n")
    
    # 測試修正後的寫法
    correct = CorrectSolution()
    test_data_2 = [0, 1, 0, 3, 12]
    correct.moveZeroes(test_data_2)
    print(f"修正寫法執行後 (LeetCode 看到的結果): {test_data_2}")
    if test_data_2 == [1, 3, 12, 0, 0]:
        print("-> 成功！資料已原地修改。")

if __name__ == "__main__":
    test_leetcode()
