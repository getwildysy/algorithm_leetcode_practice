# Day 2: 架構：建立 HTML 結構與 Git Repository

規劃好了，今天我們來打地基。

## 1. 建立專案資料夾

建議結構 (我們使用 SCSS)：

```
my-portfolio/
├── index.html
├── assets/
│   ├── images/
│   └── css/ (編譯後的 css 放在這)
├── scss/
│   ├── main.scss (進入點)
│   ├── _variables.scss
│   ├── _reset.scss
│   └── _layout.scss
└── README.md
```

## 2. 初始化 Git

版本控制是工程師的必備技能。

```bash
# 在專案資料夾內執行 Terminal
git init
git add .
git commit -m "Initial commit"
```

建議去 GitHub 開一個新的 Repository，然後把它們連結起來。

## 3. HTML 骨架 (index.html)

先寫出語意化的空標籤，還不用填內容：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Portfolio</title>
    <link rel="stylesheet" href="assets/css/main.css">
    <!-- 引入字體、Icon -->
</head>
<body>

    <nav class="navbar">
        <!-- Logo & Menu -->
    </nav>

    <header id="hero" class="hero">
        <!-- Introduction -->
    </header>

    <main>
        <section id="about" class="about">
            <!-- About Me -->
        </section>

        <section id="projects" class="projects">
            <!-- Project Cards -->
        </section>

        <section id="contact" class="contact">
            <!-- Form -->
        </section>
    </main>

    <footer>
        <!-- Copyright -->
    </footer>

</body>
</html>
```

## 4. SCSS 預備 (`main.scss`)

```scss
@import "variables";
@import "reset";
@import "layout";

body {
    font-family: 'Inter', sans-serif;
    color: $text-color;
    background-color: $bg-color;
}
```

今天做到這裡就好，地基打穩，後面蓋樓才會快。
