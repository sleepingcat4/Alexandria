from scripts.llm import ask_LLM
import scripts.prompts
import scripts.api_key

API_KEY = scripts.api_key.API_KEY



API_KEY =  "xxx"
import requests

def ask_LLM(modelname, systemprompt, content, API_KEY, temperature, top_p, max_tokens, frequency_penalty, presence_penalty):
    # Construct the payload
    data = {
        "model": modelname,
        "messages": [
            {
                "role": "system",
                "content": systemprompt
            },
            {
                "role": "user",
                "content": content
            }
        ],
        "max_tokens": max_tokens,
        "temperature": temperature,
        #"top_p": top_p,
        #"frequency_penalty": frequency_penalty,
        #"presence_penalty": presence_penalty,
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # URL updated to match the Together API endpoint
    API_BASE = "https://api.together.xyz/v1"
    # Send a POST request
    response = requests.post(f"{API_BASE}/chat/completions", headers=headers, json=data)

    # Display the response (you can format this better if needed)
    if response.status_code == 200:
        assistant_message = response.json().get('choices', [{}])[0].get('message', {}).get('content', '')
        return assistant_message
    else:
        print("Error:", response.status_code, response.text)
        return response.status_code
    





def extract_answer(text):
    """
    Extracts multiple-choice answers from a semicolon-separated string.

    Parameters:
    - text (str): The string containing multiple-choice answers separated by semicolons.

    Returns:
    - List[str]: A list of answers (e.g., ["A", "B", "C", "D"]).
    """
    answers = []
    data_list = [item.strip() for item in text.split(";")]
    for item in data_list:
        if item in ["A", "B", "C", "D"]:
            answers.append(item)
    return answers


def answer_questions(questions, context):
    """
    Takes questions and a context, then retrieves answers from GPT-4 based on that context.

    Parameters:
    - questions (str): The questions to be answered.
    - context (str): The context or background information necessary to understand and answer the questions.

    Returns:
    - List[str]: A list of answers, each marked clearly with a capital letter (e.g., "A", "B").
    """
    answers=[]
    for question in questions:

      # Format the prompt for the language model
      prompt = scripts.prompts.answer_questions_prompts(context, question)
      print("len(prompt):", len(prompt))
      # Attempt to get answers from the language model
      try:

          text = ask_LLM ("meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
                           "You are a very smart very intelligence assistant who is very helpful.",
                             prompt , API_KEY ,temperature=0.5,top_p=0.95,max_tokens=10000,
                               frequency_penalty=1.05,presence_penalty=1.05)



          answer = extract_answer(text)[0]
          print(question, answer)
          answers.append(answer)
      except:
          try:
              # Retry fetching answers on failure
              text = ask_LLM ("meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
                               "You are a very smart very intelligence assistant who is very helpful.",
                                 prompt , API_KEY ,temperature=0.5,top_p=0.95,max_tokens=10000,
                                   frequency_penalty=1.05,presence_penalty=1.05)
              #ask_LLM ("mistral-large-latest", "You are a very smart, intelligent, helpful assistant. You try your best to do whatever the user asks you. You are very good at coding and at common sense.", prompt, temperature=0.5, top_p=0.95,max_tokens=length)
              answer = extract_answer(text)[0]
              print(question, answer)
              answers.append(answer)
          except:
              pass

    return answers

