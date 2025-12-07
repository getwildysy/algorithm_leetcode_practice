# let 與 const 宣告

ES6 引入了 `let` 和 `const` 來取代傳統的 `var`，解決了變數提升 (Hoisting) 和作用域 (Scope) 的問題。

## 1. 區塊作用域 (Block Scope)

`var` 的作用域是**函式作用域 (Function Scope)**，這意味著變數在 `if` 或 `for` 區塊中宣告後，區塊外仍然可以存取，這容易造成變數汙染。

`let` 和 `const` 是**區塊作用域 (Block Scope)**，它們只在 `{}` 包圍的區塊內有效。

```javascript
// 使用 var
if (true) {
    var a = 10;
}
console.log(a); // 10 (洩漏到全域)

// 使用 let
if (true) {
    let b = 20;
}
// console.log(b); // ReferenceError: b is not defined
```

## 2. 不可重複宣告

在同一個作用域內，`let` 和 `const` 不允許重複宣告同一個變數，而 `var` 可以。

```javascript
let user = "Alice";
// let user = "Bob"; // SyntaxError: Identifier 'user' has already been declared
```

## 3. 暫時性死區 (TDZ)

雖然 `let` 和 `const` 也會有提升 (Hoisting) 的行為，但它們會進入「暫時性死區 (Temporal Dead Zone, TDZ)」，直到程式執行到宣告的那一行。在 TDZ 期間存取變數會拋出錯誤。

```javascript
console.log(x); // undefined (var 的提升)
var x = 5;

// console.log(y); // ReferenceError (在 TDZ 內)
let y = 10;
```

## 4. const 的特性

`const` 用於宣告常數，一旦宣告就**必須初始化**，且**不能重新賦值**。

```javascript
const PI = 3.14;
// PI = 3.14159; // TypeError: Assignment to constant variable.
```

### const 物件與陣列

`const` 鎖定的是**變數的參考 (Reference)**，而不是變數指向的內容。如果 `const` 宣告的是物件或陣列，**其內容是可以修改的**。

```javascript
const list = [1, 2];
list.push(3); // 合法！
console.log(list); // [1, 2, 3]

// list = [4, 5]; // 非法！不能指向新的陣列
```

## 總結建議

1.  **預設使用 `const`**：除非你知道這個變數之後會被修改。
2.  **需要修改時用 `let`**：例如迴圈計數器 `i`。
3.  **完全不要用 `var`**：除非你在維護非常舊的程式碼。
