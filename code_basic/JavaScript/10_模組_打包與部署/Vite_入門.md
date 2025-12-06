# Vite 入門

**Vite (法語「快」)** 是一個現代前端建構工具，由 Vue.js 的作者尤雨溪開發。它旨在提供極致快速的開發體驗。Vite 利用瀏覽器原生 ES Modules (ESM) 和各種工具來實現其速度優勢。

## 1. 為什麼選擇 Vite？

*   **極速啟動**：開發伺服器啟動速度飛快。
*   **瞬間熱模組替換 (HMR)**：修改程式碼後，瀏覽器幾乎即時更新，無需重新載入頁面。
*   **優化的生產建構**：基於 Rollup 進行生產環境建構，產出優化過的靜態資源。
*   **原生 ESM**：開發環境下，Vite 直接利用瀏覽器對 ES Modules 的支援，不需綑綁 (Bundle) 程式碼。
*   **預設支援多種框架**：Vue, React, Preact, Lit, Svelte 等。
*   **插件化 (Plugin-driven)**：高度可擴展，可透過插件支援各種需求。

## 2. 建立一個 Vite 專案

使用 `npm` (或 `yarn`, `pnpm`) 執行一行指令即可快速建立專案。

```bash
# npm 6.x
npm init vite@latest my-vue-app -- --template vue

# npm 7+, 必須額外加兩條短橫線
npm create vite@latest my-react-app -- --template react-ts

# 或者互動式選擇
npm create vite@latest
```

指令執行後，它會詢問你：
1.  專案名稱 (Project name)
2.  選擇框架 (Select a framework): `vanilla`, `vue`, `react`, `preact`, `lit`, `svelte`, `solid`
3.  選擇變種 (Select a variant): `JavaScript`, `TypeScript`, `SWC`

範例：建立一個基於 React + TypeScript 的專案
```bash
npm create vite@latest my-react-project
# Project name: my-react-project
# Select a framework: React
# Select a variant: TypeScript
```

## 3. 專案結構 (以 React + TS 為例)

```
my-react-project/
├── public/                # 靜態資源，會被直接複製
│   └── vite.svg
├── src/
│   ├── assets/
│   │   └── react.svg
│   ├── components/
│   │   └── HelloWorld.tsx
│   ├── App.tsx            # 主要應用程式元件
│   ├── index.css
│   └── main.tsx           # 入口檔案，渲染根元件
├── index.html             # 根 HTML 檔案，Vite 會注入打包後的 JS
├── package.json
├── tsconfig.json
├── vite.config.ts         # Vite 設定檔
└── README.md
```

## 4. 開發與建構

進入專案資料夾後，執行以下指令：

```bash
cd my-react-project

# 安裝依賴
npm install

# 啟動開發伺服器
npm run dev

# 進行生產環境建構
npm run build

# 預覽生產建構後的結果 (如果 build 過)
npm run preview
```

### `index.html` 的特殊之處

Vite 使用 `index.html` 作為開發伺服器的入口點。你的 JavaScript 檔案將透過 `<script type="module" src="/src/main.tsx"></script>` 被引入。在開發模式下，Vite 會攔截這個請求並根據需要轉換你的模組。

## 5. Vite 設定檔 (`vite.config.ts` 或 `vite.config.js`)

你可以透過這個檔案自訂 Vite 的行為，例如：
*   設定代理 (Proxy)
*   配置插件 (Plugins)
*   設定別名 (Alias)
*   配置 CSS 預處理器 (Preprocessors)

```typescript
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000, // 自訂開發伺服器埠號
    proxy: {
      '/api': 'http://localhost:8080', // 代理 API 請求
    }
  },
  resolve: {
    alias: {
      '@': '/src', // 設定 @ 別名指向 src 資料夾
    },
  },
});
```
