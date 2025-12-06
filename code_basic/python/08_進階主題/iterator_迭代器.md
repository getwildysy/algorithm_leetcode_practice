# 迭代器 (Iterator)

迭代器是 Python 迴圈機制的基石。任何可以被 `for` 迴圈遍歷的物件（如 list, tuple, dict, str）都是**可迭代物件 (Iterable)**，但它們本身不一定是迭代器。

## 1. 可迭代物件 vs 迭代器

*   **Iterable (可迭代物件)**: 實作了 `__iter__()` 方法的物件。可以使用 `iter()` 函式取得其對應的迭代器。
*   **Iterator (迭代器)**: 實作了 `__iter__()` 和 `__next__()` 方法的物件。可以使用 `next()` 函式取得下一個值。當沒有更多元素時，拋出 `StopIteration` 例外。

## 2. 手動使用迭代器

```python
numbers = [1, 2, 3] # Iterable

it = iter(numbers) # 取得 Iterator
print(type(it))    # <class 'list_iterator'>

print(next(it)) # 1
print(next(it)) # 2
print(next(it)) # 3
# print(next(it)) # StopIteration Error
```

## 3. 自訂迭代器

我們可以透過實作 `__iter__` 和 `__next__` 方法來建立自己的迭代器類別。

```python
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        
        num = self.current
        self.current -= 1
        return num

# 使用
counter = CountDown(3)
for num in counter:
    print(num)
# 3, 2, 1
```

## 4. `for` 迴圈的原理

Python 的 `for` 迴圈本質上就是自動執行以下步驟：
1.  呼叫 `iter(obj)` 取得迭代器。
2.  無限呼叫 `next(iterator)`。
3.  捕捉 `StopIteration` 例外來結束迴圈。
