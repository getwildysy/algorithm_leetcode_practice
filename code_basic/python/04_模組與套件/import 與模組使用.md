# 模組化與 Import

模組 (Module) 是一個包含 Python 定義和語句的檔案（`.py` 檔）。模組化開發有助於組織程式碼，提高可維護性和重用性。

## 1. 基本 Import 用法

假設有一個標準庫模組 `math`。

### (1) 匯入整個模組

```python
import math

print(math.pi)
print(math.sqrt(16))
```

### (2) 匯入特定成員

```python
from math import pi, sqrt

print(pi) # 不需要 math. 前綴
print(sqrt(16))
```

### (3) 給模組取別名 (Alias)

常用於簡化長名稱或避免衝突。

```python
import numpy as np
import pandas as pd
import math as m

print(m.pi)
```

### (4) 匯入所有內容 (不推薦)

```python
from math import *
# 可能會汙染命名空間，覆蓋現有變數
```

## 2. 模組搜尋路徑 (sys.path)

當你 import 一個模組時，Python 會依序在以下位置搜尋：
1.  當前目錄。
2.  `PYTHONPATH` 環境變數中的目錄。
3.  標準函式庫目錄。
4.  site-packages 目錄 (安裝第三方套件的地方)。

可以透過 `sys.path` 查看。

```python
import sys
print(sys.path)
```

## 3. `__name__ == "__main__"`

這是 Python 中常見的慣用寫法。
當一個 Python 檔案被**直接執行**時，`__name__` 變數的值會是 `"__main__"`。
當它被**作為模組匯入**時，`__name__` 的值會是模組名稱。

這允許我們撰寫既可以被匯入使用，又可以作為腳本直接執行的程式碼（通常用於測試）。

```python
# my_module.py

def func():
    print("Function in module")

if __name__ == "__main__":
    print("這段程式碼只有在直接執行 my_module.py 時才會跑")
    func()
```
