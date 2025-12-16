# Day 4: 互動心理學 (按鈕回饋、Skeleton Loading)

動畫不只是為了炫技，更重要的是「回饋感 (Feedback)」與「預期心理 (Perceived Performance)」。

## 1. 按鈕回饋 (Button Feedback)

使用者點擊按鈕時，如果畫面完全沒反應，他會以為當機然後狂按。
好的按鈕應該有三態變化：
1.  **Normal**: 告訴使用者「我是按鈕，可以按」。
2.  **Hover**: 告訴使用者「你瞄準我了」。
3.  **Active**: 告訴使用者「我收到你的點擊了」。

```css
.btn {
    /* Normal */
    background: #007bff;
    transform: scale(1);
    transition: transform 0.1s;
}

.btn:hover {
    /* Hover: 稍微放大或變亮，暗示可點擊 */
    background: #0069d9;
}

.btn:active {
    /* Active: 稍微縮小，模擬按下去的物理質感 */
    transform: scale(0.95);
}
```

---

## 2. 骨架屏 (Skeleton Loading)

當資料還在載入時，不要顯示「Loading...」文字，而是顯示一個「灰色的框框動畫」，讓使用者預期「這裡等一下會有圖片/文字」。這能大幅降低使用者的焦慮感。

### 製作原理
利用 `background-image` 的漸層 + `animation` 移動背景位置。

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        @keyframes shimmer {
            0%   { background-position: -200% 0; }
            100% { background-position: 200% 0; }
        }

        .skeleton {
            background: #eee;
            background-image: linear-gradient(
                90deg, 
                #eee 25%, 
                #f5f5f5 50%, /* 中間比較亮 */
                #eee 75%
            );
            background-size: 200% 100%;
            animation: shimmer 1.5s infinite;
            border-radius: 4px;
        }

        /* 模擬卡片 */
        .card { width: 300px; padding: 20px; border: 1px solid #ddd; }
        .sk-img { width: 100%; height: 200px; margin-bottom: 10px; }
        .sk-title { width: 80%; height: 24px; margin-bottom: 10px; }
        .sk-text { width: 100%; height: 16px; margin-bottom: 5px; }
    </style>
</head>
<body>

    <div class="card">
        <div class="skeleton sk-img"></div>
        <div class="skeleton sk-title"></div>
        <div class="skeleton sk-text"></div>
        <div class="skeleton sk-text"></div>
        <div class="skeleton sk-text" style="width: 60%"></div>
    </div>

</body>
</html>
```
這就是你在 Facebook 或 YouTube 上看到的載入效果。
