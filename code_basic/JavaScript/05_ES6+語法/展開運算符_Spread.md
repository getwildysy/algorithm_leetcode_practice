# 展開運算符 (Spread Operator)

展開運算符使用三個點 `...`，它可以將陣列或物件「展開」成個別的元素。這在複製、合併和傳遞參數時非常強大。

## 1. 陣列展開

### 複製陣列 (淺拷貝)

```javascript
const arr1 = [1, 2, 3];
const arr2 = [...arr1]; 

arr2.push(4);
console.log(arr1); // [1, 2, 3] (原陣列不受影響)
```

### 合併陣列

取代舊有的 `concat()` 方法。

```javascript
const part1 = [1, 2];
const part2 = [3, 4];
const combined = [...part1, ...part2]; // [1, 2, 3, 4]

// 也可以插入中間
const middle = [0, ...part1, 2.5, ...part2];
```

### 將陣列轉為函式引數

取代舊有的 `Function.prototype.apply`。

```javascript
const numbers = [5, 10, 15];
console.log(Math.max(...numbers)); // 15
// 等同於 Math.max(5, 10, 15)
```

## 2. 物件展開 (ES2018)

用於複製或合併物件屬性。

### 複製與新增屬性

```javascript
const user = { name: "Alice", age: 25 };
const updatedUser = { 
    ...user, 
    city: "New York" // 新增屬性
};
```

### 合併物件與覆寫

後面的屬性會覆蓋前面的屬性。這常用於更新狀態 (State)。

```javascript
const defaultSettings = { theme: "light", showSidebar: true };
const userSettings = { theme: "dark" };

const finalSettings = { 
    ...defaultSettings, 
    ...userSettings 
};

console.log(finalSettings); 
// { theme: "dark", showSidebar: true }
```

## 3. 剩餘運算符 (Rest Operator)

雖然符號也是 `...`，但當它用在**宣告或定義**的位置時，稱為 Rest，作用是「收集」剩餘的元素變成一個陣列或物件。

### 陣列中的 Rest

```javascript
const [first, ...rest] = [1, 2, 3, 4];
console.log(first); // 1
console.log(rest);  // [2, 3, 4]
```

### 物件中的 Rest

常用於剔除某些屬性。

```javascript
const { password, ...publicData } = { id: 1, name: "Bob", password: "123" };
console.log(publicData); // { id: 1, name: "Bob" }
```
