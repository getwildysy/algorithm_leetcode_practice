# 實戰演練：使用 Vite 建立第一個 Hello World 專案並解析目錄結構

## 目標

- ✅ 建立你的第一個 React + Vite 專案
- ✅ 理解專案的目錄結構
- ✅ 運行開發伺服器
- ✅ 修改程式碼並看到即時更新

## 步驟 1：建立專案

### 使用 npm

```bash
# 建立新專案
npm create vite@latest hello-react -- --template react

# 進入專案目錄
cd hello-react

# 安裝依賴
npm install

# 啟動開發伺服器
npm run dev
```

### 預期輸出

```bash
$ npm run dev

  VITE v5.0.0  ready in 324 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help
```

## 步驟 2：在瀏覽器開啟

打開瀏覽器，訪問 `http://localhost:5173/`

你應該看到 Vite + React 的歡迎頁面！

## 步驟 3：目錄結構解析

```
hello-react/
├── node_modules/          # 依賴套件（自動產生）
├── public/                # 靜態資源目錄
│   └── vite.svg          # Vite 圖示
├── src/                   # 原始碼目錄
│   ├── assets/           # 資源檔案
│   │   └── react.svg     # React 圖示
│   ├── App.css           # App 元件樣式
│   ├── App.jsx           # App 元件
│   ├── index.css         # 全域樣式
│   └── main.jsx          # 應用程式入口
├── .gitignore            # Git 忽略設定
├── index.html            # HTML 模板
├── package.json          # 專案配置
├── package-lock.json     # 鎖定依賴版本
├── README.md             # 專案說明
└── vite.config.js        # Vite 配置檔
```

### 重要檔案說明

#### `index.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vite + React</title>
  </head>
  <body>
    <div id="root"></div>
    <!-- 注意這裡：模組入口 -->
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
```

**重點**：
- `<div id="root"></div>` - React 掛載點
- `<script type="module">` - ES 模組入口

#### `src/main.jsx`

```jsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

// 將 React 應用掛載到 DOM
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
```

**重點**：
- `ReactDOM.createRoot()` - React 18 的新 API
- `<React.StrictMode>` - 開發模式的額外檢查
- `<App />` - 根元件

#### `src/App.jsx`

```jsx
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
      </div>
    </>
  )
}

export default App
```

#### `package.json`

```json
{
  "name": "hello-react",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",              // 開發伺服器
    "build": "vite build",      // 生產建置
    "preview": "vite preview"   // 預覽建置結果
  },
  "dependencies": {
    "react": "^18.3.1",
    "react-dom": "^18.3.1"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.3.1",
    "vite": "^5.4.2"
  }
}
```

## 步驟 4：修改程式碼

### 任務：建立你的 Hello World

修改 `src/App.jsx`：

```jsx
function App() {
  return (
    <div>
      <h1>Hello World!</h1>
      <p>這是我的第一個 React 應用程式</p>
    </div>
  )
}

export default App
```

**儲存檔案**，瀏覽器會自動更新！這就是 Vite 的熱模組替換（HMR）。

## 步驟 5：體驗 React 的互動性

### 加入狀態管理

```jsx
import { useState } from 'react'

function App() {
  const [name, setName] = useState('世界')

  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <h1>Hello {name}!</h1>
      <input 
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="輸入你的名字"
        style={{ fontSize: '16px', padding: '8px' }}
      />
    </div>
  )
}

export default App
```

**試試看**：
- 在輸入框中輸入文字
- 標題會即時更新
- 這就是 React 的響應式特性！

## 步驟 6：新增樣式

### 修改 `src/App.css`

```css
.container {
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
  text-align: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 10px;
  color: white;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

h1 {
  font-size: 3rem;
  margin-bottom: 20px;
  animation: fadeIn 1s ease-in;
}

input {
  font-size: 1.2rem;
  padding: 12px;
  border: none;
  border-radius: 5px;
  width: 80%;
  max-width: 300px;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

### 更新 `src/App.jsx`

```jsx
import { useState } from 'react'
import './App.css'

function App() {
  const [name, setName] = useState('世界')

  return (
    <div className="container">
      <h1>Hello {name}!</h1>
      <input 
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="輸入你的名字"
      />
    </div>
  )
}

export default App
```

## 步驟 7：生產建置

### 建置專案

```bash
npm run build
```

### 輸出

```bash
vite v5.0.0 building for production...
✓ 34 modules transformed.
dist/index.html                   0.45 kB │ gzip:  0.30 kB
dist/assets/index-abc123.css      1.23 kB │ gzip:  0.65 kB
dist/assets/index-xyz789.js      143.21 kB │ gzip: 46.13 kB
✓ built in 1.42s
```

### 預覽建置結果

```bash
npm run preview
```

## 常用指令總結

```bash
# 開發模式
npm run dev         # 啟動開發伺服器

# 生產建置
npm run build       # 建置生產版本
npm run preview     # 預覽生產版本

# 依賴管理
npm install         # 安裝所有依賴
npm install [套件]  # 安裝新套件
```

## 故障排除

### 問題 1：port 被佔用

```bash
# 錯誤訊息
Port 5173 is in use, trying another one...

# 解決方案：Vite 會自動使用其他 port
# 或者在 vite.config.js 中指定
```

### 問題 2：模組找不到

```bash
# 確保安裝了依賴
npm install

# 清除快取
rm -rf node_modules
npm install
```

## 進階練習

### 練習 1：多個元件

建立 `src/components/Greeting.jsx`：

```jsx
function Greeting({ name }) {
  return <h1>Hello {name}!</h1>
}

export default Greeting
```

在 `App.jsx` 中使用：

```jsx
import Greeting from './components/Greeting'

function App() {
  return (
    <div>
      <Greeting name="Alice" />
      <Greeting name="Bob" />
    </div>
  )
}
```

### 練習 2：按鈕計數器

```jsx
import { useState } from 'react'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>計數: {count}</h1>
      <button onClick={() => setCount(count + 1)}>增加</button>
      <button onClick={() => setCount(count - 1)}>減少</button>
      <button onClick={() => setCount(0)}>重置</button>
    </div>
  )
}
```

## 小結

恭喜！你已經：
- ✅ 成功建立了第一個 React 專案
- ✅ 理解了專案結構
- ✅ 體驗了 Vite 的快速開發
- ✅ 實作了簡單的 React 元件
- ✅ 學會了基本的狀態管理

**下一步**：前往第 2 章，補強 JavaScript 基礎知識！
