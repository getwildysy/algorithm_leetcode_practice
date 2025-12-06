# NumPy: 數值計算基礎

NumPy (Numerical Python) 是 Python 科學計算的核心庫，提供了高效的多維陣列物件 (ndarray) 以及用於處理這些陣列的工具。

## 1. 安裝

```bash
pip install numpy
```

## 2. 建立陣列 (ndarray)

NumPy 陣列比 Python 的 List 更快、更省記憶體，且支援向量化運算。

```python
import numpy as np

# 從 List 建立
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr)) # <class 'numpy.ndarray'>

# 建立特定陣列
zeros = np.zeros(5)          # [0. 0. 0. 0. 0.]
ones = np.ones((2, 3))       # 2x3 全為 1 的矩陣
range_arr = np.arange(0, 10, 2) # [0 2 4 6 8] (類似 range)
linspace = np.linspace(0, 1, 5) # [0.   0.25 0.5  0.75 1.  ] (均分)
```

## 3. 陣列運算 (向量化)

不需要寫迴圈，直接對整個陣列進行運算。

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b) # [5 7 9]
print(a * 2) # [2 4 6]
print(a ** 2) # [1 4 9]
print(a > 2) # [False False True] (布林遮罩)
```

## 4. 索引與切片

```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])

print(matrix[0, 1]) # 2 (第 0 列，第 1 行)
print(matrix[:, 1]) # [2 5] (取所有列的第 1 行)
```

## 5. 常用統計函式

```python
arr = np.array([1, 2, 3, 4, 5])

print(np.mean(arr))   # 平均值
print(np.sum(arr))    # 總和
print(np.max(arr))    # 最大值
print(np.std(arr))    # 標準差
```
