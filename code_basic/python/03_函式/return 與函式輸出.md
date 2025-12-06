# Return 與函式輸出

`return` 語句用於結束函式的執行，並將結果回傳給呼叫者。

## 1. 回傳單一值

```python
def square(x):
    return x * x

result = square(5) # result 為 25
```

## 2. 回傳多個值 (Tuple Packing)

Python 允許函式看似回傳多個值，實際上它是回傳一個 **Tuple**。

```python
def get_user_info():
    name = "Alice"
    age = 30
    return name, age # 自動打包成 ('Alice', 30)

# 接收時自動解包
user_name, user_age = get_user_info()
print(user_name) # "Alice"

# 或者作為一個 Tuple 接收
info = get_user_info()
print(info) # ('Alice', 30)
```

## 3. 不回傳值 (None)

如果函式中沒有 `return` 語句，或者只有 `return` 但後面沒有接值，函式預設回傳 `None`。

```python
def print_msg(msg):
    print(msg)
    # 隱含 return None

result = print_msg("Hello")
print(result) # None
```

## 4. 提早結束 (Early Return)

`return` 可以用來在滿足特定條件時提早跳出函式，這是一種常見的重構技巧 (Guard Clauses)，可以減少巢狀縮排。

```python
def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero")
        return None # 提早結束
    
    return a / b
```
