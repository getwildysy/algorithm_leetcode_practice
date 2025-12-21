# 第 8 章：GitHub 社交編碼流程 (Social Coding)

## 8.1 協作模式比較

在 GitHub 上有兩種主要的協作模式，取決於你的權限：

| 模式 | **Shared Repository (團隊模式)** | **Fork & Pull (開源模式)** |
| :--- | :--- | :--- |
| **適用對象** | 公司同事、專案核心成員 | 陌生人、開源貢獻者 |
| **權限** | 大家都有 Write 權限 (直接 Push) | 你沒有原始專案的權限 (不能 Push) |
| **流程** | Clone -> Feature Branch -> PR | **Fork** -> Clone -> Feature Branch -> PR |

本章專注於 **Fork & Pull** 模式，這是開源世界的標準語言。

---

## 8.2 三角形工作流 (The Triangle Workflow)

當你 Fork 別人的專案時，實際上涉及三個端點。搞清楚這三者的關係，你就弄懂了開源貢獻。

```mermaid
graph TD
    Upstream[原始專案 (Upstream)]
    Origin[你的 Fork (Origin)]
    Local[你的電腦 (Local)]
    
    Upstream -.->|Fork| Origin
    Origin -->|git clone| Local
    Local -->|git push| Origin
    Origin -->|Pull Request| Upstream
    
    Upstream -.->|git fetch / pull| Local
    
    style Upstream fill:#f9f
    style Origin fill:#bbf
    style Local fill:#bfb
```

1.  **Upstream (上游)**：原始作者的專案 (例如 Facebook/React)。你**只能讀 (Pull)，不能寫**。
2.  **Origin (你的)**：你 Fork 回來的專案 (例如 YourName/React)。你**擁有完全控制權**。
3.  **Local (本機)**：你電腦裡的程式碼。

---

## 8.3 實戰演練：貢獻開源專案

### 1. 準備工作 (Setup)
```bash
# 1. Clone 你的 Fork
git clone https://github.com/your-name/react.git

# 2. 設定 Upstream (只須做一次)
# 這樣你才能抓到原始作者最新的更新
git remote add upstream https://github.com/facebook/react.git

# 檢查設定
git remote -v
# origin    https://github.com/your-name/react.git (fetch/push)
# upstream  https://github.com/facebook/react.git (fetch/push)
```

### 2. 開發流程 (Loop)
永遠保持一個原則：**從 Upstream 拿最新的 Code，推到 Origin 請求合併**。

```bash
# Step 1: 同步更新 (確保你是最新的)
git checkout main
git pull upstream main

# Step 2: 開分支修 Bug
git checkout -b fix-typo

# Step 3: 修改與提交
git add .
git commit -m "Fix typo"

# Step 4: 推送到「你的」Fork
git push origin fix-typo
```

### 3. 發起 Pull Request (PR)
推上去後，GitHub 頁面會自動提示你 "Compare & pull request"。
這時候你是在對原始作者說：「請把我的 `your-name/fix-typo` 合併進你們的 `facebook/main`」。

---

## 8.4 同步你的 Fork (Syncing a Fork)

這是一般新手最容易卡關的地方：「我 Fork 了一個專案，過了半年它更新了很多，我的 Fork 變得超舊，怎麼辦？」

**千萬不要刪掉重 Fork！** (這樣你會失去所有貢獻紀錄)。請善用 `upstream`。

```bash
# 1. 抓取上游最新資料 (存在 .git 資料庫裡)
git fetch upstream

# 2. 切換回你的主分支
git checkout main

# 3. 合併上游的更新 (這通常是快轉合併)
git merge upstream/main

# 4. 更新你 GitHub 上的 Fork (讓雲端也跟著變新)
git push origin main
```
現在，你的 Local、你的 Origin、以及 Upstream 三者都同步了。
