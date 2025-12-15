# 第 1 章：為什麼是 Next.js？ (Why Next.js?)

歡迎來到 Next.js 的世界。在開始撰寫程式碼之前，我們需要先建立正確的心智模型。為什麼我們需要 Next.js？它解決了什麼 React 本身難以解決的問題？本章將帶你從 Web 開發的演進史看起，深入理解 React Server Components (RSC) 的革命性改變。

## 1.1 Web 開發演進史：從 CSR 到 SSR 再到 RSC 的典範轉移

Web 開發的歷史就像一個鐘擺，在「伺服器端」與「用戶端」之間來回擺盪。

### 1. 多頁面應用 (MPA) 時代
早期的網頁（如 PHP, JSP, ASP.NET）都是 **MPA (Multi-Page Application)**。
*   **流程**：瀏覽器請求 -> 伺服器動態產生 HTML -> 回傳完整 HTML。
*   **優點**：SEO 友善，首屏載入快（因為只有 HTML）。
*   **缺點**：每次換頁都要重新整理，使用者體驗（UX）卡頓，互動性差。

### 2. 單頁面應用 (SPA) 與 CSR 的崛起
隨著 AJAX 與 JavaScript 的進步，React, Vue, Angular 推動了 **SPA (Single-Page Application)** 的流行。
*   **流程**：伺服器只回傳一個空的 HTML (`<div id="root"></div>`) -> 瀏覽器下載龐大的 JS -> JS 執行並渲染畫面 (CSR - Client Side Rendering)。
*   **優點**：換頁不刷新，操作流暢如原生 App。
*   **缺點**：SEO 差（爬蟲初期看不懂 JS），首屏載入慢（要等 JS 下載執行完才看得到東西），Bundle Size 隨專案變大而失控。

### 3. SSR 與 SSG 的修正
為了同時擁有 MPA 的 SEO 與 SPA 的 UX，Next.js (Pages Router 時代) 提供了 **SSR (Server Side Rendering)** 與 **SSG (Static Site Generation)**。
*   **概念**：在伺服器先跑一次 React，產出 HTML 讓使用者先看到，JS 下載完後再「注水 (Hydrate)」接管頁面互動。
*   **問題**：這仍然沒有解決「傳送過多 JS 到瀏覽器」的問題。Hydration 過程仍然昂貴。

### 4. RSC：Server Components 的全新典範
Next.js 13+ 引入的 App Router 與 **React Server Components (RSC)** 是最新的典範轉移。
*   **概念**：元件預設在伺服器執行，甚至不傳送 JS 到瀏覽器。只有需要互動的部分（如按鈕、表單）才標記為 Client Component。
*   **結果**：極致的效能，極小的 Bundle Size，且能直接在元件內讀取資料庫。

---

## 1.2 渲染模式大觀園：CSR、SSR、SSG 與 ISR 的差異與應用場景

如果把網頁比喻為一道菜，不同的渲染模式就是不同的「出餐方式」：

| 模式 | 全名 | 譬喻 | 適用場景 |
| :--- | :--- | :--- | :--- |
| **CSR** | Client-Side Rendering | **自助火鍋**：給你生食材（JS），客人自己煮（瀏覽器運算）。 | 後台管理系統、互動極高的儀表板。 |
| **SSR** | Server-Side Rendering | **現點現做**：客人點餐後，廚房馬上煮好端出來。 | 個人化資料、股市即時報價、社群動態牆。 |
| **SSG** | Static Site Generation | **自助餐便當**：開店前就煮好一大堆，客人來直接夾。 | 部落格文章、行銷活動頁、文件網站。 |
| **ISR** | Incremental Static Regeneration | **定時補菜**：便當還是先煮好，但每隔一段時間（如 60秒）廚房會重做新的替換舊的。 | 電商商品頁（允許價格有短暫延遲）。 |

Next.js App Router 的強大之處在於，你可以在**同一個專案、甚至同一個頁面中**混合使用這些模式。

---

## 1.3 React Server Components (RSC) 解密：Server vs. Client 的邊界

這是初學者最容易卡關的地方。請記住核心原則：**預設都是 Server Component**。

