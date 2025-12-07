# BOM 與瀏覽器 API：計時器 (setTimeout, setInterval)

JavaScript 提供了內建的計時器函數，用於延遲執行或重複執行程式碼。這些函數是瀏覽器環境 (BOM) 或 Node.js 環境提供的。

## 1. `setTimeout(callback, delay, arg1, arg2, ...)`

*   **功能**：在指定的延遲時間 (毫秒) 後，執行一次 `callback` 函式。
*   **回傳值**：一個數字 ID，可以用於取消該計時器。

```javascript
console.log("Start");

setTimeout(() => {
    console.log("這會在 2 秒後顯示");
}, 2000); // 2000 毫秒 = 2 秒

console.log("End");

// 輸出順序: Start -> End -> "這會在 2 秒後顯示"
```

### 取消 `setTimeout` - `clearTimeout(id)`

```javascript
const timerId = setTimeout(() => {
    console.log("這永遠不會被執行");
}, 3000);

// 在 1 秒後取消計時器
setTimeout(() => {
    clearTimeout(timerId);
    console.log("計時器已取消");
}, 1000);
```

## 2. `setInterval(callback, delay, arg1, arg2, ...)`

*   **功能**：每隔指定的延遲時間 (毫秒) 重複執行 `callback` 函式。
*   **回傳值**：一個數字 ID，用於取消該計時器。

```javascript
let count = 0;
const intervalId = setInterval(() => {
    count++;
    console.log(`計數: ${count}`);
    if (count >= 3) {
        clearInterval(intervalId); // 達到 3 次後停止計時
        console.log("計數已停止");
    }
}, 1000); // 每秒執行一次
```

### 取消 `setInterval` - `clearInterval(id)`

```javascript
// 上述範例中已展示
```

## 3. 注意事項

### (1) 延遲不準確性

`delay` 參數並非保證 `callback` 會在精確的時間點執行，而是表示**至少**延遲那麼長時間。實際執行時間可能因瀏覽器負載、其他任務執行等因素而稍晚。這是因為 JavaScript 是單執行緒的，計時器回呼會被放入任務佇列 (Task Queue)，等待主執行緒空閒時才會被執行。

### (2) `this` 綁定

在 `setTimeout` 或 `setInterval` 的回呼函式中，如果使用傳統函式，`this` 預設會指向全域物件 (例如瀏覽器的 `window`)。使用箭頭函式可以避免這個問題，因為箭頭函式會繼承定義時外層作用域的 `this`。

```javascript
const obj = {
    message: "Hello",
    logMessage: function() {
        console.log(this.message); // 正確指向 obj.message

        setTimeout(function() {
            console.log(this.message); // undefined (this 指向 window)
        }, 100);

        setTimeout(() => {
            console.log(this.message); // Hello (箭頭函式繼承外層的 this)
        }, 200);
    }
};

obj.logMessage();
```
