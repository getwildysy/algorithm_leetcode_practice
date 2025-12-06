# 除錯技巧與 `console` 物件

除錯 (Debugging) 是軟體開發不可或缺的一部分，它幫助我們理解程式碼的行為、找出錯誤並修復它們。JavaScript 提供了多種除錯工具，其中最常用的是瀏覽器的開發者工具和 `console` 物件。

## 1. 瀏覽器開發者工具 (Developer Tools)

現代瀏覽器（如 Chrome, Firefox, Edge, Safari）都內建了強大的開發者工具。通常透過 `F12` 鍵或右鍵「檢查」開啟。

### (1) Elements (元素) 面板
*   檢查和即時修改 DOM 結構和 CSS 樣式。

### (2) Console (控制台) 面板
*   查看 `console.log()` 的輸出。
*   查看錯誤訊息和警告。
*   執行 JavaScript 程式碼，測試變數和函式。

### (3) Sources (來源) 面板
*   查看原始碼。
*   設定**斷點 (Breakpoints)**：程式執行到斷點處會暫停。
    *   **行斷點**：點擊行號即可設定。
    *   **條件斷點**：右鍵點擊行號，設定條件，條件為真時暫停。
    *   **DOM 變更斷點**：右鍵 DOM 元素，在元素被修改、刪除或子樹變更時暫停。
*   **逐步執行**：
    *   `Step over` (F10): 執行下一行程式碼。
    *   `Step into` (F11): 如果下一行是函式呼叫，進入函式內部。
    *   `Step out` (Shift+F11): 跳出當前函式。
    *   `Resume script execution` (F8): 繼續執行到下一個斷點或程式結束。
*   **觀察變數** (Watch)：監控特定變數的值。
*   **呼叫堆疊** (Call Stack)：查看函式呼叫的順序。
*   **作用域** (Scope)：查看當前作用域中的變數。

### (4) Network (網路) 面板
*   監控所有網路請求 (HTTP/HTTPS)。
*   查看請求的狀態、時間、標頭、回應內容等。

## 2. `console` 物件的除錯方法

`console` 物件不僅有 `log()`，還有許多其他實用的方法。

### (1) `console.log(message, ...)`
最常用，輸出一般訊息。

### (2) `console.warn(message, ...)`
輸出警告訊息，通常帶有黃色背景或圖示。

### (3) `console.error(message, ...)`
輸出錯誤訊息，通常帶有紅色背景或圖示，並顯示堆疊追蹤。

### (4) `console.info(message, ...)`
輸出資訊訊息，類似 `log()`。

### (5) `console.table(data)`
將陣列或物件資料以表格形式輸出，非常適合查看結構化數據。

```javascript
const users = [
    { id: 1, name: "Alice", age: 30 },
    { id: 2, name: "Bob", age: 25 }
];
console.table(users);
```

### (6) `console.assert(condition, message)`
如果 `condition` 為 `false`，則輸出錯誤訊息。

```javascript
const num = 10;
console.assert(num > 0, "num 必須是正數");
```

### (7) `console.time(label)` / `console.timeEnd(label)`
測量一段程式碼執行的時間。

```javascript
console.time("ArrayLoop");
for (let i = 0; i < 100000; i++) {
    // some heavy operation
}
console.timeEnd("ArrayLoop"); // 輸出 "ArrayLoop: 12.345ms"
```

### (8) `console.group(label)` / `console.groupEnd()`
將 `console` 輸出分組，使輸出更有組織。

```javascript
console.group("使用者資訊");
console.log("名稱: Alice");
console.log("年齡: 30");
console.groupEnd();
```

### (9) `debugger` 關鍵字
在程式碼中加入 `debugger;`，當開發者工具開啟時，程式執行到這裡會自動暫停，效果等同於設定了一個斷點。

```javascript
function calculate(a, b) {
    let sum = a + b;
    debugger; // 程式會在這裡暫停
    let product = a * b;
    return product;
}
```
