# React 現代化開發實戰

> 從零開始，掌握 React 18+ 與現代前端開發

## 📚 關於本書

這是一本專注於 **現代 React 開發** 的實戰教學書籍。我們摒棄過時的 Class Component，全面擁抱 **Functional Component + Hooks**，帶你建立正確的 React 開發思維。

### 適合對象

✅ 想學習 React 的前端新手  
✅ 有基礎 JavaScript 知識的開發者  
✅ 想從 Class Component 轉向 Hooks 的開發者  
✅ 希望系統化學習現代 React 的學習者

### 不適合對象

❌ 完全沒有程式設計基礎的人  
❌ 尋找 React Native 教學的人  
❌ 只想學習 Class Component 的人

## 🎯 學習目標

完成本書後，你將能夠：

- ✅ 熟練使用 React 18+ 的現代開發方式
- ✅ 掌握 Hooks 的核心概念與使用技巧
- ✅ 建立完整的單頁應用 (SPA)
- ✅ 整合狀態管理與 API 串接
- ✅ 具備業界所需的 React 開發能力

## 📖 內容架構

本書分為四大篇章，共 10+ 章節：

### [第一篇：起手式 —— 觀念重塑與環境建置](./第一篇_起手式/README.md)

建立正確的 React 開發觀念，打好 JavaScript 基礎。

- 第 1 章：為什麼是 React？
- 第 2 章：JavaScript 極速補給站 (ES6+)
- 第 3 章：JSX 與 Component 初體驗

### [第二篇：核心引擎 —— Hooks 與資料流](./第二篇_核心引擎/README.md)

深入理解 React 的渲染機制與 Hooks 使用規範。

- 第 4 章：賦予元件生命 —— State (useState)
- 第 5 章：副作用的處理 —— Effect (useEffect)
- 第 6 章：表單與列表處理

### [第三篇：進階架構 —— 邏輯複用與全域狀態](./第三篇_進階架構/README.md)

從「寫得出來」進階到「寫得漂亮、好維護」。

- 第 7 章：自定義 Hooks (Custom Hooks)
- 第 8 章：單向資料流的救贖 —— Context API 與狀態管理
- 第 9 章：與伺服器共舞 —— API 串接

### [第四篇：生態系與未來 —— 邁向專業之路](./第四篇_生態系與未來/README.md)

整合路由、樣式與效能優化，銜接業界需求。

- 第 10 章：SPA 的領航員 —— React Router
- 第 11 章：樣式的藝術（規劃中）
- 第 12 章：效能優化（規劃中）
- 第 13 章：測試與除錯（規劃中）

## 🛠️ 技術棧

本書採用的現代技術棧：

| 技術 | 版本 | 說明 |
|------|------|------|
| React | 18+ | 現代化的 React 開發 |
| Vite | 最新版 | 快速的開發建置工具 |
| React Router | v6+ | 單頁應用路由 |
| Zustand | 最新版 | 輕量級狀態管理 |
| TanStack Query | v5+ | 伺服器狀態管理 |
| Axios | 最新版 | HTTP 請求函式庫 |

## 📝 學習方式

### 建議學習順序

1. **循序漸進**：按照章節順序學習，不要跳章
2. **動手實作**：每章都有實戰演練，務必完成
3. **筆記整理**：記錄重點與心得
4. **專案實作**：學完每篇後建立一個小專案

### 預估學習時間

- **第一篇**：1-2 週
- **第二篇**：2-3 週
- **第三篇**：3-4 週
- **第四篇**：3-4 週

**總計：約 2-3 個月**（視個人基礎與投入時間而定）

## 💻 開發環境需求

### 必要環境

- Node.js 18+ ([下載連結](https://nodejs.org/))
- npm 或 yarn
- 程式碼編輯器（推薦 VS Code）

### 推薦的 VS Code 擴充套件

- ES7+ React/Redux/React-Native snippets
- Prettier - Code formatter
- ESLint
- Auto Rename Tag
- Path Intellisense

## 🎓 前置知識

建議具備以下基礎知識：

### 必要知識

- ✅ HTML 基礎
- ✅ CSS 基礎
- ✅ JavaScript 基礎（變數、函式、陣列、物件）

### 加分知識（非必要）

- ⭐ ES6+ 語法
- ⭐ npm/yarn 使用
- ⭐ Git 版本控制
- ⭐ 基礎命令列操作

## 🚀 快速開始

### 建立第一個 React 專案

```bash
# 使用 Vite 建立專案
npm create vite@latest my-react-app -- --template react

# 進入專案目錄
cd my-react-app

# 安裝依賴
npm install

# 啟動開發伺服器
npm run dev
```

詳細說明請參考 [第 1 章](./第一篇_起手式/第1章_為什麼是React/README.md)。

## 📚 實戰專案

本書包含多個實戰專案，逐步提升難度：

1. **個人資訊卡**（第 3 章）- Props 傳遞練習
2. **互動式計數器**（第 4 章）- useState 基礎
3. **待辦事項清單**（第 6 章）- 整合表單與列表
4. **天氣預報 APP**（第 9 章）- API 串接實戰
5. **購物車系統**（第 8 章）- 全域狀態管理
6. **部落格系統**（第 10 章）- 完整 SPA 應用

## 🌟 本書特色

### ✨ 現代化導向

完全聚焦於現代 React 開發（Functional Component + Hooks），不浪費時間在過時技術。

### ✨ 觀念深入

不只教你「怎麼做」，更重要的是「為什麼這樣做」，建立正確的開發思維。

### ✨ 實戰導向

每章都有實戰演練，學完立即應用，不只是紙上談兵。

### ✨ 業界接軌

採用業界主流的技術棧與最佳實踐，學完即可投入實戰。

### ✨ 循序漸進

從基礎到進階，層層遞進，確保每個概念都能扎實掌握。

## 📖 學習資源

### 官方文件

- [React 官方文件](https://react.dev/)
- [React Router](https://reactrouter.com/)
- [Vite](https://vitejs.dev/)
- [TanStack Query](https://tanstack.com/query/latest)

### 推薦資源

- [MDN Web Docs](https://developer.mozilla.org/zh-TW/)
- [JavaScript.info](https://javascript.info/)
- [Can I Use](https://caniuse.com/)

## 💡 學習建議

### Do ✅

- 動手寫程式，不要只看不練
- 遇到問題先思考，再查資料
- 建立個人筆記與心得
- 加入社群，與他人交流
- 持續關注 React 生態系的發展

### Don't ❌

- 不要跳章學習
- 不要死背程式碼
- 不要忽略基礎知識
- 不要害怕犯錯
- 不要放棄實作練習

## 🤝 貢獻與反饋

如果你在學習過程中發現任何問題或有改進建議，歡迎提出！

## 📄 授權

本教材僅供學習使用。

## 🎉 開始你的 React 學習之旅！

準備好了嗎？讓我們從 [第一篇：起手式](./第一篇_起手式/README.md) 開始吧！

---

**祝你學習順利！記住：最好的學習方式就是不斷地實作！** 🚀
