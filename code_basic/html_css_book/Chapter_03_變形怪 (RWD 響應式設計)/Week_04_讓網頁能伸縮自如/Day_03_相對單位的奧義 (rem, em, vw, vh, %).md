# Day 3: 相對單位的奧義 (rem, em, vw, vh, %)

在 RWD 世界裡，把 `px` 寫死通常是萬惡之源。我們要學習使用「相對單位」，讓元素跟著環境縮放。

---

## 1. 字體單位的對決：`rem` vs `em`

這兩者都是「倍數」的概念。

### `em` (Relative to Parent)
相對**父元素**的字體大小。
*   如果父元素 font-size 是 16px，那 2em = 32px。
*   **缺點 (巢狀地獄)**：如果你有很多層 div 都在設 em，數值會像複利一樣這滾越大 (1.2 * 1.2 * 1.2...)，最後很難算。

### `rem` (Relative to Root)
相對 **根元素 (html)** 的字體大小。
*   瀏覽器預設 `html` 字體是 16px。
*   所以 `1rem` 永遠等於 16px (除非你去改 html 設定)。
*   `2rem` = 32px。
*   **優點**：基準統一，全站好維護。

**結論**：除了特殊的局部元件外，**請全面使用 `rem` 設定字體大小、Margin 和 Padding。**

---

## 2. 視窗單位的對決：`vw`, `vh`

這兩個單位是直接跟著「瀏覽器視窗大小 (Viewport)」走的。

*   `100vw` = 視窗寬度的 100%。(跟 `width: 100%` 很像，但不被父層限制)。
*   `100vh` = 視窗高度的 100%。

### 常見應用
*   **Hero Section (首頁大圖)**：
    ```css
    .hero {
        height: 100vh; /* 剛好佔滿一整個螢幕的高度 */
        width: 100vw;
    }
    ```
*   **響應式字體 (謹慎使用)**：
    ```css
    h1 {
        font-size: 5vw; /* 字體會隨著視窗變寬而變大 */
    }
    ```

---

## 3. 百分比 `%`

*   `width: 50%`：佔**父元素**寬度的一半。
*   **注意**：Margin 和 Padding 如果設 `%`，是參考**父元素的「寬度」** (連垂直方向的 padding-top 也是參考寬度喔！)。

---

## 4. 實作練習：用 rem 打造可全站縮放的系統

這是一個很常見的技巧。如果我們想讓所有東西在超大螢幕上自動變大，只需要改一行 CSS。

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        html {
            /* 預設 16px */
            font-size: 16px; 
        }

        /* 在大螢幕上，調大基準值 */
        @media (min-width: 1200px) {
            html {
                font-size: 18px; /* 這裡一改，下面所有用 rem 的東西都會變大 */
            }
        }

        .card {
            /* 全部使用 rem */
            width: 20rem; 
            padding: 2rem;
            margin: 1rem;
            border: 1px solid #ddd;
        }

        h2 { font-size: 1.5rem; }
        p { font-size: 1rem; }
    </style>
</head>
<body>

    <div class="card">
        <h2>Responsive Card</h2>
        <p>This formatting scales with the root font size.</p>
    </div>

</body>
</html>
```

## 5. 本日總結
1.  字體、間距盡量用 `rem`。
2.  全螢幕區塊用 `vh` / `vw`。
3.  區域佈局用 `%` 或 Flex/Grid。
4.  少用 `px` 寫死寬高。
