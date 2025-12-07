# Matplotlib: 資料視覺化

Matplotlib 是 Python 最基礎的繪圖庫，`pyplot` 模組提供了類似 MATLAB 的繪圖介面。

## 1. 安裝

```bash
pip install matplotlib
```

## 2. 繪製折線圖 (Line Plot)

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, label='y = 2x', color='blue', marker='o')

plt.title("Simple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend() # 顯示圖例
plt.grid(True) # 顯示網格

plt.show() # 顯示圖表
```

## 3. 繪製散佈圖 (Scatter Plot)

```python
plt.scatter(x, y, color='red')
plt.title("Scatter Plot")
plt.show()
```

## 4. 繪製長條圖 (Bar Chart)

```python
categories = ['A', 'B', 'C']
values = [10, 20, 15]

plt.bar(categories, values, color=['red', 'green', 'blue'])
plt.title("Bar Chart")
plt.show()
```

## 5. 繪製直方圖 (Histogram)

用於顯示資料分佈。

```python
import numpy as np
data = np.random.randn(1000) # 1000 個常態分佈亂數

plt.hist(data, bins=30, alpha=0.7)
plt.title("Histogram")
plt.show()
```

## 6. 中文顯示問題

Matplotlib 預設字體不支援中文，需手動設定。

```python
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] # 設定微軟正黑體
plt.rcParams['axes.unicode_minus'] = False # 解決負號顯示問題
```
