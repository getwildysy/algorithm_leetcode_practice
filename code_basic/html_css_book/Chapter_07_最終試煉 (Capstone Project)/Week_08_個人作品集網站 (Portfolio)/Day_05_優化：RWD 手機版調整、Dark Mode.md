# Day 5: 優化：RWD 手機版調整、Dark Mode

功能都做好了，現在我們要讓細節更完美。

## 1. RWD 走查 (Device Testing)

打開 Chrome DevTools (F12) -> Device Mode。
檢查以下幾點：
1.  **iPhone SE (375px)**: 內容有沒有被切掉？字會不會太小？
2.  **iPad (768px)**: 兩欄變一欄的時機點是否自然？
3.  **大螢幕**: 是否需要 `max-width` 限制內容不要散太開？

## 2. Dark Mode (深色模式)

我們使用 CSS Variables 來實作一鍵換膚。

### 定義變數
```css
:root {
    /* 預設: 亮色 */
    --bg-color: #ffffff;
    --text-color: #333333;
    --card-bg: #f5f5f5;
}

/* 當 body 有 .dark 類別時: 深色 */
body.dark {
    --bg-color: #1a1a1a;
    --text-color: #f0f0f0;
    --card-bg: #2d2d2d;
}
```

### 套用變數
```css
body {
    background-color: var(--bg-color);
    color: var(--text-color);
    transition: background-color 0.3s, color 0.3s;
}
```

### 切換開關 (JavaScript)
只需要幾行 JS 就能切換 class。
```js
const toggleBtn = document.getElementById('theme-toggle');

toggleBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark');
});
```

現在，你的網站有了靈魂。
