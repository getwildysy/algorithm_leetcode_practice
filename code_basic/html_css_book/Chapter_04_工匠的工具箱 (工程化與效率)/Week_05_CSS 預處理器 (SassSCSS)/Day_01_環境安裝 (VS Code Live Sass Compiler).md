# Day 1: 環境安裝 (VS Code Live Sass Compiler)

CSS 寫久了你會發現：
1.  一直重複寫父元素名稱很煩 (巢狀結構)。
2.  顏色代碼 `#4a90e2` 到處複製貼上，要改的時候找不到人。
3.  數學計算很麻煩。

Sass (Syntactically Awesome Style Sheets) 就是為了自救而生的「CSS 預處理器」。

---

## 1. 什麼是預處理器？

瀏覽器**看不懂** Sass (.scss 檔)。
瀏覽器只看得懂 CSS (.css 檔)。

所以我們需要一個「翻譯軟體 (Compiler)」，在我們寫完 Sass 後，自動幫我們轉成 CSS 給瀏覽器看。

## 2. 安裝步驟 (VS Code 擴充套件)

我們不需要裝複雜的 Node.js 環境，只需要裝一個 VS Code Extension。

1.  打開 VS Code Extension 面板 (Ctrl+Shift+X)。
2.  搜尋 **"Live Sass Compiler"** (作者是 *Glenn Marks*，最早是 Ritwick Dey 開發的)。
3.  點擊 **Install**。

## 3. Hello Sass

1.  在資料夾建立一個 `style.scss` (注意副檔名是 **scss**)。
2.  在 VS Code 底部狀態列，點擊 **"Watch Sass"** 按鈕。
3.  你會發現它自動幫你產生了一個 `style.css` 和 `style.css.map`。

### 測試一下

在 `style.scss` 寫下：
```scss
/* 這是 SCSS */
$primary-color: pink;

body {
    background: $primary-color;
    h1 {
        color: white;
    }
}
```
存檔後，去檢查 `style.css`，應該會看到：
```css
/* 這是編譯後的 CSS */
body {
  background: pink;
}
body h1 {
  color: white;
}
```
這就代表成功了！

---

## 4. 檔案架構建議

通常我們會把 scss 放在一個獨立的資料夾：
```
project/
├── index.html
├── css/
│   └── style.css (自動生成的，不要手動改它！)
└── scss/
    └── style.scss (我們都在這裡工作)
```

## 5. 常見問題
*   **如果不小心改了 CSS 檔怎麼辦？**
    下次你存檔 SCSS 時，它會直接**覆蓋** CSS 檔。所以**永遠只改 SCSS**。
