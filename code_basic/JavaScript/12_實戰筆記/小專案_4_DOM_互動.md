# 小專案 4：DOM 互動 (Dynamic DOM Interaction)

**核心概念**: 動態 DOM 操作、事件監聽、屬性修改、樣式控制

這個專案專注於練習如何使用 JavaScript 來實時地改變網頁的內容、結構和樣式，以實現動態的使用者介面。

## 專案功能點

1.  **動態內容更新**：點擊按鈕改變某個元素的文字內容。
2.  **元素顯示/隱藏**：點擊按鈕切換元素的顯示或隱藏狀態。
3.  **樣式切換**：點擊按鈕改變元素的顏色、大小或套用預設的 CSS Class。
4.  **圖片輪播**：點擊按鈕切換圖片。
5.  **動態新增/刪除項目**：點擊按鈕在列表中新增或刪除項目。
6.  **表單驗證**：即時檢查使用者輸入並給予回饋。

## 主要技術點

### 1. HTML 結構 (基本骨架)

*   多個 `button` 元素用於觸發不同的互動。
*   `div`, `p`, `img` 等元素用於展示被修改的內容。
*   列表 (`ul/li`) 用於演示新增/刪除。
*   表單 (`form`, `input`) 用於驗證。

```html
<!-- 範例 HTML 骨架 -->
<div class="interactive-container">
    <h1>DOM 互動練習</h1>

    <section>
        <h2>文字內容與樣式</h2>
        <p id="displayText">初始文字</p>
        <button id="changeTextBtn">改變文字</button>
        <button id="toggleStyleBtn">切換樣式</button>
    </section>

    <section>
        <h2>顯示/隱藏方塊</h2>
        <div id="toggleBox" style="width: 100px; height: 100px; background-color: blue;"></div>
        <button id="toggleBoxBtn">切換方塊顯示</button>
    </section>

    <section>
        <h2>動態列表</h2>
        <ul id="dynamicList">
            <li>項目 A</li>
            <li>項目 B</li>
        </ul>
        <input type="text" id="newItemInput" placeholder="新增項目">
        <button id="addItemBtn">新增列表項目</button>
        <button id="removeItemBtn">刪除最後一個項目</button>
    </section>

    <section>
        <h2>簡單表單驗證</h2>
        <form id="myForm">
            <input type="email" id="emailInput" placeholder="Email">
            <p id="emailError" style="color: red;"></p>
            <button type="submit">提交</button>
        </form>
    </section>
</div>
```

### 2. JavaScript 邏輯

#### (1) 元素查詢與事件監聽

*   使用 `document.querySelector` 或 `getElementById` 獲取所有需要互動的 DOM 元素。
*   為每個互動功能綁定 `addEventListener`。

#### (2) 改變文字內容

*   監聽按鈕點擊，修改 `element.textContent` 或 `element.innerHTML`。

```javascript
const displayText = document.querySelector("#displayText");
document.querySelector("#changeTextBtn").addEventListener('click', () => {
    displayText.textContent = "文字已改變！" + new Date().toLocaleTimeString();
});
```

#### (3) 切換樣式

*   **直接修改 `element.style.property`**：
    ```javascript
    const toggleBox = document.querySelector("#toggleBox");
    document.querySelector("#toggleStyleBtn").addEventListener('click', () => {
        toggleBox.style.backgroundColor = toggleBox.style.backgroundColor === 'blue' ? 'green' : 'blue';
    });
    ```
*   **透過 `element.classList.toggle()`**：
    ```javascript
    // CSS 定義: .active { background-color: red; }
    // element.classList.toggle('active');
    ```

#### (4) 顯示/隱藏元素

*   **透過 `element.style.display`**：
    ```javascript
    const box = document.querySelector("#toggleBox");
    document.querySelector("#toggleBoxBtn").addEventListener('click', () => {
        box.style.display = box.style.display === 'none' ? 'block' : 'none';
    });
    ```
*   **透過 `element.classList.toggle()`**：
    ```javascript
    // CSS 定義: .hidden { display: none; }
    // element.classList.toggle('hidden');
    ```

#### (5) 動態新增/刪除列表項目

*   **新增**：
    *   `document.createElement('li')` 建立新元素。
    *   設定 `li.textContent`。
    *   `listElement.appendChild(newLi)` 插入。
*   **刪除**：
    *   `listElement.lastElementChild.remove()` 移除最後一個子元素。

```javascript
const dynamicList = document.querySelector("#dynamicList");
const newItemInput = document.querySelector("#newItemInput");

document.querySelector("#addItemBtn").addEventListener('click', () => {
    const text = newItemInput.value.trim();
    if (text) {
        const li = document.createElement("li");
        li.textContent = text;
        dynamicList.appendChild(li);
        newItemInput.value = ""; // 清空輸入框
    }
});

document.querySelector("#removeItemBtn").addEventListener('click', () => {
    if (dynamicList.lastElementChild) {
        dynamicList.lastElementChild.remove();
    }
});
```

#### (6) 簡單表單驗證

*   監聽 `input` 的 `input` 事件 (即時驗證) 或 `form` 的 `submit` 事件。
*   使用正規表達式或簡單的條件判斷來檢查輸入。
*   顯示錯誤訊息。

```javascript
const emailInput = document.querySelector("#emailInput");
const emailError = document.querySelector("#emailError");

emailInput.addEventListener('input', () => {
    if (emailInput.value.includes('@')) {
        emailError.textContent = "";
    } else {
        emailError.textContent = "請輸入有效的 Email 地址";
    }
});
```

## 3. CSS 樣式 (簡述)

*   使用 CSS 美化元素。
*   定義不同狀態的 class (如 `.hidden`, `.active`, `.error`)。

## 4. 進階考量

*   **動畫**：使用 CSS Transitions/Animations 或 JavaScript 動畫庫讓互動更流暢。
*   **效能優化**：對於大量動態操作，考慮虛擬 DOM 或其他性能優化技術。
*   **模組化**：將不同的互動邏輯分離到不同的函式或模組中。
*   **可訪問性**：確保所有互動都考慮到螢幕閱讀器或其他輔助技術。
