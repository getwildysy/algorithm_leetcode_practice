# JavaScript 變數宣告：let, const, var

JavaScript 歷經演變，目前有三種宣告變數的方式。現代開發 (ES6+) 強烈建議主要使用 `const` 與 `let`，並盡量避免使用 `var`。

## 1. const (常數)

*   **特性**：宣告後**不能重新賦值** (Reassignment)。
*   **作用域**：區塊作用域 (Block Scope)，只在 `{ ... }` 內有效。
*   **使用時機**：**預設首選**。只要變數意圖不會被重新賦值，就用 `const`。這能提高程式碼可讀性，明確告知閱讀者這個變數不會改變。

```javascript
const PI = 3.14159;
// PI = 3.14; // TypeError: Assignment to constant variable.

// 注意：如果 const 宣告的是物件或陣列，其內容是可以修改的！
const user = { name: "Alice" };
user.name = "Bob"; // 合法！因為沒有修改 user 變數儲存的記憶體位址。
// user = { name: "Charlie" }; // 錯誤！不能重新指向新物件。
```

## 2. let (變數)

*   **特性**：可以重新賦值。
*   **作用域**：區塊作用域 (Block Scope)。
*   **使用時機**：當變數需要被改變時（例如：迴圈計數器、累加值、狀態切換）。

```javascript
let score = 0;
score = 10; // 合法

if (true) {
    let x = 5;
    console.log(x); // 5
}
// console.log(x); // ReferenceError: x is not defined (因為 x 離開了區塊)
```

## 3. var (舊式變數)

*   **特性**：可以重新賦值，可以重複宣告 (Re-declaration)。
*   **作用域**：函式作用域 (Function Scope)，它會忽略普通的區塊 `{}` (如 if, for)。
*   **提升 (Hoisting)**：`var` 宣告的變數會被提升到函式頂端，並初始化為 `undefined`。
*   **使用時機**：現代開發中**應盡量避免**，除非是維護舊有的 Legacy Code。

```javascript
if (true) {
    var y = 10;
}
console.log(y); // 10 (var 穿透了 if 區塊，洩漏到外部)

console.log(z); // undefined (不會報錯，因為 z 被提升了)
var z = 5;
```

## 總結比較

| 特性 | const | let | var |
| :--- | :--- | :--- | :--- |
| **作用域** | 區塊 (Block) | 區塊 (Block) | 函式 (Function) |
| **重新賦值** | ❌ | ✅ | ✅ |
| **重複宣告** | ❌ | ❌ | ✅ |
| **提升行為** | 有 (但在 TDZ*) | 有 (但在 TDZ*) | 初始化為 undefined |
| **全域物件屬性** | 否 | 否 | 是 (在瀏覽器是 window 屬性) |

> **TDZ (Temporal Dead Zone, 暫時性死區)**: 指在程式碼區塊開始到變數被宣告的那一行之間。在這段區域內存取該變數會拋出 `ReferenceError`。這保護了程式碼邏輯，避免存取未初始化的變數。
