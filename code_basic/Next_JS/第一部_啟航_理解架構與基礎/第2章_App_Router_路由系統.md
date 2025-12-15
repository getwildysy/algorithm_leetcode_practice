# 第 2 章：App Router 路由系統 (Routing)

如果說 Component 是房子的磚塊，那 Routing (路由) 就是房子的格局與動線。Next.js 13 的 App Router 採用了直觀的「檔案系統即路由 (File-system Based Routing)」機制。只要你會建立資料夾與檔案，你就學會了一半的路由設定。

## 2.1 檔案即路由：page, layout, template 的職責

在 `app` 資料夾下，每一個**資料夾**代表一個 **URL 路徑片段 (Route Segment)**，而資料夾內的**特殊檔案**則定義了該路徑的行為。

### 核心檔案角色
*   **`page.tsx` (必要)**：該路徑的 UI 進入點。如果一個資料夾沒有 `page.tsx`，該路徑就會回傳 404。
*   **`layout.tsx` (重要)**：該路徑（及其子路徑）的共用版型。
    *   **特性**：切換子頁面時，Layout **不會**重新渲染 (Preserves State)。
    *   **用途**：導航列 (Navbar)、側邊欄 (Sidebar)、Footer。
*   **`template.tsx` (進階)**：類似 Layout，但**每次**切換路徑都會重新掛載 (Remount)。
    *   **用途**：需要重置狀態的功能（如進入頁面時的淡入動畫）。
*   **`not-found.tsx`**：處理 404 錯誤的 UI。

### 範例結構與 URL 對照
```text
app/
├── page.tsx          -> URL: /
├── about/
│   └── page.tsx      -> URL: /about
├── blog/
│   ├── page.tsx      -> URL: /blog
│   └── layout.tsx    -> /blog 下的所有頁面都會套用此版型
└── contact/          -> (沒有 page.tsx) -> URL: /contact 會顯示 404
```

---

## 2.2 動態路由與參數捕捉

網頁應用常需要處理不確定的路徑，例如 `blog/1` 或 `product/abc`。這時候就需要「動態路由」。

### 1. 基本動態路由 `[slug]`
使用中括號 `[]` 包裹資料夾名稱。
*   路徑：`app/blog/[id]/page.tsx`
*   URL：`/blog/123`
*   **如何取得參數**：
    透過 `params` prop 傳入 page 元件。

```tsx
// app/blog/[id]/page.tsx
export default function BlogPost({ params }: { params: { id: string } }) {
  return <h1>正在閱讀文章 ID: {params.id}</h1>;
}
```

### 2. 捕捉所有路由 `[...slug]` (Catch-all Segments)
捕捉該路徑後的所有層級。
*   路徑：`app/docs/[...slug]/page.tsx`
*   URL：`/docs/a` 或 `/docs/a/b` 或 `/docs/a/b/c`
*   參數結果：`params.slug` 會是一個陣列 `['a', 'b', 'c']`。

### 3. 可選捕捉路由 `[[...slug]]` (Optional Catch-all)
加上雙中括號，連「根目錄」本身都能捕捉。
*   路徑：`app/shop/[[...category]]/page.tsx`
*   URL：
    *   `/shop/shoes` -> `params.category = ['shoes']`
    *   `/shop` -> `params.category = undefined` (不會 404，而是顯示此頁)

---

## 2.3 導航與連結：Link 與 useRouter

### `<Link>` 元件
這是 Next.js 提供的超連結元件，取代傳統的 `<a>` 標籤。
```tsx
import Link from 'next/link';

<Link href="/about">關於我們</Link>
```
*   **優點**：SPA 體驗（不會整頁刷新）。
*   **預取 (Prefetching)**：當 `<Link>` 出現在使用者的視口 (Viewport) 中，Next.js 會自動在背景預先下載該頁面的資料。當使用者真正點擊時，頁面幾乎是瞬間切換。

