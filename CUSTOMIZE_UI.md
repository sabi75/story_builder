# 🎨 UI Customization Guide

This guide explains how to customize the beautiful modern UI to match your preferences.

## Quick Start

### Run the App
```bash
streamlit run app.py
```

The web interface opens automatically at `http://localhost:8501`

## Customizing Colors

Edit the CSS section in `app.py` (around line 18):

### Current Color Scheme
```css
--primary-color: #6366f1;        /* Indigo */
--secondary-color: #8b5cf6;      /* Purple */
--success-color: #10b981;        /* Green */
--warning-color: #f59e0b;        /* Orange */
```

### Popular Color Schemes

**1. Ocean Blue Theme**
```css
.header-title {
    background: linear-gradient(135deg, #3b82f6 0%, #06b6d4 100%);
}
.story-card {
    background: linear-gradient(135deg, #3b82f6 0%, #06b6d4 100%);
}
```

**2. Sunset Theme**
```css
.header-title {
    background: linear-gradient(135deg, #f97316 0%, #ec4899 100%);
}
.story-card {
    background: linear-gradient(135deg, #f97316 0%, #ec4899 100%);
}
```

**3. Forest Theme**
```css
.header-title {
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
}
.story-card {
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
}
```

**4. Pink Dream Theme**
```css
.header-title {
    background: linear-gradient(135deg, #ec4899 0%, #f472b6 100%);
}
.story-card {
    background: linear-gradient(135deg, #ec4899 0%, #f472b6 100%);
}
```

## Customizing Fonts

### Header Title Size
```python
# In CSS section, find .header-title
.header-title {
    font-size: 3rem;  # Change this value
    font-weight: 900; # 700-900 for different weights
}
```

### Available Sizes
```
1rem = 16px (small)
2rem = 32px (medium)
3rem = 48px (large) ← Current
4rem = 64px (extra large)
```

## Customizing Layout

### Sidebar Width
The sidebar is controlled by Streamlit. To adjust:

```python
# Add to beginning of app.py
st.set_page_config(
    layout="wide",  # "centered" for narrower, "wide" for wider
)
```

### Column Proportions
Look for lines like:
```python
col1, col2 = st.columns([3, 1])  # 3:1 ratio
# [2, 2] = 1:1 ratio (equal)
# [1, 2, 1] = 1:2:1 ratio
```

## Customizing Buttons

### Button Styling
```css
.stButton > button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 0.75rem 2rem;    # Adjust padding
    border-radius: 8px;       # Adjust corner roundness
    font-weight: 600;         # Adjust font weight
}
```

### Rounded Corners
```css
border-radius: 8px;   /* 0 = sharp, 16 = very round, 50px = pill shape */
```

## Customizing Cards

### Story Card Style
```css
.story-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 2rem;           # Adjust padding
    border-radius: 15px;     # Adjust corners
    box-shadow: 0 8px 16px rgba(0,0,0,0.1);  # Adjust shadow
}
```

### Shadow Depth
```css
/* Subtle shadow */
box-shadow: 0 2px 4px rgba(0,0,0,0.05);

/* Medium shadow */
box-shadow: 0 4px 8px rgba(0,0,0,0.1);

/* Deep shadow */
box-shadow: 0 16px 32px rgba(0,0,0,0.2);
```

## Customizing Messages & Icons

### Change Header Title
```python
st.markdown('<h1 class="header-title">🌟 My Custom Title</h1>', unsafe_allow_html=True)
```

### Change Tab Names
```python
tab1, tab2, tab3 = st.tabs(["🎨 Create", "📖 Read", "❓ FAQ"])
```

### Change Button Labels
```python
st.button("Your Custom Label", use_container_width=True, type="primary")
```

## Customizing Emojis

Current emojis used:
- 📖 Book
- ✨ Sparkles
- 🤖 Robot
- 🎨 Palette
- 🎯 Target
- 📝 Memo
- 🔄 Refresh
- ✅ Check
- ❌ Error

### Change Emojis
Find and replace in `app.py`:
```python
st.markdown("### 📖 Step 1")      # Change 📖 to any emoji
st.button("✨ Generate Story")    # Change ✨ to any emoji
```

[Find emojis here](https://emojipedia.org/)

## Customizing Info Boxes

### Box Colors
```css
/* Blue info box (current) */
.info-box {
    background-color: #dbeafe;
    border-left: 4px solid #3b82f6;
}

/* Green success box (current) */
.success-box {
    background-color: #d1fae5;
    border-left: 4px solid #10b981;
}

/* Red warning box */
.warning-box {
    background-color: #fee2e2;
    border-left: 4px solid #ef4444;
}

/* Yellow caution box */
.caution-box {
    background-color: #fef3c7;
    border-left: 4px solid #f59e0b;
}
```

### Add Custom Box
```python
st.markdown("""
<div class="info-box">
<strong>ℹ️ Your Message Here</strong>
</div>
""", unsafe_allow_html=True)
```

## Customizing Animations

### Hover Effects
```css
.stButton > button:hover {
    transform: translateY(-2px);           /* Move up on hover */
    box-shadow: 0 12px 24px rgba(0,0,0,0.15);
    transition: all 0.3s ease;
}
```

### Animations Available
```css
/* Subtle: translateY(-2px) */
/* Medium: translateY(-5px) */
/* Dramatic: scale(1.05) */
/* Spin: rotate(360deg) */
```

## Advanced Customizations

### Add Custom Font
```python
import streamlit as st

st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap" rel="stylesheet">
    <style>
    body {
        font-family: 'Poppins', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)
```

### Add Background Image
```python
st.markdown("""
    <style>
    .main {
        background-image: url('https://your-image-url.com/image.jpg');
        background-size: cover;
    }
    </style>
""", unsafe_allow_html=True)
```

### Dark Mode Toggle
Streamlit automatically provides this in the settings menu (top right)

## Troubleshooting

### CSS Not Applying?
- Clear browser cache (Ctrl+Shift+Del)
- Restart the app: `streamlit run app.py`
- Check CSS syntax for typos

### Colors Look Different?
- Different browsers render colors differently
- Use hex codes (#RRGGBB) for consistency
- Test on multiple devices

### Layout Broken?
- Check column ratios add up (e.g., [2,2] = 4 total)
- Ensure proper indentation in Python
- Use `st.columns()` for responsive layouts

## Resources

- **Color Picker**: [coolors.co](https://coolors.co/)
- **Gradients**: [gradient.pages.dev](https://gradient.pages.dev/)
- **Fonts**: [fonts.google.com](https://fonts.google.com/)
- **Emojis**: [emojipedia.org](https://emojipedia.org/)
- **Streamlit Docs**: [docs.streamlit.io](https://docs.streamlit.io/)

## Example: Complete Theme Change

To change to a blue theme:

```python
st.markdown("""
    <style>
    .header-title {
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(135deg, #3b82f6 0%, #06b6d4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .story-card {
        background: linear-gradient(135deg, #0ea5e9 0%, #06b6d4 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #06b6d4 100%);
    }
    </style>
""", unsafe_allow_html=True)
```

## Tips for Great Designs

1. **Limit colors to 3-4** for cohesion
2. **Use complementary gradients** for visual interest
3. **Maintain consistent spacing** for professionalism
4. **Test on mobile** for responsiveness
5. **Keep text readable** with good contrast
6. **Use white space** to avoid cluttered UI

Have fun customizing! 🎨✨
