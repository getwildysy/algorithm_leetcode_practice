# 多執行緒 (Threading)

多執行緒適用於 **I/O 密集型 (I/O Bound)** 的任務，例如網路爬蟲、檔案讀寫。由於 Python 的 GIL (Global Interpreter Lock)，多執行緒無法利用多核心 CPU 進行平行運算，因此不適合 CPU 密集型任務。

## 1. 基本用法

使用 `threading` 模組。

```python
import threading
import time

def worker(name, delay):
    print(f"{name} started")
    time.sleep(delay)
    print(f"{name} finished")

# 建立執行緒
t1 = threading.Thread(target=worker, args=("Thread-1", 2))
t2 = threading.Thread(target=worker, args=("Thread-2", 1))

# 啟動
t1.start()
t2.start()

# 等待執行緒結束 (Join)
t1.join()
t2.join()

print("All threads finished")
```

## 2. 使用類別繼承

可以繼承 `threading.Thread` 並覆寫 `run` 方法。

```python
class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"{self.name} is running")

t = MyThread("MyThread")
t.start()
```

## 3. 執行緒同步 (Lock)

當多個執行緒同時修改同一個變數時，會發生 Race Condition。使用 `Lock` 來保護臨界區。

```python
counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        # 獲取鎖
        with lock:
            counter += 1
        # 釋放鎖 (with 區塊結束自動釋放)

threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads: t.start()
for t in threads: t.join()

print(counter) # 200000 (如果沒有 lock，結果可能小於 200000)
```

## 4. ThreadPoolExecutor (推薦)

使用 `concurrent.futures` 模組，提供更高階的介面。

```python
from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    time.sleep(1)
    return n * n

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, [1, 2, 3, 4, 5])
    
    for result in results:
        print(result)
```
