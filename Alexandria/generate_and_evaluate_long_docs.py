

"""
Knowledge Graph Construction and Reconstruction Pipeline

This code implements a pipeline for constructing knowledge graphs from scientific articles
and then reconstructing the text based on these graphs. The main steps are:

1. Load scientific articles from an ArXiv dataset CSV file.
2. For each article:
   a. Determine the writing style.
   b. Split the text into manageable chunks.
   c. Construct a knowledge graph for each chunk.
   d. Reconstruct the text based on the knowledge graph.
3. Evaluate the performance of the reconstruction.

The pipeline uses a Large Language Model (LLM) for various tasks including style analysis,
knowledge graph construction, and text reconstruction. It's designed to process long-form
scientific texts and create structured representations of their content.

Key components:
- Text preprocessing and chunking
- Knowledge graph construction
- Text reconstruction from knowledge graphs
- Performance evaluation

This pipeline can be used for various applications such as text summarization,
information extraction, and testing the capability of language models to understand
and regenerate complex scientific content.
"""


import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import re
import random
import requests
from scripts.style_generation import get_style_genre
from scripts.first_n_words import get_first_n_words
from scripts.llm import ask_LLM

from scripts.kg_content import extract_kg_content
from scripts.minhash_vector import create_minhash_vector
from scripts.reconstruction_content import extract_reconstruction_content
from scripts.evaluate import evaluate_peformance


# Download necessary NLTK data
nltk.download('punkt', quiet=True)


import scripts.prompts
import scripts.api_key

# Configuration

API_KEY = scripts.api_key.API_KEY 
model_name = "mistral-small-latest" # "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"

API_BASE = 'https://api.hyprlab.io/v1' #"https://api.together.xyz/v1" # 'https://api.hyprlab.io/v1'

system_prompt = "You are a very smart very intelligence assistant who is very helpful."
INPUT_FILE ="pubmed_articles.csv"

characters_to_consider = 30000
WORDCHUCHSIZE=200

df = pd.read_csv(INPUT_FILE)
#df=df [:1]

print(df)
print(API_KEY)

# Function to generate intermediate filename
def get_intermediate_filename(input_filename):
    return input_filename.rsplit('.', 1)[0] + '_kgs.csv'

intermediate_filename = get_intermediate_filename(INPUT_FILE)

import concurrent.futures
import functools

def timeout_wrapper(func, timeout_duration):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(func, *args, **kwargs)
            try:
                return future.result(timeout=timeout_duration)
            except concurrent.futures.TimeoutError:
                print(f"Function {func.__name__} timed out after {timeout_duration} seconds")
                return None
    return wrapper


# Wrap the ask_LLM function with a 60-second timeout
ask_LLM_with_timeout = timeout_wrapper(ask_LLM, 60)

#print(ask_LLM_with_timeout (model_name, "You are a helpful assistant", "What is milk?",API_KEY))

# Download necessary NLTK data
nltk.download('punkt', quiet=True)

