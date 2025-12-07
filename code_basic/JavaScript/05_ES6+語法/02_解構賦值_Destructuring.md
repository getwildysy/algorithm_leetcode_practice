# 解構賦值 (Destructuring Assignment)

解構賦值是一種特殊的語法，可以將陣列中的值或物件中的屬性「拆解」出來，賦值給獨立的變數。這讓資料提取變得非常簡潔。

## 1. 陣列解構 (Array Destructuring)

依照順序將陣列的值賦予變數。

### 基本用法

```javascript
const numbers = [1, 2, 3];
const [a, b, c] = numbers;

console.log(a); // 1
console.log(b); // 2
```

### 跳過元素

使用逗號 `,` 可以跳過不需要的元素。

```javascript
const [first, , third] = numbers;
console.log(first); // 1
console.log(third); // 3
```

### 預設值

如果解構的值是 `undefined`，可以使用預設值。

```javascript
const [x, y = 10] = [5];
console.log(x); // 5
console.log(y); // 10 (使用預設值)
```

### 交換變數

不需要暫存變數即可交換兩個變數的值。

```javascript
let m = 1;
let n = 2;
[m, n] = [n, m];
```

## 2. 物件解構 (Object Destructuring)

依照屬性名稱提取值，與順序無關。

### 基本用法

```javascript
const user = {
    id: 101,
    username: "Alice",
    email: "alice@example.com"
};

const { id, username } = user;
console.log(username); // "Alice"
```

### 重新命名變數

如果想將屬性值賦予不同名稱的變數，使用 `屬性名: 新變數名`。

```javascript
const { username: name, id: userId } = user;
console.log(name); // "Alice"
// console.log(username); // Error: username is not defined
```

### 巢狀解構

解構深層物件。

```javascript
const data = {
    title: "Post",
    meta: {
        author: "Bob",
        views: 100
    }
};

const { meta: { author } } = data;
console.log(author); // "Bob"
```

## 3. 函式參數解構

在函式參數定義時直接解構，這在處理設定物件 (Config Object) 時非常有用。

```javascript
function displayUser({ name, age = 18 }) {
    console.log(`User: ${name}, Age: ${age}`);
}

const person = { name: "Charlie", gender: "M" };
displayUser(person); // User: Charlie, Age: 18
```
