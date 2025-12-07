# Python 常用內建模組

Python 被稱為「自帶電池 (Batteries Included)」的語言，因為它擁有強大的標準函式庫。以下介紹幾個最常用的內建模組。

## 1. `os` - 作業系統介面

用於與作業系統互動，如檔案路徑操作、目錄管理。

```python
import os

# 取得當前工作目錄
print(os.getcwd())

# 列出目錄內容
print(os.listdir('.'))

# 建立目錄
# os.mkdir('new_folder')

# 路徑結合 (跨平台安全)
path = os.path.join('folder', 'subfolder', 'file.txt')
print(path) # Windows: folder\subfolder\file.txt, Linux: folder/subfolder/file.txt

# 檢查檔案是否存在
print(os.path.exists('file.txt'))
```

## 2. `sys` - 系統參數與函式

與 Python 直譯器互動。

```python
import sys

# 取得命令列參數
# python script.py arg1 arg2 -> sys.argv 為 ['script.py', 'arg1', 'arg2']
print(sys.argv)

# 模組搜尋路徑
print(sys.path)

# 終止程式
# sys.exit(0)
```

## 3. `random` - 亂數生成

```python
import random

# 0.0 <= x < 1.0 的浮點數
print(random.random())

# 指定範圍整數 (包含頭尾)
print(random.randint(1, 10)) 

# 從序列中隨機選擇
items = ['apple', 'banana', 'cherry']
print(random.choice(items))

# 打亂序列 (原地修改)
random.shuffle(items)
print(items)

# 隨機抽樣 (不重複)
print(random.sample(range(100), 5))
```

## 4. `math` - 數學函式

```python
import math

print(math.pi)
print(math.ceil(4.2))  # 5 (無條件進位)
print(math.floor(4.8)) # 4 (無條件捨去)
print(math.sqrt(16))   # 4.0
print(math.pow(2, 3))  # 8.0
```

## 5. `datetime` - 日期與時間

```python
from datetime import datetime, timedelta

# 當前時間
now = datetime.now()
print(now)

# 格式化輸出
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# 時間計算
tomorrow = now + timedelta(days=1)
print(tomorrow)
```
