# 🚀 Quick Start Guide

## Installation

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Get OpenRouter API Key:**
   - Visit https://openrouter.ai/
   - Sign up for free
   - Copy your API key from dashboard

## Running the App

### Option 1: Beautiful Modern Web UI (Recommended) ✨
```bash
streamlit run app.py
```

This launches a beautiful modern web interface at `http://localhost:8501`

**Features:**
- 🎨 Modern, responsive design
- 🖥️ Web-based interface
- 📱 Mobile-friendly
- ⚡ Real-time generation progress
- 💾 Download stories
- 🌓 Dark/Light mode support

### Option 2: Command-Line Interface
```bash
python story_generator.py
```

Terminal-based interface for quick story generation

## Browser First Visit

When you run the Streamlit app:
1. Terminal shows: `You can now view your Streamlit app in your browser.`
2. It opens automatically or go to: `http://localhost:8501`
3. Enter your OpenRouter API key in the sidebar
4. Start creating stories!

## Features

### Web UI (Streamlit) - **RECOMMENDED**
✅ Beautiful modern design
✅ Gradient buttons and cards
✅ 5 tabs: Create, View Story, Help
✅ Real-time progress bar
✅ Model comparison in sidebar
✅ Download stories
✅ Responsive mobile design
✅ Professional appearance

### CLI (Python)
✅ Interactive menus
✅ Same functionality
✅ No graphics/styling

## Model Selection

**In Web UI:**
- Click model buttons: Grok, DeepSeek, Mistral 7B, GPT-4O Mini, Qwen
- See model info in sidebar

**In CLI:**
- Menu numbered 1-5 at start
- Default is Mistral 7B

## Troubleshooting

**"Streamlit not found"**
```bash
pip install streamlit
```

**"Connection refused"**
- Check your OpenRouter API key
- Verify internet connection

**"Port 8501 already in use"**
```bash
streamlit run app.py --server.port 8502
```

**"Module not found"**
```bash
pip install -r requirements.txt
```

## Tips

1. Use the **Web UI** for best experience
2. Keep your API key safe (don't share)
3. Start with DeepSeek for budget-friendly stories
4. Use GPT-4O Mini for premium quality
5. Qwen is fastest if you're in a hurry

## Keyboard Shortcuts (Web UI)

- `C` - Clear cache
- `R` - Rerun
- `S` - Settings

## Files

```
app.py                 # Modern Streamlit web UI
story_generator.py     # CLI version
requirements.txt       # Dependencies
USAGE.md              # Full documentation
README.md             # This file
readme.txt            # Original specifications
```

## Environment Variables (Optional)

```bash
# Windows PowerShell
$env:OPENROUTER_API_KEY = "your-key-here"

# Linux/Mac
export OPENROUTER_API_KEY=your-key-here
```

Then use in code:
```python
import os
api_key = os.getenv("OPENROUTER_API_KEY")
```

## Support

- 📖 [OpenRouter Documentation](https://openrouter.ai/docs)
- 🔑 [Get API Key](https://openrouter.ai/keys)
- 🤖 [Available Models](https://openrouter.ai/)
- 📚 [Streamlit Docs](https://docs.streamlit.io/)

## Next Steps

1. Run: `streamlit run app.py`
2. Enter your API key
3. Create your first story!
4. Download and share with kids

Happy storytelling! 📖✨
