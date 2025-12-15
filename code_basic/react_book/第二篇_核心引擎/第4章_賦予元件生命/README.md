# 第 4 章：賦予元件生命 —— State (useState)

## 本章大綱

### 4.1 狀態 vs. 變數：為什麼不能直接修改變數？
- [4.1 狀態 vs 變數：為什麼不能直接修改變數.md](4.1%20狀態%20vs%20變數：為什麼不能直接修改變數.md)
- React 的渲染公式 `UI = f(State)`
- Render Cycle 與 Snapshot 模型
- 為什麼 `let` 變數無法觸發畫面更新

### 4.2 useState 詳解：初始化與更新機制
- [4.2 useState 詳解：初始化與更新機制.md](4.2%20useState%20詳解：初始化與更新機制.md)
- 函式式更新 (Functional Update) 的重要性
- 物件狀態的更新策略 (Spread Operator)
- 惰性初始化 (Lazy Initialization) 效能優化

### 4.3 異步更新的陷阱：為什麼 State 不會馬上變？
- [4.3 異步更新的陷阱：為什麼 State 不會馬上變.md](4.3%20異步更新的陷阱：為什麼%20State%20不會馬上變.md)
- React 18 自動批次更新 (Automatic Batching)
- 閉包陷阱 (Stale Closure) 原理解析
- 如何正確獲取最新的 State

## 實戰演練

### 1. 互動式計數器
**功能需求:**
- 增加/減少按鈕
- 重置按鈕
- 顯示當前數值

### 2. 多頁籤切換器 (Tabs)
**功能需求:**
- 多個頁籤選項
- 點擊切換內容
- 高亮當前選中的頁籤

### 4.4 練習題與自我測驗
- [4.4 練習題與自我測驗.md](4.4%20練習題與自我測驗.md)
- State 機制觀念測驗
- 常見陷阱除錯挑戰

- [ ] 理解 State 與普通變數的差異
- [ ] 熟練使用 useState Hook
- [ ] 掌握狀態更新的機制
- [ ] 完成計數器與頁籤切換器實作

## 範例程式碼

```jsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>當前數值: {count}</p>
      <button onClick={() => setCount(count + 1)}>增加</button>
      <button onClick={() => setCount(count - 1)}>減少</button>
      <button onClick={() => setCount(0)}>重置</button>
    </div>
  );
}
```

## 常見錯誤

1. 直接修改狀態值
2. 在 render 期間呼叫 setState
3. 狀態更新後立即讀取

## 相關資源

- [React - useState](https://react.dev/reference/react/useState)
- [React - 狀態管理](https://react.dev/learn/managing-state)
