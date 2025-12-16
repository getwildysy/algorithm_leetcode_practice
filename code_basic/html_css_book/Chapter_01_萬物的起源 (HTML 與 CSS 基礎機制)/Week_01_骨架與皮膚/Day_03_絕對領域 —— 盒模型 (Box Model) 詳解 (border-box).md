# Day 3: 絕對領域 —— 盒模型 (Box Model) 詳解

## 1. 網頁上的萬物皆是盒子

在 CSS 的眼中，網頁上的每一個元素 (Element)，無論是圖片、標題還是段落，本質上都是一個長方形的盒子。

這個盒子由四個洋蔥般的層次組成（由內而外）：

1.  **Content (內容)**：文字、圖片實際顯示的區域。
2.  **Padding (內距)**：內容與邊框之間的緩衝區（但在背景色範圍內）。
3.  **Border (邊框)**：盒子的邊界線。
4.  **Margin (外距)**：盒子與其他盒子之間的距離（是透明的）。

---

## 2. 世紀大坑：`box-sizing`

這是新手最容易撞牆的地方。CSS 有兩種計算盒子大小的方式：

### A. `content-box` (預設值，也是坑)
當你設定 `width` 時，設定的**只是 Content 的寬度**。Padding 和 Border 會**加上去**，導致元素實際大小比你預期的還大。

*   設定：`width: 100px; padding: 20px; border: 5px solid;`
*   **實際佔用寬度** = 100 + 20*2 + 5*2 = **150px**
*   結果：版面很容易爆掉、破版。

### B. `border-box` (現代標準，推薦使用)
當你設定 `width` 時，**包含了 Content + Padding + Border**。瀏覽器會自動扣掉 Padding 和 Border 的厚度，算出剩下的寬度給 Content。

*   設定：`width: 100px; padding: 20px; border: 5px solid;`
*   **實際佔用寬度** = **100px** (此時內容區只剩 50px)
*   結果：你設定多少它就是多少，排版直覺輕松。

---

## 3. CSS Reset 的起手式

現代網頁開發的第一步，就是把所有元素的 `box-sizing` 全部改成 `border-box`。這會讓你的人生好過很多。

請將這段程式碼加入你每一個 CSS 檔案的最上方：

```css
/* CSS Reset / Base Styles */
*, *::before, *::after {
    box-sizing: border-box;
}

/* 移除瀏覽器預設的 margin (例如 body, h1 等) */
body, h1, h2, h3, p, ul {
    margin: 0;
    padding: 0;
}
```

---

## 4. 實作範例：比較兩種盒模型

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .box {
            width: 200px;
            height: 100px;
            padding: 20px;
            border: 10px solid #333;
            margin-bottom: 20px;
            color: white;
            font-family: sans-serif;
            font-weight: bold;
            text-align: center;
        }

        /* 預設行為：實際寬度會變成 200 + 40 + 20 = 260px */
        .content-box {
            box-sizing: content-box;
            background-color: #e74c3c; /* 紅色 */
        }

        /* 推薦行為：實際寬度鎖死在 200px */
        .border-box {
            box-sizing: border-box;
            background-color: #27ae60; /* 綠色 */
        }
    </style>
</head>
<body>

    <div class="box content-box">Content Box<br>(260px)</div>
    <div class="box border-box">Border Box<br>(200px)</div>

</body>
</html>
```

## 5. Developer Tools (F12) 檢測技巧

打開 Chrome 開發者工具 (F12) -> **Elements** 面板。
在右側樣式欄位往下滑到底，你會看到一個彩色的「方塊圖 (Computed Box Model)」。

*   藍色區塊：Content
*   綠色區塊：Padding
*   黃色區塊：Border
*   橘色區塊：Margin

當你發現元素位置怪怪的，把滑鼠移到這個方塊圖上，網頁上的元素就會高亮顯示對應區域，這是 Debug 必備技能。
