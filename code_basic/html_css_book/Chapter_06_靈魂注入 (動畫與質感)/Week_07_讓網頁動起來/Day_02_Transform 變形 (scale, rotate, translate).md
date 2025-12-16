# Day 2: Transform 變形 (scale, rotate, translate)

若說 `transition` 是控制時間，那 `transform` 就是控制空間。
它是 CSS 動畫的核心，因為它的效能極好 (使用 GPU 加速)，不會觸發瀏覽器的 Reflow (重排)。

## 1. 2D 變形三巨頭

### A. Translate (位移)
移動元素的位置。
`transform: translateX(10px) translateY(20px);`
*   與 `position: absolute` top/left 的差別？
    *   Top/Left 會觸發 Reflow (牽一髮動全身)，動畫會卡頓。
    *   Translate 只是視覺上的移動，不影響周圍佈局，非常流暢。

### B. Scale (縮放)
放大或縮小。
`transform: scale(1.2);` (放大 1.2 倍)
*   常用在 Hover 時讓卡片稍微變大。

### C. Rotate (旋轉)
旋轉角度。
`transform: rotate(45deg);` (順時針 45 度)

---

## 2. 組合技

你可以同時套用多個變形，順序很重要 (通常是先位移再旋轉)。
`transform: translate(100px, 0) rotate(45deg) scale(0.5);`

---

## 3. 變形原點 (Transform Origin)

預設的原點是中心點 (`center center` 或 `50% 50%`)。
你可以改變它，例如像「掛鐘」一樣擺動，原點就要設在頂部。

`transform-origin: top center;`

---

## 4. 實作練習：互動卡片

我們要用 `translateY` 和 `box-shadow` 做出「浮起來」的感覺。這是現代網頁最常見的微互動。

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: sans-serif; padding: 50px; background: #f0f0f0; }

        .card {
            width: 200px;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            
            /* 關鍵：設定 Transition */
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .card:hover {
            /* 1. 往上浮動 10px (記得 Y grid 是向下的，所以往上是負值) */
            transform: translateY(-10px);
            
            /* 2. 陰影變大變模糊，營造離地感 */
            box-shadow: 0 15px 30px rgba(0,0,0,0.2);
        }
    </style>
</head>
<body>

    <div class="card">
        <h3>Floating Card</h3>
        <p>Hover me to see the effect.</p>
    </div>

</body>
</html>
```

## 5. 為什麼不要用 `width/height` 做動畫？
如果你想做一個「展開/收合」的動畫，直覺會想用 `transition: height 0.3s`。
但這**效能很差**，因為高度改變會推擠到下面的內容，瀏覽器要重新計算所有元素的位置。

**最佳實踐**：盡量只對 `opacity` 和 `transform` 做動畫。
