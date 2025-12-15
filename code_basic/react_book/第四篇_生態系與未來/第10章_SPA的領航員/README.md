# 第 10 章：SPA 的領航員 —— React Router

## 本章簡介

本章將深入探討 React Router，這是 React 生態系中最重要的路由解決方案。我們將學習如何建立單頁應用 (SPA) 的路由系統，實現頁面間的導航，並掌握進階的路由技巧。

## 本章大綱

### 10.1 什麼是 SPA？為什麼需要路由？
- [10.1 什麼是 SPA？為什麼需要路由？.md](10.1%20什麼是%20SPA？為什麼需要路由？.md)
- MPA vs SPA 的差異
- Client Side Routing 原理 (攔截點擊 + History API)

### 10.2 React Router 基礎
- [10.2 React Router 基礎.md](10.2%20React%20Router%20基礎.md)
- `<BrowserRouter>` 設定
- `<Routes>` 與 `<Route>` 定義
- `<Link>` 與 `<NavLink>` 的使用 (禁止使用 a 標籤)

### 10.3 動態路由與參數
- [10.3 動態路由與參數.md](10.3%20動態路由與參數.md)
- URL Params: `useParams`
- Query String: `useSearchParams`
- 程式化導航: `useNavigate`

### 10.4 巢狀路由與佈局
- [10.4 巢狀路由與佈局.md](10.4%20巢狀路由與佈局.md)
- Nested Routes 結構設計
- `<Outlet>` 的佔位符功能
- 製作 Dashboard Layout

### 10.5 路由守衛與導航
- 程式化導航 (useNavigate)
- 受保護的路由
- 導航守衛的實作
- 路由攔截

### 10.6 進階功能
- Lazy Loading (程式碼分割)
- 錯誤頁面 (404)
- 路由過渡動畫
- 麵包屑導航

## 學習目標

- [ ] 理解 SPA 與客戶端路由的概念
- [ ] 熟練使用 React Router 建立路由系統
- [ ] 掌握動態路由與參數傳遞
- [ ] 實作巢狀路由與共用佈局
## 學習目標

### 10.7 練習題與自我測驗
- [10.7 練習題與自我測驗.md](10.7%20練習題與自我測驗.md)
- Link vs A tag 觀念測驗
- 實作 Active Link 與 PrivateRoute

## 相關資源

- [React Router 官方文件](https://reactrouter.com/)
- [React Router Tutorial](https://reactrouter.com/en/main/start/tutorial)
- [單頁應用路由原理](https://developer.mozilla.org/zh-TW/docs/Web/API/History_API)
