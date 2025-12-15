# 第 8 章：單向資料流的救贖 —— Context API 與狀態管理

## 本章大綱

### 8.1 Prop Drilling (層層傳遞) 的痛苦
- [8.1 Prop Drilling (層層傳遞) 的痛苦.md](8.1%20Prop%20Drilling%20(層層傳遞)%20的痛苦.md)
- 視覺化問題：像鑽地機一樣的資料流
- 何時該在意？何時不該過早優化？

### 8.2 Context API 實戰：製作全域主題切換 (Dark Mode)
- [8.2 Context API 實戰：製作全域主題切換 (Dark Mode).md](8.2%20Context%20API%20實戰：製作全域主題切換%20(Dark%20Mode).md)
- Context 三部曲：Create, Provide, Consume
- 實戰 Pattern：封裝 Provider 與 Custom Hook
- Context 的效能陷阱 (Re-render issue)

### 8.3 狀態管理戰國時代：簡介 Redux Toolkit 與 Zustand
- 狀態管理的演進
- Redux Toolkit 簡介
  - 核心概念
  - 基本用法
  - 適用場景
- Zustand 簡介
  - 為什麼推薦初學者？
  - 簡潔的 API
  - 基本用法
- 如何選擇狀態管理方案？

## 實戰演練

**實作「全域購物車」功能**

### 功能需求
- 新增商品到購物車
- 修改商品數量
- 移除商品
- 計算總金額
- 購物車在不同頁面保持同步

## 學習目標

- [ ] 理解 Prop Drilling 的問題
- [ ] 熟練使用 Context API
- [ ] 掌握 Provider 與 Consumer 的用法
- [ ] 了解 Redux Toolkit 與 Zustand
## 學習目標

### 8.4 練習題與自我測驗
- [8.4 練習題與自我測驗.md](8.4%20練習題與自我測驗.md)
- Context vs Zustand 觀念測驗
- 實作 AuthContext 與 Counter 用法

## 範例程式碼

### Dark Mode with Context API

```jsx
// ThemeContext.jsx
import { createContext, useContext, useState } from 'react';

const ThemeContext = createContext();

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');

  const toggleTheme = () => {
    setTheme(prev => prev === 'light' ? 'dark' : 'light');
  };

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

export function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider');
  }
  return context;
}

// App.jsx
import { ThemeProvider } from './ThemeContext';

function App() {
  return (
    <ThemeProvider>
      <Layout />
    </ThemeProvider>
  );
}

// ThemeToggle.jsx
import { useTheme } from './ThemeContext';

function ThemeToggle() {
  const { theme, toggleTheme } = useTheme();

  return (
    <button onClick={toggleTheme}>
      切換到 {theme === 'light' ? '深色' : '淺色'} 模式
    </button>
  );
}
```

### Shopping Cart with Zustand

```jsx
// store/cartStore.js
import { create } from 'zustand';

export const useCartStore = create((set) => ({
  items: [],
  
  addItem: (product) => set((state) => {
    const existingItem = state.items.find(item => item.id === product.id);
    
    if (existingItem) {
      return {
        items: state.items.map(item =>
          item.id === product.id
            ? { ...item, quantity: item.quantity + 1 }
            : item
        )
      };
    }
    
    return { items: [...state.items, { ...product, quantity: 1 }] };
  }),
  
  removeItem: (productId) => set((state) => ({
    items: state.items.filter(item => item.id !== productId)
  })),
  
  updateQuantity: (productId, quantity) => set((state) => ({
    items: state.items.map(item =>
      item.id === productId ? { ...item, quantity } : item
    )
  })),
  
  clearCart: () => set({ items: [] }),
  
  getTotalPrice: () => {
    return useCartStore.getState().items.reduce(
      (total, item) => total + item.price * item.quantity,
      0
    );
  }
}));

// Cart.jsx
import { useCartStore } from './store/cartStore';

function Cart() {
  const items = useCartStore(state => state.items);
  const removeItem = useCartStore(state => state.removeItem);
  const updateQuantity = useCartStore(state => state.updateQuantity);

  const totalPrice = items.reduce(
    (total, item) => total + item.price * item.quantity,
    0
  );

  return (
    <div>
      <h2>購物車</h2>
      {items.map(item => (
        <div key={item.id}>
          <span>{item.name}</span>
          <input
            type="number"
            value={item.quantity}
            onChange={(e) => updateQuantity(item.id, parseInt(e.target.value))}
          />
          <span>${item.price * item.quantity}</span>
          <button onClick={() => removeItem(item.id)}>移除</button>
        </div>
      ))}
      <div>總計: ${totalPrice}</div>
    </div>
  );
}
```

## Context API 效能優化技巧

1. 拆分 Context（避免不必要的重渲染）
2. 使用 useMemo 與 useCallback
3. 考慮使用 Context Selector

## 狀態管理方案比較

| 方案 | 複雜度 | 學習曲線 | 效能 | 適用場景 |
|------|--------|----------|------|----------|
| Context API | 低 | 容易 | 中 | 簡單的全域狀態 |
| Zustand | 低 | 容易 | 高 | 中小型應用 |
| Redux Toolkit | 高 | 陡峭 | 高 | 大型複雜應用 |

## 相關資源

- [React - Context](https://react.dev/learn/passing-data-deeply-with-context)
- [Zustand 官方文件](https://zustand-demo.pmnd.rs/)
- [Redux Toolkit 官方文件](https://redux-toolkit.js.org/)
