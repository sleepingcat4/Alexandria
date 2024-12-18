import requests

# def ask_LLM(modelname, systemprompt, content, API_KEY, temperature, top_p, max_tokens, frequency_penalty, presence_penalty):
#     # Construct the payload
#     data = {
#         "model": modelname,
#         "messages": [
#             {
#                 "role": "system",
#                 "content": systemprompt
#             },
#             {
#                 "role": "user",
#                 "content": content
#             }
#         ],
#         "max_tokens": max_tokens,
#         "temperature": temperature,
#         #"top_p": top_p,
#         #"frequency_penalty": frequency_penalty,
#         #"presence_penalty": presence_penalty,
#     }

#     headers = {
#         "Authorization": f"Bearer {API_KEY}",
#         "Content-Type": "application/json"
#     }

#     # URL updated to match the Together API endpoint
#     API_BASE = "https://api.together.xyz/v1"
#     # Send a POST request
#     response = requests.post(f"{API_BASE}/chat/completions", headers=headers, json=data)

#     # Display the response (you can format this better if needed)
#     if response.status_code == 200:
#         assistant_message = response.json().get('choices', [{}])[0].get('message', {}).get('content', '')
#         return assistant_message
#     else:
#         print("Error:", response.status_code, response.text)
#         return response.status_code
    

# ask_LLM('NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO',
#                                               "You are a very smart very intelligence assistant who is very helpful.",
#                                               text, API_KEY, temperature=0.5, top_p=0.95, max_tokens=1000,
#                                               frequency_penalty=1.1, presence_penalty=1.1)


from ollama import Client
client = Client(host='http://gpu5.research.tib.eu:11434')


def ask_Ollama(modelname, systemprompt, content, API_KEY, temperature, top_p, max_tokens, frequency_penalty, presence_penalty):
    response = client.chat(model='llama3:8b', messages=[
    {
        'role': 'user',
        'content': content},
        ])

        # print(response)
    return response['message']['content']
