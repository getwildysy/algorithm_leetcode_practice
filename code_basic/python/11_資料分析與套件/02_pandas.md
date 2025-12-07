# Pandas: 資料處理與分析

Pandas 建立在 NumPy 之上，提供了強大的資料結構 `Series` (一維) 和 `DataFrame` (二維，類似 Excel 表格)，讓資料清洗和分析變得非常容易。

## 1. 安裝

```bash
pip install pandas
```

## 2. 建立 DataFrame

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}

df = pd.DataFrame(data)
print(df)
```

## 3. 資料讀取與寫入

Pandas 支援 CSV, Excel, JSON, SQL 等多種格式。

```python
# 讀取 CSV
# df = pd.read_csv('data.csv')

# 寫入 CSV
# df.to_csv('output.csv', index=False)
```

## 4. 查看資料

```python
print(df.head())      # 看前 5 筆
print(df.info())      # 查看資料型別、缺漏值
print(df.describe())  # 數值欄位的基本統計 (平均、標準差等)
```

## 5. 資料選取

```python
# 選取單一欄位 (回傳 Series)
print(df['Name'])

# 選取多欄位 (回傳 DataFrame)
print(df[['Name', 'Age']])

# 條件篩選 (Filtering)
adults = df[df['Age'] > 28]
print(adults)
```

## 6. 資料處理

```python
# 新增欄位
df['Is_Adult'] = df['Age'] >= 18

# 刪除欄位
df = df.drop(columns=['City'])

# 處理缺漏值
# df.dropna() # 刪除有空值的列
# df.fillna(0) # 將空值填為 0
```
