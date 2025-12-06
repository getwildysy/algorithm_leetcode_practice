# 檔案讀取 (Read)

Python 內建的 `open()` 函式用於開啟檔案。

## 1. 基本語法

`open(file, mode='r', encoding=None)`

*   `file`: 檔案路徑。
*   `mode`: 模式。`'r'` (讀取，預設), `'w'` (寫入), `'a'` (追加), `'b'` (二進位)。
*   `encoding`: 編碼。通常指定 `'utf-8'`。

## 2. 使用 `with` 語句 (推薦)

`with` 語句（Context Manager）會自動處理檔案的關閉，即使發生錯誤也能確保檔案被正確關閉。

```python
# 讀取整個檔案
with open('example.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
```

## 3. 逐行讀取

對於大檔案，逐行讀取比較節省記憶體。

```python
with open('example.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip()) # strip() 去除行尾換行符
```

## 4. `readlines()`

將所有行讀取到一個列表中。

```python
with open('example.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines) # ['第一行\n', '第二行\n']
```

## 5. 檔案不存在的處理

讀取不存在的檔案會拋出 `FileNotFoundError`。

```python
try:
    with open('not_exist.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("檔案不存在！")
```
