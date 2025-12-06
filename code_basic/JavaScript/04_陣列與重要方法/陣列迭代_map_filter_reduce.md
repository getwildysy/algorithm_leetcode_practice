# 陣列迭代方法：map, filter, reduce

這是現代 JavaScript (ES6+) 處理陣列資料最核心的三劍客。它們是**高階函式 (Higher-Order Functions)**，且**不會修改原陣列** (Immutable)，而是回傳新結果。

## 1. `map()` - 映射

將陣列中的每個元素傳入 callback 函式處理，並將處理後的結果組成一個**新陣列**回傳。
**長度不變，內容改變。**

```javascript
const numbers = [1, 2, 3, 4];
const doubled = numbers.map(num => num * 2);

console.log(doubled); // [2, 4, 6, 8]
console.log(numbers); // [1, 2, 3, 4] (原陣列不變)
```

應用：物件陣列轉換
```javascript
const users = [
    { id: 1, name: "Alice" },
    { id: 2, name: "Bob" }
];
const names = users.map(user => user.name); // ["Alice", "Bob"]
```

## 2. `filter()` - 過濾

將陣列中的每個元素傳入 callback 檢查，保留回傳 `true` 的元素，組成**新陣列**。
**長度變短 (或不變)，內容不變。**

```javascript
const scores = [85, 40, 90, 55, 70];
const passed = scores.filter(score => score >= 60);

console.log(passed); // [85, 90, 70]
```

應用：刪除特定 ID 的資料
```javascript
const currentUsers = users.filter(user => user.id !== 1);
// 只剩下 id 為 2 的 Bob
```

## 3. `reduce()` - 歸納

將陣列中的所有元素透過一個累加器 (Accumulator) 簡化為**單一值** (數字、字串、物件皆可)。

語法：`arr.reduce(callback(accumulator, currentValue), initialValue)`

### 範例 1：數字加總

```javascript
const nums = [1, 2, 3, 4];

// acc: 累加值, curr: 當前元素
// 0 是初始值 (initialValue)
const sum = nums.reduce((acc, curr) => {
    return acc + curr;
}, 0);

console.log(sum); // 10
```

執行過程：
1.  acc=0, curr=1 -> return 1
2.  acc=1, curr=2 -> return 3
3.  acc=3, curr=3 -> return 6
4.  acc=6, curr=4 -> return 10

### 範例 2：統計出現次數 (進階)

```javascript
const fruits = ["apple", "banana", "apple", "orange", "banana", "apple"];

const count = fruits.reduce((obj, fruit) => {
    if (!obj[fruit]) {
        obj[fruit] = 1;
    } else {
        obj[fruit]++;
    }
    return obj;
}, {}); // 初始值是一個空物件

console.log(count); 
// { apple: 3, banana: 2, orange: 1 }
```

## 4. `forEach()` - 僅遍歷

這不是 functional 方法，它**沒有回傳值** (undefined)，單純用來跑迴圈執行副作用 (Side Effects)，如 `console.log`。

```javascript
const items = ['a', 'b', 'c'];
items.forEach((item, index) => {
    console.log(`${index}: ${item}`);
});
```
> 如果需要轉換資料，請用 `map`；如果需要過濾，請用 `filter`；不要在 `forEach` 裡面做這些事。
