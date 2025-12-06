# JavaScript 錯誤處理：try...catch

在程式設計中，錯誤是不可避免的。JavaScript 提供了 `try...catch` 語句來處理執行時錯誤 (runtime errors)，防止程式因錯誤而崩潰，從而提高程式的穩定性。

## 1. `try...catch` 語句

`try...catch` 語句包含兩個主要區塊：

*   **`try` 區塊**：放置你認為可能拋出錯誤的程式碼。
*   **`catch` 區塊**：當 `try` 區塊中的程式碼拋出錯誤時，`catch` 區塊會被執行，用於處理這個錯誤。它會接收一個錯誤物件 (error object) 作為參數。

```javascript
try {
    // 這裡的程式碼可能會拋出錯誤
    const result = someUndefinedVariable * 2; // ReferenceError
    console.log(result);
} catch (error) {
    // 這裡的程式碼會在錯誤發生時執行
    console.error("發生錯誤:", error);
    console.log("錯誤訊息:", error.message);
    console.log("錯誤名稱:", error.name);
    // console.log("錯誤堆疊:", error.stack); // 錯誤的堆疊追蹤
}

console.log("程式繼續執行");
```

## 2. `finally` 區塊

`finally` 區塊是可選的，它會**總是在 `try...catch` 語句執行完畢後執行**，無論 `try` 區塊是否拋出錯誤，或 `catch` 區塊是否被執行。通常用於執行清理工作。

```javascript
try {
    console.log("嘗試執行程式碼...");
    // throw new Error("Oops, an error occurred!"); // 手動拋出錯誤
} catch (error) {
    console.error("在 catch 區塊處理錯誤:", error.message);
} finally {
    console.log("finally 區塊總會執行，用於清理資源。");
}

console.log("程式繼續執行");
```

## 3. `throw` 語句

`throw` 語句允許你**手動拋出**一個錯誤（或任何 JavaScript 值）。當 `throw` 被執行時，程式碼的執行會立即停止，並開始尋找最近的 `catch` 區塊。

```javascript
function divide(a, b) {
    if (b === 0) {
        throw new Error("除數不能為零！"); // 拋出一個 Error 物件
    }
    return a / b;
}

try {
    const result = divide(10, 0);
    console.log(result);
} catch (error) {
    console.error("錯誤:", error.message); // 錯誤: 除數不能為零！
}
```

## 4. 錯誤物件 (Error Object)

JavaScript 提供了多種內建的錯誤類型，它們都繼承自 `Error` 物件：

*   `Error`: 通用的錯誤。
*   `ReferenceError`: 引用未定義變數。
*   `TypeError`: 變數或參數不是預期型別。
*   `SyntaxError`: 語法錯誤 (通常在解析時發生，`try...catch` 無法捕捉)。
*   `RangeError`: 數值超出有效範圍。
*   `URIError`: URI 相關函式 (如 `decodeURI`) 參數無效。
*   `EvalError`: `eval()` 函式相關錯誤 (現在很少用)。

這些錯誤物件通常有 `name` (錯誤名稱) 和 `message` (錯誤描述) 屬性。
