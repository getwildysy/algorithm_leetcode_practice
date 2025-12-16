# Day 2: Flex Item 的伸縮設定 (flex-grow, shrink, basis)

昨天我們學會了控制父親 (`.container`)，今天我們要來控制孩子 (`.item`) 自己的行為。

Flexbox 最強大的地方就在於它能「彈性伸縮」：空間太多時要不要變大？空間不夠時要不要縮小？這一切都由 `flex` 三兄弟控制。

---

## 1. 簡寫屬性 `flex`

我們通常不分開寫，而是使用縮寫：
```css
.item {
    /* flex: <flex-grow> <flex-shrink> <flex-basis> */
    flex: 0 1 auto; /* 這是預設值 */
}
```

---

## 2. `flex-grow` (成長比例)
*   **意義**：當 Container 還有 **剩餘空間** 時，我可以分到多少？
*   **預設值**：`0` (不成長，即使有空間也不變大)。
*   **用法**：
    *   如果有三個 item，大家都設 `flex-grow: 1` -> 大家平分剩餘空間 (等寬)。
    *   如果有兩個 item，一個設 `1`，一個設 `2` -> 2 的那個會分到比 1 多兩倍的 **剩餘空間** (注意：是分到剩餘空間的比例，不是總寬度的比例！)。

## 3. `flex-shrink` (收縮比例)
*   **意義**：當 Container **空間不夠** (爆掉) 時，我原本的寬度要被「砍掉」多少？
*   **預設值**：`1` (大家一起等比例縮小，避免破版)。
*   **用法**：
    *   設為 `0`：**「死都不縮小」**。適合用在 Logo 或固定寬度的側邊欄。
    *   數字越大，縮得越凶。

## 4. `flex-basis` (基準尺寸)
*   **意義**：在開始分配空間之前，我原本理想的寬度是多少？
*   **預設值**：`auto` (看內容大小或原本的 width 屬性)。
*   **用法**：可以設具體的 px 或 %。
    *   `flex-basis: 0` 是一個神奇設定，代表「忽略內容原本大小，強制從 0 開始分配」。這在做「絕對等寬」排版時很常用。

---

## 5. 常見組合拳 (必背！)

### A. `flex: 1` (絕對均分)
等同於 `flex: 1 1 0%`。
這代表無視內容多寡，所有 item 強制等寬。
```css
.item { flex: 1; }
```

### B. `flex: auto` (依內容大小均分)
等同於 `flex: 1 1 auto`。
這代表內容越長的人，最後的寬度會越寬。適合做 Navbar。

### C. `flex: none` (固定大小)
等同於 `flex: 0 0 auto`。
不伸不縮，width 設定多少就是多少。適合做「固定寬度側邊欄」。

---

## 6. 實作範例：經典佈局 (固定側邊欄 + 自適應內容)

這是一個非常常見的版型：左邊選單固定 200px，右邊內容自動填滿剩下空間。

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .layout {
            display: flex; /* 啟動 Flexbox */
            height: 100vh;
        }

        .sidebar {
            /* 關鍵！不成長、不縮小、固定 200px */
            flex: 0 0 200px; 
            background-color: #2c3e50;
            color: white;
        }

        .main-content {
            /* 關鍵！吃掉剩下所有空間 */
            flex: 1; 
            background-color: #ecf0f1;
            padding: 20px;
        }
    </style>
</head>
<body>

    <div class="layout">
        <aside class="sidebar">
            Sidebar (Fixed 200px)
        </aside>
        <main class="main-content">
            Main Content (Auto fill)
        </main>
    </div>

</body>
</html>
```

使用 Flexbox 做這種版型，比傳統的 `float` 或 `position` 簡單一萬倍。
