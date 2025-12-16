# Python 字串 (String)

字串是 Python 中最常用的資料型別之一，用於儲存文字資料。Python 的字串是**不可變 (Immutable)** 的序列。

## 1. 建立字串

可以使用單引號 `'`、雙引號 `"` 或三引號 `'''` / `"""` (用於多行字串) 來建立。

```python
s1 = 'Hello'
s2 = "World"
s3 = """這是一個
多行字串"""
```

## 2. 字串操作

### 串接與重複

```python
first = "Hello"
second = "Python"

# 串接 (+)
full = first + " " + second  # "Hello Python"

# 重複 (*)
repeat = first * 3  # "HelloHelloHello"
```

### 索引與切片 (Indexing & Slicing)

```python
text = "Python"

print(text[0])    # 'P' (第一個字元)
print(text[-1])   # 'n' (最後一個字元)

# 切片 [start:stop:step]
print(text[0:2])  # 'Py' (包含開頭，不包含結尾)
print(text[2:])   # 'thon' (從索引 2 到最後)
print(text[::-1]) # 'nohtyP' (反轉字串)
```

## 3. 常用方法 (Methods)

Python 字串提供了豐富的內建方法。

### 大小寫轉換

```python
s = "Hello Python"
print(s.upper())      # "HELLO PYTHON"
print(s.lower())      # "hello python"
print(s.capitalize()) # "Hello python" (首字母大寫)
print(s.title())      # "Hello Python" (每個單字首字母大寫)
```

### 搜尋與取代

```python
s = "Hello World"
print(s.find("World"))    # 6 (回傳索引，找不到回傳 -1)
print(s.replace("World", "Python")) # "Hello Python"
print(s.count("l"))       # 3 (計算出現次數)
print(s.startswith("He")) # True
print(s.endswith("ld"))   # True
print(s.index("World"))   # 6 (類似 find，但找不到會噴錯 ValueError)
print(s.rfind("l"))       # 9 (從右邊開始找，回傳最後出現的索引)
```

### 分割與結合

```python
# split: 字串 -> 列表
csv = "apple,banana,orange"
fruits = csv.split(",")   # ['apple', 'banana', 'orange']

# join: 列表 -> 字串
new_csv = "-".join(fruits) # "apple-banana-orange"
```

### 去除空白

```python
s = "  Hello  "
print(s.strip())  # "Hello" (去除頭尾空白)
print(s.lstrip()) # "Hello  " (去除左邊空白)
print(s.rstrip()) # "  Hello" (去除右邊空白)
```

### 字串性質檢查

```python
s = "Python3"
print(s.isalnum()) # True (是否只包含字母和數字)
print(s.isalpha()) # False (是否只包含字母)
print(s.isdigit()) # False (是否只包含數字)
print("   ".isspace()) # True (是否只包含空白)
```

### 字串排版與對齊

```python
s = "Python"
print(s.center(10, "*")) # "**Python**" (置中，不足補*)
print(s.ljust(10, "-"))  # "Python----" (靠左，不足補-)
print(s.rjust(10, "-"))  # "----Python" (靠右，不足補-)
print(s.zfill(10))       # "0000Python" (補零，常用於數字字串)
```
```

## 4. 格式化字串 (String Formatting)

### f-string (Python 3.6+ 推薦)

最簡潔、效能最好的方式。

```python
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
# 支援表達式
print(f"Next year I will be {age + 1}.")
```

### format() 方法

```python
print("My name is {} and I am {} years old.".format(name, age))
print("My name is {0} and I am {1} years old.".format(name, age))
```

### % 操作符 (舊式)

```python
print("My name is %s and I am %d years old." % (name, age))
```
