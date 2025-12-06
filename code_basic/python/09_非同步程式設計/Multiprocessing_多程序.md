# 多程序 (Multiprocessing)

多程序適用於 **CPU 密集型 (CPU Bound)** 的任務，例如影像處理、大數據運算。每個 Process 都有獨立的記憶體空間和 Python 直譯器，因此不受 GIL 限制，可以利用多核心 CPU。

## 1. 基本用法

使用 `multiprocessing` 模組。介面與 `threading` 非常相似。

```python
import multiprocessing
import time

def cpu_task(num):
    print(f"Processing {num}")
    result = sum(i * i for i in range(10000000))
    return result

if __name__ == '__main__': # Windows 下必須加這行
    p1 = multiprocessing.Process(target=cpu_task, args=(1,))
    p2 = multiprocessing.Process(target=cpu_task, args=(2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("Finished")
```

## 2. ProcessPoolExecutor (推薦)

```python
from concurrent.futures import ProcessPoolExecutor
import time

def square(n):
    return n * n

if __name__ == '__main__':
    with ProcessPoolExecutor() as executor:
        numbers = [1, 2, 3, 4, 5]
        results = executor.map(square, numbers)
        
        for res in results:
            print(res)
```

## 3. Queue (處理程序間通訊)

由於記憶體不共享，Process 之間通訊需要透過 `Queue` 或 `Pipe`。

```python
from multiprocessing import Process, Queue

def producer(q):
    q.put("Hello")
    q.put("World")

def consumer(q):
    print(q.get())
    print(q.get())

if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()
```

## 4. Threading vs Multiprocessing

| 特性 | Threading (執行緒) | Multiprocessing (程序) |
| :--- | :--- | :--- |
| **適用場景** | I/O 密集型 (爬蟲、API) | CPU 密集型 (計算) |
| **GIL 影響** | 受限 (同一時間僅一核運作) | 不受限 (多核並行) |
| **記憶體** | 共享 (需注意同步) | 獨立 (需序列化通訊) |
| **開銷** | 低 (建立快) | 高 (建立慢，佔記憶體) |