async def evaluate_knowledge_graph(modelname, input_text, knowledge_graph, API_KEY):
    instruction = f"""
    Carefully analyze the following knowledge graph, which was created based on the given input text.
    Identify any hallucinations, factual errors, or contradictions in the knowledge graph.
    
    Definitions:
    - A hallucination is any information in the knowledge graph that is not present in or directly inferrable from the input text.
    - A factual error is any information that contradicts the input text or misrepresents names, events, or facts from the input text.
    - A minor error is an unimportant spelling mistake, a slight rewording that doesn't change the meaning, or the addition of explanatory information that doesn't contradict the input text.
    - A serious error is the invention of completely new information, misrepresentation of key concepts, or any error that significantly alters the meaning of the original content.
    If the knowledge graph does not mention an important fact from the input text, consider this as a serious error.
    If the knowledge graph does not mention an unimportant fact from the input text, do not consider this as an error, not even a minor error.
        
    The following additional tags and their contents should not be reviewed and ignored: <style_analysis> , <segment ...> & <source_sentence_min_hash>

    Have a close look at the Input Text and Knowledge Graph here:
    Input Text:
    {input_text}

    Knowledge Graph:
    {knowledge_graph}

    Instructions:
    1. Examine each triplet in the knowledge graph carefully.
    2. Compare the information in each triplet to the input text.
    3. List any hallucinations, factual errors, or contradictions you find. A lack of information in the KG does not count as an error, but wrong information does.
    4. For each identified issue:
       a) Provide a brief explanation.
       b) Classify it as either a minor or serious error/hallucination.
       c) Specify whether it's an error or a hallucination.
    5. After your analysis, provide:
       a) A total count of minor errors and hallucinations in normal double brackets, e.g., ((3))
       b) A total count of serious errors and hallucinations in double square brackets, e.g., [[5]]

    Your response should be structured as follows:
    1. Detailed analysis of errors and hallucinations, with each issue clearly labeled as minor or serious, and as an error or hallucination.
    2. Summary:
       Minor errors/hallucinations: ((X))
       Serious errors/hallucinations: [[Y]]

    Before starting, have a second close look at the Input Text and Knowledge Graph here:
    Input Text:
    {input_text}

    Knowledge Graph:
    {knowledge_graph}

    Be thorough in your analysis and ensure your counts accurately reflect the number and severity of issues found.
    """

    system_prompt = """
    You are an expert in information verification and knowledge representation.
    Your task is to critically analyze the given knowledge graph and identify any discrepancies with the provided input text.
    Be meticulous, unbiased, and provide clear explanations for any issues you discover.
    Ensure you distinguish between minor and serious errors/hallucinations, and provide accurate counts for both categories.
    """
    max_retries = 3
    for attempt in range(max_retries):
        result = ask_LLM_with_timeout(modelname, system_prompt, instruction, API_KEY)
        print("result:", result)
        # Extract the error counts using regex
        minor_error_count_match = re.search(r'\(\((\d+)\)\)', result)
        serious_error_count_match = re.search(r'\[\[(\d+)\]\]', result)
        
        if minor_error_count_match and serious_error_count_match:
            minor_error_count = int(minor_error_count_match.group(1))
            serious_error_count = int(serious_error_count_match.group(1))
            return result, serious_error_count, minor_error_count
        
        # If no valid error count is found, wait and retry
        if attempt < max_retries - 1:
            print(f"No valid error count found. Retrying (attempt {attempt + 1}/{max_retries})...")
            await asyncio.sleep(random.uniform(1, 3))
    
    # If all retries fail, return the last result with error counts of -1
    print("Failed to extract valid error counts after multiple attempts.")
    return result, -1, -1

def split_long_sentence(sentence, max_words):
    """
    Splits a long sentence into smaller parts, preferably at commas.
    
    This function is useful for breaking down complex, long sentences into more manageable chunks.
    It first attempts to split at commas, and if parts are still too long, it splits by word count.
    
    Args:
    sentence (str): The input sentence to be split
    max_words (int): The maximum number of words per part
    
    Returns:
    list: A list of sentence parts, each containing no more than max_words
    """
    comma_parts = re.split(r',\s*', sentence)
    
    result = []
    current_part = []
    current_word_count = 0
    
    for part in comma_parts:
        words = part.split()
        if current_word_count + len(words) <= max_words:
            current_part.append(part)
            current_word_count += len(words)
        else:
            if current_part:
                result.append(', '.join(current_part))
                current_part = []
                current_word_count = 0
            
            if len(words) > max_words:
                while words:
                    sub_part = ' '.join(words[:max_words])
                    result.append(sub_part)
                    words = words[max_words:]
            else:
                current_part.append(part)
                current_word_count = len(words)
    
    if current_part:
        result.append(', '.join(current_part))
    
    return result

