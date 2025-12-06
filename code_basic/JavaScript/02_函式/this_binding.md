# this 的綁定機制

`this` 是 JavaScript 中最令人困惑但也最強大的概念之一。初學者常誤以為 `this` 指向函式本身或函式的範圍，但實際上，`this` 的值是在**函式被呼叫時**確定的（執行環境），而非定義時。

## 1. 四種綁定規則

要判斷 `this` 指向哪裡，依序檢查以下規則：

### (1) new 綁定 (New Binding)

使用 `new` 關鍵字呼叫建構函式時，`this` 會指向**新建立出來的物件**。

```javascript
function Person(name) {
    this.name = name;
}
const p = new Person("Charlie");
console.log(p.name); // Charlie
```

### (2) 顯式綁定 (Explicit Binding)

使用 `call`, `apply`, `bind` 方法，強制指定 `this` 要綁定哪個物件。

```javascript
function greet() {
    console.log(`Hello, ${this.name}`);
}
const user = { name: "Bob" };

greet.call(user); // Hello, Bob
```

*   `call(obj, arg1, arg2)`: 立即執行。
*   `apply(obj, [argsArray])`: 立即執行，參數放陣列。
*   `bind(obj)`: **不立即執行**，回傳一個已經綁定好 `this` 的新函式。

### (3) 隱式綁定 (Implicit Binding)

當函式作為物件的方法被呼叫時 (`obj.method()`)，`this` 指向**點符號左邊**的那個物件（上下文物件）。

```javascript
const user = {
    name: "Alice",
    greet: function() {
        console.log(this.name);
    }
};
user.greet(); // Alice (this 是 user)
```

**陷阱：隱式綁定遺失**
如果將方法賦值給另一個變數再呼叫，綁定會遺失，變成預設綁定。

```javascript
const say = user.greet;
say(); // undefined (變成預設綁定)
```

### (4) 預設綁定 (Default Binding)

如果以上規則都不適用（例如獨立呼叫函式 `foo()`），`this` 會套用預設規則。

*   **非嚴格模式**：指向全域物件 (瀏覽器中是 `window`)。
*   **嚴格模式 ("use strict")**：`this` 為 `undefined`。

```javascript
function foo() {
    console.log(this);
}
foo(); // window 或 undefined
```

## 2. 箭頭函式的 this

箭頭函式**不適用**上述四種規則。

箭頭函式的 `this` 是**詞法作用域 (Lexical Scope)**，也就是說，它單純由**程式碼寫在哪裡**決定。它會繼承外層函式的 `this`。

一旦箭頭函式的 `this` 被綁定（定義時），就無法被 `call`、`apply` 或 `bind` 修改。

```javascript
const obj = {
    name: "Arrow",
    test: function() {
        // 這裡的 this 是 obj
        const arrow = () => console.log(this.name);
        arrow(); 
    }
};
obj.test(); // "Arrow"
```

## 總結判斷流程

1.  函式是用 `new` 呼叫的嗎？ -> `this` 是新物件。
2.  有用 `call` / `apply` / `bind` 嗎？ -> `this` 是指定的物件。
3.  函式是透過 `物件.方法()` 呼叫的嗎？ -> `this` 是那個物件。
4.  是不是箭頭函式？ -> `this` 繼承外層。
5.  都不是 -> `this` 是全域物件或 `undefined`。
