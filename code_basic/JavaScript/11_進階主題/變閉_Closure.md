# 閉包 (Closure)

**閉包 (Closure)** 是 JavaScript 中一個非常重要且強大的概念，它允許函式記住並存取它被定義時所處的詞法環境 (Lexical Environment)，即使該函式已經離開了它被定義時的作用域。

簡單來說，當一個內層函式 (Inner function) 被外層函式 (Outer function) 回傳或傳遞到其他地方，並且這個內層函式仍然引用著外層函式作用域中的變數時，閉包就形成了。

## 1. 閉包的形成

*   一個函式 (A) 裡面定義了另一個函式 (B)。
*   內層函式 (B) 引用了外層函式 (A) 的變數。
*   外層函式 (A) 執行完畢並回傳了內層函式 (B)。
*   即使外層函式的執行上下文已經被銷毀，內層函式仍然可以存取外層函式的作用域變數。

```javascript
function outerFunction(outerVar) {
    // outerVar 是 outerFunction 的局部變數
    return function innerFunction(innerVar) {
        // innerFunction 引用了 outerFunction 的 outerVar
        console.log(`外部變數: ${outerVar}, 內部變數: ${innerVar}`);
    };
}

const closureFn = outerFunction("Hello"); // outerFunction 執行完畢，但其作用域被 innerFunction 記住了
closureFn("World"); // 輸出: 外部變數: Hello, 內部變數: World
```
在這個例子中，`closureFn` 變數現在持有 `innerFunction`。當 `outerFunction` 執行完成時，它的執行上下文被銷毀，但 `outerVar` 變數並沒有被垃圾回收，因為 `innerFunction` 仍然引用著它。`closureFn` 就是一個閉包。

## 2. 閉包的常見應用場景

### (1) 隱藏變數 (資料封裝)
建立私有變數和方法，實現資料封裝。

```javascript
function createCounter() {
    let count = 0; // 私有變數，外部無法直接存取
    return {
        increment: function() {
            count++;
            return count;
        },
        decrement: function() {
            count--;
            return count;
        },
        getCount: function() {
            return count;
        }
    };
}

const counter = createCounter();
console.log(counter.increment()); // 1
console.log(counter.getCount());  // 1
// console.log(counter.count);    // undefined
```

### (2) 建立函式工廠 (Function Factory)
根據不同參數建立具有不同行為的函式。

```javascript
function makeMultiplier(factor) {
    return function(number) {
        return number * factor;
    };
}

const double = makeMultiplier(2);
const triple = makeMultiplier(3);

console.log(double(5)); // 10
console.log(triple(5)); // 15
```

### (3) 模組模式 (Module Pattern)
在 ES6 模組標準化之前，閉包常用於實現模組化。

```javascript
const Module = (function() {
    let privateVar = "這是私有變數";

    function privateMethod() {
        console.log("這是私有方法");
    }

    return {
        publicMethod: function() {
            console.log(privateVar);
            privateMethod();
        }
    };
})();

Module.publicMethod();
// console.log(Module.privateVar); // undefined
```

## 3. 閉包的注意事項

*   **記憶體消耗**：閉包會使被引用的變數不會被垃圾回收，如果閉包過多或引用了大型物件，可能導致記憶體消耗增加。
*   **`this` 的問題**：閉包不會綁定 `this`，它會繼承外部作用域的 `this`。在使用時需要注意 `this` 的指向。

儘管有這些注意事項，閉包仍然是 JavaScript 中不可或缺的特性，理解並善用閉包對於編寫高質量、可維護的 JavaScript 程式碼至關重要。