def split_long_text(text, min_words=WORDCHUCHSIZE, max_words=WORDCHUCHSIZE+200):
    """
    Splits a long text into segments of full sentences.
    
    This function is crucial for breaking down long articles into manageable chunks
    for processing. It ensures that each chunk is neither too short nor too long,
    maintaining sentence integrity where possible.
    
    Args:
    text (str): The input text to be split
    min_words (int): The minimum number of words per segment (default 500)
    max_words (int): The maximum number of words per segment (default 1000)
    
    Returns:
    list: A list of text segments, each containing between min_words and max_words
    """
    sentences = sent_tokenize(text)
    
    segments = []
    current_segment = []
    current_word_count = 0
    
    for i, sentence in enumerate(sentences):
        sentence_words = word_tokenize(sentence)
        sentence_word_count = len(sentence_words)
        
        if sentence_word_count > max_words:
            split_sentence = split_long_sentence(sentence, max_words)
            for sub_sentence in split_sentence:
                sub_word_count = len(word_tokenize(sub_sentence))
                
                if current_word_count + sub_word_count > max_words and current_word_count >= min_words:
                    segments.append(' '.join(current_segment))
                    current_segment = []
                    current_word_count = 0
                
                current_segment.append(sub_sentence)
                current_word_count += sub_word_count
        else:
            if current_word_count + sentence_word_count > max_words and current_word_count >= min_words:
                segments.append(' '.join(current_segment))
                current_segment = []
                current_word_count = 0
            
            current_segment.append(sentence)
            current_word_count += sentence_word_count
        
        if i < len(sentences) - 1:
            next_sentence_word_count = len(word_tokenize(sentences[i + 1]))
            if current_word_count >= min_words and next_sentence_word_count + current_word_count > max_words:
                segments.append(' '.join(current_segment))
                current_segment = []
                current_word_count = 0
    
    if current_segment:
        segments.append(' '.join(current_segment))
    
    return segments


