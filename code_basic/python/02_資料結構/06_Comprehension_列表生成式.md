# 列表生成式 (List Comprehension)

列表生成式是 Python 提供的一種簡潔、優雅且高效的方式，用於從一個序列建立新的列表。它通常比傳統的 `for` 迴圈更具可讀性且執行速度更快。

## 1. 基本語法

```python
# [表達式 for 項目 in 可迭代物件]
```

### 範例：計算平方

```python
# 傳統寫法
squares = []
for x in range(10):
    squares.append(x**2)

# 生成式寫法
squares = [x**2 for x in range(10)]
# 結果: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## 2. 帶有條件的生成式

可以在後面加上 `if` 來過濾元素。

```python
# [表達式 for 項目 in 可迭代物件 if 條件]
```

### 範例：只取偶數

```python
evens = [x for x in range(10) if x % 2 == 0]
# 結果: [0, 2, 4, 6, 8]
```

### 範例：巢狀條件 (if...else)

如果要根據條件改變**值**，則 `if...else` 寫在 `for` 前面。

```python
# 偶數保持不變，奇數變負數
result = [x if x % 2 == 0 else -x for x in range(5)]
# 結果: [0, -1, 2, -3, 4]
```

## 3. 其他生成式

除了列表，Python 也支援字典和集合的生成式。

### 字典生成式 (Dict Comprehension)

```python
# 建立一個 {數字: 平方} 的字典
squares_dict = {x: x**2 for x in range(5)}
# 結果: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### 集合生成式 (Set Comprehension)

```python
# 類似列表生成式，但使用 {}
unique_squares = {x**2 for x in [1, -1, 2, -2]}
# 結果: {1, 4} (自動去重)
```

### 生成器表達式 (Generator Expression)

如果數據量很大，不希望一次產生所有列表元素佔用記憶體，可以使用小括號 `()` 建立生成器。

```python
gen = (x**2 for x in range(1000000))
print(gen) # <generator object ...>

# 可以透過 next() 或 for 迴圈取值
print(next(gen)) # 0
print(next(gen)) # 1
```

## 4. 巢狀迴圈生成式 (Nested)

```python
# 產生 (x, y) 座標組合
points = [(x, y) for x in range(3) for y in range(2)]
# 結果: [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
```

這等同於：

```python
points = []
for x in range(3):
    for y in range(2):
        points.append((x, y))
```
