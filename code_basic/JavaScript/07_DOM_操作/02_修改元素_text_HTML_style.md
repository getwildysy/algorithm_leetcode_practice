# DOM 操作：修改元素 (Text, HTML, Style)

查詢到 DOM 元素後，最常見的操作就是修改它們的內容、結構或樣式。

## 1. 修改元素內容

### (1) `textContent`
*   **功能**：取得或設定元素的**純文字內容**。
*   **安全性**：會自動將 HTML 標籤轉義，因此**比較安全**，不會產生 XSS 攻擊風險。

```javascript
const myDiv = document.querySelector("#myDiv");

// 取得內容
console.log(myDiv.textContent); // "Hello <strong>World</strong>"

// 設定內容 (純文字)
myDiv.textContent = "這是新內容";
// 頁面上顯示：這是新內容
```

### (2) `innerHTML`
*   **功能**：取得或設定元素的**HTML 內容**。
*   **安全性**：設定時會解析 HTML 標籤。如果內容來源不可信，可能導致 XSS 攻擊。

```javascript
const myDiv = document.querySelector("#myDiv");

// 取得內容
console.log(myDiv.innerHTML); // "Hello <strong>World</strong>"

// 設定內容 (包含 HTML)
myDiv.innerHTML = "<h1>標題</h1><p>段落</p>";
// 頁面上顯示：一個 h1 標題和一個 p 段落
```

## 2. 修改元素屬性 (Attributes)

### 直接存取 (常見屬性)
許多常見的 HTML 屬性可以直接透過元素物件的屬性來存取和修改。

```javascript
const myImage = document.querySelector("#myImage"); // <img id="myImage" src="old.jpg">
myImage.src = "new.jpg";
myImage.alt = "新圖片";
myImage.className = "active highlight"; // 修改 class
myImage.id = "newID"; // 修改 id
```

### `setAttribute()` 與 `getAttribute()`
對於非標準屬性、自訂屬性或在某些情況下更通用的存取方式。

```javascript
const myLink = document.querySelector("#myLink"); // <a id="myLink" href="#">Link</a>

myLink.setAttribute("href", "https://example.com");
myLink.setAttribute("target", "_blank");
myLink.setAttribute("data-id", "123"); // 設定自訂 data 屬性

console.log(myLink.getAttribute("href")); // https://example.com
```

### `removeAttribute()`
刪除元素的屬性。

```javascript
myLink.removeAttribute("target"); // 移除 target="_blank"
```

## 3. 修改元素樣式 (Style)

### `element.style.property`
直接修改元素的內聯樣式 (Inline Style)。屬性名稱使用**駝峰式命名**。

```javascript
const box = document.querySelector(".box");

box.style.backgroundColor = "blue";
box.style.width = "200px";
box.style.border = "1px solid black";
```

### `classList` API
用於更方便地操作元素的 class。

*   `add(className)`: 添加一個 class
*   `remove(className)`: 移除一個 class
*   `toggle(className)`: 存在則移除，不存在則添加
*   `contains(className)`: 檢查是否包含某個 class

```javascript
const myElement = document.querySelector("#myElement");

myElement.classList.add("active");
myElement.classList.remove("highlight");

if (myElement.classList.contains("active")) {
    console.log("包含 active class");
}

myElement.classList.toggle("hidden"); // 如果有 hidden 就移除，沒有就加上
```
