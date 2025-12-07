# Python 字典 (Dictionary)

字典 (Dictionary) 是 Python 中用於儲存**鍵值對 (Key-Value Pairs)** 的資料結構。
它是**無序的** (Python 3.7+ 保持插入順序)、**可變的**，且 Key 必須是**唯一**且**不可變**的 (如字串、數字、Tuple)。

## 1. 建立字典

使用大括號 `{}` 或 `dict()`。

```python
# 字面量
person = {
    "name": "Alice",
    "age": 25,
    "city": "Taipei"
}

# 建構式
person2 = dict(name="Bob", age=30)
```

## 2. 存取與修改

```python
# 存取
print(person["name"]) # "Alice"

# 如果 Key 不存在會報錯 (KeyError)
# print(person["email"]) 

# 使用 get() (推薦)
# 如果不存在回傳 None (或預設值)，不會報錯
print(person.get("email"))          # None
print(person.get("email", "N/A"))   # "N/A"

# 新增或修改
person["email"] = "alice@example.com" # 新增
person["age"] = 26                    # 修改
```

## 3. 刪除元素

*   `pop(key)`: 刪除並回傳 Value。
*   `del dict[key]`: 刪除。
*   `popitem()`: 刪除並回傳最後插入的 (Key, Value)。
*   `clear()`: 清空。

```python
email = person.pop("email")
del person["city"]
```

## 4. 遍歷字典

```python
data = {"a": 1, "b": 2, "c": 3}

# 預設遍歷 Key
for key in data:
    print(key, data[key])

# 遍歷 Key
for key in data.keys():
    print(key)

# 遍歷 Value
for value in data.values():
    print(value)

# 遍歷 Key 和 Value (最常用)
for key, value in data.items():
    print(f"{key}: {value}")
```

## 5. 常用方法

*   `update(other_dict)`: 合併字典。
*   `setdefault(key, default)`: 取得 Key 的值，若不存在則設定為 default 並回傳。

```python
defaults = {"theme": "light", "volume": 50}
user_settings = {"volume": 80}

defaults.update(user_settings)
print(defaults) # {'theme': 'light', 'volume': 80}
```
