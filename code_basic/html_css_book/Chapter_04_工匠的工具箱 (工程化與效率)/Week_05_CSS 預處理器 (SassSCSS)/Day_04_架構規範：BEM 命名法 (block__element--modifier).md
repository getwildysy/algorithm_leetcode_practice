# Day 4: 架構規範：BEM 命名法 (block__element--modifier)

寫 CSS 最難的不是語法，而是「命名」。
`div class="wrapper"`
`div class="container-2"`
`div class="box-red-final"`
這種命名讓維護變成了地獄。

**BEM (Block, Element, Modifier)** 是一套命名公約，雖然名字會變很長，但能讓結構一目瞭然。

---

## 1. BEM 結構解析

### Block (區塊)
獨立的元件，本身就有意義。
*   命名：`.card`, `.btn`, `.menu`

### Element (元素)
依附在 Block 裡面的零件，離開 Block 就沒意義。
*   命名：使用雙底線 `__` 連接。
*   範例：`.card__title`, `.menu__item` (注意：是 menu item，不是 menu li)

### Modifier (修飾)
用來改變外觀或狀態。
*   命名：使用雙連字號 `--` 連接。
*   範例：`.btn--primary`, `.card--dark`, `.menu__item--active`

---

## 2. 實例示範

### 傳統寫法 (Bad)
```html
<div class="card">
    <div class="title active">Title</div>
    <div class="text">Content</div>
    <a href="#" class="btn red">Button</a>
</div>
```
問題：`.title`, `.text`, `.red` 都太氾濫，容易汙染到其他元件。

### BEM 寫法 (Good)
```html
<div class="card">
    <div class="card__title card__title--active">Title</div>
    <div class="card__content">Content</div>
    <a href="#" class="card__btn btn btn--danger">Button</a>
</div>
```

雖然 class 看起來很長，但你在寫 CSS 時會非常安全：
```css
.card { }
.card__title { } /* 絕對不會影響到 .article__title */
.card__content { }
```

---

## 3. 搭配 SCSS 寫 BEM

SCSS 的 `&` 符號簡直是為了 BEM 而生的。

```scss
.card {
    background: white;
    
    &__title {
        font-size: 20px;
        
        &--active {
            color: red;
        }
    }
    
    &__content {
        padding: 10px;
    }
}
```
編譯出來就是標準 BEM CSS，而且原始碼結構完全對應 HTML。

---

## 4. 常見問題

### Q: 可以寫 `.block__element__element` 嗎？ (Element 裡面包 Element)
**A: 不行！** BEM 是扁平的。
即使 HTML 結構是 Grandparent > Parent > Child， class 命名應該是：
*   `.block`
*   `.block__parent`
*   `.block__child` (不要寫 `.block__parent__child`)

目的就是為了讓 CSS 權重保持在同一層級 (10分)。

### Q: 名字太長怎麼辦？
**A: 忍著。** 長名字換來的是「可讀性」與「零衝突」。這在大型專案中是非常值得的代價。