# Function to construct knowledge graphs and reconstruct text
def KG_construction_and_reconstruction(input_text, model, preprocessing_type="none"):
    """
    This function takes an input text and a model, and performs the following steps:
    1. Determines the writing style of the input text
    2. Constructs a knowledge graph from the input text
    3. Reconstructs the text based on the knowledge graph
    
    Args:
    input_text (str): The input text to process
    model (str): The name of the language model to use

    Returns:
    tuple: Contains the input text, constructed knowledge graph, and reconstructed text
    """
    # Determine the writing style of the input text
    writing_style = get_style_genre(model_name, API_KEY, system_prompt ,get_first_n_words(  input_text, len(input_text) ) )

    if preprocessing_type=="none":

      sentence_chunks= split_long_text(input_text)
    
      print(sentence_chunks)
      print("Number of segments in this chapter:", len(sentence_chunks))

    
    if preprocessing_type=="paraphrasation":
      paraphrasation_list=[]
      chunks= split_long_text(input_text)
      for chunk in chunks:
        paraphrasation = ask_LLM_with_timeout(model_name, system_prompt, "Paraphrase the following text so that the resulting text consists entirely of short sentences of with less than 15 words per sentence and with simple grammar, while still using all important facts, contents, names, pharses, nouns and adjectives. BE VERY FACTUAL WHEN DOING THIS. The paraphrased text should still contain the same information (facts, nouns, verbs, adjectives, meaning, dates, numbers, names, places, variables, ...) as the INPUT TEXT, but with clean & easily understandable grammer. If there are broken tables, broken citations, gibberish or spam in the INPUT TEXT, just leave them out. Each sentence in PARAPHRASATION should end with either a dot (.) , a question mark (?) or an exklamation mark (!) and consist only of sentences that are shorter than 15 word. Do only output the PARAPHRASATION, nothing else. Even if the sentences are short, they should be very intelligent and very factual. INPUT TEXT:" +chunk + "\nPARAPHRASATION: ", API_KEY, temperature=0.5, top_p=0.95, max_tokens=1000,
                                                    frequency_penalty=1.0, presence_penalty=1.0)
        paraphrasation_list.append(paraphrasation)
        print(paraphrasation)
        
      # Initialize variables for knowledge graph construction
      sentences = sent_tokenize(" ".join(paraphrasation_list) )
      sentence_chunks= concatenate_to_min_length(sentences)
    
      print(sentence_chunks)
      print("Number of segments in this chapter:", len(sentence_chunks))

    if preprocessing_type=="list_of_facts":
      lists_of_facts_list=[]
      chunks= split_long_text(input_text)
      for chunk in chunks:
        facts = ask_LLM_with_timeout(model_name, system_prompt, "Write for the following text a list of ALL facts, events, actions, thoughts, ideas, quotes, ... in as VERY FACTUAL MANNER, that presents them on the point, so that it would be an ideal learning script to prepare for a question - answer exam about this text, without unnecessary fluff. Keep preserving all important facts, contents, names, pharses, nouns and adjectives. BE VERY FACTUAL WHEN DOING THIS. The resulting text should still contain the same information (facts, nouns, verbs, adjectives, meaning, dates, numbers, names, places, variables, ...) as the INPUT TEXT, but with clean & easily understandable grammer. If there are broken tables, broken citations, gibberish or spam in the INPUT TEXT, just leave them out. Each sentence in FACTS should end with either a dot (.) , a question mark (?) or an exklamation mark (!) and consist only of sentences that are shorter than 15 word. Do only output the FACTS, nothing else. Even if the sentences are short, they should be very intelligent and very factual. INPUT TEXT:" +chunk + "\nFACTS: ", API_KEY, temperature=0.5, top_p=0.95, max_tokens=1000,
                                                    frequency_penalty=1.0, presence_penalty=1.0)
        lists_of_facts_list.append(facts)
        print(facts)
        
      # Initialize variables for knowledge graph construction
      sentences = sent_tokenize(" ".join(lists_of_facts_list) )
      sentence_chunks= concatenate_to_min_length(sentences)
    
      print(sentence_chunks)
      print("Number of segments in this chapter:", len(sentence_chunks))


    current_kg = []
    current_kg.append("<style_analysis>" + writing_style + "</style_analysis>")
    segment_nr = 1
    reconstruction_so_far = ""
    input_string_so_far = ""
    print("<style_analysis>"+ writing_style + "</style_analysis>")
    # Process each sentence in the input text
    for sentence in sentence_chunks:
        
        input_string_so_far += sentence

        
        
        # Get the context for the current knowledge graph segment
        current_kg_context = current_kg[-10:] if len(current_kg) > 10 else current_kg
        current_kg_context = ' '.join(current_kg_context)

        # Generate the prompt for knowledge graph construction
        text = scripts.prompts.KG_format_example_prompt2(current_kg_context, sentence)
        #print("Prompt:", text)

        
        # Generate the knowledge graph segment
        try:
            for i in range(3):
                print("*************************************")

                print("INSTRUCTION SENT TO SERVER:",text)
                knowledge_graph_segment = ask_LLM_with_timeout(model_name, system_prompt, text, API_KEY, temperature=0.5, top_p=0.95, max_tokens=5000,
                                                frequency_penalty=1.0, presence_penalty=1.0)
                #if "</div>" in knowledge_graph_segment:
                     
                #     continue
                print("Constructed KG:")
                if not (extract_kg_content(knowledge_graph_segment) == None):
                    break
            
            # Add the knowledge graph segment to the current knowledge graph
            try:
                current_kg.append("<segment " + str(segment_nr) + ">\n" + extract_kg_content(
                        knowledge_graph_segment) + "<source_sentence_min_hash: " + str(
                        create_minhash_vector(sentence)) + " >\n" + "</segment " + str(segment_nr) + ">\n")
                print("<segment " + str(segment_nr) + ">\n" + extract_kg_content(
                        knowledge_graph_segment) + "<source_sentence_min_hash: " + str(
                        create_minhash_vector(sentence)) + " >\n" + "</segment " + str(segment_nr) + ">\n")
            except:
                current_kg.append(
                        "<segment " + str(segment_nr) + ">\n" + knowledge_graph_segment + "<source_sentence_min_hash: " + str(
                            create_minhash_vector(sentence)) + " >\n" + "</segment " + str(segment_nr) + ">\n")
                
                print("<segment " + str(segment_nr) + ">\n" + knowledge_graph_segment + "<source_sentence_min_hash: " + str(
                        create_minhash_vector(sentence)) + " >\n" + "</segment " + str(segment_nr) + ">\n")

            # Generate the prompt for text reconstruction
            prompt = scripts.prompts.KG_reconstruction_prompt(reconstruction_so_far, current_kg)
            
            # Reconstruct the text based on the knowledge graph
            for i in range(2):
                next_reconstruction = ask_LLM_with_timeout(model_name,
                                                "You are a very smart very intelligence assistant who is very helpful.",
                                                prompt, API_KEY, temperature=0.5, top_p=0.95, max_tokens=5000,
                                                frequency_penalty=1.1, presence_penalty=1.1)
                if not (extract_reconstruction_content(next_reconstruction) == None):
                    break

            reconstruction_so_far += extract_reconstruction_content(next_reconstruction)
            print("Recontructed Segment:", extract_reconstruction_content(next_reconstruction))
            segment_nr += 1

        except Exception as e:
            print("No Kg found: "+ str(e))
            
    return input_string_so_far, current_kg, reconstruction_so_far



