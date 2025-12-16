# Day 3: 常用 Utility (Spacing, Typography, Flex)

Tailwind 的 class 命名有很強的規律性。一旦你抓到邏輯，甚至不用查文件就能猜到 class name。

## 1. Spacing (間距)

格式：`{property}-{size}`
*   Property: `m` (Margin), `p` (Padding)
*   Direction: `t` (Top), `b` (Bottom), `l` (Left), `r` (Right), `x` (Left+Right), `y` (Top+Bottom)
*   Size: 數值通常是 `0.25rem` 的倍數。
    *   `1` = 0.25rem (4px)
    *   `4` = 1rem (16px)
    *   `8` = 2rem (32px)

**範例**：
*   `m-4` => `margin: 1rem;`
*   `px-2` => `padding-left: 0.5rem; padding-right: 0.5rem;`
*   `mt-8` => `margin-top: 2rem;`

---

## 2. Typography (文字)

*   **大小**：`text-xs`, `text-sm`, `text-base` (預設), `text-lg`, `text-xl`, `text-2xl`...
*   **粗細**：`font-light`, `font-normal`, `font-bold`...
*   **顏色**：`text-{color}-{shade}`
    *   `text-blue-500`
    *   `text-gray-100` (淺) -> `text-gray-900` (深)
*   **對齊**：`text-center`, `text-right`

---

## 3. Flexbox & Grid

這部分跟標準 CSS 幾乎一樣，只是變短了。

| 標準 CSS | Tailwind Class |
| :--- | :--- |
| `display: flex;` | `flex` |
| `flex-direction: column;` | `flex-col` |
| `justify-content: center;` | `justify-center` |
| `align-items: center;` | `items-center` |
| `flex: 1 1 0%;` | `flex-1` |
| `display: grid;` | `grid` |
| `grid-template-columns: repeat(3, 1fr);` | `grid-cols-3` |
| `gap: 1rem;` | `gap-4` |

---

## 4. 尺寸與背景

*   **寬度**：`w-full` (100%), `w-screen` (100vw), `w-1/2` (50%), `w-4` (1rem)
*   **高度**：`h-full`, `h-screen`, `h-10`
*   **背景色**：`bg-red-500`, `bg-white`, `bg-transparent`

---

## 5. 實作練習

把下面的 HTML 複製去跑跑看：

```html
<!-- 一個置中的藍色按鈕 -->
<div class="flex justify-center mt-10">
    <button class="bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-700">
        Click Me
    </button>
</div>

<!-- 一個雙欄卡片 -->
<div class="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl mt-10">
  <div class="md:flex">
    <div class="md:shrink-0">
      <img class="h-48 w-full object-cover md:h-full md:w-48" src="https://picsum.photos/200/300" alt="Random image">
    </div>
    <div class="p-8">
      <div class="uppercase tracking-wide text-sm text-indigo-500 font-semibold">Case Study</div>
      <a href="#" class="block mt-1 text-lg leading-tight font-medium text-black hover:underline">Finding customers for your start-up</a>
      <p class="mt-2 text-slate-500">Tailwind CSS is amazing once you get used to it.</p>
    </div>
  </div>
</div>
```
