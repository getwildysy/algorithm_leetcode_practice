# 模組化 (Modules): import 與 export

在 ES6 之前，JavaScript 沒有內建的模組系統，開發者通常依賴 `<script>` 標籤或第三方庫 (如 CommonJS/RequireJS)。ES6 正式引入了標準的模組系統 (ES Modules, ESM)。

模組化的好處：
1.  **封裝**：避免汙染全域命名空間。
2.  **重用**：方便在不同檔案間共用程式碼。
3.  **維護**：依賴關係明確。

## 1. 匯出 (Export)

有兩種主要的匯出方式：**具名匯出 (Named Export)** 和 **預設匯出 (Default Export)**。

### 具名匯出 (Named Export)

一個模組可以有多個具名匯出。匯入時必須使用相同的名稱（需加花括號）。

```javascript
// math.js

// 方式 1: 直接在宣告前匯出
export const PI = 3.14;

export function add(a, b) {
    return a + b;
}

// 方式 2: 集中匯出
const subtract = (a, b) => a - b;
export { subtract };
```

### 預設匯出 (Default Export)

一個模組只能有一個預設匯出。通常用於匯出該模組的主要功能（如一個 Class 或一個元件）。匯入時可以使用任意名稱（不加花括號）。

```javascript
// User.js
export default class User {
    constructor(name) {
        this.name = name;
    }
}
```

## 2. 匯入 (Import)

### 匯入具名匯出

必須使用解構語法 `{}`，名稱需匹配。可以使用 `as` 重新命名。

```javascript
// main.js
import { PI, add, subtract as sub } from './math.js';

console.log(add(PI, 1));
```

### 匯入預設匯出

不需要花括號，可以自訂名稱。

```javascript
// main.js
import MyUser from './User.js'; // MyUser 對應 default export

const u = new MyUser("Alice");
```

### 混合匯入

```javascript
import MyUser, { PI } from './someModule.js';
```

### 匯入所有內容 (Namespace Import)

將模組的所有匯出收集到一個物件中。

```javascript
import * as MathUtils from './math.js';

console.log(MathUtils.add(1, 2));
console.log(MathUtils.PI);
```

## 3. 在瀏覽器中使用

如果在瀏覽器中直接使用 ES Modules，`<script>` 標籤必須加上 `type="module"`。

```html
<script type="module" src="main.js"></script>
```

注意事項：
*   使用 `type="module"` 的腳本會自動處於**嚴格模式**。
*   它們會**延遲執行** (類似 `defer`)。
*   必須透過伺服器 (HTTP/HTTPS) 載入，不能直接開啟檔案 (file://)，否則會有 CORS 錯誤。
