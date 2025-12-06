# 上下文管理器 (Context Manager)

上下文管理器主要用於資源管理，確保在程式碼區塊執行前後自動執行特定的操作（如開啟/關閉檔案、取得/釋放鎖）。最常見的語法是 `with`。

## 1. 使用 `with` 語句

```python
# 自動關閉檔案
with open("test.txt", "w") as f:
    f.write("Hello")
# 離開區塊後，f.close() 會被自動呼叫
```

## 2. 自訂上下文管理器 (Class 實作)

需要實作 `__enter__` 和 `__exit__` 方法。

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Opening file...")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing file...")
        if self.file:
            self.file.close()
        # 如果回傳 True，則會抑制例外
        return False

with FileManager("test.txt", "w") as f:
    f.write("Custom Context Manager")
```

## 3. 使用 `contextlib` (Generator 實作)

使用 `@contextmanager` 裝飾器可以更簡單地建立上下文管理器。

```python
from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    print("Opening...")
    f = open(file, mode)
    try:
        yield f # 這裡暫停，將控制權交給 with 區塊
    finally:
        print("Closing...")
        f.close()

with open_file("test.txt", "w") as f:
    f.write("Hello via contextlib")
```
