# 第 6 章：表單與列表處理

## 本章大綱

### 6.1 列表渲染：key 值的重要性（別再用 index 當 key 了）
- [6.1 列表渲染：key 值的重要性.md](6.1%20列表渲染：key%20值的重要性.md)
- DOM Diffing 與 Key 的關係
- 為什麼不能用 index 當 Key
- 正確的 Key 選擇策略 (UUID vs DB ID)

### 6.2 受控元件 (Controlled Components)：雙向綁定的實作
- [6.2 受控元件：雙向綁定的實作.md](6.2%20受控元件：雙向綁定的實作.md)
- 單一 Input 與多重 Inputs 處理
- Textarea, Select, Checkbox 的特殊處理
- 受控 vs 非受控元件的抉擇

### 6.3 複雜表單處理：簡介 React Hook Form (業界標準)
- [6.3 複雜表單處理：React Hook Form 簡介.md](6.3%20複雜表單處理：React%20Hook%20Form%20簡介.md)
- Uncontrolled Component 效能優勢
- `useForm`, `register`, `handleSubmit` 基本用法
- 整合驗證規則

## 實戰演練

**製作一個「待辦事項清單 (To-Do List)」**

### 功能需求
- 新增待辦事項
- 顯示待辦事項列表
- 標記完成/未完成
- 刪除待辦事項
- 篩選顯示（全部/未完成/已完成）
- 資料持久化（localStorage）

## 學習目標

### 6.4 練習題與自我測驗
- [6.4 練習題與自我測驗.md](6.4%20練習題與自我測驗.md)
- Key 與 List 觀念測驗
- 受控表單實作挑戰

- [ ] 理解列表渲染與 key 的重要性
- [ ] 掌握受控元件的實作方式
- [ ] 熟悉各種表單元素的處理
- [ ] 了解 React Hook Form 的基本用法
- [ ] 完成待辦事項清單實作

## 範例程式碼

```jsx
import { useState } from 'react';

function TodoList() {
  const [todos, setTodos] = useState([]);
  const [inputValue, setInputValue] = useState('');

  const addTodo = () => {
    if (inputValue.trim()) {
      setTodos([
        ...todos,
        {
          id: Date.now(), // 使用時間戳作為唯一 key
          text: inputValue,
          completed: false
        }
      ]);
      setInputValue('');
    }
  };

  const toggleTodo = (id) => {
    setTodos(todos.map(todo =>
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ));
  };

  const deleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  return (
    <div>
      <input
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        onKeyPress={(e) => e.key === 'Enter' && addTodo()}
      />
      <button onClick={addTodo}>新增</button>
      
      <ul>
        {todos.map(todo => (
          <li key={todo.id}>
            <input
              type="checkbox"
              checked={todo.completed}
              onChange={() => toggleTodo(todo.id)}
            />
            <span style={{ textDecoration: todo.completed ? 'line-through' : 'none' }}>
              {todo.text}
            </span>
            <button onClick={() => deleteTodo(todo.id)}>刪除</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
```

## 進階挑戰

1. 加入編輯功能
2. 加入優先級排序
3. 加入到期日期
4. 實作拖曳排序

## 相關資源

- [React - 列表與 Key](https://react.dev/learn/rendering-lists)
- [React - 表單](https://react.dev/reference/react-dom/components/input)
- [React Hook Form 官方文件](https://react-hook-form.com/)
