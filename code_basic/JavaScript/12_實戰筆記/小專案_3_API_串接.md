# 小專案 3：API 串接 (Connecting to an API)

**核心概念**: Fetch API、Promise / async/await、JSON 處理、錯誤處理、動態 DOM 渲染

與外部 API 進行資料串接是現代前端應用程式的核心功能之一。這個專案旨在學習如何發送 HTTP 請求、處理回應以及將資料渲染到頁面。

## 專案功能點

1.  **選擇 API**：選擇一個公開的 API (例如：GitHub API, JSONPlaceholder, Star Wars API)。
2.  **發送請求**：點擊按鈕或在頁面載入時自動發送 HTTP 請求。
3.  **顯示載入狀態**：在請求過程中顯示一個 Loading 訊息或圖示。
4.  **處理回應**：成功時顯示 API 返回的資料，失敗時顯示錯誤訊息。
5.  **動態渲染**：根據取得的資料動態生成 HTML 內容。
6.  **錯誤處理**：友善地處理網路錯誤或 API 回傳的錯誤。

## 主要技術點

### 1. HTML 結構 (基本骨架)

*   一個按鈕用於觸發 API 請求（或在 `DOMContentLoaded` 時自動請求）。
*   一個 `div` 或 `ul` 用於顯示從 API 取得的資料。
*   一個 `p` 或 `div` 用於顯示載入或錯誤訊息。

```html
<!-- 範例 HTML 骨架 -->
<div class="api-container">
    <h1>GitHub 使用者資訊</h1>
    <input type="text" id="usernameInput" placeholder="輸入 GitHub 用戶名">
    <button id="fetchButton">獲取資訊</button>
    
    <p id="loadingMessage" style="display: none;">載入中...</p>
    <div id="userInfo" class="card" style="display: none;">
        <h2><a id="userLink" target="_blank"></a></h2>
        <img id="userAvatar" alt="User Avatar" width="100">
        <p>追隨者: <span id="followers"></span></p>
        <p>公開儲存庫: <span id="repos"></span></p>
    </div>
    <p id="errorMessage" class="error" style="display: none; color: red;"></p>
</div>
```

### 2. JavaScript 邏輯

#### (1) 元素查詢與事件監聽

*   獲取按鈕、輸入框、顯示區、載入訊息和錯誤訊息的 DOM 引用。
*   監聽按鈕的 `click` 事件。

#### (2) 使用 Fetch API 發送請求

*   定義 API 終點 (Endpoint) URL。
*   使用 `fetch()` 函式發送 GET 請求。
*   **Promise 鏈**：
    *   `fetch(url)` -> 回傳 Response Promise。
    *   `response.json()` -> 回傳 JSON 資料 Promise。
    *   `data => ...` -> 處理資料。
*   **`async/await`** (推薦):
    *   將發送請求的函式宣告為 `async`。
    *   使用 `await fetch(url)` 和 `await response.json()`。

#### (3) 處理載入狀態

*   在發送請求前，顯示 `loadingMessage` 並隱藏 `userInfo` 和 `errorMessage`。
*   在 `finally` 區塊（使用 `.then().catch().finally()` 或 `try...catch...finally`）中隱藏 `loadingMessage`。

#### (4) 渲染資料

*   成功取得資料後，更新 `userInfo` 元素的 `innerHTML` 或 `textContent`，填充用戶名、頭像、追隨者等資訊。
*   顯示 `userInfo` 區塊。

#### (5) 錯誤處理

*   在 `fetch` 回應中，檢查 `response.ok` (HTTP 狀態碼 200-299)。如果不是，拋出錯誤。
*   使用 `.catch(error => ...)` 或 `try...catch` 區塊捕捉所有網路錯誤或自訂拋出的錯誤。
*   顯示 `errorMessage`。

#### (6) 輸入處理

*   從輸入框獲取使用者名稱。
*   將使用者名稱動態插入到 API URL 中。

## 3. CSS 樣式 (簡述)

*   美化頁面，讓資料顯示清晰。
*   為載入狀態和錯誤訊息添加樣式。

## 4. 進階考量

*   **API 金鑰**：如果 API 需要，管理 API 金鑰（注意不要直接暴露在客戶端程式碼）。
*   **認證**：處理使用者登入和授權。
*   **分頁**：如果資料量大，實現分頁功能。
*   **節流/去抖 (Throttling/Debouncing)**：避免在使用者快速輸入時頻繁發送請求。
*   **錯誤重試機制**。
*   **模組化**：將 API 請求邏輯封裝到單獨的模組中。
