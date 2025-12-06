# Lambda 函式 (匿名函式)

Lambda 函式是一種小型的匿名函式。它可以接受任意數量的參數，但**只能有一個表達式**。

## 1. 語法

```python
lambda arguments : expression
```
表達式的結果會自動被回傳。

## 2. 基本用法

```python
# 傳統函式
def add(x, y):
    return x + y

# Lambda 函式
add_lambda = lambda x, y: x + y

print(add_lambda(5, 3)) # 8
```

## 3. 應用場景

Lambda 函式通常不會被賦值給變數，而是作為參數傳遞給高階函式（如 `map`, `filter`, `sort`）。

### 搭配 `map()`

```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared) # [1, 4, 9, 16]
```

### 搭配 `filter()`

```python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens) # [2, 4, 6]
```

### 搭配 `sorted()` (自訂排序鍵)

這是 Lambda 最常用的場景之一。

```python
students = [
    ("Alice", 25),
    ("Bob", 20),
    ("Charlie", 23)
]

# 根據年齡 (第二個元素) 排序
students.sort(key=lambda student: student[1])
print(students) 
# [('Bob', 20), ('Charlie', 23), ('Alice', 25)]
```

## 4. 限制

*   Lambda 函式只能包含一個表達式，不能包含複雜的邏輯（如 `if...elif...else` 區塊，雖然可以用三元運算符 `x if c else y`）。
*   過度使用 Lambda 可能會降低程式碼可讀性。如果邏輯稍微複雜，建議定義標準函式。
