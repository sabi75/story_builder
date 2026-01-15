"""
Children's Story Generator AI
Generates child-safe, imaginative stories for ages 7-10 based on user input.
Uses OpenRouter API with affordable LLM models.
"""

import requests
import sys
import os

def select_model():
    """Let user select which LLM model to use."""
    print("\n" + "="*60)
    print("CHILDRENS STORY GENERATOR")
    print("="*60)
    print("\n🤖 Select your AI model:\n")
    print("1. Grok (X's AI - fast, creative)")
    print("2. DeepSeek (Chinese model - very cheap)")
    print("3. Mistral 7B (Default - balanced)")
    print("4. GPT-4O Mini (OpenAI - best quality)")
    print("5. Code Fast/Qwen (Ultra-fast, budget)")
    
    model_choice = input("\nChoose 1-5 (default: 3)\n> ").strip() or "3"
    
    models = {
        "1": ("xai/grok-2", "Grok"),
        "2": ("deepseek/deepseek-chat", "DeepSeek"),
        "3": ("mistralai/mistral-7b-instruct", "Mistral 7B"),
        "4": ("openai/gpt-4o-mini", "GPT-4O Mini"),
        "5": ("qwen/qwen-2-7b-instruct", "Qwen Code Fast")
    }
    
    return models.get(model_choice, models["3"])

def get_user_input():
    """Collect story parameters from the user."""
    print("\nWelcome! Let us create a magical story for children ages 7-10.\n")
    
    story_idea = input("What is your story idea or theme? (e.g., A brave penguin, Magic in the forest)\n> ").strip()
    if not story_idea:
        story_idea = "A friendly animal adventure"
    
    print("\nHow long should the story be?")
    print("1. Short (300-400 words)")
    print("2. Medium (500-700 words)")
    print("3. Long (800-1000+ words)")
    length_choice = input("Choose 1, 2, or 3 (default: 2)\n> ").strip() or "2"
    
    length_map = {
        "1": "short (300-400 words)",
        "2": "medium (500-700 words)",
        "3": "long (800-1000+ words)"
    }
    story_length = length_map.get(length_choice, "medium (500-700 words)")
    
    print("\nWhat genre would you prefer?")
    print("1. Fantasy")
    print("2. Adventure")
    print("3. Bedtime/Cozy")
    print("4. Educational")
    print("5. Mystery")
    genre_choice = input("Choose 1-5 (default: 1)\n> ").strip() or "1"
    
    genre_map = {
        "1": "fantasy",
        "2": "adventure",
        "3": "bedtime/cozy",
        "4": "educational",
        "5": "mystery"
    }
    genre = genre_map.get(genre_choice, "fantasy")
    
    print("\nWhat's an important lesson for the story?")
    print("1. Kindness")
    print("2. Honesty")
    print("3. Teamwork")
    print("4. Courage")
    print("5. Friendship")
    print("6. Creativity")
    moral_choice = input("Choose 1-6 (default: 1)\n> ").strip() or "1"
    
    moral_map = {
        "1": "kindness",
        "2": "honesty",
        "3": "teamwork",
        "4": "courage",
        "5": "friendship",
        "6": "creativity"
    }
    moral = moral_map.get(moral_choice, "kindness")
    
    num_characters = input("\nHow many main characters? (default: 3)\n> ").strip() or "3"
    
    return {
        "story_idea": story_idea,
        "length": story_length,
        "genre": genre,
        "moral": moral,
        "num_characters": num_characters
    }

def generate_story(params, model_id):
    """Generate a story using OpenRouter API with selected model."""
    
    prompt = f"""You are an expert children's story writer AI specializing in stories for children aged 7–10.

TASK: Generate a complete, original, child-safe story based on the following parameters:

Story Idea/Theme: {params['story_idea']}
Story Length: {params['length']}
Genre: {params['genre']}
Moral/Lesson: {params['moral']}
Number of Characters: {params['num_characters']}

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

    print("\n⏳ Generating your story... this may take a moment.\n")
    
    # Get API key from environment
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY environment variable not set. Please set it and try again.")
    
    # OpenRouter API endpoint
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://github.com/boombook",
        "X-Title": "Children Story Generator"
    }
    
    payload = {
        "model": model_id,  # User-selected model from OpenRouter
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 1500
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=60)
        response.raise_for_status()
        
        result = response.json()
        
        if "error" in result:
            raise ValueError(f"API Error: {result['error'].get('message', 'Unknown error')}")
        
        return result["choices"][0]["message"]["content"]
    
    except requests.exceptions.Timeout:
        raise TimeoutError("Story generation took too long. Please try again.")
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Failed to connect to OpenRouter: {e}")

def save_story(story, filename="generated_story.txt"):
    """Save the story to a file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(story)
    print(f"\n✅ Story saved to: {filename}")

def main():ValueError as e:
        print(f"\n❌ Configuration Error: {e}")
        sys.exit(1)
    except (ConnectionError, TimeoutError) as e:
        print(f"\n❌ Connection Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected flow."""
    try:
        # Get user input
        params = get_user_input()
        
        # Generate story
        story = generate_story(params, model_id)
        
        # Display story
        print("\n" + "="*60)
        print("YOUR GENERATED STORY")
        print("="*60 + "\n")
        print(story)
        print("\n" + "="*60 + "\n")
        
        # Ask if user wants to save
        save_choice = input("Would you like to save this story? (yes/no, default: yes)\n> ").strip().lower() or "yes"
        if save_choice in ["yes", "y"]:
            filename = input("Enter filename (default: generated_story.txt)\n> ").strip() or "generated_story.txt"
            save_story(story, filename)
        
        print("\n✨ Thank you for using the Children's Story Generator!")
        
    except KeyboardInterrupt:
        print("\n\n👋 Story generation cancelled.")
        sys.exit(0)
    except anthropic.APIError as e:
        print(f"\n❌ API Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
