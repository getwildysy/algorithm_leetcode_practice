# 第 5 章：副作用的處理 —— Effect (useEffect)

## 本章大綱

### 5.1 什麼是副作用 (Side Effect)？
- [5.1 什麼是副作用.md](5.1%20什麼是副作用.md)
- 純函式 (Pure Function) vs 副作用
- 為什麼需要 `useEffect`：同步外部系統
- Effect 的執行時機 (Render 之後)
- 常見的副作用類型
  - API 請求
  - 訂閱事件
  - 操作 DOM
  - 計時器

### 5.2 useEffect 的依賴陣列 (Dependency Array)：什麼時候該執行？
- [5.2 useEffect 的依賴陣列：什麼時候該執行.md](5.2%20useEffect%20的依賴陣列：什麼時候該執行.md)
- 依賴陣列的三種模式 `[]` vs `[dep]` vs 省略
- 淺層比較機制 (Object.is) 與無限迴圈陷阱
- ESLint 規則的重要性

### 5.3 清理機制 (Cleanup Function)：防止記憶體洩漏
- [5.3 清理機制：防止記憶體洩漏.md](5.3%20清理機制：防止記憶體洩漏.md)
- Cleanup 執行流程： 先清舊的 -> 再跑新的
- 實戰：清除 Event Listener 與 Timer
- 避免 Race Condition (Ignore Flag 模式)

## 實戰演練

### 1. 即時視窗大小偵測器
**功能需求:**
- 偵測瀏覽器視窗大小
- 即時顯示寬度與高度
- 正確清理事件監聽器

### 2. 倒數計時器
**功能需求:**
- 設定倒數秒數
- 開始/暫停/重置功能
- 倒數結束時顯示提示
- 正確清理計時器

### 5.4 練習題與自我測驗
- [5.4 練習題與自我測驗.md](5.4%20練習題與自我測驗.md)
- Effect 流程觀念測驗
- 記憶體洩漏修復挑戰

- [ ] 理解副作用的概念
- [ ] 熟練使用 useEffect Hook
- [ ] 掌握依賴陣列的設定
- [ ] 學會實作清理函式
- [ ] 完成視窗偵測器與計時器實作

## 範例程式碼

```jsx
import { useState, useEffect } from 'react';

function WindowSize() {
  const [size, setSize] = useState({
    width: window.innerWidth,
    height: window.innerHeight
  });

  useEffect(() => {
    function handleResize() {
      setSize({
        width: window.innerWidth,
        height: window.innerHeight
      });
    }

    window.addEventListener('resize', handleResize);
    
    // 清理函式
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []); // 空陣列表示只在掛載時執行

  return (
    <div>
      <p>寬度: {size.width}px</p>
      <p>高度: {size.height}px</p>
    </div>
  );
}
```

## 常見陷阱

1. 忘記清理副作用
2. 依賴陣列設定錯誤
3. 在 useEffect 中更新狀態導致無限迴圈
4. 非同步操作的處理

## 相關資源

- [React - useEffect](https://react.dev/reference/react/useEffect)
- [React - 同步化副作用](https://react.dev/learn/synchronizing-with-effects)
