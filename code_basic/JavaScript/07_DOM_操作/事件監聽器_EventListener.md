# DOM 事件監聽器 (Event Listener)

事件監聽器 (Event Listener) 是 JavaScript 處理使用者互動或瀏覽器行為的核心機制。它允許我們在特定事件發生時執行指定的程式碼。

## 1. 什麼是事件？

事件是網頁上發生的一些動作，例如：
*   使用者點擊按鈕 (`click`)
*   滑鼠移動 (`mousemove`)
*   鍵盤輸入 (`keydown`, `keyup`)
*   表單提交 (`submit`)
*   頁面載入完成 (`load`)
*   圖片載入失敗 (`error`)

## 2. 註冊事件監聽器

### `element.addEventListener(event, handler, options)` (推薦)
這是最現代和推薦的方式，它允許為同一個元素和同一個事件註冊多個監聽器，而不會互相覆蓋。

*   `event`: 欲監聽的事件類型字串 (例如 `'click'`, `'mouseover'`)。
*   `handler`: 事件發生時要執行的函式 (稱為事件處理器)。
*   `options`: (可選) 一個物件，用於設定監聽器的行為，最常見的是 `capture`。

```html
<button id="myButton">Click Me</button>
```
```javascript
const myButton = document.querySelector("#myButton");

// 方式一：匿名函式
myButton.addEventListener('click', function() {
    alert('Button clicked!');
});

// 方式二：具名函式 (方便移除)
function handleClick() {
    console.log("Button was clicked!");
}
myButton.addEventListener('click', handleClick);
```

### 移除事件監聽器 `removeEventListener()`
如果需要移除監聽器，必須傳入**完全相同**的事件類型、事件處理器函式和選項。這就是為什麼通常建議使用具名函式作為事件處理器。

```javascript
myButton.removeEventListener('click', handleClick);
```

### 透過 HTML 屬性 (不推薦)
直接在 HTML 標籤中寫 `onclick="..."`。
*   **缺點**：HTML 與 JS 混雜，維護性差；只能有一個處理器。

```html
<button onclick="alert('Hello from HTML!')">Click Me (HTML)</button>
```

### 透過 DOM 屬性 (不推薦)
直接設定元素的 `onclick` 等屬性。
*   **缺點**：只能有一個處理器，後面的會覆蓋前面的。

```javascript
const anotherButton = document.querySelector("#anotherButton");
anotherButton.onclick = function() {
    console.log("First handler");
};
anotherButton.onclick = function() { // 會覆蓋上面那個
    console.log("Second handler");
};
```

## 3. Event 物件

當事件發生時，瀏覽器會自動建立一個 `Event` 物件，並將其作為第一個參數傳遞給事件處理器函式。這個物件包含了事件的詳細資訊。

```javascript
myButton.addEventListener('click', function(event) {
    console.log(event.type);        // "click"
    console.log(event.target);      // 觸發事件的元素 (即 myButton)
    console.log(event.clientX);     // 滑鼠在視窗中的 X 座標
    event.preventDefault();         // 阻止事件的預設行為 (例如提交表單)
});
```
