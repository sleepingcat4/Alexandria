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
from scripts.style_generation import get_style_genre
from scripts.first_n_words import get_first_n_words
from scripts.llm import ask_LLM
from scripts.kg_content import extract_kg_content
from scripts.minhash_vector import create_minhash_vector
from scripts.reconstruction_content import extract_reconstruction_content
from scripts.evaluate import evaluate_peformance

import scripts.prompts
import scripts.api_key

# Download necessary NLTK data
nltk.download('punkt', quiet=True)

# Configuration
API_KEY = "bc8ec9e53b89739f63f5e35cc60cfa152f25b24455dbb77e8cb7cf4860bbdfa6"
model_name = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"
system_prompt = "You are a very smart very intelligence assistant who is very helpful."

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

def split_long_text(text, min_words=500, max_words=1000):
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
        paraphrasation = ask_LLM(model_name, system_prompt, "Paraphrase the following text so that the resulting text consists entirely of short sentences of with less than 15 words per sentence and with simple grammar, while still using all important facts, contents, names, pharses, nouns and adjectives. BE VERY FACTUAL WHEN DOING THIS. The paraphrased text should still contain the same information (facts, nouns, verbs, adjectives, meaning, dates, numbers, names, places, variables, ...) as the INPUT TEXT, but with clean & easily understandable grammer. If there are broken tables, broken citations, gibberish or spam in the INPUT TEXT, just leave them out. Each sentence in PARAPHRASATION should end with either a dot (.) , a question mark (?) or an exklamation mark (!) and consist only of sentences that are shorter than 15 word. Do only output the PARAPHRASATION, nothing else. Even if the sentences are short, they should be very intelligent and very factual. INPUT TEXT:" +chunk + "\nPARAPHRASATION: ", API_KEY, temperature=0.5, top_p=0.95, max_tokens=1000,
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
        facts = ask_LLM(model_name, system_prompt, "Write for the following text a list of ALL facts, events, actions, thoughts, ideas, quotes, ... in as VERY FACTUAL MANNER, that presents them on the point, so that it would be an ideal learning script to prepare for a question - answer exam about this text, without unnecessary fluff. Keep preserving all important facts, contents, names, pharses, nouns and adjectives. BE VERY FACTUAL WHEN DOING THIS. The resulting text should still contain the same information (facts, nouns, verbs, adjectives, meaning, dates, numbers, names, places, variables, ...) as the INPUT TEXT, but with clean & easily understandable grammer. If there are broken tables, broken citations, gibberish or spam in the INPUT TEXT, just leave them out. Each sentence in FACTS should end with either a dot (.) , a question mark (?) or an exklamation mark (!) and consist only of sentences that are shorter than 15 word. Do only output the FACTS, nothing else. Even if the sentences are short, they should be very intelligent and very factual. INPUT TEXT:" +chunk + "\nFACTS: ", API_KEY, temperature=0.5, top_p=0.95, max_tokens=1000,
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
        current_kg_context = current_kg[-20:] if len(current_kg) > 20 else current_kg
        current_kg_context = ' '.join(current_kg_context)

        # Generate the prompt for knowledge graph construction
        text = scripts.prompts.KG_format_example_prompt(current_kg_context, sentence)
        #print("Prompt:", text)

        
        # Generate the knowledge graph segment
        try:
            for i in range(2):
                knowledge_graph_segment = ask_LLM(model_name, system_prompt, text, API_KEY, temperature=0.5, top_p=0.95, max_tokens=1000,
                                                    frequency_penalty=1.1, presence_penalty=1.1)
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
                next_reconstruction = ask_LLM(model_name,
                                                "You are a very smart very intelligence assistant who is very helpful.",
                                                prompt, API_KEY, temperature=0.5, top_p=0.95, max_tokens=5000,
                                                frequency_penalty=1.1, presence_penalty=1.1)
                if not (extract_reconstruction_content(next_reconstruction) == None):
                    break

            reconstruction_so_far += extract_reconstruction_content(next_reconstruction)
            print("Recontructed Segment:", extract_reconstruction_content(next_reconstruction))
            segment_nr += 1

        except:
            print("No Kg found")
            
    return input_string_so_far, current_kg, reconstruction_so_far



# Main execution

# Load ArXiv articles from CSV
df = pd.read_csv('pubmed_articles.csv')

print(df)

all_input_texts = []
all_kg_results = []
all_reconstruction_results = []
import time
s= time.time()

# Process each article
for index, row in df.iterrows():
    input_text = row['article'] 
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

df.to_csv(f'pubmed_articles_kgs.csv', index=False)
