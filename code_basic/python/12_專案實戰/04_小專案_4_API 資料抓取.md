# 小專案 4：API 資料抓取與儲存

**目標**: 綜合練習 `requests` (網路請求) 和 `json`/`csv` (檔案存取)。
**任務**: 從 JSONPlaceholder API 抓取使用者列表，並將其儲存為 CSV 檔案。

## 程式碼實作

```python
import requests
import csv

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    print(f"正在抓取資料: {url} ...")
    
    try:
        response = requests.get(url)
        response.raise_for_status() # 檢查狀態碼
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"抓取失敗: {e}")
        return []

def save_to_csv(users, filename):
    if not users:
        print("沒有資料可儲存。")
        return

    # 定義 CSV 標頭 (欄位名稱)
    headers = ['id', 'name', 'username', 'email', 'phone', 'website']

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            
            writer.writeheader() # 寫入標頭
            
            for user in users:
                # 提取需要的欄位
                row = {
                    'id': user['id'],
                    'name': user['name'],
                    'username': user['username'],
                    'email': user['email'],
                    'phone': user['phone'],
                    'website': user['website']
                }
                writer.writerow(row)
                
        print(f"資料已成功儲存至 {filename}")
        
    except IOError as e:
        print(f"寫入檔案失敗: {e}")

if __name__ == "__main__":
    users_data = fetch_users()
    if users_data:
        print(f"共取得 {len(users_data)} 筆使用者資料。")
        save_to_csv(users_data, "users.csv")
```
