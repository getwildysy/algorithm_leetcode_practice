# BOM 與瀏覽器 API：Fetch API

Fetch API 提供了一個現代化的、基於 Promise 的接口，用於在瀏覽器中執行網路請求。它取代了較為傳統和複雜的 `XMLHttpRequest` (XHR)。

## 1. 基本 Fetch 請求

`fetch()` 函式接受一個 URL 作為第一個參數，回傳一個 `Promise`。

```javascript
// GET 請求 (預設)
fetch('https://api.example.com/data')
    .then(response => {
        // response 物件包含請求的相關資訊 (狀態碼、標頭等)
        // 檢查 HTTP 狀態碼
        if (!response.ok) { // response.ok 是 response.status >= 200 && response.status < 300
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        // 將回應主體解析為 JSON 格式 (這也會回傳一個 Promise)
        return response.json(); 
    })
    .then(data => {
        console.log('資料:', data);
    })
    .catch(error => {
        console.error('Fetch 發生錯誤:', error);
    });
```

### Response 物件常用方法
*   `response.json()`: 將回應主體解析為 JSON 物件。
*   `response.text()`: 將回應主體解析為純文字。
*   `response.blob()`: 解析為 Blob 物件 (用於檔案)。
*   `response.formData()`: 解析為 FormData 物件。

## 2. POST 請求與設定

`fetch()` 函式還可以接受第二個參數，一個設定物件，用於配置請求。

```javascript
const postData = {
    title: 'foo',
    body: 'bar',
    userId: 1,
};

fetch('https://jsonplaceholder.typicode.com/posts', {
    method: 'POST', // 指定請求方法
    headers: {
        'Content-Type': 'application/json', // 設定內容類型
    },
    body: JSON.stringify(postData), // 將資料轉換為 JSON 字串
})
    .then(response => response.json())
    .then(data => console.log('POST 回應:', data))
    .catch(error => console.error('POST 錯誤:', error));
```

### 設定物件的常用屬性
*   `method`: HTTP 請求方法 (GET, POST, PUT, DELETE, etc.)。
*   `headers`: 設定請求標頭。
*   `body`: 請求的主體內容，通常是 `JSON.stringify()` 轉換後的資料。
*   `mode`: 請求模式 (如 `cors`, `no-cors`, `same-origin`)。
*   `credentials`: 憑證模式 (如 `omit`, `same-origin`, `include`)，用於處理 Cookie。

## 3. 使用 `async/await` 處理 Fetch

結合 `async/await` 可以讓非同步程式碼看起來更像同步，提升可讀性。

```javascript
async function fetchData(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Fetch 失敗:', error);
        throw error; // 重新拋出錯誤以便外部捕捉
    }
}

// 呼叫範例
fetchData('https://api.example.com/another-data')
    .then(data => console.log('取得資料:', data))
    .catch(err => console.error('最終錯誤:', err));

// 或直接在 async 函式中使用
async function loadPageData() {
    const users = await fetchData('https://api.example.com/users');
    const products = await fetchData('https://api.example.com/products');
    console.log('所有資料:', { users, products });
}
loadPageData();
```
