# 其他瀏覽器 API (BOM)

除了 DOM 操作和網路請求外，瀏覽器還提供了許多強大的 API (Browser Object Model, BOM)，讓我們可以與瀏覽器本身、視窗、文件位置等進行互動。

## 1. `window` 物件

`window` 物件代表瀏覽器視窗。它是所有全域 JavaScript 物件、函式和變數的父物件。`window` 物件的屬性和方法通常可以直接使用，無需加上 `window.` 前綴。

### 常用屬性與方法

*   `window.innerWidth`, `window.innerHeight`: 視窗內部寬高。
*   `window.scrollX`, `window.scrollY`: 頁面捲動的座標。
*   `window.open(url, target, features)`: 開啟新視窗/標籤頁。
*   `window.close()`: 關閉當前視窗 (只能關閉由 `window.open` 開啟的視窗)。
*   `window.alert()`, `window.confirm()`, `window.prompt()`: 彈出對話框 (已在基本語法介紹)。

## 2. `document` 物件

`document` 物件代表當前載入的 HTML 文件。這是 DOM 的入口點，我們所有 DOM 操作都從它開始。
*   `document.head`, `document.body`: 存取 `<head>` 和 `<body>` 元素。
*   `document.title`: 存取和修改網頁標題。
*   `document.URL`, `document.domain`: 存取當前網頁的 URL 和網域。

## 3. `location` 物件

`location` 物件包含了當前網頁的 URL 資訊。

```javascript
console.log(window.location.href);     // 完整的 URL
console.log(window.location.protocol);  // 協定 (e.g., "http:", "https:")
console.log(window.location.hostname);  // 主機名稱
console.log(window.location.port);      // 埠號
console.log(window.location.pathname);  // 路徑名
console.log(window.location.search);    // 查詢字串 (包含 "?")
console.log(window.location.hash);      // 錨點 (包含 "#")
```

### 常用方法
*   `location.assign(url)`: 載入新文件。
*   `location.replace(url)`: 載入新文件，但會替換掉歷史記錄中的當前頁面 (使用者無法返回)。
*   `location.reload()`: 重新載入當前頁面。

## 4. `history` 物件

`history` 物件提供了瀏覽器歷史記錄的存取，讓你可以控制瀏覽器的前進和後退。

*   `history.back()`: 回到上一頁。
*   `history.forward()`: 前進到下一頁。
*   `history.go(delta)`: 前進或後退 `delta` 步數。
*   `history.pushState(state, title, url)`: 添加一個新的歷史記錄條目 (不重新載入頁面)，用於單頁應用程式 (SPA)。
*   `history.replaceState(state, title, url)`: 替換當前歷史記錄條目。

## 5. `navigator` 物件

`navigator` 物件包含瀏覽器本身的資訊。

*   `navigator.userAgent`: 瀏覽器的使用者代理字串。
*   `navigator.platform`: 瀏覽器運行的平台。
*   `navigator.language`: 瀏覽器語言。
*   `navigator.onLine`: 判斷瀏覽器是否在線。

## 6. `screen` 物件

`screen` 物件包含有關使用者螢幕的資訊。

*   `screen.width`, `screen.height`: 螢幕的寬度和高度 (像素)。
*   `screen.availWidth`, `screen.availHeight`: 螢幕可用寬度和高度 (減去操作系統介面，如工作列)。
