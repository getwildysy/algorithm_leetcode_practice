# 常用的物件方法 (Object Methods)

JavaScript 的 `Object` 建構函式提供了許多靜態方法，用於操作、遍歷和複製物件。

## 1. 遍歷物件 (Iterating)

### `Object.keys(obj)`
回傳一個包含所有**屬性名稱 (Keys)** 的陣列。

```javascript
const user = { name: "Alice", age: 25, city: "Taipei" };
const keys = Object.keys(user);
console.log(keys); // ["name", "age", "city"]
```

### `Object.values(obj)`
回傳一個包含所有**屬性值 (Values)** 的陣列。

```javascript
const values = Object.values(user);
console.log(values); // ["Alice", 25, "Taipei"]
```

### `Object.entries(obj)`
回傳一個包含 `[key, value]` 陣列的陣列，常用於 `for...of` 迴圈。

```javascript
for (const [key, value] of Object.entries(user)) {
    console.log(`${key}: ${value}`);
}
```

## 2. 複製與合併 (Copying & Merging)

### `Object.assign(target, ...sources)`
將一個或多個來源物件的屬性複製到目標物件。

```javascript
const target = { a: 1 };
const source = { b: 2 };
const result = Object.assign(target, source);

console.log(result); // { a: 1, b: 2 }
// 注意：target 本身也會被修改
```

> **現代寫法**：現在更常用**展開運算符 (Spread Operator)** `...` 來合併物件。
> `const result = { ...target, ...source };`

## 3. 凍結與封裝 (Immutability)

### `Object.freeze(obj)`
**完全凍結**物件。不能新增、刪除或修改屬性。是**淺層 (Shallow)** 的。

```javascript
const obj = { prop: 42 };
Object.freeze(obj);
obj.prop = 33; // 無效 (嚴格模式下會報錯)
console.log(obj.prop); // 42
```

### `Object.seal(obj)`
**密封**物件。不能新增或刪除屬性，但**可以修改**現有屬性的值。

```javascript
const obj = { prop: 42 };
Object.seal(obj);
obj.prop = 33; // 成功修改
delete obj.prop; // 無效
```

## 4. 屬性描述符 (Property Descriptors)

每個屬性都有對應的描述符，控制其行為（如是否可寫、可列舉）。

### `Object.defineProperty(obj, prop, descriptor)`

```javascript
const person = {};
Object.defineProperty(person, "name", {
    value: "John",
    writable: false, // 不可寫入
    enumerable: true, // 可被 for...in 遍歷
    configurable: false // 不可刪除或修改設定
});

person.name = "Doe"; // 無效
console.log(person.name); // "John"
```
