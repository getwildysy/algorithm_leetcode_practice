# Day 1: Viewport 概念與 Media Queries (@media) 語法

歡迎來到 RWD (Responsive Web Design) 響應式網頁設計的世界。
在以前，手機版和電腦版是分開的兩個網站 (m.facebook.com vs facebook.com)。但現在，我們希望「同一個網站程式碼，能適應各種螢幕大小」。

---

## 1. 必備咒語：Viewport Meta Tag

如果你做過手機版網頁，卻發現字超級小，必須用手指放大才看得到，那就是少了這行。

在 HTML 的 `<head>` 裡一定要加上：
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

這句話的意思是：
*   **width=device-width**：告訴瀏覽器，請把網頁寬度視為裝置寬度 (而不是預設的 980px 桌機寬度)。
*   **initial-scale=1.0**：初始縮放比例為 1 (不要縮小也不要放大)。

沒有這行，RWD 就不會生效。

---

## 2. 也是咒語：@media query

Media Query 是 CSS 的「條件判斷式」。
如果滿足條件，就套用這塊 CSS；如果不滿足，就跳過。

### 基本語法
```css
/* 預設樣式 (通常是為了手機或全通用) */
body {
    background-color: white;
}

/* 當視窗寬度「至少」有 768px (平板以上) 時，變成黃色 */
@media (min-width: 768px) {
    body {
        background-color: yellow;
    }
}

/* 當視窗寬度「至少」有 1024px (電腦以上) 時，變成綠色 */
@media (min-width: 1024px) {
    body {
        background-color: green;
    }
}
```

---

## 3. 常見雷區：覆蓋順序

CSS 是有順序性的 (Cascading)。
如果你用 `min-width` (由小到大)，請確保你的寫法順序是「由小排到大」。

### ❌ 錯誤寫法
```css
@media (min-width: 1024px) { body { color: red; } }
@media (min-width: 768px) { body { color: blue; } } /* 這會蓋掉上面的 1024 設定！ */
```
因為 1200px 的螢幕同時符合 >768 和 >1024，而 768 寫在「後面」，所以它贏了。

### ✅ 正確寫法 (Mobile First)
```css
/* 1. Base (Mobile) */
body { ... }

/* 2. Tablet */
@media (min-width: 768px) { ... }

/* 3. Desktop */
@media (min-width: 1024px) { ... }
```

---

## 4. 實作範例：RWD 三欄式版型

```html
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .container {
            display: flex;
            flex-wrap: wrap; /* 關鍵！空間不夠要能換行 */
        }

        .box {
            width: 100%; /* 預設手機版：佔滿 100% (一欄) */
            height: 100px;
            margin-bottom: 10px;
            background-color: #ddd;
            border: 1px solid #999;
            text-align: center;
            line-height: 100px;
        }

        /* 平板以上：變成兩欄 (50%) */
        @media (min-width: 600px) {
            .box {
                width: 50%;
            }
        }

        /* 電腦以上：變成四欄 (25%) */
        @media (min-width: 900px) {
            .box {
                width: 25%;
            }
        }
    </style>
</head>
<body>

    <div class="container">
        <div class="box">1</div>
        <div class="box">2</div>
        <div class="box">3</div>
        <div class="box">4</div>
    </div>

</body>
</html>
```
你可以試著調整瀏覽器視窗大小，觀察方塊的變化。
