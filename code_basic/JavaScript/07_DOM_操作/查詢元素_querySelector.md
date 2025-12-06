# DOM 操作：查詢元素 (Querying Elements)

DOM (Document Object Model) 是 HTML/XML 文件的一個編程介面。它將網頁文件表示為一個由物件組成的樹狀結構，讓 JavaScript 能夠存取、操作網頁內容和結構。

要操作 DOM 元素，首先需要能夠**查詢 (Query)** 到它們。

## 1. 最常用的查詢方法

### (1) `document.querySelector(selector)`
*   **功能**：回傳文件中**第一個**符合指定 CSS 選擇器 (`selector`) 的元素。
*   **回傳值**：一個 `Element` 物件，如果找不到則回傳 `null`。

```javascript
// 查詢第一個 ID 為 "myButton" 的元素
const myButton = document.querySelector("#myButton");

// 查詢第一個 class 為 "item" 的元素
const firstItem = document.querySelector(".item");

// 查詢第一個 div 中的 p 元素
const divP = document.querySelector("div p");
```

### (2) `document.querySelectorAll(selector)`
*   **功能**：回傳文件中**所有**符合指定 CSS 選擇器 (`selector`) 的元素。
*   **回傳值**：一個 `NodeList` 物件（類似陣列，但不是真正的陣列），如果找不到則回傳空的 `NodeList`。

```javascript
// 查詢所有 class 為 "item" 的元素
const allItems = document.querySelectorAll(".item");

// 遍歷 NodeList
allItems.forEach(item => {
    console.log(item.textContent);
});

// 轉換為真正的陣列 (方便使用更多陣列方法)
const itemsArray = Array.from(allItems);
```

## 2. 其他查詢方法 (較舊或特定用途)

### (1) `document.getElementById(id)`
*   **功能**：回傳文件中 ID 為 `id` 的元素。
*   **回傳值**：一個 `Element` 物件，如果找不到則回傳 `null`。
*   **特點**：效率非常高，但只能透過 ID 查詢。

```javascript
const header = document.getElementById("mainHeader");
```

### (2) `document.getElementsByClassName(name)`
*   **功能**：回傳文件中所有 class 名稱為 `name` 的元素。
*   **回傳值**：一個 `HTMLCollection` 物件（實時更新的類陣列）。

```javascript
const highlighted = document.getElementsByClassName("highlight");
```

### (3) `document.getElementsByTagName(name)`
*   **功能**：回傳文件中所有指定標籤名稱 (`name`) 的元素。
*   **回傳值**：一個 `HTMLCollection` 物件。

```javascript
const allParagraphs = document.getElementsByTagName("p");
```

## 3. 從元素內部查詢

上述方法都是從 `document` 物件開始查詢整個文件。但也可以從一個已有的元素內部查詢其後代元素。

```html
<div id="container">
    <p class="text">First paragraph</p>
    <p class="text">Second paragraph</p>
</div>
```

```javascript
const container = document.querySelector("#container");

// 從 container 內部查詢第一個 class 為 text 的 p 元素
const p1 = container.querySelector(".text"); 

// 從 container 內部查詢所有 class 為 text 的 p 元素
const allTextsInContainer = container.querySelectorAll(".text");
```
