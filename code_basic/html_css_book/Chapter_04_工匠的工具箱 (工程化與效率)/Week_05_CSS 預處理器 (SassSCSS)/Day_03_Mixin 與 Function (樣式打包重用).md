# Day 3: Mixin 與 Function (樣式打包重用)

Sass 讓我們可以像寫程式一樣，把重複的邏輯打包成「函式」。

## 1. Mixin (混合)

Mixin 就像是「樣式包」，你可以把一整坨 CSS 屬性打包起來，隨時呼叫。

### 定義 Mixin
使用 `@mixin` 定義，使用 `@include` 呼叫。

```scss
// 定義一個用來處理 Flex 置中的 mixin
@mixin flex-center {
    display: flex;
    justify-content: center;
    align-items: center;
}

// 使用它
.card {
    width: 100px;
    background: red;
    
    // 一行抵三行
    @include flex-center; 
}
```

### 帶參數的 Mixin
Mixin 還可以自訂參數，更靈活。

```scss
@mixin box($w, $h, $bg) {
    width: $w;
    height: $h;
    background-color: $bg;
}

.avatar {
    @include box(50px, 50px, blue);
}
```

---

## 2. 實戰應用：RWD Breakpoint Manager

這是 Mixin 最經典的用法，用來管 RWD 斷點。

```scss
// _mixins.scss

$breakpoint-md: 768px;

@mixin pad {
    @media (min-width: $breakpoint-md) {
        @content; // 這裡會填入你呼叫時包在裡面的程式碼
    }
}

// style.scss
.header {
    background: red;
    
    // 當是 Pad 以上時
    @include pad {
        background: blue; // 這行會被放進 @media 裡
    }
}
```

這樣的寫法比手寫 `@media (min-width: 768px)` 清楚很多，而且統一管理數據。

---

## 3. Function (函式)

Mixin 是輸出「一坨 CSS 樣式」，而 Function 是輸出「一個值」 (例如計算後的 px, color)。

Sass 內建很多好用的函式，例如顏色運算：

```scss
.btn {
    // 讓顏色變亮 20%
    background-color: lighten(#000, 20%); 
    
    // 讓顏色變暗 10%
    border-color: darken(#000, 10%);
}
```

我們也可以自定義 Function：

```scss
// 把 px 轉成 rem 的函式
@function px-to-rem($px) {
    @return $px / 16px * 1rem;
}

h1 {
    font-size: px-to-rem(32px); // 編譯出來會變成 2rem
}
```

---

## 4. `import` (或是 `@use`)

我們可以把 mixin, function, variables 拆分到不同的檔案 (例如 `_variables.scss`, `_mixins.scss`)，然後在主檔案引入：

```scss
@import "variables";
@import "mixins";

body {
    // ...
}
```

> **注意**：新版 Sass 推薦使用 `@use` 取代 `@import`，但如果是用 Live Sass Compiler，`@import` 目前還是最方便且相容的選擇。
