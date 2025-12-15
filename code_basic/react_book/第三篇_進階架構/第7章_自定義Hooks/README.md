# 第 7 章：自定義 Hooks (Custom Hooks)

## 本章大綱

### 7.1 Don't Repeat Yourself (DRY)：抽離邏輯的藝術
- [7.1 Don't Repeat Yourself：抽離邏輯的藝術.md](7.1%20Don't%20Repeat%20Yourself：抽離邏輯的藝術.md)
- Custom Hook 的定義 (單純的 JS 函式 + Hook)
- 範例：從 Component 抽離 `useWindowSize`
- 邏輯複用 vs 狀態複用 (Hook 不會共享狀態)

### 7.2 Hook 的規則：為什麼不能在迴圈中使用 Hook？
- Hook 的呼叫規則
  - 只在最頂層呼叫 Hook
  - 只在 React 函式中呼叫 Hook
- React 如何追蹤 Hooks
- 違反規則的後果
- ESLint 插件的輔助

## 實戰演練

### 1. 封裝 useFetch
**功能需求:**
- 處理 API 請求
- 管理 loading、error、data 狀態
- 支援重新請求
- 自動清理

### 2. 封裝 useLocalStorage
**功能需求:**
- 讀取 localStorage
- 寫入 localStorage
- 與 useState 整合
- 自動序列化/反序列化

## 學習目標

### 7.3 實戰通用 Hooks
- [7.3 實戰通用 Hooks.md](7.3%20實戰通用%20Hooks.md)
- `useWindowSize`
- `useDebounce`
- `useLocalStorage`

### 7.4 練習題與自我測驗
- [7.4 練習題與自我測驗.md](7.4%20練習題與自我測驗.md)
- Hook 命名規則測驗
- 實作 useToggle 與 useDocumentTitle

- [ ] 理解自定義 Hooks 的概念
- [ ] 掌握 Hooks 的使用規則
- [ ] 學會識別可重用的邏輯
- [ ] 完成 useFetch 與 useLocalStorage 實作
- [ ] 能夠設計自己的 Custom Hooks

## 範例程式碼

### useFetch

```jsx
import { useState, useEffect } from 'react';

function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let cancelled = false;

    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await fetch(url);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const result = await response.json();
        
        if (!cancelled) {
          setData(result);
          setError(null);
        }
      } catch (err) {
        if (!cancelled) {
          setError(err.message);
          setData(null);
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    };

    fetchData();

    return () => {
      cancelled = true;
    };
  }, [url]);

  return { data, loading, error };
}

// 使用範例
function UserProfile({ userId }) {
  const { data, loading, error } = useFetch(`/api/users/${userId}`);

  if (loading) return <div>載入中...</div>;
  if (error) return <div>錯誤: {error}</div>;
  
  return <div>{data.name}</div>;
}
```

### useLocalStorage

```jsx
import { useState, useEffect } from 'react';

function useLocalStorage(key, initialValue) {
  // 初始化狀態
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error(error);
      return initialValue;
    }
  });

  // 更新 localStorage
  const setValue = (value) => {
    try {
      const valueToStore = value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error(error);
    }
  };

  return [storedValue, setValue];
}

// 使用範例
function ThemeToggle() {
  const [theme, setTheme] = useLocalStorage('theme', 'light');

  return (
    <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
      當前主題: {theme}
    </button>
  );
}
```

## 常用 Custom Hooks 範例

1. `useDebounce` - 防抖處理
2. `useThrottle` - 節流處理
3. `useWindowSize` - 視窗大小
4. `useOnClickOutside` - 點擊外部偵測
5. `useKeyPress` - 鍵盤事件
6. `useToggle` - 布林值切換
7. `usePrevious` - 保存前一個值

## 最佳實踐

1. 命名以 `use` 開頭
2. 保持單一職責
3. 適當的參數設計
4. 返回值的設計考量
5. 完善的錯誤處理

## 相關資源

- [React - 自訂 Hook](https://react.dev/learn/reusing-logic-with-custom-hooks)
- [usehooks.com](https://usehooks.com/)
- [react-use 函式庫](https://github.com/streamich/react-use)
