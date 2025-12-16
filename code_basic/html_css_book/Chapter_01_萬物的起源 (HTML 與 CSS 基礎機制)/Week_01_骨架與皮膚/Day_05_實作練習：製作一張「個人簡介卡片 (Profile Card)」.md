# Day 5: 實作練習：製作一張「個人簡介卡片 (Profile Card)」

今天我們要綜合運用 Week 1 學到的所有知識：HTML 語意化、Class 命名、盒模型、Margin/Padding，來完成一個漂亮的個人簡介卡片。

## 1. 任務目標
製作一個包含頭像、姓名、職稱、簡介文字、以及社群按鈕的卡片。
要求：
1.  結構語意化。
2.  使用 `border-box`。
3.  運用 Margin 與 Padding 創造適當的留白。
4.  按鈕要有 Hover 效果。

---

## 2. HTML 結構設計

我們先不用 CSS，先把骨架搭好。

```html
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <title>Profile Card</title>
    <link rel="stylesheet" href="style.css">
    <!-- 引入 Font Awesome 圖示 (非必要，為了好看先加) -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>

    <!-- 整個頁面的容器，用來置中卡片 -->
    <main class="container">
        
        <!-- 卡片本體 -->
        <article class="profile-card">
            
            <!-- 上半部：頭像區 -->
            <header class="card-header">
                <img src="https://i.pravatar.cc/150?img=12" alt="User Avatar" class="avatar">
                <h2 class="name">Alex Chen</h2>
                <p class="job-title">Frontend Developer</p>
            </header>

            <!-- 中間：簡介內容 -->
            <section class="card-body">
                <p>
                    熱愛寫 Code 的前端工程師，喜歡探索新技術。
                    目前正在鑽研 React 與 Next.js，夢想是做出能改變世界的產品。
                </p>
            </section>

            <!-- 下半部：操作按鈕 -->
            <footer class="card-footer">
                <a href="#" class="btn btn-primary">Follow</a>
                <a href="#" class="btn btn-outline">Message</a>
            </footer>

        </article>

    </main>

</body>
</html>
```

---

## 3. CSS 樣式實作

請建立 `style.css` 並貼上以下內容。請仔細閱讀註解，理解每一行的用意。

```css
/* 1. Reset & Global Styles */
*, *::before, *::after {
    box-sizing: border-box; /* 必備！ */
}

body {
    margin: 0;
    font-family: 'Segoe UI', sans-serif;
    background-color: #f3f4f6; /* 淺灰背景，襯托白色卡片 */
    display: flex;
    justify-content: center; /* 水平置中 (Week 2 會教) */
    align-items: center;     /* 垂直置中 (Week 2 會教) */
    min-height: 100vh;       /* 讓 body 至少跟視窗一樣高 */
}

/* 2. Card Container */
.profile-card {
    background-color: white;
    width: 320px;
    border-radius: 12px; /* 圓角 */
    overflow: hidden;    /* 確保內容不超出圓角 */
    box-shadow: 0 4px 15px rgba(0,0,0,0.1); /* 陰影讓卡片浮起來 */
    text-align: center;
}

/* 3. Header Section */
.card-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); /* 漸層背景 */
    padding: 30px 20px;
    color: white;
}

.avatar {
    width: 100px;
    height: 100px;
    border-radius: 50%; /* 圓形圖片 */
    border: 4px solid rgba(255,255,255,0.3); /* 半透明邊框 */
    object-fit: cover;
    margin-bottom: 10px;
}

.name {
    margin: 5px 0;
    font-size: 1.5rem;
}

.job-title {
    margin: 0;
    font-size: 0.9rem;
    opacity: 0.8; /* 稍微透明一點，區分層次 */
}

/* 4. Body Section */
.card-body {
    padding: 20px 25px;
    color: #4a5568;
    line-height: 1.6; /* 增加行高，閱讀更舒適 */
    font-size: 0.95rem;
}

/* 5. Footer Section & Buttons */
.card-footer {
    padding: 0 25px 25px; /* 上0, 左右25, 下25 */
    display: flex;
    gap: 10px; /* 按鈕之間的間距 */
}

.btn {
    flex: 1; /* 讓按鈕平均分配寬度 */
    padding: 10px;
    border-radius: 6px;
    text-decoration: none;
    font-weight: 600;
    transition: all 0.2s; /* 平滑過渡效果 */
}

.btn-primary {
    background-color: #764ba2;
    color: white;
}
.btn-primary:hover {
    background-color: #5b3a7d;
}

.btn-outline {
    background-color: transparent;
    border: 1px solid #764ba2;
    color: #764ba2;
}
.btn-outline:hover {
    background-color: #f3e8ff;
}
```

---

## 4. 挑戰項目 (Optional)
做完上面的基本款後，試著加入以下功能：
1.  在圖片下方加入一排社群圖示 (FB, IG, GitHub)。
2.  將卡片加上 hover 效果，滑鼠移過去時卡片稍微往上浮起 (`transform: translateY(-5px)`)。
