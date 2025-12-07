# Python 元組 (Tuple)

元組 (Tuple) 與列表非常相似，但它是**不可變的 (Immutable)**。一旦建立，就不能修改、新增或刪除元素。通常用於儲存不應該被改變的資料，或作為函式的回傳值。

## 1. 建立元組

使用小括號 `()`。

```python
# 空元組
empty = ()

# 多個元素
point = (10, 20)

# 單一元素 (必須加逗號，否則會被視為括號運算)
single = (1,) 
not_tuple = (1) # 這只是整數 1

# 省略括號 (Packing)
coords = 10, 20, 30 
```

## 2. 不可變特性

```python
t = (1, 2, 3)

# t[0] = 10 # TypeError: 'tuple' object does not support item assignment
```

但是，如果 Tuple 包含可變物件 (如 List)，該物件的內容是可以修改的。

```python
t_mutable = (1, [2, 3])
t_mutable[1].append(4)
print(t_mutable) # (1, [2, 3, 4])
```

## 3. 解包 (Unpacking)

可以將 Tuple 的元素直接賦值給變數。

```python
coordinates = (4, 5)
x, y = coordinates
print(x) # 4
print(y) # 5

# 交換變數值
a = 10
b = 20
a, b = b, a # Python 經典寫法
```

使用 `*` 收集剩餘元素：

```python
nums = (1, 2, 3, 4, 5)
first, *rest, last = nums
print(first) # 1
print(rest)  # [2, 3, 4]
print(last)  # 5
```

## 4. Tuple 的優勢

1.  **安全性**：保證資料不會被意外修改。
2.  **效能**：由於不可變，Tuple 的迭代速度比 List 稍快，且佔用記憶體較少。
3.  **作為字典的 Key**：Tuple 是可雜湊的 (Hashable)，可以用作 Dictionary 的 Key，而 List 不行。

```python
locations = {
    (40.71, -74.00): "New York",
    (35.68, 139.76): "Tokyo"
}
```

## 5. 常用方法

因為不可變，Tuple 的方法很少，只有兩個：

*   `count(value)`: 計算出現次數。
*   `index(value)`: 取得索引。

```python
t = (1, 2, 3, 2)
print(t.count(2)) # 2
print(t.index(3)) # 2
```
