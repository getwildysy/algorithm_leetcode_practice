# Day 2: 變數 (Variables) 與 巢狀 (Nesting)

Sass 有兩個最強大的功能，能讓你的 CSS 寫起來像 JavaScript 一樣優雅。

## 1. 變數 (Variables)

以前我們要改主色系，要 Ctrl+F 搜尋取代全部的 `#007bff`。
現在，只要改一個地方。

### 語法
使用 `$` 符號開頭：
```scss
/* 定義變數 */
$primary-color: #007bff;
$text-color: #333;
$spacing-unit: 10px;

/* 使用變數 */
.btn {
    background-color: $primary-color;
    color: white;
    padding: $spacing-unit * 2; /* 甚至可以做數學運算！ */
}

.title {
    color: $text-color;
}
```

---

## 2. 巢狀 (Nesting)

這是讓 HTML 結構與 CSS 結構對齊的神器。不要再重複寫父類別名稱了。

### SCSS 寫法
```scss
.navbar {
    background: white;
    padding: 10px;

    /* 裡面的 Logo */
    .logo {
        font-size: 20px;
        color: black;
    }

    /* 裡面的連結 */
    a {
        text-decoration: none;
        
        /* 連結的 Hover 狀態 */
        /* & 代表 "父層自己" (.navbar a) */
        &:hover {
            color: blue;
        }
    }
}
```

### 編譯後的 CSS (結果)
```css
.navbar {
  background: white;
  padding: 10px;
}
.navbar .logo {
  font-size: 20px;
  color: black;
}
.navbar a {
  text-decoration: none;
}
.navbar a:hover {
  color: blue;
}
```

---

## 3. `&` 符號的妙用

`&` 代表「當前的選擇器」。常用在偽類 (`:hover`, `:after`) 或 BEM 命名連字號。

```scss
.btn {
    background: blue;
    
    // 等同於 .btn:hover
    &:hover { background: darkblue; }
    
    // 等同於 .btn__text (BEM 寫法)
    &__text { font-size: 16px; }
    
    // 等同於 .btn--large
    &--large { padding: 20px; }
    
    // 等同於 body.dark-mode .btn (當父層有 class 時)
    body.dark-mode & {
        background: white;
    }
}
```

---

## 4. 巢狀的陷阱

**不要巢狀疊太多層！** 建議不要超過 3 層。

### ❌ 錯誤示範
```scss
.header {
    .nav {
        ul {
            li {
                a {
                    span { color: red; }
                }
            }
        }
    }
}
```
產出的 CSS 權重會超級高 (`.header .nav ul li a span`)，且效能差、難維護。
盡量保持扁平。
