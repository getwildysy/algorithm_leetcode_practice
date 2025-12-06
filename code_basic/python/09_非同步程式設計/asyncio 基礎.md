# asyncio 基礎

`asyncio` 是 Python 3.4+ 引入的標準庫，用於編寫**單執行緒併發**程式碼。它基於協程 (Coroutine) 和事件循環 (Event Loop)，是現代 Python 非同步編程的核心。

## 1. 核心概念

*   **Event Loop**: 負責調度及執行任務，監聽 I/O 事件。
*   **Coroutine**: 使用 `async def` 定義的函式，內部可以使用 `await`。
*   **Task**: 被包裝進 Event Loop 執行的 Coroutine。
*   **Future**: 代表一個未來會產生的結果。

## 2. Hello World

```python
import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(1) # 非同步等待 1 秒 (不阻塞)
    print("World")

# 執行 Event Loop (Python 3.7+)
asyncio.run(main())
```

## 3. 並發執行 (gather)

使用 `asyncio.gather` 同時執行多個協程。

```python
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    # 兩個任務同時啟動
    # 總耗時將由最慢的那個決定 (2秒)，而不是 1+2=3秒
    await asyncio.gather(
        say_after(1, 'hello'),
        say_after(2, 'world')
    )

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
```

## 4. 限制

`asyncio` 適用於 I/O 密集型任務。如果在協程中執行耗時的 CPU 計算或使用阻塞的 I/O (如 `time.sleep`, `requests` 模組)，會阻塞整個 Event Loop，導致所有任務卡住。

*   **錯誤**: `time.sleep(1)`
*   **正確**: `await asyncio.sleep(1)`
