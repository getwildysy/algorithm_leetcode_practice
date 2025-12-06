# Python 集合 (Set)

集合 (Set) 是一個**無序**、**不重複**元素的集合。它的主要用途是去重 (去除重複值) 和進行數學上的集合運算 (交集、聯集等)。

## 1. 建立集合

使用大括號 `{}` 或 `set()`。
注意：建立空集合必須用 `set()`，因為 `{}` 代表空字典。

```python
# 建立集合
fruits = {"apple", "banana", "cherry"}
print(fruits) 

# 自動去重
numbers = {1, 2, 2, 3, 3, 3}
print(numbers) # {1, 2, 3}

# 空集合
empty = set()
```

## 2. 新增與刪除

*   `add(item)`: 新增一個元素。
*   `update(iterable)`: 新增多個元素。
*   `remove(item)`: 刪除元素 (若不存在會報錯 KeyError)。
*   `discard(item)`: 刪除元素 (若不存在**不會**報錯)。
*   `pop()`: 隨機刪除並回傳一個元素。

```python
s = {1, 2, 3}
s.add(4)        # {1, 2, 3, 4}
s.remove(1)     # {2, 3, 4}
s.discard(99)   # 不會報錯
```

## 3. 集合運算

這是 Set 最強大的功能。

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 交集 (Intersection): 兩者都有
print(a & b) # {3, 4}
print(a.intersection(b))

# 聯集 (Union): 其中一個有
print(a | b) # {1, 2, 3, 4, 5, 6}
print(a.union(b))

# 差集 (Difference): a 有但 b 沒有
print(a - b) # {1, 2}
print(a.difference(b))

# 對稱差集 (Symmetric Difference): 只有其中一方有 (不重疊部分)
print(a ^ b) # {1, 2, 5, 6}
print(a.symmetric_difference(b))
```

## 4. 去除列表重複值 (實用技巧)

```python
lst = [1, 2, 2, 3, 4, 4, 5]
unique_lst = list(set(lst))
print(unique_lst) # [1, 2, 3, 4, 5] (注意：順序可能會被打亂)
```
