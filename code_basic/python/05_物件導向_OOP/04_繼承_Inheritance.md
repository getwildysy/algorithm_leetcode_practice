# 繼承 (Inheritance)

繼承允許我們定義一個類別（子類別 Child Class），繼承另一個類別（父類別 Parent Class）的所有屬性和方法。這提高了程式碼的重用性。

## 1. 基本語法

```python
class Parent:
    pass

class Child(Parent):
    pass
```

## 2. 範例

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass 

class Dog(Animal): # Dog 繼承 Animal
    def speak(self):
        return "Woof!"

class Cat(Animal): # Cat 繼承 Animal
    def speak(self):
        return "Meow!"

d = Dog("Buddy")
print(d.name)   # Buddy (繼承自 Animal)
print(d.speak()) # Woof! (定義在 Dog)
```

## 3. `super()` 函式

用於呼叫父類別的方法，最常用於擴充 `__init__`。

```python
class Bird(Animal):
    def __init__(self, name, can_fly):
        # 呼叫父類別的 __init__ 初始化 name
        super().__init__(name)
        self.can_fly = can_fly

b = Bird("Tweety", True)
print(b.name)
print(b.can_fly)
```

## 4. 覆寫 (Overriding)

子類別可以重新定義父類別的方法，以提供特定的實作。上面的 `speak` 方法就是覆寫的例子。

## 5. 多重繼承

Python 支援一個類別同時繼承多個父類別。

```python
class Flyer:
    def fly(self):
        print("Flying")

class Swimmer:
    def swim(self):
        print("Swimming")

class Duck(Flyer, Swimmer):
    pass

d = Duck()
d.fly()
d.swim()
```
