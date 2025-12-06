# requests 模組使用

`requests` 是 Python 最受歡迎的第三方 HTTP 庫，比內建的 `urllib` 更人性化。
需先安裝：`pip install requests`

## 1. 發送 GET 請求

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print(response.status_code) # 200
print(response.text)        # 回傳的字串內容
print(response.json())      # 自動解析 JSON 為 Dict
```

## 2. 發送 POST 請求

```python
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "My Post",
    "body": "Hello World",
    "userId": 1
}

# json=data 會自動設定 Content-Type 為 application/json 並序列化
response = requests.post(url, json=data) 

print(response.status_code) # 201 (Created)
print(response.json())
```

## 3. 傳遞參數 (Query Parameters)

用於 GET 請求，如 `url?key=value`。

```python
params = {"userId": 1}
response = requests.get(url, params=params)
# 實際請求 URL: https://.../posts?userId=1
```

## 4. 自訂 Headers

常用於模擬瀏覽器 (User-Agent) 或 API 認證。

```python
headers = {
    "User-Agent": "Mozilla/5.0",
    "Authorization": "Bearer my_token"
}
response = requests.get(url, headers=headers)
```

## 5. 錯誤處理

```python
try:
    response = requests.get("https://not-exist.com", timeout=3)
    response.raise_for_status() # 如果狀態碼不是 200，拋出 HTTPError
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
```
