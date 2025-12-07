# HTTP 基礎

HTTP (HyperText Transfer Protocol) 是網際網路上應用最廣泛的協議。了解 HTTP 對於進行 API 串接和網路爬蟲至關重要。

## 1. 請求 (Request)

由客戶端（如瀏覽器、Python 程式）發送給伺服器。包含：

*   **URL**: 資源的地址 (如 `https://api.github.com/users`)。
*   **Method (方法)**:
    *   `GET`: 獲取資料 (最常用)。
    *   `POST`: 提交資料 (如表單、建立新資源)。
    *   `PUT`: 更新資源。
    *   `DELETE`: 刪除資源。
*   **Headers (標頭)**: 請求的元數據 (Metadata)，如 `User-Agent` (瀏覽器資訊), `Content-Type` (資料格式), `Authorization` (憑證)。
*   **Body (主體)**: POST/PUT 請求時攜帶的資料 (如 JSON, Form Data)。

## 2. 回應 (Response)

伺服器回傳給客戶端。包含：

*   **Status Code (狀態碼)**:
    *   `2xx`: 成功 (e.g., 200 OK, 201 Created)。
    *   `3xx`: 重新導向 (e.g., 301 Moved Permanently)。
    *   `4xx`: 客戶端錯誤 (e.g., 400 Bad Request, 404 Not Found, 403 Forbidden)。
    *   `5xx`: 伺服器錯誤 (e.g., 500 Internal Server Error)。
*   **Headers**: 回應的元數據，如 `Content-Type` (HTML, JSON)。
*   **Body**: 實際的資料內容 (HTML 原始碼, JSON 字串)。

## 3. 常見資料格式

*   **HTML**: 網頁結構。
*   **JSON**: 輕量級資料交換格式，API 最常用。
*   **XML**: 較舊的格式，結構較繁瑣。
