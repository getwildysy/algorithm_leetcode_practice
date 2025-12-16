# Day 5: 實作練習：製作一組具備 Hover/Click 動畫的按鈕

今天我們要運用變形 (Transform) 與轉場 (Transition) 來製作一組有質感的 Ghost Button 與 3D Button。

## 1. Ghost Button (幽靈按鈕)

利用 `::before` 偽元素做一個背景滑動的特效。

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .btn-ghost {
            position: relative;
            padding: 12px 24px;
            color: #333;
            border: 2px solid #333;
            background: transparent;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            overflow: hidden; /* 關鍵：藏住跑出去的背景 */
            transition: color 0.4s;
            z-index: 1; /* 確保文字在背景上面 */
        }

        /* 偽元素：原本在左邊很遠的地方 */
        .btn-ghost::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: #333;
            
            /* 將這層黑色背景移到最左邊看不見 */
            transform: translateX(-100%); 
            transition: transform 0.4s ease;
            z-index: -1; /* 放在文字下面 */
        }

        /* Hover 時：文字變白，背景移回來 */
        .btn-ghost:hover {
            color: white;
        }

        .btn-ghost:hover::before {
            transform: translateX(0);
        }
    </style>
</head>
<body>
    <button class="btn-ghost">Hover Me</button>
</body>
</html>
```

---

## 2. 3D Press Button (立體按壓按鈕)

利用 `box-shadow` 的垂直位移來模擬厚度。

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .btn-3d {
            background-color: #ff4757;
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 18px;
            border-radius: 8px;
            cursor: pointer;
            transition: transform 0.1s;
            
            /* 關鍵：利用 solid 陰影做出厚度 */
            box-shadow: 0 5px 0 #c23616; /* 深紅色的厚度 */
            
            /* 按鈕原本要浮起來一點，留給厚度空間 */
            transform: translateY(0);
        }

        .btn-3d:active {
            /* 按下去時：往下移，同時陰影消失 (變成平的) */
            transform: translateY(5px);
            box-shadow: 0 0 0 #c23616;
        }
    </style>
</head>
<body>
    <br><br>
    <button class="btn-3d">Push Meeee</button>
</body>
</html>
```

## 3. 結語
這週我們賦予了網頁生命。你會發現，只要加一點點微動畫，整個網站的質感就會提升一個檔次。

下週是最後一週，我們要把學到的所有技能 (HTML, CSS, Flex, Grid, RWD, Sass, Animation) 全部綜合起來，完成你的畢業作品 (Capstone Project)！