### Server Components (後場廚房)
*   **執行位置**：伺服器。
*   **能力**：
    *   ✅ 直接連線資料庫。
    *   ✅ 讀取內部檔案系統。
    *   ✅ 隱藏敏感資訊（API Keys）。
*   **限制**：
    *   ❌ 不能使用 `useState`, `useEffect`。
    *   ❌ 不能使用瀏覽器 API (window, document)。
    *   ❌ 不能綁定事件 (onClick)。

### Client Components (前場服務生)
*   **執行位置**：伺服器預先渲染 HTML + 瀏覽器執行 JS Hydration。
*   **如何啟用**：在檔案最上方加上 `'use client'`。
*   **能力**：
    *   ✅ 使用所有 React Hooks (`useState`, `useEffect`, `useRouter` 等)。
    *   ✅ 監聽事件 (`onClick`, `onChange`)。
*   **限制**：
    *   ❌ 不建議直接連資料庫（會暴露帳密）。
    *   ❌ 會增加 Client Bundle Size。

### 邊界圖解
想像一個元件樹：
```text
Page (Server)
 ├─ Header (Server)
 ├─ PostList (Server) -> 直接讀 DB
 │   └─ LikeButton (Client) -> 'use client', onClick 事件
 └─ Footer (Server)
```
我們只在「末端」的互動節點使用 Client Component，保持樹幹與樹枝都是輕量的 Server Component。

---

## 1.4 環境建置與專案結構

讓我們開始動手實作。

### 建立專案
請打開終端機，執行以下指令：

```bash
npx create-next-app@latest my-next-app
```

安裝過程中的問答建議：
*   TypeScript: **Yes** (本書全程使用 TS)
*   ESLint: **Yes**
*   Tailwind CSS: **Yes** (現代開發標配)
*   src/ directory: **No** (為了簡化路徑，本書使用根目錄結構，選 Yes 亦可)
*   App Router: **Yes** (這是重點！)
*   Customize the default import alias (@/*): **No**

### 關鍵檔案結構

```text
my-next-app/
├── app/                  # App Router 的核心目錄
│   ├── layout.tsx        # 全域版型 (Root Layout)，必須包含 <html> 與 <body>
│   ├── page.tsx          # 首頁 (/) 的 UI
│   ├── global.css        # 全域樣式
│   └── loading.tsx       # (可選) 載入中狀態
├── public/               # 靜態檔案 (圖片, fonts)
├── next.config.js        # Next.js 設定檔
├── package.json          # 依賴套件表
└── tsconfig.json         # TypeScript 設定
```

---

## [範例演練]：建立 Hello World 專案

我們來修改首頁，體驗 RSC 的寫法。

**目標**：在首頁顯示伺服器時間（證明是在 Server 執行）。

1.  開啟 `app/page.tsx`，清空內容並貼上：

```tsx
// 這裡不需要 'use client'，所以預設是 Server Component

export default function Home() {
  // 這個 console.log 只會出現在「終端機」，不會出現在瀏覽器的 F12 Console
  console.log("現在是伺服器時間，正在渲染首頁...");
  
  const time = new Date().toLocaleString();

  return (
    <main style={{ padding: '2rem', fontFamily: 'system-ui' }}>
      <h1>Hello, Next.js!</h1>
      <p>這是一個 Server Component。</p>
      <p>伺服器產生這這頁面的時間是：<strong>{time}</strong></p>
      
      <div style={{ marginTop: '20px', padding: '10px', background: '#f0f0f0' }}>
        <p>試試看重新整理頁面，你會發現時間變了，但網頁載入速度非常快。</p>
      </div>
    </main>
  );
}
```

2.  執行開發伺服器：
    ```bash
    npm run dev
    ```

3.  打開瀏覽器 `http://localhost:3000`。
    *   你會看到時間顯示在頁面上。
    *   **檢查**：按右鍵「檢視網頁原始碼」，你會發現時間文字已經直接寫在 HTML 裡了（SEO 友善），而不是由 JS 動態生成的。

這就是 Next.js 帶給我們的第一份禮物：**既有動態資料的彈性，又有靜態 HTML 的效能。**
