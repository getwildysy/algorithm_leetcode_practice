# Day 2: CSS 選取器的權重戰爭 (Specificities)

## 1. 什麼是 CSS 權重 (Specificity)？

當兩條 CSS 規則同時設定同一個元素的樣式時，誰會贏？這不是看誰先寫，而是看**誰的權重比較高**。

如果權重相同，則**後寫的蓋過先寫的**。

## 2. 權重計分板

我們可以把權重想像成四個等級的分數 `(Inline, ID, Class, Type)`：

| 選取器類型 | 範例 | 權重分數 | 備註 |
| :--- | :--- | :--- | :--- |
| **!important** | `color: red !important;` | **無敵** | 破壞規則，盡量少用 |
| **Inline Styles** | `<div style="color: red;">` | **(1, 0, 0, 0)** | 寫在 HTML 屬性裡 |
| **ID 選取器** | `#navbar` | **(0, 1, 0, 0)** | 高權重，每個頁面唯一 |
| **Class / Attribute / Pseudo-class** | `.btn`, `[type="text"]`, `:hover` | **(0, 0, 1, 0)** | 最常用，建議主力使用 |
| **Type (Tag) / Pseudo-element** | `div`, `h1`, `::before` | **(0, 0, 0, 1)** | 權重最低 |
| **通配選取器** | `*` | **(0, 0, 0, 0)** | 沒權重 |

### 計算範例

1.  `h1` -> 分數 0-0-0-1 (1分)
2.  `.title` -> 分數 0-0-1-0 (10分)
3.  `h1.title` -> 分數 0-0-1-1 (11分)
4.  `#main-title` -> 分數 0-1-0-0 (100分)
5.  `#header h1.title` -> 分數 0-1-1-1 (111分)

**規則：**
*   **ID 永遠大於 Class**：不管你有多少個 Class (例如 10 個 `.class` 加起來)，都贏不過 1 個 ID。
*   **Class 永遠大於 Tag**。

---

## 3. 常見雷點與最佳實踐

### ❌ 壞習慣：過度依賴 ID
由於 ID 權重太重 (100分)，一旦你用了 `#sidebar .link { color: blue; }`，之後想在某個特殊連結改色，用 `.link-active { color: red; }` 根本蓋不過去 (因為只有 10 分)，最後你就會被迫寫出 `!important`，導致維護地獄。

**建議**：**CSS 樣式盡量只用 Class (`.`) 來定義**，保留 ID 給 JavaScript 抓取元素或錨點連結使用。

### ❌ 壞習慣：巢狀過深 (Nesting)
```css
/* 權重太高且綁死結構 (0-0-3-3) */
.header .nav .menu ul li a { color: black; }
```
這不僅效能差，而且很難覆寫。如果哪天 HTML 結構變了，這段 CSS 就失效了。

**建議**：保持扁平。
```css
/* 簡單明瞭 (0-0-1-0) */
.nav-link { color: black; }
```

---

## 4. 實作範例

試著計算以下 CSS 對於 `<h1 class="title" id="page-title">Hello</h1>` 的顏色結果：

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        /* A: Tag Selector (1分) */
        h1 { color: blue; }

        /* B: Class Selector (10分) */
        .title { color: green; }

        /* C: ID Selector (100分) */
        #page-title { color: red; }

        /* D: Class Selector + Tag (11分) */
        h1.title { color: purple; }
        
        /* E: !important (無敵) */
        /* 如果解開下面註解，文字會變什麼色？ */
        /* h1 { color: orange !important; } */
    </style>
</head>
<body>
    <h1 id="page-title" class="title">猜猜我是什麼顏色？</h1>
</body>
</html>
```

**答案：**
1.  在沒有 `!important` 的情況下，**紅色** (ID #page-title 勝出)。
2.  即使 `.title` 寫在 `#page-title` 後面，ID 權重依然大於 Class。
3.  如果解開 `color: orange !important`，則變成 **橘色**。

---

## 5. 什麼時候可以用 `!important`？

幾乎不要用。唯一能接受的情況是：
1.  **覆蓋第三方套件的強制樣式** (當你無法修改套件原始碼時)。
2.  **Utility Classes (工具類)**：例如 Bootstrap 的 `.d-none` (display: none !important)，目的是「無論如何都要隱藏」。

## 6. 本日任務
檢查你的 Code，是否充滿了 `#id` 來寫樣式？試著把它們重構成 Class。
