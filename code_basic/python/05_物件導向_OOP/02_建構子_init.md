# 建構子 (Constructor) - `__init__`

`__init__` 是一個特殊的方法（Magic Method），稱為建構子或初始化方法。

## 1. 作用

當一個物件被建立（實體化）時，Python 會**自動呼叫** `__init__` 方法。它通常用於：
1.  初始化物件的屬性。
2.  執行物件建立時必要的設定操作。

## 2. 基本語法

```python
class Person:
    def __init__(self, name, age):
        print("正在初始化 Person 物件...")
        self.name = name
        self.age = age

p1 = Person("Alice", 30) 
# 輸出: 正在初始化 Person 物件...

print(p1.name) # Alice
```

## 3. 預設值參數

`__init__` 就像普通函式一樣，可以設定參數的預設值。

```python
class Student:
    def __init__(self, name, grade=1):
        self.name = name
        self.grade = grade

s1 = Student("Bob")
s2 = Student("Charlie", 2)

print(s1.grade) # 1
print(s2.grade) # 2
```

## 4. `self` 的重要性

在 `__init__` 中，我們使用 `self.variable = value` 來將資料綁定到特定的物件實體上。如果只寫 `variable = value`，那它就只是一個普通的區域變數，函式執行完就消失了，不會變成物件的屬性。

```python
class Mistake:
    def __init__(self, name):
        name = name # 錯誤！這只是區域變數賦值，沒有存入 self
        # 正確應為: self.name = name

m = Mistake("Test")
# print(m.name) # AttributeError: 'Mistake' object has no attribute 'name'
```
