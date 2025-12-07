# 檔案寫入 (Write)

## 1. 寫入模式

*   `'w'` (Write): 寫入模式。**會覆蓋**原檔案內容。如果檔案不存在則建立。
*   `'a'` (Append): 追加模式。寫入的內容會加到檔案末尾。
*   `'x'` (Exclusive creation): 獨佔建立。如果檔案已存在則報錯。

## 2. 覆蓋寫入 ('w')

```python
lines = ["Hello\n", "World\n", "Python\n"]

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write("這是一行文字。\n")
    f.writelines(lines) # 寫入列表中的字串
```

## 3. 追加寫入 ('a')

```python
with open('output.txt', 'a', encoding='utf-8') as f:
    f.write("這是追加的文字。\n")
```

## 4. 寫入二進位檔案 ('wb')

例如複製圖片。

```python
# 讀取圖片
with open('image.jpg', 'rb') as source:
    data = source.read()

# 寫入新圖片
with open('image_copy.jpg', 'wb') as dest:
    dest.write(data)
```
