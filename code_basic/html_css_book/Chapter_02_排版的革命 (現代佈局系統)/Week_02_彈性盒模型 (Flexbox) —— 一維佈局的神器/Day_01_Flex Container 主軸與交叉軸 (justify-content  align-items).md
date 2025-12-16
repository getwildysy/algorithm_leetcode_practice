# Day 1: Flex Container 主軸與交叉軸 (justify-content / align-items)

## 1. 什麼是 Flexbox (彈性盒模型)？

Flexbox (Flexible Box Layout) 是 CSS3 推出的排版神氣，專門用來解決「一維佈局」的問題（也就是處理一條線上的排列，不管是橫的還是直的）。

使用 Flexbox 的第一步，就是要在父元素 (Container) 上設下結界：
```css
.container {
    display: flex;
}
```
一旦這行寫下去，所有的子元素 (Items) 就會乖乖變成「Flex Items」，並且預設會「橫向」排列。

---

## 2. 兩個軸線：主軸與交叉軸

要精通 Flexbox，你必須心中有兩條線：

1.  **Main Axis (主軸)**：預設是 **水平方向 (左到右)**。
2.  **Cross Axis (交叉軸)**：預設是 **垂直方向 (上到下)**。

> **注意**：這兩條軸是可以旋轉的！如果設定了 `flex-direction: column`，主軸就會變成垂直的。

---

## 3. 控制主軸：`justify-content`

這個屬性決定了「Flex Items 在主軸 (預設是橫軸) 上如何分佈」。

| 屬性值 | 效果說明 | 示意圖 |
| :--- | :--- | :--- |
| `flex-start` (預設) | 全部靠左 (起點) | `[1][2][3].......` |
| `flex-end` | 全部靠右 (終點) | `.......[1][2][3]` |
| `center` | 居中 | `...[1][2][3]...` |
| `space-between` | 若離若即 (頭尾貼邊，中間均分) | `[1].....[2].....[3]` |
| `space-around` | 兩側留白 (每個 Item 左右留白相等) | `.[1]...[2]...[3].` |
| `space-evenly` | 絕對均分 (所有間距都一樣大) | `..[1]..[2]..[3]..` |

---

## 4. 控制交叉軸：`align-items`

這個屬性決定了「Flex Items 在交叉軸 (預設是縱軸) 上如何對齊」。

| 屬性值 | 效果說明 |
| :--- | :--- |
| `stretch` (預設) | **拉伸**。如果你沒設高度，Item 會自動拉長填滿整個 Container 的高度。 |
| `flex-start` | **靠上對齊**。 |
| `flex-end` | **靠下對齊**。 |
| `center` | **垂直置中** (最常用！)。 |
| `baseline` | **基線對齊** (依照文字底部對齊，適合字體大小不一時使用)。 |

---

## 5. 實作範例：視覺化 Playground

試著把以下程式碼 copy 到你的編輯器，修改 `.container` 的屬性來觀察變化。

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .container {
            display: flex;
            /* 試著修改這裡： */
            justify-content: space-between; 
            align-items: center;
            
            height: 300px;
            border: 5px solid #333;
            background-color: #f0f0f0;
        }

        .box {
            width: 80px;
            /* 沒設 height，測試 align-items: stretch */
            /* height: 80px; */ 
            background-color: #007bff;
            color: white;
            font-size: 2rem;
            
            /* 讓文字在盒子內也置中 */
            display: flex;
            justify-content: center;
            align-items: center;
            
            margin: 5px; /* 為了看清楚邊界 */
        }
        
        .box:nth-child(2) { height: 120px; background-color: #e74c3c; } /* 讓第二個盒子高一點 */
    </style>
</head>
<body>

    <div class="container">
        <div class="box">1</div>
        <div class="box">2</div>
        <div class="box">3</div>
    </div>

</body>
</html>
```

## 6. 小考題
如果我想讓三個方塊「垂直排列」，並且「左右置中」，該怎麼寫？

**答案：**
```css
.container {
    display: flex;
    flex-direction: column; /* 把主軸轉成垂直 */
    align-items: center;    /* 交叉軸 (現在是水平) 置中 */
}
```
這點非常重要：**當 `flex-direction` 改變時，`justify-content` 和 `align-items` 控制的方向也會跟著轉向！**
