# Day 5: 實作練習：製作「Header-Sidebar-Content-Footer」標準版型

我們已經學會了 `grid-template-areas`，今天就來實作一個最經典的網站後台管理介面版型。這個練習將是目前為止最接近真實專案的版型。

## 1. 任務目標
製作一個 Dashboard 版型：
1.  **Header**：固定在上方，包含 Logo 和 User Menu。
2.  **Sidebar**：固定在左側，包含導覽連結。
3.  **Content**：右側主要內容區，內容很多時要有捲軸。
4.  **Footer**：固定在最下方。

要求：
*   使用 Grid Area 排版。
*   Sidebar 寬度固定 250px，內容區自動填滿。
*   **Sticky Footer (黏底)**：就算內容很少，Footer 也要貼在視窗底部。

---

## 2. 實作程式碼

```html
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <title>Grid Dashboard Layout</title>
    <style>
        /* 1. Reset */
        * { box-sizing: border-box; }
        body { margin: 0; font-family: sans-serif; }

        /* 2. Container 設定 */
        .layout-container {
            display: grid;
            
            /* 設定高度為 100vh，這樣才能撐滿整個視窗 */
            height: 100vh;
            
            /* 行與列的定義 */
            grid-template-columns: 250px 1fr; /* 左邊固定，右邊彈性 */
            grid-template-rows: 60px 1fr 50px; /* Header高, 內容自動, Footer高 */
            
            /* 區域地圖 */
            grid-template-areas: 
                "header header"
                "sidebar main"
                "header-btm header-btm"; /* 修正：上面打錯了嗎？不，看下面的 trick */
        }
        
        /* 修正地圖：Footer 應該要在最下面 */
         .layout-container {
            grid-template-areas: 
                "header header"
                "sidebar main"
                "footer footer"; /* 還是習慣 sidebar 到底？看需求 */
                /* 如果 sidebar 要通到底：
                   "header header"
                   "sidebar main"
                   "sidebar footer"
                */
        }
        
        /* 為了美觀，稍微調整一下 */
        .header { 
            grid-area: header; 
            background-color: #2c3e50; 
            color: white; 
            display: flex;
            align-items: center;
            padding: 0 20px;
        }

        .sidebar { 
            grid-area: sidebar; 
            background-color: #34495e; 
            color: #ecf0f1; 
            padding: 20px;
        }

        .main { 
            grid-area: main; 
            background-color: #ecf0f1; 
            padding: 20px;
            overflow-y: auto; /* 重點！如果內容太長，只有這裡會捲動，Sidebar 不動 */
        }

        .footer { 
            grid-area: footer; 
            background-color: #95a5a6; 
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 0.8rem;
        }
    </style>
</head>
<body>

    <div class="layout-container">
        
        <header class="header">
            <h3>My Dashboard</h3>
        </header>
        
        <aside class="sidebar">
            <p>Navigation</p>
            <ul>
                <li>Home</li>
                <li>Users</li>
                <li>Settings</li>
            </ul>
        </aside>
        
        <main class="main">
            <h1>Welcome Back!</h1>
            <p>這裡是可以捲動的內容區。</p>
            <p>試著複製很多段文字讓這裡變長...</p>
            <div style="height: 1000px; background: white; margin-top: 20px;">
                Long content area...
            </div>
        </main>
        
        <footer class="footer">
            &copy; 2023 Grid Layout Master
        </footer>

    </div>

</body>
</html>
```

## 3. 進階變化題：Footer 在 Sidebar 右邊？
有些人喜歡 Sidebar 是一路通到底長條的 (像 VS Code 一樣)，Footer 只在 Main 的下面。
這時候只需要改一行：

```css
grid-template-areas: 
    "sidebar header"
    "sidebar main"
    "sidebar footer";
```
(當然 `grid-template-columns` 可能也要微調，看你想不想讓 Header 蓋過 Sidebar)

這就是 Grid 強大的地方，改版型只需要改 CSS 字串，HTML 完全不用動。
