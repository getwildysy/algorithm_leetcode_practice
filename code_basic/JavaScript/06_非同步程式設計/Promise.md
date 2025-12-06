# Promise

Promise 是 ES6 引入的標準非同步處理解決方案，旨在解決 Callback Hell 的問題，提供更優雅的鏈式調用 (Chaining) 和統一的錯誤處理機制。

## 1. 什麼是 Promise？

Promise 是一個物件，代表一個非同步操作的**最終完成**（或失敗）及其結果值。

Promise 有三種狀態：
1.  **Pending (擱置)**：初始狀態，尚未完成。
2.  **Fulfilled / Resolved (已實現)**：操作成功完成。
3.  **Rejected (已拒絕)**：操作失敗。

## 2. 建立 Promise

使用 `new Promise()` 建構函式。它接受一個執行函式 (executor)，該函式有兩個參數：`resolve` 和 `reject`。

```javascript
const myPromise = new Promise((resolve, reject) => {
    const success = true;

    if (success) {
        // 成功時呼叫 resolve，並傳遞結果
        resolve("Operation Successful!");
    } else {
        // 失敗時呼叫 reject，並傳遞原因
        reject("Something went wrong");
    }
});
```

## 3. 使用 Promise：then, catch, finally

*   `.then()`: 當 Promise 狀態變為 Fulfilled 時執行。接收 resolve 的回傳值。
*   `.catch()`: 當 Promise 狀態變為 Rejected 時執行。接收 reject 的錯誤原因。
*   `.finally()`: 無論成功或失敗都會執行（常用於隱藏 Loading spinner）。

```javascript
myPromise
    .then((data) => {
        console.log(data); // "Operation Successful!"
        return "Next Step"; // 可以回傳值給下一個 .then
    })
    .then((step) => {
        console.log(step); // "Next Step"
    })
    .catch((error) => {
        console.error(error);
    })
    .finally(() => {
        console.log("Cleanup done");
    });
```

## 4. 解決 Callback Hell

使用 Promise Chain (鏈式調用) 將巢狀結構攤平。

```javascript
login(username, password)
    .then(user => getUserId(user))
    .then(id => getFriends(id))
    .then(friends => getFriendPhoto(friends[0]))
    .then(photo => console.log(photo))
    .catch(error => console.error(error)); // 統一捕捉所有步驟的錯誤
```

## 5. Promise 常用靜態方法

### `Promise.all([p1, p2, p3])`
並行執行多個 Promise。只有當**所有** Promise 都成功時才回傳成功（結果是陣列）；只要有一個失敗，整個就失敗。

```javascript
Promise.all([fetch(url1), fetch(url2)])
    .then(([res1, res2]) => { ... })
    .catch(err => { ... });
```

### `Promise.race([p1, p2])`
回傳**最快**完成（無論成功或失敗）的那個 Promise 的結果。

### `Promise.allSettled([p1, p2])` (ES2020)
等待所有 Promise 完成，無論成功或失敗。回傳每個 Promise 的狀態物件陣列。
