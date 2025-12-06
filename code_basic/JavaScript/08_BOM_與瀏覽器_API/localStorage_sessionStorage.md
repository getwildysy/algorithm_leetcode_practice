# BOM 與瀏覽器 API：localStorage 與 sessionStorage

`localStorage` 和 `sessionStorage` 提供了在客戶端瀏覽器中儲存鍵值對 (Key-Value Pairs) 資料的方式。它們屬於 Web Storage API 的一部分，比傳統的 Cookie 更大、更安全、更易用。

## 1. 共同特性

*   儲存上限較大（通常為 5MB 或以上）。
*   資料儲存為**字串**。若要儲存物件或陣列，需要使用 `JSON.stringify()` 轉換；讀取時使用 `JSON.parse()` 轉換回來。
*   資料不會隨每次 HTTP 請求發送到伺服器，減少網路流量。
*   只能被相同**同源 (Same-origin)** 的頁面存取。

## 2. `localStorage`

### 特點
*   **持久性儲存**：資料在瀏覽器關閉後仍然保留，除非手動清除或程式碼清除。
*   沒有過期時間。

### 常用方法

*   `setItem(key, value)`: 儲存一個鍵值對。
*   `getItem(key)`: 根據鍵獲取值。如果鍵不存在，回傳 `null`。
*   `removeItem(key)`: 根據鍵移除資料。
*   `clear()`: 清除所有儲存的資料。
*   `key(index)`: 獲取指定索引的鍵名。
*   `length`: 獲取儲存的資料數量。

### 範例

```javascript
// 儲存資料 (會自動轉為字串)
localStorage.setItem('username', 'Alice');

// 儲存物件
const userSettings = { theme: 'dark', notifications: true };
localStorage.setItem('settings', JSON.stringify(userSettings));

// 獲取資料
const username = localStorage.getItem('username'); // 'Alice'

// 獲取物件並解析
const settingsString = localStorage.getItem('settings');
const settings = JSON.parse(settingsString);
console.log(settings.theme); // 'dark'

// 移除單個資料
localStorage.removeItem('username');

// 清除所有資料
// localStorage.clear();
```

## 3. `sessionStorage`

### 特點
*   **會話期儲存**：資料只在當前瀏覽器會話期間有效。當使用者關閉瀏覽器視窗或標籤頁時，資料會被清除。
*   與 `localStorage` 擁有相同的 API。

### 範例

```javascript
sessionStorage.setItem('currentSessionId', 'abc123xyz');

const sessionId = sessionStorage.getItem('currentSessionId');
console.log(sessionId); // 'abc123xyz'

// 當頁面關閉或標籤頁關閉後，此資料將會消失。
```

## 4. `storage` 事件

當 `localStorage` 或 `sessionStorage` 中的資料發生變化時（**但在不同標籤頁或視窗中**），會觸發 `storage` 事件。

```javascript
window.addEventListener('storage', (event) => {
    console.log('Storage event fired!');
    console.log('Key:', event.key);
    console.log('Old Value:', event.oldValue);
    console.log('New Value:', event.newValue);
    console.log('URL:', event.url);
    console.log('Storage Area:', event.storageArea); // localStorage 或 sessionStorage
});
```

> **注意**：`storage` 事件不會在資料發生變化的**同一個頁面**中觸發。它設計用於在多個標籤頁之間同步儲存狀態。
