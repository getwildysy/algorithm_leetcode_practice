# 網路爬蟲 (Web Scraping): BeautifulSoup & Selenium

當網站沒有提供 API 時，我們可以使用爬蟲技術直接從網頁 HTML 中提取資料。

## 1. 靜態爬蟲: BeautifulSoup (bs4)

適用於伺服器端渲染 (SSR) 的網頁，資料直接包含在 HTML 原始碼中。
需安裝：`pip install beautifulsoup4`

```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 取得標題
    title = soup.title.string
    print(f"標題: {title}")
    
    # 尋找所有連結
    links = soup.find_all("a")
    for link in links:
        print(link.get("href"))
        
    # 透過 CSS Selector 尋找 (類似 jQuery/querySelector)
    # content = soup.select_one(".main-content p")
```

## 2. 動態爬蟲: Selenium

適用於用戶端渲染 (CSR) 的網頁，資料由 JavaScript 動態加載。Selenium 可以模擬真實瀏覽器行為。
需安裝：`pip install selenium` 並下載對應瀏覽器的 Driver (如 ChromeDriver)。

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 初始化瀏覽器 (這裡以 Chrome 為例)
options = webdriver.ChromeOptions()
# options.add_argument("--headless") # 無頭模式 (不顯示視窗)
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://spa-website.com")
    
    # 等待 JS 加載
    time.sleep(3) 
    
    # 尋找元素
    element = driver.find_element(By.CSS_SELECTOR, ".dynamic-data")
    print(element.text)
    
finally:
    driver.quit() # 關閉瀏覽器
```

## 3. 注意事項 (爬蟲禮儀)

1.  **檢查 `robots.txt`**: 確認網站是否允許爬取。
2.  **設定 User-Agent**: 偽裝成瀏覽器，避免被簡單阻擋。
3.  **限制頻率 (Rate Limiting)**: 每次請求間隔一段時間 (如 `time.sleep(1)`)，避免造成伺服器負擔或被封鎖 IP。
4.  **法律問題**: 尊重版權和隱私政策。
