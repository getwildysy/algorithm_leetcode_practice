# Day 3: 比較：Flexbox vs Grid 的使用時機判斷

學了兩個排版神器，很多人會問：「那我現在是不是全部都用 Grid 就好了？」

答案是：**NO**。它們是互補的，不是取代關係。

---

## 1. 核心差異：一維 vs 二維

| 特性 | Flexbox | Grid |
| :--- | :--- | :--- |
| **維度** | **一維 (1D)** | **二維 (2D)** |
| **關注點** | **內容 (Content-first)** | **佈局 (Layout-first)** |
| **控制力** | 我讓內容自己決定大小，空間夠就排，不夠就換行 | 我先把格子畫好，內容再來填空 |
| **重疊** | 很難 (要用負 margin) | 很容易 (指定同一個 grid area) |

---

## 2. 判斷流程圖 (Decision Tree)

請依照以下問題來決定用哪一個：

1.  **你需要同時對齊「行」與「列」嗎？**
    *   Yes -> **Grid** (例如：圖片牆、整個網頁的版型 Header/Sidebar/Main)。
    *   No -> 往下一題。

2.  **你只是要把一堆東西排成一列 (或一行) 嗎？**
    *   Yes -> **Flexbox** (例如：導覽列、按鈕群組)。
    *   No -> 往下一題。

3.  **你希望內容大小不固定時，還是能保持嚴格的網格對齊嗎？**
    *   Yes -> **Grid** (它能強制對齊寬度)。
    *   No -> **Flexbox** (它比較隨性，內容多少就多少)。

---

## 3. 實戰場景舉例

### 用 Flexbox 的時候
*   **Navbar**：Logo 在左，選單在右。
*   **Vertical Center**：把東西垂直置中。
*   **Tag List**：一堆標籤 `Tag A` `Tag B`，長度不一，自動換行。

### 用 Grid 的時候
*   **Page Layout**：Header + Sidebar + Main + Footer。
*   **Image Gallery**：圖片庫，不管圖片直的橫的，都要塞在整齊的格子裡。
*   **Dashboard**：儀表板，有很多大小不一的卡片要拼湊在一起。

---

## 4. 混合雙打 (Combo)

這才是現代網頁開發的常態：**大架構用 Grid，小元件用 Flex**。

```css
/* 大架構：整個頁面 */
.page-container {
    display: grid;
    grid-template-columns: 200px 1fr;
    /* ... */
}

/* 小元件：Header 裡面的導覽按鈕 */
.header-nav {
    display: flex;
    justify-content: space-between;
}
```

## 5. 總結
*   **Flexbox** 是「流動」的，適合讓元件依內容大小自然排列。
*   **Grid** 是「剛性」的，適合規劃整體的版面架構。
*   **小孩才做選擇，大人全都要**：把它們兩個結合起來使用。
