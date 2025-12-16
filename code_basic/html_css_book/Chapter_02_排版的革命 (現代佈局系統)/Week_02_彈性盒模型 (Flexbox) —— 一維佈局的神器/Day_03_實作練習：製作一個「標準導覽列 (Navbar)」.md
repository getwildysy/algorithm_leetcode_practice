# Day 3: 實作練習：製作一個「標準導覽列 (Navbar)」

今天我們要用 Flexbox 來實作幾乎每個網站都會有的元件：導覽列。

## 1. 任務目標
製作一個包含三部分的 Navbar：
1.  **左側**：Logo (靠左)。
2.  **右側**：選單連結 (靠右)。
3.  **最右側**：登入按鈕 (靠右，與選單有點距離)。

---

## 2. 結構分析

最簡單的做法是使用 `justify-content: space-between`。
我們可以把內容分成兩大群組：
1.  Logo
2.  導覽連結區塊 (包含連結與按鈕)

或者，更直覺的做法：
Container 設為 flex，然後利用 `margin-left: auto` 的特性來推擠元素。

---

## 3. 實作程式碼

我們採用 `margin-left: auto` 的技巧，這是在 Flexbox 裡把某元素「推到最右邊」的密技。

```html
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <title>Flexbox Navbar</title>
    <style>
        /* 基礎 Reset */
        body { margin: 0; font-family: sans-serif; }
        ul { margin: 0; padding: 0; list-style: none; }
        a { text-decoration: none; color: #333; }

        /* Navbar 本體 */
        .navbar {
            display: flex;         /* 1. 啟動 Flex */
            align-items: center;   /* 2. 垂直置中 */
            padding: 0 20px;       /* 左右留點空隙 */
            height: 60px;          /* 固定高度 */
            background-color: white;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            color: #2c3e50;
            margin-right: 30px;
        }

        .nav-links {
            display: flex; /* 讓 li 橫排 */
            gap: 20px;     /* 每個連結之間的間距 (現代 CSS 超好用屬性) */
        }

        .nav-links a {
            font-weight: 500;
            transition: color 0.3s;
        }
        .nav-links a:hover {
            color: #007bff;
        }

        /* 關鍵技巧！ */
        .auth-buttons {
            margin-left: auto; /* 3. 將自己推到最右邊 */
            
            display: flex; /* 按鈕自己也要橫排 */
            gap: 10px;
        }

        .btn {
            padding: 8px 16px;
            border-radius: 4px;
            font-size: 0.9rem;
        }
        .btn-login {
            border: 1px solid #ddd;
        }
        .btn-signup {
            background-color: #007bff;
            color: white;
        }
    </style>
</head>
<body>

    <nav class="navbar">
        <!-- Logo -->
        <a href="#" class="logo">Brand</a>

        <!-- 中間選單 -->
        <ul class="nav-links">
            <li><a href="#">Home</a></li>
            <li><a href="#">Features</a></li>
            <li><a href="#">Pricing</a></li>
            <li><a href="#">About</a></li>
        </ul>

        <!-- 右側按鈕 -->
        <div class="auth-buttons">
            <a href="#" class="btn btn-login">Login</a>
            <a href="#" class="btn btn-signup">Sign Up</a>
        </div>
    </nav>

    <!-- 為了展示 Navbar 下方內容 -->
    <div style="padding: 20px;">
        <h1>Welcome to Layout Master</h1>
        <p>Try resizing the browser window.</p>
    </div>

</body>
</html>
```

## 4. 學習點 (Takeaway)

1.  **`align-items: center`**：這是讓 Logo、文字連結、按鈕都在同一條水平線上垂直居中的關鍵。沒有它，大家會忽高忽低。
2.  **`gap`**：以前我們要用 `margin-right` 還要處理最後一個元素的 margin，現在直接用 `gap` 設定間距，乾淨俐落。
3.  **`margin-left: auto`**：在 Flex container 中，如果你對一個 item 設 `margin-left: auto`，它會吃掉左邊所有剩餘空間，導致自己被擠到最右邊。這是做導覽列最常用的技巧。
