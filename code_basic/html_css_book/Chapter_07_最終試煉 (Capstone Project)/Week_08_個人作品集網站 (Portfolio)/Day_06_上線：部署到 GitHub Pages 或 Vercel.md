# Day 6: 上線：部署到 GitHub Pages 或 Vercel

寫在自己電腦裡的網站沒人看得到。今天我們要讓全世界都能透過 URL 訪問它。

## 方法一：GitHub Pages (最經典)

1.  確保你的程式碼已經推送到 GitHub Repository。
2.  進入 Repo 的 **Settings** > **Pages**。
3.  在 **Source** 選擇 `main` branch (或 `root` folder)。
4.  按下 Save。
5.  等待幾分鐘，你会得到一個網址 `https://你的帳號.github.io/你的專案/`。

> **注意**：如果不顯示圖片，通常是路徑問題。請確保圖片路徑是相對路徑 (例如 `assets/img/pic.jpg`) 而不是絕對路徑 (`/assets/...`)。

## 方法二：Vercel (最推薦，速度快)

1.  去 [Vercel](https://vercel.com) 註冊帳號。
2.  點擊 **Add New...** > **Project**。
3.  連結你的 GitHub 帳號，選擇剛才的 Repo。
4.  點擊 **Deploy**。
5.  完成！Vercel 會給你一個 HTTPS 的網址，而且每次你 `git push` 時，它都會自動重新部署。

---

## 檢查清單 (Pre-flight Checklist)
- [ ] 圖片都顯示正常嗎？
- [ ] 連結點擊後都有反應嗎？
- [ ] console.log 有沒有紅字報錯？
- [ ] 分享連結給朋友，請他們用手機打開看看。
