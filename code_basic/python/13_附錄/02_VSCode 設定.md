# VSCode 設定建議

為了讓 Python 開發更順暢，建議進行以下設定。

## 1. `settings.json` (使用者設定)

按下 `Ctrl + ,` 開啟設定，點擊右上角的 "Open Settings (JSON)"。

```json
{
    "editor.formatOnSave": true, // 存檔時自動格式化
    "python.formatting.provider": "black", // 使用 Black 作為格式化工具 (需 pip install black)
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true, // 啟用 Pylint
    "editor.rulers": [88], // 顯示 88 字元長度參考線 (Black 標準)
    "files.autoSave": "onFocusChange" // 切換視窗時自動存檔
}
```

## 2. 推薦擴充套件

除了 Python 核心套件外，推薦安裝：

*   **Pylance**: 提供強大的 Intellisense (自動補全)、型別檢查。
*   **Black Formatter**: 自動排版程式碼，保持風格一致。
*   **isort**: 自動排序 import。
*   **Jupyter**: 讓你在 VS Code 中直接執行 Jupyter Notebook (`.ipynb`)。

## 3. 終端機設定

如果習慣使用 Git Bash (Windows)，可以在設定中搜尋 `terminal.integrated.defaultProfile.windows` 並選擇 `Git Bash`。
