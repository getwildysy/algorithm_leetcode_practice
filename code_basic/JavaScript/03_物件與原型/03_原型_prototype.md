# 原型 (Prototype) 與 原型鏈 (Prototype Chain)

JavaScript 是基於**原型 (Prototype-based)** 的語言，這與 Java 或 C++ 等基於類別 (Class-based) 的語言有本質上的不同。雖然 ES6 引入了 `class` 語法，但其骨子裡仍然是原型機制。

## 1. 什麼是原型？

在 JavaScript 中，每個物件都有一個私有屬性（通常稱為 `[[Prototype]]`），指向另一個物件，這個物件就是它的**原型 (Prototype)**。

當我們試圖存取一個物件的屬性時，如果該物件本身沒有這個屬性，JavaScript 引擎就會去它的原型物件中尋找。

## 2. `__proto__` 與 `prototype`

這是最容易混淆的兩個屬性：

*   **`__proto__`**: 這是**每個物件**都有的屬性，指向該物件的**原型**（即它的父物件）。
*   **`prototype`**: 這是只有**函式 (Function)** 才有的屬性。當這個函式被用作建構函式 (`new Func()`) 時，新建立物件的 `__proto__` 會指向這個函式的 `prototype` 屬性。

```javascript
function Person(name) {
    this.name = name;
}

// 在 Person 的 prototype 上新增方法
Person.prototype.sayHello = function() {
    console.log(`Hello, I am ${this.name}`);
};

const p1 = new Person("Alice");
const p2 = new Person("Bob");

p1.sayHello(); // Hello, I am Alice

// 驗證關係
console.log(p1.__proto__ === Person.prototype); // true
console.log(Person.prototype.constructor === Person); // true
```

## 3. 原型鏈 (Prototype Chain)

如果原型的屬性也找不到，引擎會繼續找「原型的原型」，這樣一層一層往上找，直到找到 `Object.prototype`（它的原型是 `null`），這就是**原型鏈**。

```javascript
// p1 自身沒有 toString 方法
// p1.__proto__ (Person.prototype) 也沒有 toString
// p1.__proto__.__proto__ (Object.prototype) 有 toString！
console.log(p1.toString()); // [object Object]
```

**查找過程：**
`p1` -> `Person.prototype` -> `Object.prototype` -> `null`

## 4. 繼承 (Inheritance)

在 ES6 之前，我們透過操作原型鏈來實作繼承。

```javascript
function Animal(type) {
    this.type = type;
}
Animal.prototype.eat = function() {
    console.log("Eating...");
};

function Dog(name) {
    Animal.call(this, "Dog"); // 繼承屬性
    this.name = name;
}

// 繼承方法：將 Dog 的原型指向 Animal 的實例
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog; // 修正 constructor 指向

const d = new Dog("Buddy");
d.eat(); // Eating...
```

這種寫法相當繁瑣，因此 ES6 推出了 `class` 語法糖來簡化這個過程。
