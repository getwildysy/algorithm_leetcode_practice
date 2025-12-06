# Python 控制流程：if, elif, else 與 迴圈

控制流程是程式設計中的核心概念，它決定了程式碼執行的順序。Python 使用縮排 (Indentation) 來定義程式碼區塊，這與其他語言使用大括號 `{}` 不同。

## 1. 條件判斷 (Conditionals)

使用 `if`、`elif` 和 `else` 來根據條件執行不同的程式碼區塊。

### 基本語法

```python
if 條件1:
    # 當條件1 為 True 時執行
    pass
elif 條件2:
    # 當條件1 為 False 且 條件2 為 True 時執行
    pass
else:
    # 當上述條件皆為 False 時執行
    pass
```

### 範例

```python
score = 85

if score >= 90:
    print("優秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

### 巢狀判斷 (Nested if)

可以在一個 if 區塊內再包含另一個 if 區塊。

```python
x = 10
y = 5

if x > 0:
    print("x 是正數")
    if y > 0:
        print("y 也是正數")
```

---

## 2. 迴圈 (Loops)

Python 提供了兩種主要的迴圈結構：`for` 迴圈和 `while` 迴圈。

### for 迴圈

`for` 迴圈通常用於遍歷序列（如列表 list、元組 tuple、字串 string）或使用 `range()` 函數進行指定次數的迭代。

#### 遍歷列表

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

#### 使用 range()

`range(start, stop, step)` 生成一個數字序列。
*   `start`: 起始值 (預設為 0)
*   `stop`: 終止值 (不包含)
*   `step`: 間隔 (預設為 1)

```python
# 印出 0 到 4
for i in range(5):
    print(i)

# 印出 2, 4, 6, 8
for i in range(2, 10, 2):
    print(i)
```

### while 迴圈

`while` 迴圈會在條件為 `True` 時重複執行程式碼區塊。務必確保條件最終會變成 `False`，否則會造成無窮迴圈。

```python
count = 0
while count < 5:
    print(count)
    count += 1  # 重要：更新條件變數
```

---

## 3. 迴圈控制語句

在迴圈中，可以使用特殊的語句來改變執行流程。

### break

立即終止迴圈，跳出迴圈區塊。

```python
for i in range(10):
    if i == 5:
        break  # 當 i 等於 5 時停止迴圈
    print(i)
```

### continue

跳過當前迭代的剩餘部分，直接進入下一次迭代。

```python
for i in range(5):
    if i == 2:
        continue  # 當 i 等於 2 時跳過本次列印
    print(i)
```

### pass

`pass` 是一個空語句，不做任何事情。通常用作佔位符。

```python
if x < 0:
    pass  # 尚未實作處理邏輯
else:
    print("Positive")
```

---

## 4. 迴圈搭配 else

Python 的迴圈有一個獨特的特性：可以搭配 `else` 子句。當迴圈**正常結束**（沒有遇到 `break`）時，會執行 `else` 區塊。

```python
# 尋找質數範例
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} 等於 {x} * {n//x}")
            break
    else:
        # 內層迴圈沒有遇到 break (即沒有找到因數)
        print(f"{n} 是質數")
```
