# ES6 Class (類別)

雖然 JavaScript 是基於原型的語言，但為了讓習慣物件導向程式設計 (OOP) 的開發者更容易上手，ES6 引入了 `class` 關鍵字。它本質上是原型繼承的**語法糖 (Syntactic Sugar)**，底層邏輯依然是原型鏈。

## 1. 基本定義

使用 `class` 定義類別，`constructor` 是建構函式，用於初始化物件。

```javascript
class Person {
    // 建構函式：建立物件時自動執行
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    // 定義方法 (不需要 function 關鍵字)
    sayHello() {
        console.log(`Hello, my name is ${this.name}`);
    }
}

const p1 = new Person("Alice", 25);
p1.sayHello(); // Hello, my name is Alice
```

## 2. 繼承 (Inheritance)

使用 `extends` 關鍵字實現繼承，並使用 `super` 呼叫父類別的建構函式或方法。

```javascript
class Student extends Person {
    constructor(name, age, studentId) {
        super(name, age); // 必須先呼叫 super() 才能使用 this
        this.studentId = studentId;
    }

    // 覆寫 (Override) 父類別方法
    sayHello() {
        super.sayHello(); // 呼叫父類別方法
        console.log(`And my student ID is ${this.studentId}`);
    }
}

const s1 = new Student("Bob", 20, "S12345");
s1.sayHello();
// Output:
// Hello, my name is Bob
// And my student ID is S12345
```

## 3. 靜態方法 (Static Methods)

使用 `static` 關鍵字定義靜態方法。靜態方法是屬於**類別本身**的，而不是實例物件的，通常用於工具函式。

```javascript
class MathUtils {
    static add(x, y) {
        return x + y;
    }
}

console.log(MathUtils.add(5, 10)); // 15
// const m = new MathUtils();
// m.add(5, 10); // TypeError: m.add is not a function
```

## 4. Getter 與 Setter

使用 `get` 與 `set` 關鍵字攔截屬性的存取與修改行為，常用於封裝與驗證。

```javascript
class Circle {
    constructor(radius) {
        this._radius = radius; // 慣例：底線開頭代表私有屬性 (並非真的私有)
    }

    // 讀取屬性時執行
    get radius() {
        return this._radius;
    }

    // 寫入屬性時執行
    set radius(value) {
        if (value <= 0) {
            console.log("半徑必須大於 0");
            return;
        }
        this._radius = value;
    }
}

const c = new Circle(10);
c.radius = -5; // 半徑必須大於 0
console.log(c.radius); // 10
```

## 5. 私有欄位 (Private Fields) - ES2022

最新的標準支援真正的私有屬性，使用 `#` 開頭。

```javascript
class BankAccount {
    #balance = 0; // 私有屬性

    constructor(initialBalance) {
        this.#balance = initialBalance;
    }

    getBalance() {
        return this.#balance;
    }
}

const account = new BankAccount(1000);
// console.log(account.#balance); // SyntaxError: Private field '#balance' must be declared
console.log(account.getBalance()); // 1000
```
