# pip 套件管理

`pip` 是 Python 的標準套件管理工具，用於安裝和管理來自 [PyPI (Python Package Index)](https://pypi.org/) 的第三方套件。

## 1. 常用指令

### 安裝套件

```bash
pip install package_name

# 安裝特定版本
pip install package_name==1.0.4

# 安裝大於某版本
pip install "package_name>=1.0"
```

### 升級套件

```bash
pip install --upgrade package_name
```

### 解除安裝

```bash
pip uninstall package_name
```

### 列出已安裝套件

```bash
pip list
```

### 查看套件資訊

```bash
pip show package_name
```

## 2. Requirements 檔案

在專案開發中，我們通常會將專案依賴的所有套件及其版本記錄在 `requirements.txt` 檔案中，以便在其他環境重現。

### 匯出依賴

將當前環境的所有套件輸出到檔案：

```bash
pip freeze > requirements.txt
```

### 安裝依賴

從檔案安裝所有套件：

```bash
pip install -r requirements.txt
```

## 3. 虛擬環境 (Virtual Environments)

為了避免不同專案之間的套件版本衝突，強烈建議為每個專案建立獨立的虛擬環境。

### 使用 `venv` (Python 3 內建)

**1. 建立虛擬環境**
在專案目錄下執行：
```bash
# Windows
python -m venv venv

# macOS/Linux
python3 -m venv venv
```
這會建立一個名為 `venv` 的資料夾。

**2. 啟動虛擬環境**

*   **Windows (cmd)**: `venv\Scripts\activate`
*   **Windows (PowerShell)**: `venv\Scripts\Activate.ps1`
*   **macOS/Linux**: `source venv/bin/activate`

啟動後，命令列前面會出現 `(venv)` 字樣。此時使用 `pip` 安裝的套件只會在這個環境中生效。

**3. 退出虛擬環境**

```bash
deactivate
```
