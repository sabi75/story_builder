"""
Children's Story Generator UI - Modern Streamlit App
Beautiful web-based interface for generating child-safe stories with multiple LLM models
"""

import streamlit as st
import requests
from datetime import datetime
import json

# Page configuration
st.set_page_config(
    page_title="Children s Story Generator",
    page_icon="BOOK",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://openrouter.ai/docs",
        "Report a bug": "https://github.com/boombook",
        "About": "Childrens Story Generator with AI"
    }
)

# Custom CSS for better styling
st.markdown("""
    <style>
    /* Main background and text colors */
    :root {
        --primary-color: #6366f1;
        --secondary-color: #8b5cf6;
        --success-color: #10b981;
        --warning-color: #f59e0b;
    }
    
    /* Custom card styling */
    .story-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    }
    
    .model-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        cursor: pointer;
        transition: transform 0.3s ease;
    }
    
    .model-card:hover {
        transform: translateY(-5px);
    }
    
    .success-box {
        background-color: #d1fae5;
        border-left: 4px solid #10b981;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .info-box {
        background-color: #dbeafe;
        border-left: 4px solid #3b82f6;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    /* Header styling */
    .header-title {
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(102, 126, 234, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'story' not in st.session_state:
    st.session_state.story = None
if 'model_selected' not in st.session_state:
    st.session_state.model_selected = "3"
if 'generation_complete' not in st.session_state:
    st.session_state.generation_complete = False

# Header
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<h1 class="header-title">Children s Story Generator</h1>', unsafe_allow_html=True)
    st.markdown("**Create magical, child-safe stories powered by AI**")
with col2:
    st.info("Powered by OpenRouter")

st.divider()

# Sidebar for API configuration
with st.sidebar:
    st.markdown("### ⚙️ Configuration")
    
    api_key = st.text_input(
        "🔑 OpenRouter API Key",
        type="password",
        help="Get your API key from https://openrouter.ai/keys",
        placeholder="sk-or-..."
    )
    
    if not api_key:
        st.warning("⚠️ Please enter your OpenRouter API key to continue")
    else:
        st.success("✅ API Key configured")
    
    st.divider()
    st.markdown("### 📊 Model Information")
    
    models_info = {
        "1": {"name": "Grok", "cost": "$0.001", "speed": "⚡⚡⚡", "quality": "⭐⭐⭐⭐"},
        "2": {"name": "DeepSeek", "cost": "$0.0002", "speed": "⚡⚡⚡", "quality": "⭐⭐⭐⭐"},
        "3": {"name": "Mistral 7B", "cost": "$0.0005", "speed": "⚡⚡⚡", "quality": "⭐⭐⭐⭐"},
        "4": {"name": "GPT-4O Mini", "cost": "$0.0005-0.001", "speed": "⚡⚡", "quality": "⭐⭐⭐⭐⭐"},
        "5": {"name": "Qwen CodeFast", "cost": "$0.0001", "speed": "⚡⚡⚡⚡", "quality": "⭐⭐⭐⭐"}
    }
    
    for key, info in models_info.items():
        with st.expander(f"ℹ️ {info['name']}"):
            st.write(f"**Cost:** {info['cost']}/story")
            st.write(f"**Speed:** {info['speed']}")
            st.write(f"**Quality:** {info['quality']}")
    
    st.divider()
    st.markdown("### 💡 Tips")
    st.write("""
    - **Budget?** Use DeepSeek or Qwen
    - **Speed?** Use Qwen or Mistral
    - **Quality?** Use GPT-4O Mini
    - **Creative?** Use Grok
    """)

# Main content area
tab1, tab2, tab3 = st.tabs(["🎨 Create Story", "📚 View Story", "ℹ️ Help"])

with tab1:
    st.markdown("### 🤖 Step 1: Select Your AI Model")
    
    model_cols = st.columns(5)
    models = {
        "1": ("xai/grok-2", "Grok"),
        "2": ("deepseek/deepseek-chat", "DeepSeek"),
        "3": ("mistralai/mistral-7b-instruct", "Mistral 7B"),
        "4": ("openai/gpt-4o-mini", "GPT-4O Mini"),
        "5": ("qwen/qwen-2-7b-instruct", "Qwen")
    }
    
    for idx, (key, (model_id, model_name)) in enumerate(models.items()):
        with model_cols[idx]:
            if st.button(model_name, key=f"btn_{key}", use_container_width=True):
                st.session_state.model_selected = key
    
    # Display selected model
    selected_key = st.session_state.model_selected
    selected_model = models.get(selected_key, models["3"])
    
    st.markdown(f"""
    <div class="info-box">
    <strong>✅ Selected Model:</strong> {selected_model[1]} ({selected_model[0]})
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    st.markdown("### 📖 Step 2: Story Details")
    
    # Two-column layout for better UX
    col1, col2 = st.columns(2)
    
    with col1:
        story_idea = st.text_input(
            "📚 Story Idea or Theme",
            placeholder="e.g., 'A brave penguin', 'Magic in the forest'",
            help="Be specific for better results"
        )
        
        story_length = st.selectbox(
            "📏 Story Length",
            ["short (300-400 words)", "medium (500-700 words)", "long (800-1000+ words)"],
            index=1
        )
        
        genre = st.selectbox(
            "🎭 Genre",
            ["fantasy", "adventure", "bedtime/cozy", "educational", "mystery"],
            index=0
        )
    
    with col2:
        moral = st.selectbox(
            "💡 Moral/Lesson",
            ["kindness", "honesty", "teamwork", "courage", "friendship", "creativity"],
            index=0
        )
        
        num_characters = st.number_input(
            "👥 Number of Characters",
            min_value=1,
            max_value=10,
            value=3,
            step=1
        )
        
        custom_instruction = st.text_area(
            "📝 Optional: Additional Instructions",
            placeholder="Any special requests for the story...",
            height=80
        )
    
    st.divider()
    st.markdown("### 🎯 Step 3: Generate Story")
    
    # Create story button with better styling
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        generate_button = st.button(
            "✨ Generate Story",
            use_container_width=True,
            type="primary"
        )
    
    if generate_button:
        if not api_key:
            st.error("❌ Please enter your OpenRouter API key in the sidebar")
        elif not story_idea:
            st.error("❌ Please enter a story idea")
        else:
            # Show progress
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                status_text.text("🔄 Connecting to OpenRouter...")
                progress_bar.progress(25)
                
                # Prepare prompt
                custom_part = f"\nAdditional instruction: {custom_instruction}" if custom_instruction else ""
                
                prompt = f"""You are an expert children's story writer AI specializing in stories for children aged 7–10.

TASK: Generate a complete, original, child-safe story based on the following parameters:

Story Idea/Theme: {story_idea}
Story Length: {story_length}
Genre: {genre}
Moral/Lesson: {moral}
Number of Characters: {num_characters}{custom_part}

REQUIREMENTS:
- Use simple vocabulary and sentence structure appropriate for ages 7-10 (Grade 2-4)
- Avoid complex words, scary elements, violence, sadness, or danger
- Create memorable, friendly characters with consistent traits
- Maintain a playful and imaginative tone
- Ensure the story teaches the lesson naturally (do not preach)
- Keep all content safe, positive, and age-appropriate
- Do NOT include adult themes, fear, violence, or negativity

OUTPUT FORMAT (STRICT):

Title:
<Creative, child-friendly title>

Story Overview:
<A short 2-3 sentence summary of the story>

Characters:
- Character 1 Name: role, personality, and one defining trait
- Character 2 Name: role, personality, and one defining trait
(Include all characters clearly)

Story:
<Write the full story here in paragraphs>

Moral of the Story:
<One or two simple sentences explaining the lesson>

END OF OUTPUT

Remember: Do NOT add explanations, notes, or commentary. Do NOT mention you are an AI. Ensure smooth flow and consistent character behavior."""
                
                status_text.text("📝 Preparing request...")
                progress_bar.progress(50)
                
                # Call OpenRouter API
                headers = {
                    "Authorization": f"Bearer {api_key}",
                    "HTTP-Referer": "https://github.com/boombook",
                    "X-Title": "Children Story Generator"
                }
                
                payload = {
                    "model": selected_model[0],
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.7,
                    "max_tokens": 1500
                }
                
                status_text.text("🚀 Generating story with AI...")
                progress_bar.progress(75)
                
                response = requests.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    json=payload,
                    headers=headers,
                    timeout=120
                )
                
                if response.status_code == 200:
                    result = response.json()
                    if "error" in result:
                        st.error(f"❌ API Error: {result['error'].get('message', 'Unknown error')}")
                    else:
                        st.session_state.story = result["choices"][0]["message"]["content"]
                        st.session_state.generation_complete = True
                        progress_bar.progress(100)
                        status_text.text("✅ Story generated successfully!")
                        
                        st.success("🎉 Your story is ready! Check the 'View Story' tab to read it.")
                else:
                    st.error(f"❌ Connection failed: {response.status_code}")
                    st.error(response.text)
            
            except requests.exceptions.Timeout:
                st.error("❌ Request timed out. Please try again.")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
            
            finally:
                progress_bar.empty()
                status_text.empty()

