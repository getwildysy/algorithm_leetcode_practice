# Day 1: Tailwind 核心觀念 (Utility-First)

寫了這麼久的 CSS，你是否覺得每次都要想 class name 很痛苦？
`.wrapper`, `.container-inner`, `.header-wrapper-box`...

Tailwind CSS 的出現，就是為了終結這個命名地獄。它提倡 **Utility-First (功能類優先)**。

## 1. 什麼是 Utility-First？

傳統寫法 (Semantic Class)：
```html
<div class="chat-notification">
  <div class="chat-notification-logo-wrapper">
    <img class="chat-notification-logo" src="/img/logo.svg" alt="ChitChat Logo">
  </div>
  <div class="chat-notification-content">
    <h4 class="chat-notification-title">ChitChat</h4>
    <p class="chat-notification-message">You have a new message!</p>
  </div>
</div>

<style>
  .chat-notification {
    display: flex;
    max-width: 24rem;
    margin: 0 auto;
    padding: 1.5rem;
    border-radius: 0.5rem;
    background-color: #fff;
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
  }
  /* ... 下略 50 行 CSS */
</style>
```

Tailwind 寫法 (Utility Class)：
```html
<div class="p-6 max-w-sm mx-auto bg-white rounded-xl shadow-lg flex items-center space-x-4">
  <div class="shrink-0">
    <img class="h-12 w-12" src="/img/logo.svg" alt="ChitChat Logo">
  </div>
  <div>
    <div class="text-xl font-medium text-black">ChitChat</div>
    <p class="text-slate-500">You have a new message!</p>
  </div>
</div>
```
**不用寫一行 CSS！** 你直接在 HTML 上面「組裝」樣式。

---

## 2. 這不就是 Inline Styles 嗎？

很多人第一眼看到 Tailwind 都會說：「這跟寫 `<div style="padding: 10px">` 有什麼兩樣？」

**有很大的兩樣：**

1.  **有約束力 (Constraints)**：
    *   Inline style 你可以寫 `margin: 11px`、`margin: 13px`，造成版面混亂。
    *   Tailwind 只能用 `m-1`, `m-2` (代表固定比例的間距)，強制全站統一。
2.  **響應式設計 (RWD)**：
    *   Inline style 無法寫 Media Query。
    *   Tailwind 可以寫 `md:flex` (螢幕大時變 flex)。
3.  **狀態樣式 (Hover/Focus)**：
    *   Inline style 無法寫 Hover。
    *   Tailwind 可以寫 `hover:bg-blue-700`。

---

## 3. 為什麼它會紅？

因為它解決了 CSS 最難的兩個問題：
1.  **命名** (不用想 class name)。
2.  **維護** (刪除 HTML 時，樣式自動跟著消失，不會留下沒人敢動的 CSS 屍體)。
