# Webpack 基本概念

**Webpack** 是一個**模組打包工具 (Module Bundler)**。它將多個模組（包括 JavaScript、CSS、圖片等）及其依賴關係打包成瀏覽器可以理解的靜態資源。在 Vite 等新一代工具出現之前，Webpack 是最主流的前端打包工具。

## 1. 為什麼需要 Webpack？

*   **模組化**：瀏覽器不原生支援 CommonJS 或 ES Modules (舊瀏覽器)，Webpack 將它們轉譯。
*   **相容性**：將 ES6+ 語法轉換為舊版瀏覽器能理解的 ES5。
*   **優化**：壓縮程式碼、圖片，移除未使用的程式碼 (Tree Shaking)，提高載入速度。
*   **資源管理**：統一管理各種資源類型 (JS, CSS, 圖檔, 字型)。
*   **開發體驗**：熱模組替換 (HMR)、開發伺服器。

## 2. Webpack 的核心概念

### (1) Entry (入口)
指示 Webpack 從哪個檔案開始建構其內部依賴圖。

### (2) Output (輸出)
指示 Webpack 在哪裡輸出建構後的 bundle 檔案，以及如何命名這些檔案。

### (3) Loader (載入器)
Webpack 自身只能理解 JavaScript 和 JSON 檔案。Loader 讓 Webpack 能夠處理其他類型的檔案，將它們轉換為有效的模組，然後添加到依賴圖中。

*   **範例**：`css-loader` 處理 CSS 檔案，`babel-loader` 將 ES6+ 轉譯為 ES5。

### (4) Plugin (插件)
Plugin 可以執行更廣泛的任務，從打包優化和資產管理到環境變數注入。Loader 專注於將模組轉換，而 Plugin 則可以處理**打包過程的任何階段**。

*   **範例**：`HtmlWebpackPlugin` 自動生成 HTML 檔案並引入打包後的 JS，`CleanWebpackPlugin` 清理舊的建構檔案。

### (5) Mode (模式)
Webpack 4 引入了 `mode` 選項，用於指定環境。
*   `development`: 提供快速建構和除錯工具。
*   `production`: 啟用各種優化功能，例如程式碼壓縮。

## 3. 基本配置 (`webpack.config.js`)

一個簡單的 Webpack 配置檔案可能如下所示：

```javascript
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');

module.exports = {
  mode: 'development', // 或 'production'
  entry: './src/index.js', // 入口點
  output: {
    filename: 'bundle.[contenthash].js', // 輸出檔案名，加 hash 防止快取
    path: path.resolve(__dirname, 'dist'), // 輸出路徑
    publicPath: '/'
  },
  module: {
    rules: [
      {
        test: /\.css$/, // 匹配 .css 檔案
        use: ['style-loader', 'css-loader'], // 使用 loader 處理
      },
      {
        test: /\.js$/,
        exclude: /node_modules/, // 排除 node_modules
        use: {
          loader: 'babel-loader', // 使用 Babel 轉譯 JS
          options: {
            presets: ['@babel/preset-env']
          }
        }
      }
    ],
  },
  plugins: [
    new CleanWebpackPlugin(), // 清理 dist 資料夾
    new HtmlWebpackPlugin({
      template: './src/index.html', // 使用模板生成 HTML
      filename: 'index.html',
    }),
  ],
  devServer: {
    static: {
      directory: path.join(__dirname, 'dist'),
    },
    compress: true,
    port: 9000,
    open: true, // 自動開啟瀏覽器
  },
};
```

## 4. 運行 Webpack

在 `package.json` 中設定 scripts：

```json
{
  "scripts": {
    "start": "webpack serve --open", // 開發模式，啟動開發伺服器
    "build": "webpack"               // 生產模式，打包專案
  },
  "devDependencies": {
    "webpack": "^5.0.0",
    "webpack-cli": "^4.0.0",
    "webpack-dev-server": "^4.0.0",
    "html-webpack-plugin": "^5.0.0",
    "clean-webpack-plugin": "^4.0.0",
    "css-loader": "^6.0.0",
    "style-loader": "^3.0.0",
    "@babel/core": "^7.0.0",
    "@babel/preset-env": "^7.0.0",
    "babel-loader": "^8.0.0"
  }
}
```

然後在終端機執行：

```bash
npm install # 安裝依賴
npm run build # 打包
npm run start # 開發
```
