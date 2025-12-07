# 例外處理：else 與 finally

`try...except` 結構還可以搭配 `else` 和 `finally` 子句。

## 1. `else` 子句

`else` 區塊只有在 **`try` 區塊沒有發生任何例外**時才會執行。它通常用於放置「只有在成功時才需要執行」的程式碼，且這些程式碼本身不應該被 `try` 捕捉。

```python
try:
    num = int(input("輸入一個數字: "))
except ValueError:
    print("這不是有效的數字！")
else:
    print(f"你輸入了: {num}")
    print("轉換成功！")
```

## 2. `finally` 子句

`finally` 區塊**無論是否發生例外都會執行**。它通常用於**清理資源**，如關閉檔案、釋放連線、關閉資料庫等。

```python
try:
    f = open("data.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("檔案找不到")
finally:
    print("執行清理工作...")
    # 這裡需要小心，如果 f 開啟失敗，可能沒有定義 f 變數
    # 實際應用中通常會先檢查 f 是否存在或使用 with 語句
    if 'f' in locals() and not f.closed:
        f.close()
```

## 3. 完整結構

```python
try:
    # 1. 嘗試執行
    pass
except SomeError:
    # 2. 發生錯誤時執行
    pass
else:
    # 3. 沒發生錯誤時執行
    pass
finally:
    # 4. 總是執行
    pass
```
