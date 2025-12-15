# 第 3 章：JSX 與 Component 初體驗

## 本章大綱

### 3.1 JSX 不是 HTML：語法規則與防雷區 (className, 閉合標籤)
- [3.1 JSX 不是 HTML：語法規則與防雷區.md](3.1%20JSX%20不是%20HTML：語法規則與防雷區.md)
- JSX 的本質與編譯原理
- 語法規則：駝峰式命名、標籤閉合、Fragment
- 表達式 (Expression) vs 敘述句 (Statement)
- 條件渲染模式 (&&, Ternary)

### 3.2 Component 的思維：如何拆解 UI？原子設計 (Atomic Design) 概念導讀
- [3.2 Component 的思維：如何拆解 UI.md](3.2%20Component%20的思維：如何拆解%20UI.md)
- Component Tree 視覺化
- 原子設計 (Atomic Design) 實例解析
- 單一職責原則與 DRY
- UI 拆解實戰

### 3.3 Props 的傳遞：父子元件溝通的基本功
- [3.3 Props 的傳遞：父子元件溝通的基本功.md](3.3%20Props%20的傳遞：父子元件溝通的基本功.md)
- Props 單向資料流
- 解構賦值 (Destructuring) 與預設值
- Children Prop (插槽模式)
- Spread Props (透傳)

## 實戰演練

**製作一個「個人資訊卡 (Profile Card)」元件，透過 Props 傳入資料**

### 功能需求
- 顯示頭像、姓名、職稱
- 顯示個人簡介
- 支援客製化樣式

### 3.4 練習題與自我測驗
- [3.4 練習題與自我測驗.md](3.4%20練習題與自我測驗.md)
- JSX 觀念測驗
- Props 與 Atomic Design 挑戰

- [ ] 理解 JSX 的語法規則
- [ ] 掌握元件拆分的思維
- [ ] 熟練使用 Props 進行資料傳遞
- [ ] 完成個人資訊卡元件實作

## 範例程式碼

```jsx
// ProfileCard.jsx
function ProfileCard({ name, title, avatar, bio }) {
  return (
    <div className="profile-card">
      <img src={avatar} alt={name} />
      <h2>{name}</h2>
      <p className="title">{title}</p>
      <p className="bio">{bio}</p>
    </div>
  );
}

export default ProfileCard;
```

## 相關資源

- [React - JSX 介紹](https://react.dev/learn/writing-markup-with-jsx)
- [Atomic Design 原文](https://atomicdesign.bradfrost.com/)
