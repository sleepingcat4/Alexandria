import scripts.llm
import scripts.api_key
import scripts.prompts

import re

def sanitize_input(text):
    # Remove or replace problematic characters
    text = re.sub(r'[^\w\s\-.,;:!?()[\]{}@#$%^&*+=|~<>"]', '', text)
    
    # Escape double quotes
    text = text.replace('"', '\\"')
    
    # Truncate to a maximum length (adjust as needed)
    max_length = 8000  # Adjust based on API limitations
    if len(text) > max_length:
        text = text[:max_length]
    
    return text
def get_style_genre(model, API_KEY, system_prompt,input_text) :

      text = sanitize_input(scripts.prompts.style_genre_prompt(input_text)) #[:100]
      print("+++++++++++++", text)
      for i in range(5):
        style_genre = scripts.llm.ask_LLM (model, system_prompt, text , API_KEY ,temperature=0.5,top_p=0.95,max_tokens=100, frequency_penalty=1.1,presence_penalty=1.1)
        try:
          if not style_genre== None and len(style_genre)>100:
            break
        except:
          pass
      return style_genre
