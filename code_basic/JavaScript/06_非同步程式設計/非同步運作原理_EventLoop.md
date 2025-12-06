# 非同步運作原理：Event Loop (事件循環)

JavaScript 是**單執行緒 (Single-threaded)** 的語言，這意味著它一次只能做一件事。但為什麼它能處理非同步操作（如等待 API 回應時不卡住介面）？答案就是 **Event Loop**。

## 1. 核心組件

### (1) Call Stack (呼叫堆疊)

這是 JS 引擎執行程式碼的地方。函式呼叫會被推進 (Push) 堆疊，執行完後彈出 (Pop)。因為是單執行緒，Stack 一 SS 次只能處理一個函式。

### (2) Web APIs (瀏覽器 API)

瀏覽器提供的功能（非 JS 引擎本身），如 `setTimeout`, `DOM events`, `fetch (AJAX)`。當 Stack 執行到這些指令時，會將任務交給 Web APIs 處理（例如計時），不會阻塞 Stack。

### (3) Callback Queue (Task Queue, 任務佇列)

當 Web APIs 完成任務（如時間到、資料回來了），會將對應的 Callback 函式放入這裡排隊，等待執行。

### (4) Event Loop (事件循環)

這是協調者。它的工作非常簡單且持續進行：
**檢查 Call Stack 是否為空？**

- 如果不為空：繼續等待。
- 如果為空：從 Callback Queue 取出第一個任務，推入 Call Stack 執行。

## 2. 運作流程範例

```javascript
console.log("Start");

setTimeout(() => {
  console.log("Timeout");
}, 0);

console.log("End");
```

**執行順序分析：**

1.  `console.log("Start")` 進入 Stack -> 執行並印出 -> 移出 Stack。
2.  `setTimeout` 進入 Stack -> 呼叫 Web API 設定計時器 (0ms) -> 移出 Stack。
3.  Web API 計時結束，將 callback (() => console.log("Timeout")) 放入 **Queue**。
4.  `console.log("End")` 進入 Stack -> 執行並印出 -> 移出 Stack。
5.  此時 Stack 空了。Event Loop 發現 Queue 有東西，將 callback 推入 Stack。
6.  `console.log("Timeout")` 執行。

**結果：**
Start
End
Timeout

> 注意：即使 setTimeout 設為 0，它也必須排隊，等待所有同步程式碼執行完畢。

## 3. Microtask Queue (微任務佇列)

ES6 引入 Promise 後，多了一個 **Microtask Queue**。它的優先級**高於**一般的 Callback Queue (Macrotask)。

- **Microtasks**: `Promise.then`, `MutationObserver`, `queueMicrotask`
- **Macrotasks**: `setTimeout`, `setInterval`, `setImmediate`, I/O

**規則**：每次 Call Stack 清空後，Event Loop 會**先清空 Microtask Queue 中的所有任務**，然後才執行 Macrotask Queue 中的**一個**任務。

### 進階範例

```javascript
console.log(1);

setTimeout(() => console.log(2), 0);

Promise.resolve().then(() => console.log(3));

console.log(4);
```

**順序：**

1.  同步執行：1, 4
2.  清空 Microtasks：3
3.  執行 Macrotask：2

**結果：** 1 -> 4 -> 3 -> 2
