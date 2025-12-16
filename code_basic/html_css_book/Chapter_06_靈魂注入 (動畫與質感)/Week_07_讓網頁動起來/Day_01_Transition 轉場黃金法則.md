# Day 1: Transition 轉場黃金法則

網頁之所以會「生硬」，通常是因為狀態切換是瞬間的 (0ms)。
`transition` 是讓網頁變高級最廉價且有效的方法。

## 1. 基本語法

CSS Transition 需要四個要素 (通常我們用簡寫)：
`transition: [property] [duration] [timing-function] [delay];`

例如：
```css
.btn {
    background-color: blue;
    /* 當 background-color 改變時，花 0.3秒 平滑過渡 */
    transition: background-color 0.3s ease;
}

.btn:hover {
    background-color: red;
}
```

---

## 2. 黃金法則 (Golden Rules)

要做出有質感的動畫，請遵守以下原則：

### A. 不要過度使用 (Don't overdo it)
不是所有東西都要動。通常只有 **互動元件 (按鈕、連結、Input)** 和 **大型區塊顯隱 (Modal, Dropdown)** 需要動畫。

### B. 時間要短 (Keep it snappy)
*   **0.1s (100ms)**: 感覺像瞬間，但有極微小的柔和感。適合 Hover 變色。
*   **0.2s - 0.3s**: 最佳甜蜜點。適合大多數按鈕縮放、位移。
*   **0.5s 以上**: 感覺「拖泥帶水」。除非是大面積的區塊移動 (例如側邊欄滑出)，否則不要超過 0.3s。

### C. 緩動函數 (Timing Function)
*   `linear`: 機械感，像輸送帶。**少用**。
*   `ease` (預設): 起步慢、中間快、結尾慢。最自然。
*   `ease-out`: 一開始快，結尾慢。適合**進場 (Enter)** 動畫。
*   `ease-in`: 一開始慢，結尾快。適合**退場 (Exit)** 動畫。

---

## 3. 常見雷點：Transition `all`

很多新手懶惰會寫 `transition: all 0.3s ease;`。
這有兩個缺點：
1.  **效能**：瀏覽器要監控所有屬性，比較耗效能。
2.  **意外副作用**：如果你改變了 `margin` 想要重排版面，結果它也給你慢慢滑動，看起來會很怪。

**建議**：明確指定要動的屬性，例如 `transition: background-color 0.3s, transform 0.3s;`。

---

## 4. 實作練習

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .box {
            width: 100px;
            height: 100px;
            background: #007bff;
            margin: 50px;
            border-radius: 8px;
            cursor: pointer;
            
            /* 1. 指定屬性：寬度、顏色、陰影 */
            /* 2. 時間：0.3秒 */
            transition: width 0.3s ease, background-color 0.3s ease, box-shadow 0.3s ease;
        }

        .box:hover {
            width: 200px;
            background: #0056b3;
            box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        }
    </style>
</head>
<body>
    <div class="box"></div>
</body>
</html>
```
