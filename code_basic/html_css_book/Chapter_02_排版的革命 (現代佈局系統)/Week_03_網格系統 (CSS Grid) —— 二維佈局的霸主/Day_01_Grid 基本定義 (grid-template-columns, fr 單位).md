# Day 1: Grid 基本定義 (grid-template-columns, fr 單位)

Flexbox 解決了一維排版，但遇到「二維排版」 (同時控制行與列) 時，CSS Grid 才是真正的王者。

> **比喻**：Flexbox 像是一條珍珠項鍊 (一串連珠)；Grid 像是一個棋盤 (有行有列)。

---

## 1. 啟動 Grid

一樣是在 Container 上設定：
```css
.container {
    display: grid;
}
```

## 2. 定義欄位：`grid-template-columns`

這可能是 Grid 最常用、也最重要的屬性。它用來定義「這一列有幾欄」以及「每一欄多寬」。

### 基本單位 (px, %)
```css
.container {
    /* 三欄，分別是 100px, 200px, 100px */
    grid-template-columns: 100px 200px 100px; 
}
```

### 超級單位：`fr` (Fraction, 分數)
這是 Grid 專用的單位，代表「剩餘空間的一份」。它比 `%` 更強大，因為不用算數學。

```css
.container {
    /* 將寬度分成 3 份 (1+1+1=3)，大家各拿 1 份 -> 等寬三欄 */
    grid-template-columns: 1fr 1fr 1fr;
}
```

```css
.container {
    /* 側邊欄固定 200px，剩下的空間全部給右邊 */
    grid-template-columns: 200px 1fr;
}
```
有沒有發現？這比 Flexbox 的 `flex: 1` 更直觀！

---

## 3. 重複函式：`repeat()`

如果你要寫 12 欄網格，寫 `1fr 1fr ...` 寫 12 次會瘋掉。

```css
.container {
    /* 等同於 1fr 1fr 1fr 1fr */
    grid-template-columns: repeat(4, 1fr);
}
```

你也可以混合使用：
```css
.container {
    /* 第一欄 100px，剩下重複 3 次等寬 */
    grid-template-columns: 100px repeat(3, 1fr);
}
```

---

## 4. 定義列高：`grid-template-rows`

通常我們不設定 `rows`，讓它根據內容自動長高 (auto)。但如果有特殊需求 (例如全螢幕儀表板)，也可以設定：
```css
.container {
    height: 100vh;
    /* Header 60px, Footer 60px, 中間自動填滿 */
    grid-template-rows: 60px 1fr 60px;
}
```

---

## 5. 實作範例：經典 12 欄網格

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .grid-system {
            display: grid;
            /* 建立 12 欄網格，gap 20px */
            grid-template-columns: repeat(12, 1fr);
            gap: 20px; /* 每個格子之間的距離 */
            padding: 20px;
            background-color: #ddd;
        }

        .col {
            background-color: white;
            padding: 20px;
            text-align: center;
            border: 1px solid #999;
        }

        /* 跨欄位 (Spanning) - 明天會細講，先偷看 */
        .span-4 { grid-column: span 4; background-color: #ffcccc; }
        .span-6 { grid-column: span 6; background-color: #ccffcc; }
        .span-12 { grid-column: span 12; background-color: #ccccff; }
    </style>
</head>
<body>

    <div class="grid-system">
        <!-- 一列佔滿 12 格 -->
        <div class="col span-12">Header (Span 12)</div>

        <!-- 兩欄各半 -->
        <div class="col span-6">Half (Span 6)</div>
        <div class="col span-6">Half (Span 6)</div>

        <!-- 三欄均分 -->
        <div class="col span-4">Third (Span 4)</div>
        <div class="col span-4">Third (Span 4)</div>
        <div class="col span-4">Third (Span 4)</div>
    </div>

</body>
</html>
```

## 6. 本日重點
*   `display: grid`
*   `grid-template-columns` 決定版型結構。
*   `fr` 是分配剩餘空間的神器。
*   `repeat()` 讓你少打字。
