import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 1. 檢查拼接是否相等
        if (str1 + str2) != (str2 + str1):
            return ""

        # 2. 利用 math.gcd 計算最大公因數長度
        # 注意：math.gcd 是 Python 3 的標準庫函數
        gcd_length = math.gcd(len(str1), len(str2))

        # 3. 回傳該長度的前綴字串
        return str1[:gcd_length]
