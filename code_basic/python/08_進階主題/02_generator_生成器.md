# 生成器 (Generator)

生成器是一種簡化版的迭代器。它允許你用函式的形式來寫迭代邏輯，使用 `yield` 關鍵字來回傳值。

## 1. 為什麼需要生成器？

*   **省記憶體 (Lazy Evaluation)**：不同於 List 一次把所有資料載入記憶體，生成器是一次產生一個值。對於處理大數據或無限序列非常有用。
*   **語法簡潔**：不需要寫 Class 和 `__iter__`, `__next__`。

## 2. 建立生成器函式

只要函式中有 `yield`，它就是一個生成器函式。

```python
def my_range(n):
    print("Start")
    i = 0
    while i < n:
        yield i # 暫停並回傳 i
        i += 1
        print("Resumed")

gen = my_range(3)
print(gen) # <generator object ...>

# 只有在呼叫 next() 或用 for 迴圈時才會執行
print(next(gen)) # 輸出 "Start", 回傳 0
print(next(gen)) # 輸出 "Resumed", 回傳 1
```

## 3. 生成器表達式 (Generator Expression)

類似列表生成式，但使用小括號 `()`。

```python
# 列表生成式 (佔用較多記憶體)
squares_list = [x**2 for x in range(1000000)] 

# 生成器表達式 (幾乎不佔記憶體)
squares_gen = (x**2 for x in range(1000000))

print(next(squares_gen)) # 0
```

## 4. 應用範例：斐波那契數列 (Fibonacci)

```python
def fibonacci(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

for num in fibonacci(5):
    print(num)
# 0, 1, 1, 2, 3
```
