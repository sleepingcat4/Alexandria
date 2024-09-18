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

API_KEY = scripts.api_key.API_KEY
model_name = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"


# Load the CSV file into a DataFrame
df = pd.read_csv('arxiv_articles_kgs.csv')     
#df = df[:3]

'''
df = pd.DataFrame({
    'Input_Texts': input_split_texts,
    'Output_Graphs': kg_for_input_split_texts,
    'Output_Reconstructions': reconstruction_results_for_input_split_texts, })
'''

print(df)

print(f"Long doc evalution:", "\n")
base_percentage, original_percentage, knowledgegraph_percentage, reconstruction_percentage ,QA_df = evaluate_peformance(df, 10,
                                                                                                      "pubmed_q_a_kg.parquet")


print("No context correct answer percentage:", base_percentage, "\n")
print("Original context correct answer percentage:", original_percentage, "\n")
print("Knowledgegraph context correct answer percentage:", knowledgegraph_percentage, "\n")
print("Reconstruckted text context correct answer percentage:", reconstruction_percentage, "\n")
