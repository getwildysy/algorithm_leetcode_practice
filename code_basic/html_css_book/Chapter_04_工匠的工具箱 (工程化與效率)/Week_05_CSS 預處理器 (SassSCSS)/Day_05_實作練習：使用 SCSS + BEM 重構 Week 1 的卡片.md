# Day 5: 實作練習：使用 SCSS + BEM 重構 Week 1 的卡片

我們這週其實沒有學新的 CSS 屬性，而是學「更好的寫法」。
現在，請將你的 `style.css` 刪除，建立 `style.scss`，並用 BEM 與 SCSS 的功能來重構之前的 Profile Card。

## 1. 任務目標

1.  **結構化變數**：將顏色、間距提取為 Variables。
2.  **Mixins**：建立一個 Flex 置中的 Mixin。
3.  **BEM 命名**：全面改寫 HTML Class 與 CSS Selector。
4.  **巢狀結構**：善用 `&` 連接 BEM class。

---

## 2. 實作程式碼

### `style.scss`

```scss
// 1. 變數定義 (Variables)
$primary-color: #667eea;
$secondary-color: #764ba2;
$text-dark: #2c3e50;
$text-light: #4a5568;
$bg-color: #f3f4f6;
$border-radius: 12px;

// 2. Mixin 定義
@mixin flex-center {
    display: flex;
    justify-content: center;
    align-items: center;
}

@mixin btn-style($bg, $text) {
    background-color: $bg;
    color: $text;
    padding: 10px;
    border-radius: 6px;
    text-decoration: none;
    text-align: center;
    transition: opacity 0.2s;
    
    &:hover {
        opacity: 0.9;
    }
}

// 3. Reset
*, *::before, *::after { box-sizing: border-box; }

body {
    margin: 0;
    font-family: sans-serif;
    background-color: $bg-color;
    height: 100vh;
    @include flex-center; // 使用 Mixin
}

// 4. BEM Component
.profile-card {
    background: white;
    width: 320px;
    border-radius: $border-radius;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    
    // Header
    &__header {
        background: linear-gradient(135deg, $primary-color 0%, $secondary-color 100%);
        padding: 30px 20px;
        color: white;
        text-align: center;
    }
    
    &__avatar {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        border: 4px solid rgba(255,255,255,0.3);
        object-fit: cover;
        margin-bottom: 10px;
    }
    
    &__name {
        margin: 5px 0;
        font-size: 1.5rem;
    }
    
    &__job {
        margin: 0;
        opacity: 0.8;
        font-size: 0.9rem;
    }
    
    // Body
    &__body {
        padding: 20px 25px;
        color: $text-light;
        line-height: 1.6;
    }
    
    // Footer
    &__footer {
        padding: 0 25px 25px;
        display: flex;
        gap: 10px;
    }
    
    &__btn {
        flex: 1;
        
        // Modifier: Primary Button
        &--primary {
            @include btn-style($secondary-color, white);
        }
        
        // Modifier: Outline Button
        &--outline {
            border: 1px solid $secondary-color;
            @include btn-style(transparent, $secondary-color);
            &:hover { background-color: rgba($secondary-color, 0.1); }
        }
    }
}
```

### 對應的 HTML

```html
<article class="profile-card">
    <header class="profile-card__header">
        <img src="..." class="profile-card__avatar">
        <h2 class="profile-card__name">Alex</h2>
        <p class="profile-card__job">Dev</p>
    </header>
    
    <section class="profile-card__body">
        <p>...</p>
    </section>
    
    <footer class="profile-card__footer">
        <a href="#" class="profile-card__btn profile-card__btn--primary">Follow</a>
        <a href="#" class="profile-card__btn profile-card__btn--outline">Message</a>
    </footer>
</article>
```

你看，雖然在 SCSS 裡我們用 `&` 看起來很簡短，但編譯出來的 CSS 類別名稱 (`.profile-card__header`) 會很完整且具備隔離性。這就是現代 CSS 開發的標準姿勢。