with tab2:
    st.markdown("### 📖 Your Generated Story")
    
    if st.session_state.story:
        # Display the story in a nice format
        story_container = st.container()
        
        with story_container:
            st.markdown(f"""
            <div class="story-card">
            {st.session_state.story.replace(chr(10), '<br>')}
            </div>
            """, unsafe_allow_html=True)
        
        # Download button
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            st.download_button(
                label="📥 Download as Text",
                data=st.session_state.story,
                file_name=f"story_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )
        
        with col2:
            if st.button("🔄 Generate New Story"):
                st.session_state.story = None
                st.session_state.generation_complete = False
                st.rerun()
    else:
        st.info("📝 No story generated yet. Go to the 'Create Story' tab to generate one!")

with tab3:
    st.markdown("### 🤔 How to Use")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Getting Started:**
        1. Get API key from [OpenRouter.ai](https://openrouter.ai/)
        2. Enter your API key in the sidebar
        3. Select a model based on your needs
        4. Fill in story details
        5. Click 'Generate Story'
        
        **Tips for Best Results:**
        - Be specific with your story idea
        - Choose appropriate story length
        - Mix genres creatively
        - Use different character types
        """)
    
    with col2:
        st.markdown("""
        **Model Selection:**
        - **Budget?** → DeepSeek or Qwen
        - **Speed?** → Qwen or Mistral
        - **Quality?** → GPT-4O Mini
        - **Creative?** → Grok
        
        **Cost Breakdown:**
        | Model | Cost |
        |-------|------|
        | Qwen | $0.0001 |
        | DeepSeek | $0.0002 |
        | Mistral | $0.0005 |
        | Grok | $0.001 |
        | GPT-4O Mini | $0.0005+ |
        """)
    
    st.divider()
    
    st.markdown("### 📚 Story Requirements")
    st.info("""
    All stories are:
    - ✅ Age-appropriate (7-10 years old)
    - ✅ Simple vocabulary and sentence structure
    - ✅ Playful and imaginative tone
    - ✅ Safe, positive, no violence
    - ✅ Clear beginning, middle, and happy ending
    - ✅ Natural integration of moral lessons
    """)
    
    st.divider()
    
    st.markdown("### 🔗 Resources")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("[📖 OpenRouter Docs](https://openrouter.ai/docs)")
    
    with col2:
        st.markdown("[🔑 Get API Key](https://openrouter.ai/keys)")
    
    with col3:
        st.markdown("[💬 Models List](https://openrouter.ai/)")

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem 0;'>
    <p>✨ <strong>Children's Story Generator</strong> | Powered by OpenRouter & Streamlit</p>
    <p>Create magical stories for children aged 7-10</p>
    <p style='font-size: 0.85rem;'>© 2026 | Educational Use Only</p>
</div>
""", unsafe_allow_html=True)
