# 陣列搜尋與排序：sort, find, some, every

除了 `map`, `filter`, `reduce` 之外，JavaScript 還提供了一系列強大的陣列操作方法。

## 1. `find()` 與 `findIndex()`

### `find()`
回傳**第一個**符合條件的元素值。如果找不到，回傳 `undefined`。

```javascript
const users = [
    { id: 1, name: 'Alice' },
    { id: 2, name: 'Bob' },
    { id: 3, name: 'Charlie' }
];

const user = users.find(u => u.id === 2);
console.log(user); // { id: 2, name: 'Bob' }
```

### `findIndex()`
回傳**第一個**符合條件的元素的**索引 (Index)**。如果找不到，回傳 `-1`。

```javascript
const index = users.findIndex(u => u.name === 'Charlie');
console.log(index); // 2
```

## 2. `some()` 與 `every()`

這兩個方法回傳布林值 (`true` / `false`)。

### `some()`
檢查是否**至少有一個**元素符合條件。

```javascript
const numbers = [1, 3, 5, 8, 9];
const hasEven = numbers.some(n => n % 2 === 0);
console.log(hasEven); // true (因為有 8)
```

### `every()`
檢查是否**所有**元素都符合條件。

```javascript
const allPositive = numbers.every(n => n > 0);
console.log(allPositive); // true
```

## 3. `sort()` - 排序

`sort()` 會**原地 (In-place)** 對陣列進行排序，也就是說它會**修改原陣列**。

### 預設行為的陷阱
預設情況下，`sort()` 會將元素轉為**字串**並依照 Unicode 編碼位置排序。這對數字排序會造成災難。

```javascript
const nums = [1, 10, 2, 21];
nums.sort(); 
console.log(nums); // [1, 10, 2, 21] (錯了！因為字串 "10" 排在 "2" 前面)
```

### 正確的數字排序
必須傳入一個比較函式 `compareFunction(a, b)`。
*   若回傳負數：a 排在 b 前面
*   若回傳正數：b 排在 a 前面
*   若回傳 0：位置不變

```javascript
// 升序 (由小到大)
nums.sort((a, b) => a - b);
console.log(nums); // [1, 2, 10, 21]

// 降序 (由大到小)
nums.sort((a, b) => b - a);
```

## 4. `includes()`

檢查陣列是否包含某個特定元素，回傳布林值。比 `indexOf() !== -1` 更語意化。

```javascript
const pets = ['cat', 'dog', 'bat'];
console.log(pets.includes('cat')); // true
console.log(pets.includes('at'));  // false
```
