# Python 列表 (List)

列表 (List) 是 Python 中最靈活且常用的有序集合。它是**可變的 (Mutable)**，可以儲存不同類型的元素。

## 1. 建立列表

```python
# 空列表
empty = []

# 包含元素的列表
numbers = [1, 2, 3, 4, 5]
mixed = [1, "Hello", 3.14, True]
```

## 2. 存取與修改

```python
fruits = ["apple", "banana", "cherry"]

# 索引 (Indexing)
print(fruits[0])   # "apple"
print(fruits[-1])  # "cherry"

# 切片 (Slicing)
print(fruits[1:])  # ["banana", "cherry"]

# 修改元素
fruits[1] = "blueberry"
print(fruits)      # ["apple", "blueberry", "cherry"]
```

## 3. 新增元素

*   `append(item)`: 加到末尾。
*   `insert(index, item)`: 插入指定位置。
*   `extend(iterable)`: 將另一個序列接到末尾。

```python
nums = [1, 2]
nums.append(3)      # [1, 2, 3]
nums.insert(0, 0)   # [0, 1, 2, 3]
nums.extend([4, 5]) # [0, 1, 2, 3, 4, 5]
```

## 4. 刪除元素

*   `remove(item)`: 刪除第一個符合的值。
*   `pop(index)`: 刪除並回傳指定位置的元素 (預設為最後一個)。
*   `del`: 刪除指定位置或整個列表。
*   `clear()`: 清空列表。

```python
nums = [10, 20, 30, 40, 50]

nums.remove(30)     # [10, 20, 40, 50]
val = nums.pop()    # 50, nums 變為 [10, 20, 40]
val2 = nums.pop(0)  # 10, nums 變為 [20, 40]

del nums[0]         # [40]
nums.clear()        # []
```

## 5. 常用操作

*   `len(list)`: 長度。
*   `item in list`: 檢查是否存在。
*   `list.sort()`: 原地排序 (修改原列表)。
*   `sorted(list)`: 回傳排序後的新列表 (不修改原列表)。
*   `list.reverse()`: 原地反轉。

```python
nums = [3, 1, 4, 1, 5]
nums.sort() # [1, 1, 3, 4, 5]

print(nums.count(1)) # 2 (出現次數)
print(nums.index(3)) # 2 (第一個 3 的索引)
```

## 6. 列表複製

注意：直接賦值 (`a = b`) 只是複製引用 (Reference)，修改其中一個會影響另一個。

```python
a = [1, 2, 3]
b = a # 引用複製

# 淺拷貝 (Shallow Copy)
c = a[:]
d = a.copy()

a[0] = 99
print(b) # [99, 2, 3] (跟著變)
print(c) # [1, 2, 3] (不受影響)
```
