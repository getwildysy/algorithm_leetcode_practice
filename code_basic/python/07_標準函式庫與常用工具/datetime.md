# datetime 模組

處理日期和時間是程式開發中的常見需求。

## 1. 取得現在時間

```python
from datetime import datetime, date, time

# 當前日期時間
now = datetime.now()
print(now) # 2023-10-27 15:30:45.123456

# 當前日期
today = date.today()
print(today) # 2023-10-27
```

## 2. 建立特定時間

```python
dt = datetime(2023, 12, 25, 10, 0, 0)
print(dt)
```

## 3. 字串與時間轉換

### `strftime`: 時間 -> 字串 (Format)

```python
# %Y: 年, %m: 月, %d: 日, %H: 時, %M: 分, %S: 秒
formatted = now.strftime("%Y/%m/%d %H:%M")
print(formatted)
```

### `strptime`: 字串 -> 時間 (Parse)

```python
date_str = "2023-12-25"
dt_obj = datetime.strptime(date_str, "%Y-%m-%d")
print(dt_obj)
```

## 4. 時間運算 (`timedelta`)

```python
from datetime import timedelta

now = datetime.now()

# 兩天後
future = now + timedelta(days=2)

# 一週前
past = now - timedelta(weeks=1)

# 時間差
diff = future - now
print(diff.days)       # 2
print(diff.total_seconds())
```

## 5. Timestamp (時間戳記)

```python
ts = now.timestamp() # 轉為 float 秒數
print(ts)

dt = datetime.fromtimestamp(ts) # 轉回 datetime
```
