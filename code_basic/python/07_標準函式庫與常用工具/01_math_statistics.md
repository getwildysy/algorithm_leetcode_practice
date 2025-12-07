# 數學與統計 (`math` & `statistics`)

## 1. `math` 模組

提供標準的數學函式。

```python
import math

# 常數
print(math.pi)  # 3.14159...
print(math.e)   # 2.71828...

# 數值處理
print(math.ceil(3.1))   # 4 (無條件進位)
print(math.floor(3.9))  # 3 (無條件捨去)
print(math.trunc(3.9))  # 3 (截斷小數)
print(math.fabs(-5))    # 5.0 (絕對值 float)

# 冪與對數
print(math.pow(2, 3))   # 8.0 (2 的 3 次方)
print(math.sqrt(16))    # 4.0 (開根號)
print(math.log(100, 10)) # 2.0 (以 10 為底的對數)

# 三角函式 (輸入為弧度)
print(math.sin(math.pi / 2)) # 1.0
print(math.degrees(math.pi)) # 180.0 (弧度轉角度)
```

## 2. `statistics` 模組

Python 3.4+ 新增，用於基本的統計計算。

```python
import statistics

data = [1, 2, 3, 4, 4, 5, 100]

# 平均數 (Mean)
print(statistics.mean(data)) 

# 中位數 (Median) - 中間那個數，不受極端值影響
print(statistics.median(data)) # 4

# 眾數 (Mode) - 出現最多次的數
print(statistics.mode(data))   # 4

# 標準差 (Standard Deviation)
print(statistics.stdev(data))

# 變異數 (Variance)
print(statistics.variance(data))
```