# Main execution


all_input_texts = []
all_kg_results = []
all_reconstruction_results = []
import time
s= time.time()

# Process each article
for index, row in df.iterrows():
    input_text = row['article'] [:characters_to_consider]
    print(f"Processing article {index + 1}")
    
    # Perform KG construction and reconstruction
    input_string, kg_results, reconstruction_results = KG_construction_and_reconstruction(input_text, model_name)
    
    all_input_texts.append(input_string)
    all_kg_results.append(kg_results)
    all_reconstruction_results.append(reconstruction_results)
    print(time.time()-s)

# Evaluate performance (if evaluation function is implemented)
# performance_metrics = evaluate_performance(all_input_texts, all_reconstruction_results)
# print("Performance Metrics:", performance_metrics)

print("Processing complete.")
print(f"Processed {len(all_input_texts)} articles.")
print(f"Generated {len(all_kg_results)} knowledge graphs.")
print(f"Created {len(all_reconstruction_results)} reconstructions.")

df = pd.DataFrame({
     'Input_Texts': all_input_texts,
     'Output_Graphs': all_kg_results,
     'Output_Reconstructions': all_reconstruction_results, })

df.to_csv(intermediate_filename, index=False)




# Load the CSV file into a DataFrame
#df = pd.read_csv(intermediate_filename)     


'''
df = pd.DataFrame({
    'Input_Texts': input_split_texts,
    'Output_Graphs': kg_for_input_split_texts,
    'Output_Reconstructions': reconstruction_results_for_input_split_texts, })
'''

print(df)

print(f"Long doc evalution:", "\n")
base_percentage, original_percentage, knowledgegraph_percentage, reconstruction_percentage ,QA_df = evaluate_peformance(df, 10,
                                                                                                      "arxiv_q_a_kg.parquet") #generate 10 Q-A-Pairs per Doc

print(intermediate_filename, model_name , WORDCHUCHSIZE)
print("No context correct answer percentage:", base_percentage, "\n")
print("Original context correct answer percentage:", original_percentage, "\n")
print("Knowledgegraph context correct answer percentage:", knowledgegraph_percentage, "\n")
print("Reconstruckted text context correct answer percentage:", reconstruction_percentage, "\n")

print(intermediate_filename, model_name , WORDCHUCHSIZE)
print("No context correct answer percentage:", base_percentage, "\n")
print("Original context correct answer percentage:", original_percentage, "\n")
print("Knowledgegraph context correct answer percentage:", knowledgegraph_percentage, "\n")
print("Reconstruckted text context correct answer percentage:", reconstruction_percentage, "\n")

# First, create the filename
filename = f"{intermediate_filename.replace('.', '_')}_{model_name.replace('.', '_').replace('/', '_')}_{WORDCHUCHSIZE}_contextsummary.txt"

# Open the file in write mode
with open(filename, 'w') as f:
    # Write the output to the file
    print(intermediate_filename, model_name, WORDCHUCHSIZE, file=f)
    print("No context correct answer percentage:", base_percentage, "\n", file=f)
    print("Original context correct answer percentage:", original_percentage, "\n", file=f)
    print("Knowledgegraph context correct answer percentage:", knowledgegraph_percentage, "\n", file=f)
    print("Reconstruckted text context correct answer percentage:", reconstruction_percentage, "\n", file=f)

# Optionally, you can also print to console
print(f"Results have been saved to {filename}")
