# Day 4: 狀態修飾符 (Hover, Focus, Dark Mode)

在 Tailwind 中，所有也是「條件式」的樣式，都是透過 **Prefix (前綴)** 來達成。這個設計非常優雅且一致。

## 1. 偽類狀態 (Pseudo-classes)

語法：`{modifier}:{utility}`

### Hover (滑鼠懸停)
```html
<button class="bg-blue-500 hover:bg-blue-700 text-white ...">
  Hover me
</button>
```
這代表：預設是 `bg-blue-500`，但當 hover 時變成 `bg-blue-700`。

### Focus (獲得焦點)
通常用在 input 輸入框。
```html
<input class="border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 ...">
```

### Active (按下)
```html
<button class="bg-blue-500 active:bg-blue-800 ...">
  Click me
</button>
```

### Group Hover (父元素懸停時改變子元素)
這是一個常常有人問的情境：當我 hover 在整張卡片 (`group`) 時，卡片裡的標題要變色。

1.  在父元素加 `group`。
2.  在子元素加 `group-hover:{utility}`。

```html
<div class="group border p-4 hover:bg-gray-100">
    <!-- 當外層 hover 時，這裡的文字會變藍色 -->
    <h3 class="font-bold group-hover:text-blue-500">Card Title</h3>
    <p class="group-hover:text-gray-900">Content...</p>
</div>
```

---

## 2. 響應式斷點 (Responsive Customization)

我們在 Week 4 學過 RWD，在 Tailwind 裡這也是一種 Modifier。

| Prefix | Min-Width |
| :--- | :--- |
| `sm:` | 640px |
| `md:` | 768px |
| `lg:` | 1024px |
| `xl:` | 1280px |

```html
<!-- 手機版是直排 (block)，中螢幕以上變橫排 (flex) -->
<div class="block md:flex">
    <div class="div1">...</div>
    <div class="div2">...</div>
</div>
```

---

## 3. Dark Mode (深色模式)

Tailwind 內建深色模式支援。只要在設定檔開啟 `darkMode: 'class'`，就能透過 toggle class 來切換。

```html
<!-- 預設是白色背景，深色模式下變成黑色背景 -->
<div class="bg-white dark:bg-slate-800">
    <h1 class="text-black dark:text-white">Dark Mode Test</h1>
    <p class="text-gray-500 dark:text-gray-400">
        Try toggling the 'dark' class on the HTML tag.
    </p>
</div>
```

要測試 Dark Mode，請在 `<html>` 標籤加上 `class="dark"`：
`<html class="dark">`

---

## 4. 綜合練習

試著解讀這行 Code：
`<button class="w-full md:w-auto bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded dark:bg-green-500">`

1.  寬度：預設全寬 (`w-full`)，平板以上變自動寬 (`md:w-auto`)。
2.  背景：預設藍色，Hover 變深藍，但在 Dark Mode 下是綠色。
3.  外觀：白字、padding、圓角。

這種「把所有邏輯寫在一行 class」的爽感，就是 Tailwind 的魅力。
