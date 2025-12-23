from typing import List, Optional

# ==========================================
# 題目編號：
# 題目名稱：
# ==========================================


class Solution:
    def solveProblem(self, nums: List[int], target: int) -> List[int]:
        """
        在這裡貼上 LeetCode 上的解題邏輯
        """
        # 範例邏輯：Two Sum
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
        return []


# ==========================================
# 本機測試區 (Local Test Bench)
# ==========================================
if __name__ == "__main__":
    # 實例化解答類別
    sol = Solution()

    # 定義測試資料：(輸入資料, 預期結果)
    test_cases = [
        ({"nums": [2, 7, 11, 15], "target": 9}, [0, 1]),
        ({"nums": [3, 2, 4], "target": 6}, [1, 2]),
        ({"nums": [3, 3], "target": 6}, [0, 1]),
    ]

    print(f"--- [Local Test Started] ---")
    for i, (inputs, expected) in enumerate(test_cases):
        # 呼叫你的方法 (根據題目更改方法名稱)
        result = sol.solveProblem(**inputs)

        # 驗證結果
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"Case {i+1}: {status}")
        if status == "❌ FAIL":
            print(f"   Input: {inputs}")
            print(f"   Expected: {expected}, but got: {result}")
    print(f"---------------------------")
