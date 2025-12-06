# 範圍 (Scope)

**範圍 (Scope)** 是指變數、函式和物件的可訪問性或可見性。它決定了程式碼中的特定部分可以存取哪些數據和功能。理解範圍是理解 JavaScript 程式碼如何運作的基礎。

JavaScript 中有兩種主要的範圍類型：**全域範圍 (Global Scope)** 和 **局部範圍 (Local Scope)**。局部範圍又可以細分為**函式範圍 (Function Scope)** 和 **區塊範圍 (Block Scope)**。

## 1. 全域範圍 (Global Scope)

*   在任何函式或區塊之外宣告的變數，屬於全域範圍。
*   在全域範圍中宣告的變數可以在程式碼的任何地方被存取。
*   在瀏覽器中，全域變數會成為 `window` 物件的屬性。在 Node.js 中，會成為 `global` 物件的屬性。

```javascript
const globalVar = "我是全域變數"; // 全域範圍

function sayGlobal() {
    console.log(globalVar); // 可以存取
}
sayGlobal();

console.log(globalVar); // 可以存取
```

## 2. 函式範圍 (Function Scope)

*   在函式內部宣告的變數，屬於函式範圍。
*   函式範圍的變數只能在其被宣告的函式內部被存取。
*   這意味著不同函式中的變數不會互相衝突。
*   **`var` 宣告的變數具有函式範圍。**

```javascript
function myFunction() {
    var functionVar = "我是函式範圍變數";
    console.log(functionVar); // 可以存取
}
myFunction();

// console.log(functionVar); // ReferenceError: functionVar is not defined
```

## 3. 區塊範圍 (Block Scope)

*   在 `{}`（區塊，如 `if` 語句、`for` 迴圈、`while` 迴圈）內部宣告的變數，屬於區塊範圍。
*   區塊範圍的變數只能在其被宣告的區塊內部被存取。
*   **`let` 和 `const` 宣告的變數具有區塊範圍。**

```javascript
if (true) {
    let blockLet = "我是區塊範圍 let 變數";
    const blockConst = "我是區塊範圍 const 變數";
    console.log(blockLet);
    console.log(blockConst);
}

// console.log(blockLet); // ReferenceError
// console.log(blockConst); // ReferenceError
```

## 4. 詞法作用域 (Lexical Scope) / 靜態作用域 (Static Scope)

JavaScript 採用的是**詞法作用域**。這意味著函式的範圍在**定義時**就被決定了，而不是在執行時。內層函式可以存取外層函式的變數。

```javascript
function outer() {
    let outerVar = "外部變數";

    function inner() { // inner 函式在 outer 函式內部被定義
        let innerVar = "內部變數";
        console.log(outerVar); // inner 可以存取 outerVar
    }

    inner();
    // console.log(innerVar); // ReferenceError: outer 無法存取 innerVar
}
outer();
```

## 5. 作用域鏈 (Scope Chain)

當 JavaScript 引擎在尋找一個變數時，它會先在當前作用域尋找。如果找不到，就會向上一個外層作用域尋找，直到找到全域作用域為止。這個由內到外的尋找路徑就稱為**作用域鏈**。

```javascript
let a = 1; // 全域作用域

function f1() {
    let b = 2; // f1 作用域
    function f2() {
        let c = 3; // f2 作用域
        console.log(a, b, c); // 尋找順序: f2 -> f1 -> 全域
    }
    f2();
}
f1(); // 輸出: 1 2 3
```
