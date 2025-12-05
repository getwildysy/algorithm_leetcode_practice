names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# 寫法：注意 for 迴圈裡的括號 (name, score)
for i, (name, score) in enumerate(zip(names, scores)):
    print(f"第 {i+1} 名: {name} 考了 {score} 分")
