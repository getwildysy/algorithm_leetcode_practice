# API 串接範例

這裡示範如何串接一個真實的公開 API：GitHub API。

## 目標
取得指定 GitHub 使用者的公開資訊。

## 程式碼

```python
import requests

def get_github_user(username):
    url = f"https://api.github.com/users/{username}"
    
    try:
        response = requests.get(url)
        
        # 檢查狀態碼
        if response.status_code == 200:
            user_data = response.json()
            return {
                "name": user_data.get("name"),
                "bio": user_data.get("bio"),
                "followers": user_data.get("followers"),
                "public_repos": user_data.get("public_repos"),
                "url": user_data.get("html_url")
            }
        elif response.status_code == 404:
            print("錯誤：找不到該使用者")
        else:
            print(f"錯誤：API 回傳狀態碼 {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"連線錯誤: {e}")
    
    return None

# 測試
username = "octocat" # GitHub 的吉祥物帳號
info = get_github_user(username)

if info:
    print("=== 使用者資訊 ===")
    print(f"名稱: {info['name']}")
    print(f"簡介: {info['bio']}")
    print(f"追隨者: {info['followers']}")
    print(f"連結: {info['url']}")
```
