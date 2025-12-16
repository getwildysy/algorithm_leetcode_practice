

def find_repeat_pattern(str):
    # 將字串加倍：ABCABCABCABC
    double_str = str+str

    # 去掉第一個字元與最後一個字元，避免直接找到原本的自己
    # 然後找尋 s 第一次出現的位置
    # index 就是理論上重複單元的長度(因為跳過第一個字元)
    index = double_str.find(str, 1)

    if index != -1 and index < len(str):
        return str[:index]
    else:
        return str  # 如果沒有重複模式，回傳原字串


str = "ABAB"

print(find_repeat_pattern(str))
