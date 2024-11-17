import pandas as pd
from scripts.style_generation import get_style_genre
from scripts.first_n_words import get_first_n_words
from scripts.kg_content import extract_kg_content
from scripts.minhash_vector import create_minhash_vector
from scripts.reconstruction_content import extract_reconstruction_content
from scripts.evaluate import evaluate_peformance
import scripts.prompts
import scripts.api_key

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

torch.random.manual_seed(0)

stop_len = 50000

def load_LLM():
    model = AutoModelForCausalLM.from_pretrained(
        LLM,
        device_map="cuda",
        torch_dtype="auto",
        trust_remote_code=True,
    )

    tokenizer = AutoTokenizer.from_pretrained(LLM)

    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
    )

    generation_args = {
        "max_new_tokens": 1500,
        "return_full_text": False,
        "temperature": 0.5,
        "do_sample": False,
    }

    return model, tokenizer, pipe, generation_args

model, tokenizer, pipe, generation_args = load_LLM()

system_prompt = "You are a very smart very intelligence assistant who is very helpful. "

def ask_LLM(system_prompt, text, generation_args):
    messages = str(system_prompt)+str(text)
    output = pipe(messages, **generation_args)
    return output



def get_style_genre(input_text, system_prompt):

      text = scripts.prompts.style_genre_prompt(input_text)

      for i in range(5):
        style_genre = ask_LLM(system_prompt, text, generation_args)
        try:
          if not style_genre== None and len(style_genre)>100:
            break
        except:
          pass

      return style_genre

def KG_construction_and_reconstruction(input_text):
    writing_style = get_style_genre(input_text, system_prompt)[0]['generated_text']
    sentences = [input_text]
    current_kg = []
    current_kg.append("<style_analysis>" + writing_style + "</style_analysis>")
    segment_nr = 1
    reconstruction_so_far = ""
    input_string_so_far = ""
    for sentence in sentences:
        input_string_so_far += sentence
        if len(input_string_so_far) > stop_len:
            break
        current_kg_context = current_kg[-50:] if len(current_kg) > 50 else current_kg
        current_kg_context = ' '.join(current_kg_context)

        text = scripts.prompts.KG_format_example_prompt(current_kg_context, sentence)

        try:
            for i in range(2):
                knowledge_graph_segment = ask_LLM(system_prompt, text, generation_args)[0]['generated_text']

                print(knowledge_graph_segment)

                if not (extract_kg_content(knowledge_graph_segment) == None):
                    break
            try:
                current_kg.append("<segment " + str(segment_nr) + ">\n" + extract_kg_content(
                        knowledge_graph_segment) + "<source_sentence_min_hash: " + str(
                        create_minhash_vector(sentence)) + " >\n" + "</segment " + str(segment_nr) + ">\n")

            except:
                current_kg.append(
                        "<segment " + str(segment_nr) + ">\n" + knowledge_graph_segment + "<source_sentence_min_hash: " + str(
                            create_minhash_vector(sentence)) + " >\n" + "</segment " + str(segment_nr) + ">\n")

            prompt = scripts.prompts.KG_reconstruction_prompt(reconstruction_so_far, current_kg)#[0]['generated_text']

            for i in range(2):
                next_reconstruction = ask_LLM(system_prompt, prompt, generation_args)[0]['generated_text']

                if not (extract_reconstruction_content(next_reconstruction) == None):
                  break

            reconstruction_so_far += extract_reconstruction_content(next_reconstruction)

            segment_nr += 1

        except Exception as e:
          print(e)


        try:
            all_kg_results.append(current_kg)
            all_reconstruction_results.append(reconstruction_so_far)

            input_string_so_far_list.append(input_string_so_far)

        except:
            print("Pass because of no Kg found")

    return input_string_so_far_list, all_kg_results, all_reconstruction_results




LLM = "microsoft/Phi-3-mini-128k-instruct" #Please add the LLM from huggingface  
input_dataset = "" #add the input dataset path
output_dataset = "" #add the output dataset path
col_name = 'context' # add the column name that contain the text  

dataset = pd.read_csv(input_dataset)
rows, columns = dataset.shape
concatenated_texts = dataset[col_name]

all_kg_results = []
all_reconstruction_results = []
input_string_so_far_list = []

i = 0
for input_text in concatenated_texts[0:row]:

    i = i+1
    print(i)
    input_string_so_far_list, all_kg_results, all_reconstruction_results = KG_construction_and_reconstruction(input_text)

    df = pd.DataFrame({
        'Input_Texts': input_string_so_far_list,
        'Output_Graphs': all_kg_results,
        'Output_Reconstructions': all_reconstruction_results, })

    df.to_csv(output_dataset, encoding='utf-8', index=False)
