# 實戰演練：封裝 useFetch 與 useLocalStorage

## 專案一：useFetch Hook

### 功能需求
- [ ] 處理 API 請求
- [ ] 管理 loading、error、data 狀態
- [ ] 支援重新請求
- [ ] 自動清理（防止記憶體洩漏）
- [ ] 支援不同的 HTTP 方法

### 核心實作

```jsx
function useFetch(url, options = {}) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let cancelled = false;

    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await fetch(url, options);
        
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
  }, [url, JSON.stringify(options)]);

  const refetch = () => {
    setLoading(true);
    // 觸發重新請求
  };

  return { data, loading, error, refetch };
}

// 使用範例
function UserList() {
  const { data: users, loading, error, refetch } = useFetch('/api/users');

  if (loading) return <div>載入中...</div>;
  if (error) return <div>錯誤: {error}</div>;

  return (
    <div>
      {users.map(user => (
        <div key={user.id}>{user.name}</div>
      ))}
      <button onClick={refetch}>重新載入</button>
    </div>
  );
}
```

## 專案二：useLocalStorage Hook

### 功能需求
- [ ] 讀取 localStorage
- [ ] 寫入 localStorage
- [ ] 與 useState 整合
- [ ] 自動序列化/反序列化
- [ ] 錯誤處理
- [ ] 支援預設值

### 核心實作

```jsx
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

  // 更新 localStorage 的函式
  const setValue = (value) => {
    try {
      // 允許傳入函式（類似 useState）
      const valueToStore = value instanceof Function 
        ? value(storedValue) 
        : value;
      
      setStoredValue(valueToStore);
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error(error);
    }
  };

  return [storedValue, setValue];
}

// 使用範例
function Settings() {
  const [theme, setTheme] = useLocalStorage('theme', 'light');
  const [language, setLanguage] = useLocalStorage('language', 'zh-TW');

  return (
    <div>
      <select value={theme} onChange={(e) => setTheme(e.target.value)}>
        <option value="light">淺色</option>
        <option value="dark">深色</option>
      </select>
      
      <select value={language} onChange={(e) => setLanguage(e.target.value)}>
        <option value="zh-TW">繁體中文</option>
        <option value="en">English</option>
      </select>
    </div>
  );
}
```

## 進階挑戰

### useFetch 進階
- [ ] 加入請求快取
- [ ] 支援輪詢 (Polling)
- [ ] 支援分頁
- [ ] 樂觀更新
- [ ] 請求取消

### useLocalStorage 進階
- [ ] 監聽其他分頁的變更
- [ ] 加入過期時間
- [ ] 容量管理
- [ ] 資料遷移
- [ ] 壓縮大型資料

## 組合使用

```jsx
// 結合兩個 Custom Hooks
function TodoApp() {
  const [todos, setTodos] = useLocalStorage('todos', []);
  const { data: remoteTodos, loading } = useFetch('/api/todos');

  // 同步本地與遠端資料
  useEffect(() => {
    if (remoteTodos) {
      setTodos(remoteTodos);
    }
  }, [remoteTodos]);

  // ...
}
```

---
**狀態：** 📝 待補充完整實作與測試用例
