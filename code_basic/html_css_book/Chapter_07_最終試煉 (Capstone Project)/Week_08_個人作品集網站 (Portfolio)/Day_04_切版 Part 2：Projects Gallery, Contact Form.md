# Day 4: 切版 Part 2：Projects Gallery, Contact Form

今天我們要完成網站的下半部：展示你的實力 (作品) 與讓客戶找到你 (聯絡)。

## 1. Projects Gallery (CSS Grid)

這裏我們要用力秀肌肉。使用 CSS Grid 做出 RWD 卡片牆。

```html
<section id="projects" class="section">
    <h2 class="section-title">My Work</h2>
    <div class="grid-gallery">
        <!-- Card 1 -->
        <article class="project-card">
            <img src="project1.jpg" alt="Project 1">
            <div class="card-content">
                <h3>E-commerce Site</h3>
                <p>A full-stack shop built with React & Node.</p>
                <div class="tags">
                    <span>React</span><span>Node</span>
                </div>
            </div>
        </article>
        <!-- Card 2... -->
    </div>
</section>
```

```scss
.grid-gallery {
    display: grid;
    // 魔法語法：自動填滿，每張卡片最窄 300px
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}

.project-card {
    background: white;
    border-radius: 8px;
    overflow: hidden;
    transition: transform 0.3s ease;
    
    &:hover {
        transform: translateY(-5px); // 浮動效果
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    
    img {
        width: 100%;
        height: 200px;
        object-fit: cover;
    }
}
```

## 2. Contact Form

別忘了我們學過的 Input 樣式與 `:focus` 狀態。

```scss
.contact-form {
    max-width: 500px;
    margin: 0 auto;
    
    input, textarea {
        width: 100%;
        padding: 12px;
        margin-bottom: 1rem;
        border: 1px solid #ddd;
        border-radius: 4px;
        transition: border-color 0.3s;
        
        &:focus {
            outline: none;
            border-color: $primary-color;
            box-shadow: 0 0 0 3px rgba($primary-color, 0.1);
        }
    }
    
    button {
        width: 100%;
        padding: 12px;
        background: $primary-color;
        color: white;
        border: none;
        cursor: pointer;
        
        &:hover { background: darken($primary-color, 10%); }
    }
}
```
