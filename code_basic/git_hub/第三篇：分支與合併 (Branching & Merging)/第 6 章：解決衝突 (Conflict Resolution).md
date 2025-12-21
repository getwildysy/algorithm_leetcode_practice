# 第 6 章：解決衝突 (Conflict Resolution)

## 6.1 衝突 (Conflict) 是怎麼發生的？

許多新手對「衝突」感到恐懼，但它其實是多人協作中**極其正常**甚至**無法避免**的事情。

當 Git 進行合併 (Merge) 時，它通常很聰明，能自動把不同人的修改組合在一起。但有一種情況 Git 無法決定：
**「當兩個人修改了『同一個檔案』的『同一行』程式碼，而且內容不一樣時。」**

```mermaid
graph TD
    Base[共同祖先: 顏色=黑色]
    
    BranchA[分支 A: 改成紅色]
    BranchB[分支 B: 改成藍色]
    
    Base --> BranchA
    Base --> BranchB
    
    BranchA --> Merge((合併衝突!!))
    BranchB --> Merge
    
    note right of Merge: Git: 我該用紅色還是藍色？\n你來決定！
```

---

## 6.2 衝突解剖學 (Anatomy of a Conflict)

當你執行 `git merge` 後，如果發生衝突，Git 會暫停並把檔案變成這樣子。請看懂這些符號的意義：

```text
<<<<<<< HEAD (Current Change)
    color: red;
=======
    color: blue;
>>>>>>> feature/blue-theme (Incoming Change)
```

| 符號 | 意義 | 來源 |
| :--- | :--- | :--- |
| **`<<<<<<< HEAD`** | **開始標記** | 你目前所在的分支 (Receiver) |
| `color: red;` | **衝突內容 A** | 你原本寫的程式碼 |
| **`=======`** | **分隔線** | 分隔楚河漢界 |
| `color: blue;` | **衝突內容 B** | 準備合併進來的程式碼 |
| **`>>>>>>> branch`** | **結束標記** | 對方的分支名稱 (Input) |

---

## 6.3 解決衝突 SOP

解決衝突的步驟非常固定：

1.  **手動修改檔案**：
    打開衝突的檔案，決定你要保留哪一段程式碼。
    *   **選項 A (Accept Current)**：只留紅色。
    *   **選項 B (Accept Incoming)**：只留藍色。
    *   **選項 C (Accept Both)**：改成 `linear-gradient(red, blue)` (兩個都留)。
    *   **最重要的是：把 `<<<<<<<`, `=======`, `>>>>>>>` 這些標記全部刪除！**

2.  **加入暫存區**：
    改好後，像平常一樣操作：
    ```bash
    git add style.css
    ```
    這動作告訴 Git：「我已經解決這個檔案的衝突了 (Marked as resolved)」。

3.  **提交 (Commit)**：
    所有衝突檔案都 add 完後，執行 commit：
    ```bash
    git commit
    ```
    Git 通常會自動幫你填好「Merge branch...」的訊息，你直接儲存離開即可。

---

## 6.4 使用 VS Code 解決衝突 (推薦)

雖然手動刪除符號很硬派，但現代編輯器如 VS Code 提供了非常友善的介面。
當 VS Code 偵測到衝突標記時，會在該行上方出現四個按鈕 (Code Lens)：

![VS Code Conflict UI](https://code.visualstudio.com/assets/docs/editor/versioncontrol/merge-conflict.png)
*(示意圖)*

*   **Accept Current Change**：保留 HEAD 的內容 (你的)。
*   **Accept Incoming Change**：保留對方的內容。
*   **Accept Both Changes**：兩段都留下來。
*   **Compare Changes**：開啟並排視窗 (Diff View) 讓你左右比對。

**建議**：善用 VS Code 的這項功能，點一下按鈕就能自動清除標記並保留程式碼，既快又不容易出錯。

> **預防衝突心法**：
> 1.  Commit 粒度要小：不要累積一個月才 Commit 一次。
> 2.  **勤勞 Pull (Rebase)**：開發前先 Pull 最新的主分支下來 (`git pull --rebase`)，減少與主線脫節的時間。
> 3.  溝通：如果知道同事正在改同一個核心檔案，先講好誰改哪部分，避免撞車。
