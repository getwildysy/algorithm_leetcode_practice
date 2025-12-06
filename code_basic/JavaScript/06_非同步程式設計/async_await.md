# async / await

ES8 (ES2017) 引入了 `async` 和 `await` 關鍵字，這是基於 Promise 的語法糖，讓非同步程式碼看起來**像同步程式碼**一樣直觀。這是目前最推薦的非同步寫法。

## 1. async 函式

在函式宣告前加上 `async` 關鍵字。
*   `async` 函式總是回傳一個 **Promise**。
*   如果函式回傳一個值，Promise 會以該值 resolve。
*   如果函式拋出錯誤，Promise 會以該錯誤 reject。

```javascript
async function fetchUser() {
    return "Alice";
}

fetchUser().then(name => console.log(name)); // "Alice"
```

## 2. await 關鍵字

`await` 只能在 `async` 函式內部使用。
*   它會**暫停**函式的執行，直到等待的 Promise 被 resolve。
*   它會回傳 resolve 的值。
*   如果 Promise 被 reject，它會拋出 (throw) 錯誤。

```javascript
async function getUserData() {
    console.log("Start");
    
    // 這裡會暫停，直到 Promise 完成
    const response = await fetch("https://api.example.com/user");
    const data = await response.json();
    
    console.log(data); // 這裡可以直接拿到資料，不用寫 .then
    console.log("End");
}
```

## 3. 錯誤處理 (Error Handling)

因為 `await` 會將 reject 轉為 throw error，所以我們可以使用標準的 `try...catch` 語法來捕捉錯誤。

```javascript
async function main() {
    try {
        const user = await login();
        const posts = await getPosts(user.id);
        console.log(posts);
    } catch (error) {
        // 捕捉 login 或 getPosts 過程中的任何錯誤
        console.error("發生錯誤:", error);
    } finally {
        console.log("執行結束");
    }
}
```

## 4. 並行執行 (Parallel Execution)

新手常犯的錯誤是過度使用 `await` 導致不必要的序列執行 (Sequential)。

### 低效寫法 (序列)

```javascript
// 等完 A 才做 B，總耗時 = A + B
const user = await getUser();
const config = await getConfig();
```

### 高效寫法 (並行)

如果兩個請求沒有相依關係，應該讓它們同時發出。

```javascript
// 方法 1: 先發出請求，再 await
const userPromise = getUser();
const configPromise = getConfig();

const user = await userPromise;
const config = await configPromise;

// 方法 2: 使用 Promise.all (推薦)
const [user, config] = await Promise.all([getUser(), getConfig()]);
```

## 總結

| 特性 | Callback | Promise | async/await |
| :--- | :--- | :--- | :--- |
| **可讀性** | 差 (Callback Hell) | 中 (鏈式調用) | 優 (像同步碼) |
| **錯誤處理** | 個別處理 | `.catch()` | `try...catch` |
| **底層機制** | 函式參數 | 物件 | Promise 語法糖 |
