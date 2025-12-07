# Callback (回呼函式)

在 JavaScript 處理非同步操作（如讀取檔案、下載資料、計時器）的早期，Callback 是主要的解決方案。

## 1. 什麼是 Callback？

Callback 是一個**被當作參數傳遞給另一個函式**的函式，並在該外部函式執行完成後被呼叫。

### 同步 Callback (Synchronous)
立即執行，如 `Array.prototype.map`。

```javascript
const nums = [1, 2, 3];
nums.forEach(n => console.log(n)); // 這裡的箭頭函式就是 callback
```

### 非同步 Callback (Asynchronous)
等到任務完成後才執行。

```javascript
console.log("Start");

setTimeout(() => {
    console.log("Timeout done");
}, 1000);

console.log("End");

// 輸出順序：
// Start
// End
// Timeout done
```

## 2. Callback 實作範例

模擬一個下載資料的函式。

```javascript
function downloadData(url, callback) {
    console.log(`Downloading from ${url}...`);
    
    // 模擬網路延遲
    setTimeout(() => {
        const data = "Some data";
        console.log("Download finished");
        callback(data); // 下載完成後，執行 callback
    }, 2000);
}

function processData(content) {
    console.log(`Processing: ${content}`);
}

downloadData("https://example.com", processData);
```

## 3. Callback Hell (回呼地獄)

當非同步操作需要依序執行時（例如：先登入 -> 再取得 ID -> 再取得好友列表），就需要將 callback 巢狀嵌套。這會導致程式碼難以閱讀和維護，形狀像個橫躺的金字塔，被稱為 **Callback Hell**。

```javascript
login(username, password, (user) => {
    getUserId(user, (id) => {
        getFriends(id, (friends) => {
            getFriendPhoto(friends[0], (photo) => {
                console.log(photo);
                // 錯誤處理也很麻煩，每層都要 handle error
            });
        });
    });
});
```

為了解決這個問題，ES6 引入了 `Promise`。
