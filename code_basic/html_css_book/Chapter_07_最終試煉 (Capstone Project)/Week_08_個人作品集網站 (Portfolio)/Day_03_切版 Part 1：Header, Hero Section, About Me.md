# Day 3: 切版 Part 1：Header, Hero Section, About Me

今天我們要完成網站的上半部。這部分是用戶的第一印象，必須驚艷。

## 1. Header (Sticky)

我們希望導覽列在往下捲動時，依然固定在最上方。

```scss
.navbar {
    position: sticky; /* 黏性定位 */
    top: 0;
    z-index: 1000;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    background-color: rgba(255, 255, 255, 0.95); /* 微微透明 */
    backdrop-filter: blur(10px); /* 毛玻璃特效，質感加分 */
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}
```

## 2. Hero Section (首屏)

這是最適合展現個性的地方。我們採用「左文右圖」的兩欄式佈局，手機版自動變成單欄。

```html
<section class="hero container">
    <div class="hero__content">
        <h1>Hi, I'm <span class="highlight">Alex</span>.</h1>
        <p class="subtitle">Frontend Developer & UI Designer.</p>
        <p class="description">
            I craft responsive websites where technology meets creativity.
        </p>
        <a href="#contact" class="btn btn--primary">Hire Me</a>
    </div>
    <div class="hero__image">
        <img src="assets/images/avatar.png" alt="My Portrait">
    </div>
</section>
```

```scss
.hero {
    display: flex;
    align-items: center;
    justify-content: space-between;
    min-height: 80vh; // 確保高度足夠
    gap: 2rem;
    
    // 手機版 (小於 768px)
    @media (max-width: 768px) {
        flex-direction: column-reverse; // 圖片在文案上方
        text-align: center;
        justify-content: center;
    }

    &__content { flex: 1; }
    &__image { 
        flex: 1; 
        img { width: 100%; max-width: 400px; border-radius: 50%; }
    }
}
```

## 3. About Me

這區塊通常比較多文字。建議限制最大寬度 (`max-width: 65ch`)，提升閱讀體驗。這是排版學的黃金法則：一行字不要太長，讀者眼球才不會累。

```scss
.about {
    padding: 4rem 2rem;
    background-color: #f9f9f9;
    
    p {
        max-width: 65ch; // 約 65 個字元寬
        margin: 0 auto;
        line-height: 1.8;
        color: #555;
    }
}
```
