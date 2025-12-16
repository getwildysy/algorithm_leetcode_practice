# Day 3: Animation 與 Keyframes 自定義動畫

`transition` 只能做「A 到 B」的簡單變化。
如果你要做「一直轉圈圈」、「跳動」、「閃爍」這種複雜動作，你需要 `animation`。

## 1. 定義劇本：`@keyframes`

你要先寫好一個劇本，告訴瀏覽器動畫在 0% 和 100% (或是中間) 要長怎樣。

```css
@keyframes bounce {
    0%   { transform: translateY(0); }
    50%  { transform: translateY(-20px); }
    100% { transform: translateY(0); }
}
```

## 2. 執行劇本：`animation`

定義好後，指定給某個元素：
`animation: [name] [duration] [timing-function] [iteration-count];`

```css
.ball {
    width: 50px;
    height: 50px;
    background: red;
    border-radius: 50%;
    
    /* 執行 bounce 劇本，一次1秒，無限循環 (infinite) */
    animation: bounce 1s ease-in-out infinite;
}
```

---

## 3. 常用參數詳解

*   `animation-name`: 對應 @keyframes 的名字。
*   `animation-duration`: 多久跑完一次 (1s)。
*   `animation-iteration-count`:
    *   `1`: 跑一次就停 (預設)。
    *   `infinite`: 無限迴圈。
    *   `3`: 跑三次。
*   `animation-fill-mode` (重要！):
    *   `none`: 動畫結束後，瞬間回到最原始狀態。
    *   `forwards`: 動畫結束後，**停留在最後一格 (100%) 的樣子**。 (這常是大家要的效果)。

---

## 4. 實作練習：Loading Spinner

用 CSS 做一個一直在轉圈圈的 Loading 圖示。

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        @keyframes spin {
            0%   { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .loader {
            width: 50px;
            height: 50px;
            border: 5px solid #f3f3f3; /* 淺灰底色 */
            border-top: 5px solid #3498db; /* 藍色轉動條 */
            border-radius: 50%; /* 變成圓形 */
            
            /* 開始轉動：2秒一圈，線性 (不要忽快忽慢)，無限循環 */
            animation: spin 2s linear infinite;
        }
    </style>
</head>
<body>

    <div class="loader"></div>

</body>
</html>
```
