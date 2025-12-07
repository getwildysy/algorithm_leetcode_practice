# 作用域 (Scope) 與 LEGB 規則

作用域決定了變數的可見性和生命週期。Python 解析變數名稱時，遵循 **LEGB** 規則。

## 1. LEGB 規則

當你引用一個變數時，Python 會依照以下順序搜尋：

1.  **L (Local)**: 區域作用域。包含在函式或 Lambda 內部的變數。
2.  **E (Enclosing)**: 閉包外層函式的作用域。
3.  **G (Global)**: 全域作用域。模組頂層定義的變數。
4.  **B (Built-in)**: 內建作用域。Python 預定義的變數 (如 `print`, `len`, `range`)。

```python
x = "Global"

def outer():
    x = "Enclosing"
    
    def inner():
        x = "Local"
        print(x)
    
    inner()

outer() # 輸出 "Local"
```

## 2. Global 關鍵字

如果你需要在函式內部**修改**全域變數，必須使用 `global` 關鍵字聲明。

```python
count = 0

def increment():
    global count # 告訴 Python 這裡的 count 是全域變數
    count += 1

increment()
print(count) # 1
```

如果沒有 `global`，Python 會認為你要創建一個新的區域變數 `count`，但因為還沒賦值就嘗試 `+=`，會拋出 `UnboundLocalError`。

## 3. Nonlocal 關鍵字

如果你需要在巢狀函式 (inner function) 中修改**外層函式 (Enclosing scope)** 的變數，使用 `nonlocal`。

```python
def outer():
    x = 0
    
    def inner():
        nonlocal x
        x += 1
        print("Inner:", x)
        
    inner()
    print("Outer:", x)

outer()
# Inner: 1
# Outer: 1
```

## 4. 變數生命週期

*   區域變數在函式被呼叫時建立，函式結束時銷毀。
*   全域變數在程式執行期間一直存在。
