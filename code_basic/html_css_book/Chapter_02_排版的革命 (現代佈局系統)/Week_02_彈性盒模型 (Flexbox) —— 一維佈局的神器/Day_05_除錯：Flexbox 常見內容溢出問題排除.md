# Day 5: 除錯：Flexbox 常見內容溢出問題排除

Flexbox 雖然好用，但有時候它的「彈性」會造成一些意外的副作用，最常見的就是「內容死都不縮小」或是「寬度被撐爆」。

今天我們來看三個最經典的 Flexbox 坑。

---

## 狀況一：圖片把 Flex Item 撐爆了

### 病徵
你有一個兩欄式排版，左圖右文。結果圖片原始尺寸太大，直接無視 `flex-basis` 設定，把右邊文字擠出視窗外。

### 原因
圖片 (`<img>`) 預設的 `min-width` 是 `auto` (也就是圖片原始寬度)。即使你設了 `flex-shrink: 1`，它縮到原始寬度後就不會再縮了。

### 解藥
強制告訴圖片：你可以縮到比原始寬度還小。
```css
img {
    max-width: 100%; /* 萬用解藥 */
}
```
或者在 Flex Item 上設定：
```css
.item {
    min-width: 0; /* 允許縮小到 0 */
}
```

---

## 狀況二：文字太長不換行 (Long Text Overflow)

### 病徵
Flex Item 裡面有一串很長的網址或不換行的文字 (`white-space: nowrap`)，結果整個 Item 被撐寬，導致破版，捲軸出現。

### 原因
跟圖片一樣，Flex Item 預設的 `min-width` 是 `auto` (內容寬度)。如果內容很寬，它就認為「我不能再縮了」。

### 解藥
在父層的 Flex Item 上設定：
```css
.flex-item {
    min-width: 0; /* 關鍵咒語！告訴瀏覽器：就算內容很寬，你也可以強制縮小我 */
    /* 或者 */
    overflow: hidden;
}
```

### 實作範例
```html
<style>
    .container { display: flex; width: 300px; border: 1px solid red; }
    .left { flex: 0 0 50px; background: blue; }
    
    /* 如果沒有 min-width: 0，右邊會被文字撐爆 */
    .right { flex: 1; background: green; min-width: 0; } 
    
    .text { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
</style>

<div class="container">
    <div class="left">Icon</div>
    <div class="right">
        <div class="text">這是一段超級無敵長長長長長長到爆掉的文字</div>
    </div>
</div>
```

---

## 狀況三：Column 方向的垂直置中失效

### 病徵
`flex-direction: column`，設定了 `justify-content: center`，但內容卻還是在最上面。

### 原因
因為 Container **沒有高度**。水平排版時，block 元素預設寬度就是 100%，所以 `justify-content` 有空間可以分配。但垂直排版時，Container 的高度預設是被內容撐開的 (height: auto)，既然高度剛好等於內容高度，那自然沒有「剩餘空間」可以置中。

### 解藥
給 Container 一個明確的高度。
```css
.container {
    display: flex;
    flex-direction: column;
    height: 100vh; /* 或是具體的 px */
    justify-content: center;
}
```

---

## 總結：Flexbox 除錯三板斧

1.  **內容爆版**：先檢查圖片有沒有 `max-width: 100%`。
2.  **文字爆版**：在 Flex Item 加上 `min-width: 0`。
3.  **對齊無效**：檢查 Container 有沒有設定 `height` (垂直對齊時) 或 `width` (水平對齊時)。
