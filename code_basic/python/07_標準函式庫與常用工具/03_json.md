# JSON 資料處理

JSON (JavaScript Object Notation) 是現代網路資料交換最常用的格式。Python 的 `json` 模組提供了簡單的 API 來解析和生成 JSON。

## 1. Python 物件轉 JSON (Encoding/Serialization)

使用 `json.dumps()` (轉字串) 或 `json.dump()` (轉檔案)。

```python
import json

data = {
    "name": "Alice",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science"],
    "address": None
}

# 轉為 JSON 字串
# indent=4 用於美化輸出 (Pretty Print)
# ensure_ascii=False 允許輸出非 ASCII 字元 (如中文)
json_str = json.dumps(data, indent=4, ensure_ascii=False)
print(json_str)
```

## 2. JSON 轉 Python 物件 (Decoding/Deserialization)

使用 `json.loads()` (從字串) 或 `json.load()` (從檔案)。

對照表：
*   JSON Object `{}` -> Python Dict
*   JSON Array `[]` -> Python List
*   JSON String `""` -> Python Str
*   JSON Number -> Python Int/Float
*   JSON true/false -> Python True/False
*   JSON null -> Python None

```python
# 從 JSON 字串解析
parsed_data = json.loads(json_str)
print(parsed_data["name"]) # Alice
```

## 3. 檔案操作

```python
# 寫入 JSON 檔案
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

# 讀取 JSON 檔案
with open('data.json', 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)
    print(loaded_data)
```
