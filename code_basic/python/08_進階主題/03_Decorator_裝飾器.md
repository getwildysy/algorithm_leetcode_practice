# 裝飾器 (Decorator)

裝飾器是一種設計模式，允許你在**不修改原函式程式碼**的情況下，動態地擴充或修改函式的行為。在 Python 中，裝飾器本質上是一個**接受函式作為參數並回傳新函式的高階函式**。

## 1. 基本語法 (`@` 語法糖)

```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# 輸出:
# Before function call
# Hello!
# After function call
```

這等同於：
`say_hello = my_decorator(say_hello)`

## 2. 裝飾帶有參數的函式

`wrapper` 函式需要接收任意參數 `*args, **kwargs` 並傳遞給原函式。

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(5, 3)
```

## 3. `functools.wraps`

使用裝飾器後，原函式的 metadata (如 `__name__`, `__doc__`) 會變成 wrapper 的。使用 `@functools.wraps(func)` 可以修正這個問題。

```python
import functools

def my_decorator(func):
    @functools.wraps(func) # 保留原函式資訊
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def test():
    """Test docstring"""
    pass

print(test.__name__) # test (如果沒有 wraps 會是 wrapper)
```

## 4. 帶參數的裝飾器

這需要三層函式嵌套。

```python
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello {name}")

greet("Alice")
```
