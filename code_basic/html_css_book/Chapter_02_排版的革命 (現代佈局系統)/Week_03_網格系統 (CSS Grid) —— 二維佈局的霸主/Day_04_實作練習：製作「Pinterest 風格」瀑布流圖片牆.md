# Day 4: 實作練習：製作「Pinterest 風格」瀑布流圖片牆

瀑布流 (Masonry Layout) 是一種很受歡迎的排版方式，特點是「等寬不等高」，且方塊之間緊密排列，就像 Pinterest 的首頁一樣。

要注意的是，**純 CSS Grid 目前還無法做到 100% 完美的 Masonry (依照高度自動補位)** (註：Firefox 有實驗性屬性 `grid-template-rows: masonry`，但尚未普及)。

不過，我們可以利用 Grid 的特性來做出「近似」的效果，或者使用 `column-count` (多欄佈局) 來達成。今天我們來試試看 Grid 的 `dense` 屬性帶來的魔法。

---

## 1. 任務目標
建立一個圖片牆，圖片有長有短，要能自動填補空間，不要有破洞。

---

## 2. 核心技術：`grid-auto-flow: dense`

預設的 Grid 是乖乖排隊的，如果第一格放不下一個大塊的 item，它就會留白跳到下一行。
但加上 `dense` 之後，瀏覽器會回頭去找「有沒有前面的小洞可以塞？」，如果有就塞進去。

## 3. 實作程式碼 (Grid Dense 版)

這裡我們模擬一個「有大有小」的圖片牆。

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .gallery {
            display: grid;
            /* 自動填滿，每欄至少 200px */
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            /* 行高基準設小一點，讓 span 更細緻 */
            grid-auto-rows: 50px; 
            gap: 10px;
            
            /* 關鍵！開啟補洞模式 */
            grid-auto-flow: dense; 
        }

        .item {
            background-color: #ddd;
            border-radius: 8px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 1.5rem;
            color: #555;
            overflow: hidden;
        }
        
        .item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        /* 隨機指定高度 (透過 span rowspan) */
        /* 跨 2 格高度 (50*2 + 10 = 110px) */
        .h-2 { grid-row: span 2; background: #ffbe76; }
        
        /* 跨 3 格高度 */
        .h-3 { grid-row: span 3; background: #ff7979; }
        
        /* 跨 4 格高度 */
        .h-4 { grid-row: span 4; background: #badc58; }
        
        /* 跨 5 格高度 */
        .h-5 { grid-row: span 5; background: #dff9fb; }
        
        /* 也有胖子 (跨 2 欄寬度) */
        .w-2 { grid-column: span 2; background: #686de0; color: white; }

    </style>
</head>
<body>

    <div class="gallery">
        <div class="item h-2">1</div>
        <div class="item h-4">2</div>
        <div class="item h-3">3</div>
        <div class="item h-2">4</div>
        <div class="item w-2 h-3">5 (Big)</div> <!-- 這是一個大塊頭 -->
        <div class="item h-4">6</div>
        <div class="item h-2">7</div>
        <div class="item h-5">8</div>
        <div class="item h-3">9</div>
        <div class="item h-2">10</div>
        <!-- 試著把這裡順序打亂，grid dense 會自動幫你填補空隙 -->
    </div>

</body>
</html>
```

---

## 4. 另一種解法：`column-count` (純 CSS 真瀑布流)

如果你完全不在意順序 (由上到下，再左到右)，只想讓圖片緊密且簡單並排，這個屬性最快：

```css
.gallery-column {
    column-count: 3; /* 強制三欄 */
    column-gap: 10px;
}
.item {
    break-inside: avoid; /* 防止圖片被切一半 */
    margin-bottom: 10px;
}
```
這個做法的缺點是：內容順序是「直的」流動 (先填滿第一欄再填第二欄)，對於使用者閱讀順序 (通常是橫的 z 型) 比較不友善。

但在純展示圖片的情境下，`column-count` 是一個非常棒的選擇。
