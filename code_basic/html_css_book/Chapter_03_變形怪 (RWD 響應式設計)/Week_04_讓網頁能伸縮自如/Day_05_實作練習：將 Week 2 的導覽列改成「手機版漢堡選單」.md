# Day 5: 實作練習：將 Week 2 的導覽列改成「手機版漢堡選單」

這是所有切版新手的期中考：**RWD Navbar**。
在電腦版是橫向排列，在手機版要收納成一個漢堡選單，點擊後展開。

為了保持純粹，我們這裡挑戰 **Pure CSS (Checkbox Hack)** 的做法，不寫一行 JavaScript。

## 1. 原理：Checkbox Hack

我們利用 `<input type="checkbox">` 的狀態 (`:checked`) 來控制選單的顯示與隱藏。
1.  放一個 Checkbox (隱藏起來)。
2.  放一個 Label (就是漢堡圖示)，綁定這個 Checkbox。
3.  當 Checkbox 被選中時，選單的高度由 0 變大。

---

## 2. 實作程式碼

這段程式碼比較長，請仔細閱讀註解。

```html
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
    <title>Pure CSS Burger Menu</title>
    <style>
        /* Reset */
        body { margin: 0; font-family: sans-serif; }
        * { box-sizing: border-box; }

        /* Header 本體 */
        .header {
            background-color: #fff;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            position: relative; /* 為了讓選單定位 */
            z-index: 100;
        }

        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 20px;
            height: 60px;
            max-width: 1200px; /* 內容限制寬度 */
            margin: 0 auto;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            color: #333;
            text-decoration: none;
        }

        /* 選單樣式 (預設電腦版) */
        .menu {
            display: flex;
            list-style: none;
            margin: 0;
            padding: 0;
            gap: 20px;
        }

        .menu a {
            text-decoration: none;
            color: #555;
            transition: color 0.3s;
        }
        .menu a:hover { color: #007bff; }

        /* 隱藏的 Checkbox 與 漢堡圖示 (預設電腦版不顯示) */
        .menu-btn { display: none; } /* Checkbox */
        .menu-icon { display: none; } /* Icon */

        /* ============================
           Mobile Styles (手機版樣式)
           ============================ */
        @media (max-width: 768px) {
            
            /* 1. 顯示漢堡圖示 */
            .menu-icon {
                display: block;
                cursor: pointer;
                font-size: 1.5rem;
                user-select: none;
            }

            /* 2. 選單變形：原本是橫排，現在要變絕對定位 dropdown */
            .menu {
                /* 隱藏狀態 */
                display: none; 
                
                /* 變成直排 */
                flex-direction: column;
                gap: 0;

                /* 絕對定位 */
                position: absolute;
                top: 60px; /* Header 高度 */
                left: 0;
                width: 100%;
                background-color: #f9f9f9;
                border-top: 1px solid #ddd;
            }

            .menu li {
                width: 100%;
                text-align: center;
                border-bottom: 1px solid #eee;
            }

            .menu a {
                display: block;
                padding: 15px;
            }

            /* 3. Checkbox Hack 核心邏輯 */
            /* 當 #menu-btn 被勾選 (checked) 時，選取它後面的 (.menu) */
            #menu-btn:checked ~ .menu {
                display: flex; /* 顯示出來！ */
            }
        }
    </style>
</head>
<body>

    <header class="header">
        <nav class="navbar">
            <a href="#" class="logo">Brand</a>

            <!-- Checkbox Hack (要放在 menu 前面) -->
            <input type="checkbox" id="menu-btn" class="menu-btn">
            
            <!-- 漢堡圖示 (label bound to checkbox) -->
            <label for="menu-btn" class="menu-icon">
                ☰
            </label>

            <!-- 選單連結 -->
            <ul class="menu">
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Works</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>

    <div style="padding: 20px;">
        <h1>Resize Window!</h1>
        <p>當視窗小於 768px 時，右上角會出現漢堡選單。</p>
        <p>不需要 JavaScript 也能做到。</p>
    </div>

</body>
</html>
```

## 3. 下一步
學完了 RWD，這週我們已經能做出適應各種裝置的現代網頁了。
從 HTML 結構、CSS 排版 (Flex/Grid) 到 RWD，你已經掌握了手刻網頁的核心技能。

下週開始，我們要進入「工匠的工具箱」，學習如何透過 **Sass** 來加速我們的開發流程。