### `useRouter` Hook
如果你需要在程式邏輯中切換頁面（例如表單送出後跳轉），請使用 `useRouter`。
*   ⚠️ **注意**：這是一個 Hook，只能在 Client Component (`'use client'`) 使用。

```tsx
'use client';
import { useRouter } from 'next/navigation';

export default function LoginButton() {
  const router = useRouter();

  return (
    <button onClick={() => router.push('/dashboard')}>
      登入並跳轉
    </button>
  );
}
```

---

## 2.4 路由群組與私有資料夾

有時候我們建立資料夾只是為了「整理程式碼」，不希望影響 URL。

### 1. 路由群組 `(folder)`
將資料夾名稱用小括號包裹，該層級就會被 URL 忽略。
*   結構：
    ```text
    app/
    ├── (marketing)/
    │   ├── about/
    │   │   └── page.tsx  -> URL: /about (marketing 被無視了)
    │   └── contact/
    │   │   └── page.tsx  -> URL: /contact
    └── (shop)/
        └── cart/
            └── page.tsx  -> URL: /cart
    ```
*   **用途**：可以為不同的群組設定不同的 `layout.tsx`！例如行銷頁面跟購物車頁面長得完全不一樣，就可以利用 Route Group 隔開它們的 Layout。

### 2. 私有資料夾 `_folder`
在資料夾前方加底線 `_`，該資料夾及其內容就完全被路由系統無視，無法透過 URL 訪問。
*   用途：存放該功能專屬的元件、Utils、樣式檔。

---

## [範例演練]：打造「多層級部落格」路由系統

我們來練習一個稍微複雜的結構：一個包含側邊欄的部落格系統。

### 目標結構
1.  `/blog`：部落格首頁，顯示文章列表。
2.  `/blog/[slug]`：文章內頁。
3.  **特色**：這兩頁都要有一個共同的側邊欄（顯示分類），但首頁 (`/`) 不要這個側邊欄。

### 實作步驟

1.  建立資料夾 `app/blog`。
2.  在 `app/blog` 內建立 `layout.tsx` (定義側邊欄)：

```tsx
// app/blog/layout.tsx
export default function BlogLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div style={{ display: 'flex', gap: '20px' }}>
      {/* 側邊欄 */}
      <aside style={{ width: '200px', borderRight: '1px solid #ccc', padding: '10px' }}>
        <h3>文章分類</h3>
        <ul>
          <li>技術筆記</li>
          <li>生活隨筆</li>
        </ul>
      </aside>

      {/* 主要內容區 (這裡是 page.tsx 渲染的地方) */}
      <section style={{ flex: 1 }}>
        {children}
      </section>
    </div>
  );
}
```

3.  建立部落格首頁 `app/blog/page.tsx`：

```tsx
// app/blog/page.tsx
import Link from 'next/link';

export default function BlogHome() {
  return (
    <div>
      <h1>部落格首頁</h1>
      <ul>
        <li><Link href="/blog/hello-nextjs">Hello Next.js</Link></li>
        <li><Link href="/blog/mastering-routing">精通路由系統</Link></li>
      </ul>
    </div>
  );
}
```

4.  建立文章內頁 `app/blog/[slug]/page.tsx`：

```tsx
// app/blog/[slug]/page.tsx
export default function BlogPost({ params }: { params: { slug: string } }) {
  return (
    <article>
      <h1>文章標題：{params.slug}</h1>
      <p>這裡是可以根據 slug ({params.slug}) 去資料庫抓取的文章內容...</p>
      <hr />
      <a href="/blog">回到列表</a>
    </article>
  );
}
```

### 結果驗證
*   進入 `/blog`：你會先看到左邊的側邊欄，右邊是文章列表。
*   點擊文章進入 `/blog/hello-nextjs`：**側邊欄依然存在且沒有重新閃爍**（這就是 Layout 的威力），只有右邊的內容變成了文章內頁。

這就是 App Router 最迷人的地方：透過巢狀 Layout，輕鬆組建複雜的 UI 結構。
