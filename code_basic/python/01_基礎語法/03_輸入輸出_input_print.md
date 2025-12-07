# 輸入與輸出 (Input and Output)

程式與使用者互動最基本的方式就是輸入 (Input) 與輸出 (Output)。

## 1. 輸出 (`print`)

`print()` 函式用於將資料輸出到控制台 (Console)。

### 基本用法

```python
print("Hello, World!")
print(123)
print(3.14)
```

### 輸出多個項目

可以使用逗號 `,` 分隔多個要輸出的項目，預設會用空白隔開。

```python
name = "Alice"
age = 25
print("Name:", name, "Age:", age)
# 輸出: Name: Alice Age: 25
```

### 自訂分隔符 (`sep`)

使用 `sep` 參數可以改變項目之間的分隔符號。

```python
print("A", "B", "C", sep="-")
# 輸出: A-B-C

print("2023", "10", "27", sep="/")
# 輸出: 2023/10/27
```

### 自訂結尾符號 (`end`)

`print()` 預設會在輸出結束後自動換行 (`\n`)。使用 `end` 參數可以改變這個行為。

```python
print("Hello", end=" ")
print("World")
# 輸出: Hello World (在同一行)
```

## 2. 輸入 (`input`)

`input()` 函式用於暫停程式執行，等待使用者輸入文字，並按下 Enter 鍵。

### 基本用法

```python
name = input("請輸入你的名字: ")
print("你好, " + name)
```

### 注意事項：回傳型別

`input()` **永遠回傳字串 (String)**。如果你需要數字，必須進行型別轉換。

```python
age = input("請輸入你的年齡: ")
# print(age + 1) # TypeError: can only concatenate str to str

# 正確做法：轉為整數
age = int(age)
print("明年你將是", age + 1, "歲")
```

## 3. 格式化輸出 (Formatted Output)

雖然可以使用 `+` 或 `,` 來組合字串與變數，但使用格式化字串會更整潔。

### f-string (Python 3.6+ 推薦)

在字串開頭加上 `f`，然後在字串中用 `{}` 包裹變數。

```python
name = "Bob"
score = 95

print(f"學生 {name} 的分數是 {score} 分")
# 輸出: 學生 Bob 的分數是 95 分
```

### 格式化數字

可以在 `{}` 中指定格式，例如小數位數。

```python
pi = 3.1415926
print(f"圓周率 (小數點後兩位): {pi:.2f}")
# 輸出: 圓周率 (小數點後兩位): 3.14
```
