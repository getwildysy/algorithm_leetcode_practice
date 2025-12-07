# JavaScript 控制流程：if, switch, loop

控制流程決定了程式碼執行的順序。JavaScript 提供了多種條件判斷和迴圈結構，讓程式能根據情況執行不同的邏輯。

## 1. 條件判斷 (Conditional Statements)

### if, else if, else

這是最基本的條件判斷語句。

```javascript
let score = 85;

if (score >= 90) {
    console.log("優秀");
} else if (score >= 60) {
    console.log("及格");
} else {
    console.log("不及格");
}
```

### switch

當需要針對同一個變數的多個特定值進行判斷時，`switch` 通常比多個 `else if` 更整潔且效能稍好。

```javascript
let day = 3;
let dayName;

switch (day) {
    case 1:
        dayName = "星期一";
        break; // 重要：記得 break，否則會繼續執行下一個 case (Fall-through)
    case 2:
        dayName = "星期二";
        break;
    case 3:
        dayName = "星期三";
        break;
    default:
        dayName = "未知";
}
console.log(dayName); // 星期三
```

## 2. 迴圈 (Loops)

### for 迴圈

最常用的迴圈，適合已知執行次數的情況。

```javascript
// 語法: for (初始化; 條件; 迭代後操作)
for (let i = 0; i < 5; i++) {
    console.log(`第 ${i} 次執行`);
}
```

### while 迴圈

當條件為 `true` 時重複執行。適合未知執行次數，只知停止條件的情況。

```javascript
let count = 0;
while (count < 3) {
    console.log(count);
    count++; // 別忘了更新條件，否則會變成無窮迴圈
}
```

### do...while 迴圈

類似 `while`，但**保證至少執行一次**，因為條件檢查是在迴圈本體執行後才進行的。

```javascript
let i = 5;
do {
    console.log(i); // 即使條件一開始就不符合，也會印出 5
    i++;
} while (i < 3);
```

### for...of (ES6)

用於遍歷**可迭代物件** (如 Array, String, Map, Set)。直接取得**值 (Value)**。

```javascript
const fruits = ["apple", "banana", "orange"];
for (const fruit of fruits) {
    console.log(fruit);
}
```

### for...in

用於遍歷物件的**屬性鍵 (Key)**。**不建議**用於陣列遍歷。

```javascript
const user = { name: "Alice", age: 25 };
for (const key in user) {
    console.log(`${key}: ${user[key]}`);
}
```

## 3. 迴圈控制：break 與 continue

*   **break**: 立即跳出整個迴圈。
*   **continue**: 跳過本次迭代，直接進入下一次迭代。

```javascript
for (let i = 0; i < 10; i++) {
    if (i === 3) continue; // 跳過 3
    if (i === 6) break;    // 到 6 停下
    console.log(i);
}
// 輸出: 0, 1, 2, 4, 5
```
