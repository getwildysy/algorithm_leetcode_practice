# Day 4: 實作練習：製作一個「垂直置中」的登入畫面

在 CSS 的歷史上，「垂直置中」曾經是一個超級難題 (需要用 table, absolute + transform, 或 inline-block + weird hacks)。

但在 Flexbox 時代，這只是一塊蛋糕。

## 1. 任務目標
製作一個登入頁面：
1.  背景全螢幕漸層。
2.  登入卡片 (Login Card) 完美置於畫面正中央。
3.  卡片內包含標題、輸入框、按鈕。

---

## 2. 核心原理

要讓一個東西在畫面正中央，只需要三個咒語：

1.  父元素要有高度 (`min-height: 100vh`)。
2.  `display: flex`。
3.  `justify-content: center` (水平置中)。
4.  `align-items: center` (垂直置中)。

---

## 3. 實作程式碼

```html
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <title>Login Page</title>
    <style>
        * { box-sizing: border-box; }

        body {
            margin: 0;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            
            /* 1. 確保 Body 至少跟視窗一樣高 */
            min-height: 100vh;
            
            /* 2. 啟動 Flexbox */
            display: flex;
            
            /* 3. 水平置中 */
            justify-content: center;
            
            /* 4. 垂直置中 */
            align-items: center;

            /* 背景美化 */
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }

        .login-card {
            background-color: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            width: 100%;
            max-width: 400px; /* 限制最大寬度，避免在大螢幕太寬 */
        }

        .login-title {
            text-align: center;
            margin-bottom: 30px;
            color: #333;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-label {
            display: block;
            margin-bottom: 8px;
            color: #666;
            font-size: 0.9rem;
        }

        .form-input {
            width: 100%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-size: 1rem;
            outline: none;
            transition: border-color 0.3s;
        }
        .form-input:focus {
            border-color: #764ba2;
        }

        .btn-submit {
            width: 100%;
            padding: 12px;
            background-color: #764ba2;
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 1rem;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .btn-submit:hover {
            background-color: #5b3a7d;
        }

        .footer-link {
            display: block;
            text-align: center;
            margin-top: 20px;
            color: #888;
            font-size: 0.85rem;
            text-decoration: none;
        }
    </style>
</head>
<body>

    <div class="login-card">
        <h2 class="login-title">Welcome Back</h2>
        
        <form>
            <div class="form-group">
                <label class="form-label">Email</label>
                <input type="email" class="form-input" placeholder="user@example.com">
            </div>
            
            <div class="form-group">
                <label class="form-label">Password</label>
                <input type="password" class="form-input" placeholder="••••••••">
            </div>
            
            <button type="submit" class="btn-submit">Login</button>
        </form>

        <a href="#" class="footer-link">Forgot password?</a>
    </div>

</body>
</html>
```

## 4. 進階思考：為什麼是 `min-height: 100vh` 而不是 `height: 100vh`？

這是一個細節但重要的觀念。

*   `height: 100vh`：強制高度等於視窗高度。如果視窗變矮（例如手機轉橫屏），但 Card 的內容很高（例如使用者開啟螢幕鍵盤），內容就會**溢出**視窗且**無法捲動**，導致上面的標題或下面的按鈕被切掉。
*   `min-height: 100vh`：最小高度是視窗高度。如果內容變多了，它會自動長高，並且允許瀏覽器出現捲軸。這才是安全的做法。
