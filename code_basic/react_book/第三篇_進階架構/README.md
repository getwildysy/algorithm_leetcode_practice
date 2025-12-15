# 第三篇：進階架構 —— 邏輯複用與全域狀態

## 篇章簡介

本篇將帶領你從「寫得出來」進階到「寫得漂亮、好維護」。我們將學習如何抽離可重用的邏輯、管理全域狀態，以及與後端 API 串接。

## 重點目標

✅ 掌握邏輯複用的技巧（Custom Hooks）  
✅ 解決 Prop Drilling 問題  
✅ 學會全域狀態管理  
✅ 熟練 API 串接與伺服器狀態管理

## 章節列表

- [第 7 章：自定義 Hooks (Custom Hooks)](./第7章_自定義Hooks/README.md)
- [第 8 章：單向資料流的救贖 —— Context API 與狀態管理](./第8章_單向資料流的救贖/README.md)
- [第 9 章：與伺服器共舞 —— API 串接](./第9章_與伺服器共舞/README.md)

## 學習路徑

```
第二篇完成
 ↓
第 7 章：封裝可重用邏輯
 ↓
第 8 章：管理全域狀態
 ↓
第 9 章：串接後端 API
 ↓
進入第四篇
```

## 預期學習時間

**建議學習時間：** 3-4 週

- 第 7 章：4-5 天
- 第 8 章：5-7 天
- 第 9 章：5-7 天（含 API 串接實作）

## 核心概念

### Custom Hooks
- DRY 原則
- 邏輯抽離
- Hooks 規則

### 狀態管理
- Context API
- Zustand
- Redux Toolkit

### API 串接
- Fetch vs. Axios
- 狀態處理（Loading/Error）
- TanStack Query

## 學習建議

1. **識別模式**：學會識別可以抽離成 Custom Hook 的邏輯模式
2. **漸進式學習**：Context API → Zustand → Redux Toolkit
3. **實際串接**：找真實的公開 API 來練習
4. **理解快取**：TanStack Query 的快取機制很重要

## 檢核清單

完成本篇後，你應該能夠：

- [ ] 設計並實作 Custom Hooks
- [ ] 使用 Context API 解決 Prop Drilling
- [ ] 選擇適合的狀態管理方案
- [ ] 使用 Zustand 管理全域狀態
- [ ] 正確處理 API 請求的各種狀態
- [ ] 使用 TanStack Query 管理伺服器狀態

## 技術選擇指南

### 狀態管理方案選擇

**簡單場景（主題、語言切換）**
→ Context API

**中小型應用**
→ Zustand

**大型複雜應用**
→ Redux Toolkit

### API 請求方案選擇

**簡單請求**
→ Fetch + useState/useEffect

**複雜應用**
→ Axios + TanStack Query

## 實戰專案建議

### 1. 購物車系統（第 8 章）
- 商品列表
- 購物車管理
- 全域狀態同步

### 2. 天氣預報 APP（第 9 章）
- API 串接
- Loading/Error 處理
- 資料快取

## 進階主題

完成本篇後，可以進一步探索：

- 複雜的狀態管理模式
- 伺服器端狀態同步
- 樂觀更新 (Optimistic Updates)
- 離線支援

## 下一步

完成本篇學習後，請繼續前往 [第四篇：生態系與未來](../第四篇_生態系與未來/README.md)，學習路由系統與效能優化，邁向專業之路。
