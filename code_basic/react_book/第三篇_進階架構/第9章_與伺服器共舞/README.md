# 第 9 章：與伺服器共舞 —— API 串接

## 本章大綱

### 9.1 Fetch vs. Axios
- [9.1 Fetch vs. Axios.md](9.1%20Fetch%20vs.%20Axios.md)
- Fetch 原生語法 vs Axios 封裝優勢
- 攔截器 (Interceptors) 的應用場景
- 如何選擇適合的工具

### 9.2 處理 Loading 與 Error 狀態
- [9.2 處理 Loading 與 Error 狀態.md](9.2%20處理%20Loading%20與%20Error%20狀態.md)
- 標準 Async State Pattern (Loading/Error/Data)
- Race Condition (競態條件) 的成因與解法 (Cleanup function)

### 9.3 伺服器狀態管理：為什麼你需要 TanStack Query (React Query)？
- 客戶端狀態 vs. 伺服器狀態
- TanStack Query 解決的問題
  - 快取管理
  - 自動重新請求
  - 背景更新
  - 樂觀更新
- 基本用法
- 實用功能

## 實戰演練

**串接公開 API (如 OpenWeatherMap) 製作天氣預報 APP**

### 功能需求
- 顯示當前天氣
- 顯示未來幾天預報
- 支援城市搜尋
- Loading 與 Error 處理
- 優雅的 UI 設計

## 學習目標

- [ ] 理解 Fetch 與 Axios 的差異
- [ ] 掌握 API 請求的狀態管理
- [ ] 學會處理各種錯誤情況
- [ ] 了解 TanStack Query 的優勢
## 學習目標

### 9.4 練習題與自我測驗
- [9.4 練習題與自我測驗.md](9.4%20練習題與自我測驗.md)
- Fetch 錯誤處理測驗
- 實作 Infinite Scroll 挑戰

## 範例程式碼

### 使用 Fetch

```jsx
import { useState, useEffect } from 'react';

function Weather({ city }) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWeather = async () => {
      try {
        setLoading(true);
        const response = await fetch(
          `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=YOUR_API_KEY`
        );
        
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const result = await response.json();
        setData(result);
        setError(null);
      } catch (err) {
        setError(err.message);
        setData(null);
      } finally {
        setLoading(false);
      }
    };

    fetchWeather();
  }, [city]);

  if (loading) return <div>載入中...</div>;
  if (error) return <div>錯誤: {error}</div>;
  if (!data) return <div>無資料</div>;

  return (
    <div>
      <h2>{data.name}</h2>
      <p>溫度: {(data.main.temp - 273.15).toFixed(1)}°C</p>
      <p>天氣: {data.weather[0].description}</p>
    </div>
  );
}
```

### 使用 Axios

```jsx
import { useState, useEffect } from 'react';
import axios from 'axios';

// 建立 axios 實例
const weatherAPI = axios.create({
  baseURL: 'https://api.openweathermap.org/data/2.5',
  params: {
    appid: 'YOUR_API_KEY',
    units: 'metric'
  }
});

function Weather({ city }) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWeather = async () => {
      try {
        setLoading(true);
        const response = await weatherAPI.get('/weather', {
          params: { q: city }
        });
        setData(response.data);
        setError(null);
      } catch (err) {
        setError(err.response?.data?.message || err.message);
        setData(null);
      } finally {
        setLoading(false);
      }
    };

    fetchWeather();
  }, [city]);

  // ... (渲染邏輯同上)
}
```

### 使用 TanStack Query

```jsx
import { useQuery } from '@tanstack/react-query';
import axios from 'axios';

const weatherAPI = axios.create({
  baseURL: 'https://api.openweathermap.org/data/2.5',
  params: {
    appid: 'YOUR_API_KEY',
    units: 'metric'
  }
});

function Weather({ city }) {
  const { data, isLoading, error } = useQuery({
    queryKey: ['weather', city],
    queryFn: async () => {
      const response = await weatherAPI.get('/weather', {
        params: { q: city }
      });
      return response.data;
    },
    staleTime: 5 * 60 * 1000, // 5 分鐘內視為新鮮資料
    cacheTime: 10 * 60 * 1000, // 快取保留 10 分鐘
  });

  if (isLoading) return <div>載入中...</div>;
  if (error) return <div>錯誤: {error.message}</div>;

  return (
    <div>
      <h2>{data.name}</h2>
      <p>溫度: {data.main.temp}°C</p>
      <p>天氣: {data.weather[0].description}</p>
    </div>
  );
}

// App.jsx
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Weather city="Taipei" />
    </QueryClientProvider>
  );
}
```

## Fetch vs. Axios 比較表

| 特性 | Fetch | Axios |
|------|-------|-------|
| 瀏覽器支援 | 現代瀏覽器 | 所有瀏覽器 |
| 請求/回應攔截器 | ❌ | ✅ |
| 自動轉換 JSON | ❌ | ✅ |
| 錯誤處理 | 需手動檢查 | 自動拋出錯誤 |
| 取消請求 | AbortController | CancelToken |
| 進度追蹤 | ❌ | ✅ |
| 預設值設定 | ❌ | ✅ |

## TanStack Query 的優勢

1. **自動快取管理** - 不用手動管理快取
2. **背景更新** - 資料過期時自動更新
3. **重複請求消除** - 自動合併相同請求
4. **樂觀更新** - 提升使用者體驗
5. **離線支援** - 網路恢復時自動重試
6. **DevTools** - 強大的除錯工具

## 最佳實踐

1. 統一的錯誤處理
2. 適當的 Loading UI
3. 請求攔截器的使用
4. API 配置的集中管理
5. 環境變數管理

## 相關資源

- [Fetch API - MDN](https://developer.mozilla.org/zh-TW/docs/Web/API/Fetch_API)
- [Axios 官方文件](https://axios-http.com/)
- [TanStack Query 官方文件](https://tanstack.com/query/latest)
- [OpenWeatherMap API](https://openweathermap.org/api)
