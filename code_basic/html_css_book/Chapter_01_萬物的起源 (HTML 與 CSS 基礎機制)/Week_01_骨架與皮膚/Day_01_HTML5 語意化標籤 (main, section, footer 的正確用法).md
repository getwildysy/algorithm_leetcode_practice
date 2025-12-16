# Day 1: HTML5 語意化標籤 (main, section, footer 的正確用法)

## 1. 什麼是「語意化標籤 (Semantic Elements)」？

在 HTML5 以前，我們習慣用大量的 `<div>` 來包裝網頁區塊。雖然外觀可以透過 CSS 排版成一樣，但對於瀏覽器、搜尋引擎 (SEO) 和螢幕閱讀器 (Accessibility) 來說，這些 `<div>` 毫無意義。

**語意化標籤** 就是「用有意義的標籤名稱，來描述內容的用途」。

### 為什麼要使用語意化標籤？
1.  **SEO 優化**：搜尋引擎能更理解網頁結構，提升排名。
2.  **輔助科技友善**：盲人使用的螢幕閱讀器能直接跳轉到「主要內容」或「導覽列」。
3.  **程式碼可讀性**：開發者一眼就能看出這是頁首、頁尾還是側邊欄。

---

## 2. 常用語意化標籤詳解

### `<header>`：頁首
通常包含網站 Logo、導覽選單或搜尋框。它不只是用在整個網頁的頂部，也可以用在每篇文章的開頭（例如文章標題區）。

### `<nav>`：導覽列
包含主要連結的區塊，例如網站主選單、目錄。

### `<main>`：主要內容
**每個頁面只能有一個 `<main>`**，代表該頁面最核心、最獨特的內容。不應包含在每個頁面都重複的內容（如側邊欄、Footer）。

### `<section>`：章節 / 區塊
用來將內容分組。通常 `<section>` 裡面會有一個標題 (`<h2>` - `<h6>`)。如果你只是為了排版包裝 (CSS Styling) 而沒有語意與標題，請繼續使用 `<div>`。

### `<article>`：獨立文章
代表一段可以獨立存在的內容，例如：一篇部落格文章、一則新聞、一則 FB 貼文。即便把它單獨抽離出來，內容也是完整的。

### `<aside>`：側邊欄 / 補充資訊
與主要內容只有間接關聯的內容。例如：相關文章推薦、廣告、側邊選單。

### `<footer>`：頁尾
通常包含版權宣告、聯絡資訊、社群連結等。

---

## 3. `<div>` vs `<section>` vs `<article>` 如何選擇？

這最容易搞混，請依照以下邏輯判斷：

1.  **它是獨立完整的內容嗎？** (例如一篇文章、一則留言) -> 用 `<article>`
2.  **它是有標題的內容群組嗎？** (例如「最新消息區」、「產品介紹區」) -> 用 `<section>`
3.  **它只是為了排版或包裝樣式嗎？** (例如 flex container) -> 用 `<div>`

---

## 4. 實作範例：標準部落格結構

以下是一個經典的部落格首頁結構。

### ❌ 錯誤示範 (Div Soup)
```html
<div class="header">
    <div class="logo">My Blog</div>
    <div class="nav">...</div>
</div>
<div class="content">
    <div class="post">...</div>
    <div class="post">...</div>
</div>
<div class="footer">...</div>
```

### ✅ 正確示範 (Semantic HTML)

```html
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <title>語意化標籤範例</title>
</head>
<body>

    <!-- 頁首：全站共用 -->
    <header>
        <h1>Antigravity 技術週刊</h1>
        <nav>
            <ul>
                <li><a href="#home">首頁</a></li>
                <li><a href="#about">關於我們</a></li>
                <li><a href="#contact">聯絡方式</a></li>
            </ul>
        </nav>
    </header>

    <!-- 主要內容區：本頁獨有 -->
    <main>
        
        <!-- 文章區塊 -->
        <section id="latest-posts">
            <h2>最新文章</h2>

            <!-- 單篇文章 -->
            <article>
                <h3>HTML5 的奧義</h3>
                <p>發表於 <time datetime="2023-10-01">2023-10-01</time></p>
                <p>今天我們來談談為什麼要放棄 div...</p>
                <a href="#">閱讀更多</a>
            </article>

            <article>
                <h3>CSS Grid 攻略</h3>
                <p>發表於 <time datetime="2023-10-05">2023-10-05</time></p>
                <p>Grid 是二維排版的救星...</p>
                <a href="#">閱讀更多</a>
            </article>
        </section>

    </main>

    <!-- 側邊欄：補充資訊 -->
    <aside>
        <h3>熱門標籤</h3>
        <ul>
            <li><a href="#">Frontend</a></li>
            <li><a href="#">Design</a></li>
        </ul>
    </aside>

    <!-- 頁尾 -->
    <footer>
        <p>&copy; 2023 Antigravity Blog. All rights reserved.</p>
    </footer>

</body>
</html>
```

## 5. 課後練習
試著將你目前專案中的「導覽列」原本的 `<div class="nav">` 改為 `<nav>`，並確保裡面使用了 `<ul>` 與 `<li>` 來排列連結。
