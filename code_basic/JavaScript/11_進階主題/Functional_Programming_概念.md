# 函數式程式設計概念 (Functional Programming Concepts)

函數式程式設計 (Functional Programming, FP) 是一種程式設計範式，它將計算視為數學函式的求值，並避免狀態改變和可變數據。在 JavaScript 中，雖然它不是純粹的函數式語言，但我們可以利用其特性來應用函數式程式設計的思想，使程式碼更具可讀性、可維護性和可測試性。

## 1. 核心概念

### (1) 純粹函式 (Pure Functions)

純粹函式是函數式程式設計的基石。一個函式是純粹的，如果它滿足以下兩個條件：

*   **相同的輸入總是回傳相同的輸出**。
*   **沒有副作用 (No Side Effects)**：它不會修改其作用域外的任何數據，也不會影響外部系統（例如修改全域變數、修改傳入的參數、執行 I/O 操作等）。

**非純粹函式 (範例)**

```javascript
let total = 0; // 全域變數

function add(a, b) { // 有副作用：依賴並修改了外部狀態
    total = a + b;
    return total;
}
```

**純粹函式 (範例)**

```javascript
function addPure(a, b) { // 相同的輸入總是相同的輸出，沒有副作用
    return a + b;
}
```

### (2) 不可變性 (Immutability)

數據一旦被創建，就不能被修改。如果需要改變數據，則創建一個新的數據副本。這避免了在程式碼中追蹤狀態變化的複雜性。

```javascript
// 可變性 (Mutable)
const arr = [1, 2, 3];
arr.push(4); // 修改了原陣列
console.log(arr); // [1, 2, 3, 4]

// 不可變性 (Immutable)
const arr2 = [1, 2, 3];
const newArr = [...arr2, 4]; // 創建一個新陣列
console.log(arr2);   // [1, 2, 3] (原陣列不變)
console.log(newArr); // [1, 2, 3, 4]
```

### (3) 函式作為一等公民 (First-Class Functions)

函式可以像普通變數一樣被傳遞、賦值、儲存和回傳。這使得高階函式 (Higher-Order Functions) 成為可能。

### (4) 高階函式 (Higher-Order Functions)

*   接受一個或多個函式作為參數。
*   回傳一個函式。

`map`, `filter`, `reduce` 就是常見的高階函式。

```javascript
function operateOnArray(arr, operation) {
    return arr.map(operation); // operation 是作為參數傳入的函式
}

const numbers = [1, 2, 3];
const square = num => num * num;

const squaredNumbers = operateOnArray(numbers, square); // square 函式作為參數傳入
console.log(squaredNumbers); // [1, 4, 9]
```

## 2. 常見的函數式程式設計模式

### (1) 柯里化 (Currying)

將一個多參數的函式轉換成一系列單參數函式的技術。

```javascript
// 傳統函式
function add(a, b) {
    return a + b;
}

// 柯里化函式
function curriedAdd(a) {
    return function(b) {
        return a + b;
    };
}

const addFive = curriedAdd(5); // 回傳一個新函式，記住了 factor 5
console.log(addFive(3));    // 8
console.log(curriedAdd(10)(2)); // 12
```

### (2) 函式組合 (Function Composition)

將多個純粹函式組合成一個更複雜的函式。

```javascript
const add1 = num => num + 1;
const multiply2 = num => num * 2;

// 傳統方式
const result = multiply2(add1(5)); // 12

// 函式組合 (從右到左執行)
const compose = (...fns) => x => fns.reduceRight((acc, fn) => fn(acc), x);

const add1ThenMultiply2 = compose(multiply2, add1);
console.log(add1ThenMultiply2(5)); // 12
```

## 3. 函數式程式設計的優點

*   **易於測試**：純粹函式獨立、無副作用，測試容易。
*   **易於理解**：程式碼更具可預測性。
*   **易於維護**：數據流清晰，減少 Bug。
*   **支援並行處理**：由於沒有狀態修改，更容易進行並行處理。
