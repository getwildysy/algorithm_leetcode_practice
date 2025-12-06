# 例外處理：try, except

在程式執行過程中，可能會發生錯誤（如除以零、檔案不存在），這些稱為**例外 (Exceptions)**。如果沒有處理例外，程式會崩潰並停止執行。Python 使用 `try...except` 區塊來捕捉並處理這些錯誤。

## 1. 基本語法

```python
try:
    # 嘗試執行的程式碼 (可能發生錯誤)
    result = 10 / 0
except ZeroDivisionError:
    # 當發生 ZeroDivisionError 時執行
    print("錯誤：不能除以零！")
except ValueError:
    # 當發生 ValueError 時執行
    print("錯誤：數值無效！")
except Exception as e:
    # 捕捉所有其他類型的錯誤，並取得錯誤訊息
    print(f"發生未預期的錯誤: {e}")
```

## 2. 捕捉多個例外

```python
try:
    # ...
    pass
except (TypeError, ValueError):
    print("發生了型別或數值錯誤")
```

## 3. 什麼都不做的 except (不推薦)

```python
try:
    # ...
    pass
except:
    # 捕捉所有錯誤 (包含 SystemExit, KeyboardInterrupt)
    # 這會讓除錯變得很困難
    print("發生錯誤")
```
建議至少使用 `except Exception`。
