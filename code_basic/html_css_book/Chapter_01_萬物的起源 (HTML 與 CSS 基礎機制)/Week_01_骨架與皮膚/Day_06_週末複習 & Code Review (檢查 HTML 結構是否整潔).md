# Day 6: 週末複習 & Code Review (檢查 HTML 結構是否整潔)

恭喜你完成了第一週的訓練！這週我們建立了網頁最基礎的觀念。在進入 CSS 排版與 RWD 之前，我們必須確保地基是穩固的。

請拿出你昨天做的「Profile Card」，依照下方的 Check List 進行自我檢核。

---

## 1. HTML 結構檢核 (Structure)

- [ ] **DOCTYPE 宣告**：第一行是否有 `<!DOCTYPE html>`？
- [ ] **Lang 屬性**：`<html>` 標籤是否有加上 `lang="zh-Hant"`？ (這對瀏覽器翻譯功能和 SEO 很重要)
- [ ] **Meta Tags**：`<head>` 裡是否有 `<meta charset="UTF-8">` 與 `<meta name="viewport"...>`？
- [ ] **語意化標籤**：
    - [ ] 是否避免用 `<div>` 包辦所有事？
    - [ ] 標題是否依序使用 `<h1>`, `<h2>`, `<h3>` (不可跳級，例如 h1 完直接接 h4)？
    - [ ] 圖片是否有加上 `alt` 屬性？ (例如 `alt="User Avatar"`)？
- [ ] **縮排整齊**：程式碼是否有統一的縮排 (建議 2 格或 4 格空白)？

## 2. CSS 樣式檢核 (Styling)

- [ ] **Box Sizing**：是否有在最開頭加上 `* { box-sizing: border-box; }`？
- [ ] **權重管理**：
    - [ ] 是否盡量使用 Class (`.`) 來選取元素？
    - [ ] 是否避免使用 ID (`#`) 來寫樣式？
    - [ ] 是否完全沒有使用 `!important`？
- [ ] **單位使用**：
    - [ ] 0 是否省略單位 (例如 `margin: 0;` 而不是 `margin: 0px;`)？
- [ ] **命名規範**：
    - [ ] Class 名稱是否有意義 (例如 `.card-header` 而不是 `.box1`, `.red-text`)？
    - [ ] 是否統一使用小寫與連字號 (kebab-case，例如 `user-profile` 這樣才對)？

---

## 3. 常見壞味道 (Code Smells)

### ❌ 壞味道 1: 過度的 Div 包裝
```html
<!-- 不好的 -->
<div class="card">
    <div class="card-inner">
        <div class="card-content">
            ...
        </div>
    </div>
</div>

<!-- 好的 -->
<article class="card">
    ...
</article>
```

### ❌ 壞味道 2: 用 `<br>` 來製造距離
```html
<!-- 不好的 -->
<h2>Title</h2>
<br><br> <!-- 不要這樣做！ -->
<p>Content</p>
```
**修正**：請使用 CSS 的 `margin-bottom` 來推開距離。

### ❌ 壞味道 3: Inline Styles
```html
<!-- 不好的 -->
<p style="color: red; font-size: 20px;">Text</p>
```
**修正**：請將樣式寫在 CSS 檔案中。

---

## 4. 下週預告

下週我們要進入網頁排版最核心、也最強大的章節：**Flexbox (彈性盒模型)**。
如果你覺得這週用 margin 推來推去很難對齊，Flexbox 將會是你的一鍵救星。
準備好，我們要開始「排版」了！
