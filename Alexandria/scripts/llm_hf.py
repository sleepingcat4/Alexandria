from transformers import AutoModelForCausalLM, AutoTokenizer

def load_model(modelname):
    tokenizer = AutoTokenizer.from_pretrained(modelname)
    model = AutoModelForCausalLM.from_pretrained(modelname)
    return tokenizer, model

def ask_hf_model(tokenizer, model, systemprompt, user_input, max_tokens=400):
    conversation = f"System: {systemprompt}\nUser: {user_input}\nAssistant:"
    inputs = tokenizer(conversation, return_tensors="pt")
    outputs = model.generate(
        inputs["input_ids"],
        max_new_tokens=max_tokens,
        temperature=0.7,
        top_p=0.9,
        do_sample=True
    )
    return tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
