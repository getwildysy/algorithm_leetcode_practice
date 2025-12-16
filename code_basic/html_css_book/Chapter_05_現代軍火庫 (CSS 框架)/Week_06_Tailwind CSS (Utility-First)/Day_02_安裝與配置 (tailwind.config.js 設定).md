# Day 2: 安裝與配置 (tailwind.config.js 設定)

Tailwind 有兩種玩法：
1.  **CDN 大補帖**：適合練習、測試。直接引入 script 即可。
2.  **CLI / PostCSS 編譯**：適合正式專案。可以自訂義設定檔，並且會清除沒用到的 CSS (PurgeCSS)。

為了快速上手，我們今天先用 CDN 玩法；但在正式工作時，絕對是用 NPM 安裝的。

---

## 1. CDN 快速起手式

在你的 HTML `<head>` 加入這行腳本：
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- 引入 Tailwind -->
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
    <h1 class="text-3xl font-bold underline text-blue-600">
        Hello world!
    </h1>
</body>
</html>
```
存檔，打開瀏覽器。如果有看到藍色、底線、變大的字，恭喜你安裝成功！

---

## 2. 自訂配置 (tailwind.config.js)

就算是 CDN 模式，我們也可以自訂變數 (例如品牌色)。

在 `<script>` 標籤內設定 `tailwind.config`：

```html
<script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            clifford: '#da373d', // 自訂一個叫 clifford 的顏色
            brand: {
                DEFAULT: '#007bff',
                dark: '#0056b3'
            }
          }
        }
      }
    }
</script>

<!-- 使用自訂顏色 -->
<div class="bg-clifford text-white p-4">
    Clifford Color
</div>
<div class="text-brand-dark">
    Brand Dark Color
</div>
```

---

## 3. 正式環境安裝 (簡介)

如果你在寫 React/Vue/Next.js 專案，通常會執行：
```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init
```
這會產生 `tailwind.config.js` 檔案。你需要告訴它你的 HTML/JS 檔案在哪裡 (`content` array)，這樣它才能掃描你用到了哪些 class，並只打包那些 CSS，讓檔案從 3MB 瘦身到 10KB。

但本週為了教學方便，我們繼續使用 `<script src="https://cdn.tailwindcss.com"></script>`。
