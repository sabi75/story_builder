# Children's Story Generator

A Python app that generates original, child-safe stories for ages 7-10 using AI via OpenRouter with multiple affordable LLM models (Grok, DeepSeek, Mistral, GPT-4O Mini, Qwen).

## Features

✨ **Multi-Model Support**
- Choose between 5 different LLM models
- Grok, DeepSeek, Mistral 7B, GPT-4O Mini, Qwen
- Compare costs and quality before generating

✨ **Interactive Story Creation**
- User-friendly prompts for story parameters
- Customizable story length (short/medium/long)
- Multiple genre options (fantasy, adventure, bedtime, educational, mystery)
- Selectable moral lessons (kindness, honesty, teamwork, courage, friendship, creativity)
- Flexible character count

📖 **Story Specifications**
- Age-appropriate content (7-10 years old)
- Simple vocabulary and sentence structure
- Playful and imaginative tone
- Safe, positive, no violence or scary elements
- Clear beginning, middle, and happy ending
- Natural integration of moral lessons

💾 **Save & Export**
- Save generated stories to text files
- Clean formatting for easy reading

## Installation

1. **Install Python 3.8+** from [python.org](https://www.python.org/)

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up OpenRouter API key:**
   - Get your API key from [OpenRouter.ai](https://openrouter.ai/)
   - Sign up for a free account
   - Copy your API key from your dashboard
   - Set environment variable:
     ```bash
     # Windows PowerShell
     $env:OPENROUTER_API_KEY = "your-api-key-here"
     
     # Windows Command Prompt
     set OPENROUTER_API_KEY=your-api-key-here
     
     # Linux/Mac
     export OPENROUTER_API_KEY=your-api-key-here
     ```

## Usage

Run the application:
```bash
python story_generator.py
```

**Step 1: Choose Your AI Model**
```
1. Grok (X's AI - fast, creative)
2. DeepSeek (Chinese model - very cheap)
3. Mistral 7B (Default - balanced)
4. GPT-4O Mini (OpenAI - best quality)
5. Code Fast/Qwen (Ultra-fast, budget)
```

**Step 2: Follow the interactive prompts** to:
1. Enter your story idea/theme
2. Choose story length
3. Select genre
4. Pick a moral lesson
5. Specify number of characters

The app will generate a complete story with:
- **Title**: Creative, child-friendly name
- **Story Overview**: 2-3 sentence summary
- **Characters**: Detailed character descriptions
- **Story**: Full narrative with engaging plot
- **Moral**: Lesson explained simply

## Example Input

- **Story Idea**: "A brave little fox learns to help others"
- **Model**: DeepSeek (most affordable)
- **Length**: Medium (500-700 words)
- **Genre**: Adventure
- **Moral**: Kindness
- **Characters**: 3

## Output

Stories are formatted exactly as specified in the readme.txt file with:
- Age-appropriate language
- Consistent character behavior
- Clear narrative structure
- Positive, safe content
- Meaningful lessons woven naturally into the plot

## Requirements

- Python 3.8 or higher
- Active OpenRouter account with valid API key (free tier available)
- Internet connection

## Model Comparison

| Model | Model ID | Cost | Speed | Quality | Use Case |
|-------|----------|------|-------|---------|----------|
| **Grok** | xai/grok-2 | ~$0.001 | ⚡⚡⚡ | ⭐⭐⭐⭐ | Creative stories |
| **DeepSeek** | deepseek/deepseek-chat | ~$0.0002 | ⚡⚡⚡ | ⭐⭐⭐⭐ | Best value, very cheap |
| **Mistral 7B** | mistralai/mistral-7b-instruct | ~$0.0005 | ⚡⚡⚡ | ⭐⭐⭐⭐ | Balanced default |
| **GPT-4O Mini** | openai/gpt-4o-mini | ~$0.0005-0.001 | ⚡⚡ | ⭐⭐⭐⭐⭐ | Premium quality |
| **Qwen CodeFast** | qwen/qwen-2-7b-instruct | ~$0.0001 | ⚡⚡⚡⚡ | ⭐⭐⭐⭐ | Ultra-fast, budget |

**Cost per Story (approx):**
- 💰 **Cheapest**: Qwen (~$0.0001) 
- 💰 **Great Value**: DeepSeek (~$0.0002)
- 💰 **Balanced**: Mistral 7B (~$0.0005)
- 💸 **Premium**: GPT-4O Mini (~$0.0005-0.001)

## File Structure

```
story_generator.py    # Main application
requirements.txt      # Python dependencies (requests)
USAGE.md             # This file
readme.txt           # Original specifications
```

## Troubleshooting

**"OPENROUTER_API_KEY environment variable not set"**
- Ensure OPENROUTER_API_KEY environment variable is set
- Restart your terminal after setting the variable
- Verify at https://openrouter.ai/keys

**"Connection error"**
- Check your internet connection
- Verify API key is valid at OpenRouter dashboard
- Ensure you have credits/free tier remaining

**"Generation is slow"**
- OpenRouter may queue requests during high load
- Free tier has rate limits
- Consider upgrading to paid tier for priority
- Try a faster model like Qwen

**"Model not found"**
- Verify the model is available at https://openrouter.ai/
- Check for typos in model name
- Some models may require paid account

## Tips for Best Results

1. **Choose the right model**:
   - Budget: Use DeepSeek or Qwen
   - Quality: Use GPT-4O Mini
   - Speed: Use Qwen or Mistral
   - Creativity: Use Grok

2. **Be specific** with story ideas (e.g., "A penguin who discovers ice skating" vs just "ice")

3. **Choose appropriate length** - longer stories allow more character development

4. **Mix genres creatively** - bedtime + adventure creates cozy adventure stories

5. **Combine morals** - most stories naturally teach multiple values

6. **Vary character types** - animals, children, magical creatures, etc.

## Support

For issues or questions about OpenRouter:
- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models List](https://openrouter.ai/)
- [Getting Started Guide](https://openrouter.ai/docs/getting-started)
- [API Reference](https://openrouter.ai/docs/api/chat-completions)

## License

This is a children's story generation tool created for educational purposes.
