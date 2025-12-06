# async 與 await

這是 Python 定義協程 (Coroutine) 的關鍵字。

## 1. `async def`

定義一個協程函式。呼叫它不會立即執行，而是回傳一個協程物件。

```python
async def fetch_data():
    return "Data"

coro = fetch_data()
print(coro) # <coroutine object ...>
# print(coro.send(None)) # 手動驅動 (不推薦)
```

## 2. `await`

用於等待一個 Awaitable 物件 (Coroutine, Task, Future) 完成，並取得結果。
`await` 只能在 `async` 函式內部使用。

```python
import asyncio

async def get_result():
    return 42

async def main():
    # 暫停 main 的執行，直到 get_result 完成
    result = await get_result() 
    print(result)

asyncio.run(main())
```

## 3. 在舊版程式碼中呼叫 async

如果你在同步程式碼中需要呼叫非同步函式，必須透過 Event Loop。

```python
# Python 3.7+
asyncio.run(main())

# 舊版寫法
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()
```

## 4. 非同步上下文管理器與迭代器

```python
class AsyncContext:
    async def __aenter__(self):
        print("Entering")
        await asyncio.sleep(0.1)
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        print("Exiting")
        await asyncio.sleep(0.1)

async def main():
    async with AsyncContext() as ctx:
        print("Inside")

# ------------------

async def async_generator():
    for i in range(3):
        await asyncio.sleep(0.1)
        yield i

async def main2():
    async for item in async_generator():
        print(item)
```
