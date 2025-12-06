# 如何使用 VS Code 開發與測試 JavaScript

Visual Studio Code (VS Code) 是一個輕量但功能強大的原始碼編輯器，支援多種程式語言，並內建了許多開發工具，使其成為 JavaScript 開發者的熱門選擇。

## 1. 安裝 VS Code

首先，從 [VS Code 官方網站](https://code.visualstudio.com/) 下載並安裝適合你作業系統的版本。

## 2. 基礎設定與介面概覽

- **編輯器介面**：熟悉側邊欄 (檔案總管、搜尋、原始碼控制、執行與除錯、延伸模組)、編輯器群組、狀態列。
- **設定**：
  - 透過 `檔案(File)` > `喜好設定(Preferences)` > `設定(Settings)` (或使用快捷鍵 `Ctrl+,`) 調整編輯器行為、字體、主題等。
  - 常用的 JavaScript 相關設定：例如自動儲存、ESLint 整合等。

## 3. 重要的延伸模組 (Extensions)

VS Code 的強大之處在於其豐富的延伸模組生態系。以下是一些推薦用於 JavaScript 開發的延伸模組：

- **ESLint**：整合 ESLint，提供即時的語法檢查和風格指南。
- **Prettier - Code formatter**：自動格式化程式碼，保持一致的程式碼風格。
- **Live Server**：對於前端開發，提供一個快速啟動的本地開發伺服器，並支援瀏覽器即時重載。
- **Debugger for Chrome/Edge**：直接在 VS Code 中除錯瀏覽器中的 JavaScript 程式碼。
- **JavaScript (ES6) code snippets**：提供常用的 JavaScript 語法片段，加速開發。
- **Path Intellisense**：自動補齊檔案路徑。

## 4. 執行與除錯 JavaScript 程式碼

VS Code 提供了強大的內建除錯功能。

### 4.1. 執行 Node.js 環境下的 JavaScript

1.  **開啟整合式終端機**：`檢視(View)` > `終端機(Terminal)` (或使用快捷鍵 `Ctrl+` `)。
2.  **執行檔案**：在終端機中輸入 `node your_file_name.js`。

### 4.2. 除錯 Node.js 程式碼

1.  **設定斷點 (Breakpoints)**：在你想暫停程式碼執行的行號旁點擊，會出現一個紅點。
2.  **啟動除錯**：
    - 點擊側邊欄的「執行與除錯」圖示 (蟲子圖示)。
    - 點擊「執行並除錯 JavaScript 文件」或配置 `launch.json`。
    - `launch.json` 允許你為專案設定詳細的除錯組態，例如指定啟動檔案、傳遞參數等。
      ```json
      // .vscode/launch.json 範例
      {
        "version": "0.2.0",
        "configurations": [
          {
            "type": "node",
            "request": "launch",
            "name": "Launch Program",
            "skipFiles": ["<node_internals>/**"],
            "program": "${workspaceFolder}/your_main_file.js" // 你的主程式檔案
          }
        ]
      }
      ```
3.  **除錯操作**：
    - **繼續 (Continue)**：`F5`，執行到下一個斷點或程式結束。
    - **逐步執行 (Step Over)**：`F10`，執行當前行並跳到下一行，不進入函數內部。
    - **進入函數 (Step Into)**：`F11`，進入當前行呼叫的函數內部。
    - **跳出函數 (Step Out)**：`Shift+F11`，從當前函數跳出。
    - **重新啟動 (Restart)**：`Ctrl+Shift+F5`。
    - **停止 (Stop)**：`Shift+F5`。
4.  **監看變數 (Watch)**、**呼叫堆疊 (Call Stack)**、**變數 (Variables)** 視窗：在除錯時觀察變數的值、函數呼叫的順序。

### 4.3. 除錯瀏覽器中的 JavaScript 程式碼 (前端)

這通常需要安裝上述推薦的「Debugger for Chrome/Edge」延伸模組。

1.  **安裝延伸模組**。
2.  **配置 `launch.json`**：新增一個類型為 `chrome` 或 `msedge` 的配置。
    ```json
    // .vscode/launch.json 範例 (除錯 Chrome)
    {
      "version": "0.2.0",
      "configurations": [
        {
          "type": "chrome",
          "request": "launch",
          "name": "Launch Chrome against localhost",
          "url": "http://localhost:3000", // 你的前端應用程式位址
          "webRoot": "${workspaceFolder}"
        }
      ]
    }
    ```
3.  **啟動你的前端應用程式** (例如使用 Live Server 或其他開發伺服器)。
4.  **在 VS Code 中啟動除錯**，VS Code 會開啟一個新的瀏覽器視窗並連接到除錯器。
5.  **設定斷點並進行除錯操作**，與 Node.js 除錯類似。

## 5. 整合式終端機 (Integrated Terminal)

VS Code 內建了終端機，可以直接在編輯器內執行命令，例如 npm/yarn 命令、Git 命令等。

- **開啟**：`Ctrl+` `
- **多個終端機**：可以開啟多個終端機實例，並在它們之間切換。

## 6. 版本控制 (Git Integration)

VS Code 對 Git 有深度整合。

- **原始碼控制視圖**：側邊欄的第三個圖示，可以查看變更、暫存、提交、拉取/推送等。
- **Git 命令**：也可以直接在整合式終端機中使用 Git 命令。

透過這些功能和工具，VS Code 為 JavaScript 開發提供了一個高效且友善的環境。
