# Day 4: 圖片響應式處理 (max-width: 100%, object-fit)

圖片是網頁上最容易「爆版」的兇手。在 RWD 中，我們必須馴服它。

---

## 1. 唯一真理：`max-width: 100%`

在響應式網頁中，圖片預設不應該有固定的 `width` (例如 width: 800px)，因為手機寬度可能只有 375px。

請將這段 CSS 寫在你的全域 Reset 裡：

```css
img {
    max-width: 100%;
    height: auto; /* 保持比例，避免變形 */
    display: block; /* 移除圖片下方的不明縫隙 */
}
```
**效果**：
*   螢幕很大時：圖片顯示原始尺寸。
*   螢幕很小時：圖片會自動縮小到跟容器一樣寬。

---

## 2. 也是真理：`object-fit`

當我們要製作「卡片列表」時，常常會遇到使用者的圖片長寬比不一致 (有直的有橫的)，導致版面參差不齊。

這時候，我們可以把 `img` 當成是背景圖 (`background-image`) 來處理，但保留 `<img>` 的 SEO 優勢。

### 語法：
```css
.card-img {
    width: 100%;
    height: 200px; /* 強制固定高度 */
    
    /* 關鍵屬性 */
    object-fit: cover; 
}
```

### 屬性值比較：
| 屬性值 | 效果 | 類似背景 |
| :--- | :--- | :--- |
| `contain` | 圖片完整顯示，但旁邊會留白。 | `background-size: contain` |
| `cover` | **最常用**。填滿整個區域，超出的部分切掉 (裁切)。 | `background-size: cover` |
| `fill` | 硬拉變形 (不要用！)。 | - |

---

## 3. 藝術指導 (Art Direction)：`<picture>`

有的時候，我們不只是要「縮放」圖片，而是要「換一張圖」。
例如：電腦版用寬版大圖 (Banner)，手機版如果只是縮小會便很細一條，看不清楚，我們希望換成「正方形」的圖片。

這時候用 `<picture>` 標籤：

```html
<picture>
    <!-- 螢幕 > 800px 時，顯示 desktop.jpg -->
    <source media="(min-width: 800px)" srcset="desktop.jpg">
    
    <!-- 螢幕 < 800px 時，顯示 mobile.jpg -->
    <source media="(max-width: 799px)" srcset="mobile.jpg">
    
    <!-- 預設回 fallback (必寫) -->
    <img src="desktop.jpg" alt="Banner Image">
</picture>
```
這能大幅節省手機版的流量 (因為不用下載電腦版大圖)。

---

## 4. 實作範例：完美卡片圖

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .card {
            width: 300px;
            border: 1px solid #ddd;
            border-radius: 8px;
            overflow: hidden; /* 讓圖片不要超出圓角 */
        }

        .card-img {
            width: 100%;
            height: 200px; /* 固定高度 */
            
            /* 如果沒加這行，圖片會變形 */
            object-fit: cover; 
            
            /* 可以調整裁切中心點 */
            object-position: center center; 
        }

        .card-body { padding: 15px; }
    </style>
</head>
<body>

    <div class="card">
        <!-- 試著換一張長方形或正方形的圖來測試 -->
        <img src="https://picsum.photos/500/300" class="card-img" alt="Demo">
        <div class="card-body">
            <h3>Card Title</h3>
            <p>即使圖片尺寸不對，版面依然整齊。</p>
        </div>
    </div>

</body>
</html>
```
