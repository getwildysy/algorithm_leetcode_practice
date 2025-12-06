# 多型 (Polymorphism)

多型 (Polymorphism) 指的是不同類別的物件，可以使用相同的介面（方法名稱）來操作，而產生不同的行為。

## 1. 方法覆寫實現多型

這是最常見的多型形式。不同的子類別實作了相同名稱的方法。

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"

animals = [Dog(), Cat(), Duck()]

for animal in animals:
    # 我們不需要知道 animal 具體是什麼型別
    # 只要它有 speak() 方法就可以呼叫
    print(animal.speak())
```

## 2. 鴨子型別 (Duck Typing)

Python 是動態語言，不強制要求繼承自特定介面。**「如果它走起來像鴨子，叫起來像鴨子，那它就是鴨子。」**

只要物件擁有該方法，就可以被使用，不在乎它的型別繼承關係。

```python
class Car:
    def start(self):
        print("Engine started")

class Computer:
    def start(self):
        print("System booting")

def start_device(device):
    device.start()

# Car 和 Computer 沒有共同父類別，但都有 start 方法
start_device(Car())      # Engine started
start_device(Computer()) # System booting
```

## 3. 運算子多載 (Operator Overloading)

Python 允許類別重新定義運算子 (如 `+`, `-`, `*`) 的行為。透過實作 Magic Methods 來達成。

*   `__add__`: `+`
*   `__sub__`: `-`
*   `__str__`: `str()` 或 `print()`

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 4)
v2 = Vector(1, -1)
v3 = v1 + v2 # 自動呼叫 v1.__add__(v2)

print(v3) # Vector(3, 3) (自動呼叫 __str__)
```
