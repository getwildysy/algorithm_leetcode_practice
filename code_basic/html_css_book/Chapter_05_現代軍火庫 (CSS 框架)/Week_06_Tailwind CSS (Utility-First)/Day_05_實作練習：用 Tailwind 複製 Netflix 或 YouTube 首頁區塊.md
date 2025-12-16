# Day 5: 實作練習：用 Tailwind 複製 Netflix 或 YouTube 首頁區塊

今天我們來用 Tailwind 重切一個經典的 Netflix 風格首頁英雄區塊 (Hero Section)。

## 1. 任務目標
1.  **全螢幕背景圖** (Hero Image)。
2.  **漸層遮罩** (Overlay) 讓文字更清晰。
3.  **標題與描述**。
4.  **按鈕群組** (播放、更多資訊)。
5.  **RWD**：手機版字體較小，電腦版字體較大。

---

## 2. 實作程式碼

直接 Copy 這一段 HTML 到你的測試環境 (記得引入 Tailwind CDN)。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <title>Netflix Clone Hero</title>
</head>
<body class="bg-black text-white font-sans">

    <!-- Hero Container -->
    <!-- relative: 為了讓內層 absolute 定位 -->
    <!-- h-screen: 全螢幕高度 -->
    <!-- bg-cover bg-center: 背景圖設定 -->
    <div class="relative h-screen w-full bg-cover bg-center" style="background-image: url('https://assets.nflxext.com/ffe/siteui/vlv3/f841d4c7-10e1-40af-bcae-07a3f8dc141a/f6d7434e-d6de-4185-a6d4-c77a2d08737b/US-en-20220502-popsignuptwoweeks-perspective_alpha_website_small.jpg');">
        
        <!-- Black Gradient Overlay (漸層遮罩) -->
        <!-- 從下往上的黑色漸層，讓底部文字清楚，且跟下方內容銜接 -->
        <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-black/60"></div>

        <!-- Content -->
        <!-- flex & items-center: 垂直置中內容 -->
        <div class="relative z-10 h-full flex items-center px-4 md:px-12">
            <div class="max-w-2xl space-y-4">
                
                <!-- Title -->
                <!-- 手機 4xl, 電腦 6xl -->
                <h1 class="text-4xl md:text-6xl font-black drop-shadow-lg">
                    STRANGER THINGS
                </h1>
                
                <!-- Description -->
                <p class="text-lg md:text-xl text-gray-200 drop-shadow-md line-clamp-3 md:line-clamp-none">
                    When a young boy vanishes, a small town uncovers a mystery involving secret experiments, terrifying supernatural forces, and one strange little girl.
                </p>

                <!-- Buttons -->
                <div class="flex space-x-4 pt-4">
                    <!-- Play Button -->
                    <button class="flex items-center bg-white text-black px-6 py-2 rounded hover:bg-opacity-80 transition font-bold text-lg">
                        <!-- Icon (svg) -->
                        <svg class="w-6 h-6 mr-2" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
                        Play
                    </button>

                    <!-- More Info Button -->
                    <button class="flex items-center bg-gray-500/70 text-white px-6 py-2 rounded hover:bg-gray-500/50 transition font-bold text-lg">
                        <svg class="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                        More Info
                    </button>
                </div>

            </div>
        </div>
    </div>

    <!-- Fake Content Below -->
    <div class="p-8">
        <h2 class="text-2xl font-bold mb-4">Trending Now</h2>
        <div class="flex space-x-4 overflow-x-auto pb-8">
            <div class="w-64 h-36 bg-gray-800 rounded shrink-0"></div>
            <div class="w-64 h-36 bg-gray-800 rounded shrink-0"></div>
            <div class="w-64 h-36 bg-gray-800 rounded shrink-0"></div>
        </div>
    </div>

</body>
</html>
```

使用 Tailwind 做這種 UI 非常快，特別是處理漸層 (`bg-gradient-to-t`) 和 RWD (`md:text-6xl`) 時，完全不需要切換檔案寫 CSS。
