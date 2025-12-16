# Day 2: grid-area 區域規劃與 gap 間距設定

如果說 `grid-template-columns` 是用數字來畫格子，那 `grid-template-areas` 就是用「畫圖」的方式來排版。這功能超級直觀，是 Grid 最迷人的地方。

---

## 1. 像畫 ASCII Art 一樣排版

想像你有一個已經切好的網格，你想要把某些格子合併起來變成「Header」，某些變「Side」，某些變「Main」。

### Step 1: 定義區域名字
先在子元素上取好名字：
```css
.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main { grid-area: main; }
.footer { grid-area: footer; }
```

### Step 2: 在 Container 畫地圖
```css
.container {
    display: grid;
    grid-template-columns: 200px 1fr; /* 左邊 200px，右邊剩下 */
    grid-template-rows: 60px 1fr 60px; /* 上中下高度 */
    
    /* 這裡就是魔法發生的地方 */
    grid-template-areas: 
        "header  header"
        "sidebar main"
        "footer  footer";
}
```
瀏覽器看到這段「地圖」，就會自動把對應的子元素放到正確的位置，並且自動合併格子！

---

## 2. 間距神器：gap

在 CSS Grid 出現之前，要算 Margin 是一件很痛苦的事 (例如 `margin-right: 10px` 但最後一個不要 margin)。

現在，只需要一行：
```css
.container {
    gap: 20px; /* 行與列的間距都是 20px */
    
    /* 也可以分開設 */
    /* row-gap: 20px; */
    /* column-gap: 50px; */
}
```

---

## 3. 實作範例：手機與電腦版型切換 (預告 RWD)

這個 `grid-template-areas` 最強大的地方在於，當我們要變更版型時，只需要改「地圖」就好，完全不用動 HTML 結構。

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .container {
            display: grid;
            gap: 10px;
            height: 100vh;
        }

        .item { padding: 20px; background: #eee; border: 1px solid #999; }

        .header { grid-area: hd; background: #ffcccc; }
        .sidebar { grid-area: sd; background: #ccffcc; }
        .main { grid-area: mn; background: #ccccff; }
        .footer { grid-area: ft; background: #ffffcc; }

        /* 電腦版：標準三欄式 */
        @media (min-width: 768px) {
            .container {
                grid-template-columns: 200px 1fr;
                grid-template-rows: 60px 1fr 60px;
                grid-template-areas: 
                    "hd hd"
                    "sd mn"
                    "ft ft";
            }
        }

        /* 手機版：全部變成一條龍直排 */
        @media (max-width: 767px) {
            .container {
                grid-template-columns: 1fr;
                grid-template-rows: 60px auto 1fr 60px;
                grid-template-areas: 
                    "hd"
                    "mn" 
                    "sd" /* 注意！我們可以把 sidebar 改排在 main 下面 */
                    "ft";
            }
        }
    </style>
</head>
<body>

    <div class="container">
        <div class="header">Header</div>
        <div class="sidebar">Sidebar</div>
        <div class="main">Main Content</div>
        <div class="footer">Footer</div>
    </div>

</body>
</html>
```

注意看上面的 HTML 結構完全沒變，但我們可以透過改變 `grid-template-areas` 來隨意調換 Sidebar 和 Main 的顯示順序 (在手機版把 Sidebar 放到內容下面)，這是傳統 CSS 很難做到的。
