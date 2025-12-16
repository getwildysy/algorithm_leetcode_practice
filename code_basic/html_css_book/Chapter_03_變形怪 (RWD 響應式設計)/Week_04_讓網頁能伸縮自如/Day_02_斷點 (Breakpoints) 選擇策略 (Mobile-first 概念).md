# Day 2: 斷點 (Breakpoints) 選擇策略 (Mobile-first 概念)

RWD 最難的不是技術，而是「決策」。到底要設幾個斷點？斷點要設在多少 px？

---

## 1. 什麼是 Mobile-first (手機優先)？

這是一種設計與開發的哲學。
*   **傳統做法 (Desktop First)**：先寫電腦版 CSS，然後用 `max-width` 去「修」手機版壞掉的地方。這通常會導致程式碼很髒，且手機載入大量不必要的樣式。
*   **現代做法 (Mobile First)**：先寫手機版 CSS (作為預設值)，然後用 `min-width` 去「疊加」平板與電腦版的樣式。

**優點**：程式碼最精簡、效能最好 (小裝置跑最少 Code)。

---

## 2. 常見斷點尺寸

世界上有幾千種螢幕尺寸，你不可能為每一種都寫一個斷點。我們通常會抓幾個「大範圍」的關卡。

目前主流框架 (如 Bootstrap, Tailwind) 的標準：

| 裝置類型 | 斷點變數 (Tailwind) | 像素 (px) |
| :--- | :--- | :--- |
| **手機 (直向)** | (Default) | < 640px |
| **平板 / 大手機** | `sm` | ≥ 640px |
| **平板 (橫向)** | `md` | ≥ 768px (iPad 直向) |
| **筆電 / 桌機** | `lg` | ≥ 1024px (iPad Pro) |
| **大螢幕** | `xl` | ≥ 1280px |

**建議**：千萬不要針對「特定手機型號」設斷點 (例如 iPhone 12 Pro Max 是 428px)，不然你永遠改不完。要針對「版型崩壞點」設斷點。

---

## 3. 不需要斷點的 RWD

最高境界的 RWD，是連 `@media` 都很少寫。
善用相對單位與 Flex/Grid 的自動換行特性。

### 範例：Flexbox Wrap
```css
.container {
    display: flex;
    flex-wrap: wrap; /* 讓內容自動換行 */
    gap: 20px;
}

.card {
    /* 這裡使用 Flex basis */
    /* 基礎 300px，但允許縮小與長大 */
    flex: 1 1 300px; 
}
```
光是這一段，就能讓卡片在寬螢幕並排，在窄螢幕自動變成直排，完全沒寫到 `@media`。

---

## 4. 實作練習：Mobile First 重構

把這段 Desktop First 的代碼：
```css
/* 電腦版 (預設) */
.sidebar { width: 300px; display: block; }

/* 手機版 (覆蓋) */
@media (max-width: 767px) {
    .sidebar { display: none; }
}
```

改成 Mobile First：
```css
/* 手機版 (預設) */
.sidebar { display: none; }

/* 平板/電腦以上 (疊加) */
@media (min-width: 768px) {
    .sidebar { display: block; width: 300px; }
}
```
**邏輯轉變**：原本是「有 Sideber -> 手機隱藏」；現在是「本來隱藏 -> 螢幕夠大才顯示」。這更符合漸進增強 (Progressive Enhancement) 的概念。
