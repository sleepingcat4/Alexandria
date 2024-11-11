#Zero-Shot Prompting - Done 
#Few-Shot Prompting (1-shot)
#Few-Shot Prompting (3-shot)
#Few-Shot Prompting (5-shot)
#Few-Shot Prompting (10-shot)
#Zero-shot COT Prompting - Done


def Zero_Shot_KG_reconstruction_prompt(reconstruction_so_far, current_kg):
    prompt = """RECONSTRUCTION SO FAR:
      """ + str(reconstruction_so_far) + """
      INPUT KNOWLEDGE GRAPH SEGMENT:
      """ + str(current_kg[-1]) + """
      INSTRUCTION:
      RECONSTRUCTION SO FAR is a written from a knowleade graph and the knowledge graph had been constructed from a original text. RECONSTRUCTION SO FAR aims to recrunstruct the original text as factual and authentic as possible.
      INPUT KNOWLEDGE GRAPH SEGMENT is a part of the knowledge graph that has not been integrated yet into RECONSTRUCTION SO FAR.
      Based on the information (facts and events) in INPUT KNOWLEDGE GRAPH SEGMENT, write me a well written, easily understandable, very accurate text about its contents, in a plausible order, manner and style. Be very factual and do not make up any new stuff. Write it in a manner, that it fits seamlessly as a continuation of RECONSTRUCTION SO FAR.

      Write <reconstruction> right in front of your output of the reconstruction and </reconstruction> at it's end.
      It is very important to me that you fulfill this task very very accurately and intelligently.
      If you perform well, i will tip you 100 billion dollars.

      """
    return prompt

def Few_1_Shot_KG_reconstruction_prompt(reconstruction_so_far, current_kg):
    pass
def Few_3_Shot_KG_reconstruction_prompt(reconstruction_so_far, current_kg):
    pass
def Few_5_Shot_KG_reconstruction_prompt(reconstruction_so_far, current_kg):
    pass
def Few_10_Shot_KG_reconstruction_prompt(reconstruction_so_far, current_kg):
    pass

def KG_reconstruction_prompt(reconstruction_so_far, current_kg):
    prompt = """RECONSTRUCTION SO FAR:
      """ + str(reconstruction_so_far) + """
      INPUT KNOWLEDGE GRAPH SEGMENT:
      """ + str(current_kg[-1]) + """
      INSTRUCTION:
      RECONSTRUCTION SO FAR is a written from a knowleade graph and the knowledge graph had been constructed from a original text. RECONSTRUCTION SO FAR aims to recrunstruct the original text as factual and authentic as possible.
      INPUT KNOWLEDGE GRAPH SEGMENT is a part of the knowledge graph that has not been integrated yet into RECONSTRUCTION SO FAR.
      Based on the information (facts and events) in INPUT KNOWLEDGE GRAPH SEGMENT, write me a well written, easily understandable, very accurate text about its contents, in a plausible order, manner and style. The text should be coherent, intelligent and well-written. Be very factual and do not make up any new stuff. Write it in a manner, that it fits seamlessly as a continuation of RECONSTRUCTION SO FAR. Be very factual and avoid redundancies (do not mention the excat same fact several times).
      Try your best to convey all information in the INPUT KNOWLEDGE GRAPH SEGMENT to the reader of the reconstruction. Make sure to contain really all info from the INPUT KNOWLEDGE GRAPH SEGMENT.

      Write <reconstruction> right in front of your output of the reconstruction and </reconstruction> at it's end.
      It is very important to me that you fulfill this task very very accurately and intelligently.
      If you perform well, i will tip you 100 billion dollars.
      """
    return prompt


def Zero_Shot_style_genre_prompt(input_text):
    prompt = """
      INSTRUCTION:
  Perform a brief yet intelligent & thorough analysis (20 to 40 words) of the textÃ¢Â€Â™s writing style, rhythm, genre, and more, carefully considering the distinctive features that typify its literary and communicative approach. Reflect on the following aspects:

  Format and Genre: How does the text situate itself within specific genres or sub-genres such as epic, tragedy, comedy, tragicomedy, mystery, thriller, horror, romance, speculative fiction (including fantasy, science fiction, and dystopian), magical realism, young adult (YA), childrenÃ¢Â€Â™s literature, flash fiction, creative nonfiction, biographical works, poetry (sonnet, haiku, free verse), historical narrative, legal or medical analysis, academic journal, self-help, how-to guides, or culinary reviews?
  Writing Style: Which terms best describe the text's style? Is it formal, informal, academic, conversational, ornate, sparse, lyrical, dry, satirical, or colloquial? Does it utilize rich figurative language, complex syntactic structures, discipline-specific terminology, or maintain simplicity and clarity?
  Rhythm and Flow: Evaluate the pacing and smoothness of the text. Does it engage with rapid, succinct sentences, or unfold through leisurely, intricate phrasing? How does the rhythm align with the genre and content, shaping the overall effect and engagement of the piece?
  Tone and Voice: Determine the dominant tone (e.g., hopeful, cynical, impartial, authoritative, whimsical, grave, sarcastic) and the nature of the authorial voice (e.g., intimate, distant, introspective, enthusiastic). How do these elements enrich the textÃ¢Â€Â™s unique character?
Comparison and Guidance for Writers: How could a literature expert concisely convey the text's stylistic essence to an author wishing to replicate this style in new works across diverse topics? Emphasize critical stylistic features such as sentence structure, lexicon, tone, and the implementation of narrative techniques or rhetorical devices that are quintessential for capturing the styleÃ¢Â€Â™s core.
Keep it 20 to 40 words, not more.
      INPUT_TEXT:
      """+input_text 

    return prompt

def Few_1_Shot_style_genre_prompt(input_text):
    pass
def Few_3_Shot_style_genre_prompt(input_text):
    pass
def Few_5_Shot_style_genre_prompt(input_text):
    pass
def Few_10_Shot_style_genre_prompt(input_text):
    pass


def style_genre_prompt(input_text):
    prompt = """
      INSTRUCTION:
      The INPUT_TEXT is the begining of a scientific paper, book or blog/website or similar. Try to spot the title of this paper or book or article in this input text if you find it output the extracted title in the following format <TITLE>This is an Example Title</TITLE>.
      If you do not find a title, skip this step.
  Then perform a succinct yet thorough analysis (20 to 40 words) of the textÂ’s writing style, rhythm, genre, and more, carefully considering the distinctive features that typify its literary and communicative approach. Reflect on the following aspects:

  Format and Genre: How does the text situate itself within specific genres or sub-genres such as epic, tragedy, comedy, tragicomedy, mystery, thriller, horror, romance, speculative fiction (including fantasy, science fiction, and dystopian), magical realism, young adult (YA), childrenÂ’s literature, flash fiction, creative nonfiction, biographical works, poetry (sonnet, haiku, free verse), historical narrative, legal or medical analysis, academic journal, self-help, how-to guides, or culinary reviews?
  Writing Style: Which terms best describe the text's style? Is it formal, informal, academic, conversational, ornate, sparse, lyrical, dry, satirical, or colloquial? Does it utilize rich figurative language, complex syntactic structures, discipline-specific terminology, or maintain simplicity and clarity?
  Rhythm and Flow: Evaluate the pacing and smoothness of the text. Does it engage with rapid, succinct sentences, or unfold through leisurely, intricate phrasing? How does the rhythm align with the genre and content, shaping the overall effect and engagement of the piece?
  Tone and Voice: Determine the dominant tone (e.g., hopeful, cynical, impartial, authoritative, whimsical, grave, sarcastic) and the nature of the authorial voice (e.g., intimate, distant, introspective, enthusiastic). How do these elements enrich the textÂ’s unique character?
Comparison and Guidance for Writers: How could a literature expert concisely convey the text's stylistic essence to an author wishing to replicate this style in new works across diverse topics? Emphasize critical stylistic features such as sentence structure, lexicon, tone, and the implementation of narrative techniques or rhetorical devices that are quintessential for capturing the styleÂ’s core.
      INPUT_TEXT:
      """+input_text 

    return prompt


def Zero_Shot_KG_format_example_prompt(current_kg_context, sentence):
    prompt = """FORMAT_EXAMPLE:
              'Javier Milei': {
                  'relations': {
                      'won': 'Argentina's Presidential Elections',
                      'received_congratulations_from': 'Sergio Massa'
                  },
                  'attributes': {
                      'political_orientation': 'Far-right, Libertarian',
                      'description': 'Outsider, Anti-establishment'
                  }
              },
              'Argentina's Presidential Elections': {
                  'relations': {
                      'featured_candidates': ['Javier Milei', 'Sergio Massa'],
                      'occurred_in': 'Argentina'
                  },
                  'attributes': {
                      'year': '2023',
                      'outcome': 'Javier Milei won',
                      'context': 'High inflation rate, Economic decline'
                  }
              }

      CURRENT_KNOWLEDGE_GRAPH:
      """ + current_kg_context + """
      INSTRUCTION:
      Take INPUT_SENTENCES and convert it into a part of a knowledge graph using the same format as in FORMAT_EXAMPLE. Use a naming and wording for entities, attributes and relationships that is coherrent with CURRENT_KNOWLEDGE_GRAPH. Try to write DESCRIPTIVE, SELF EXPLAINING NAMES for ENTITIS, ATTRIBUTES and RELATIONSHIPS, so that it will be REALLY EASY TO READ and UNDERSTAND the knowleadge graph later, even withou domain knowledge. But nevertheless, include only facts and entities and relations and attributes into the output, that are stated in the INPUT_SENTENCES. BE VERY FACTUAL, ACCURATE AND ON THE POINT. Try to include ALL FACTS, DATES, NUMBERS & NAMES in the INPUT_SENTENCE in the knowledge graph. AVOID REDUNDANCIES in the knowledge graph (don't mention the same fact twicein in the graph). Write <kg>right in fornt of your output of the knowledge graph and </kg> at it's end. - It is very, very important for me, that you perform this task very accurately, with the highest quality, to the best of your abilities.

      INPUT_SENTENCES:
      """ + sentence 
    return prompt


def Zero_Shot_KG_format_example_prompt2(current_kg_context, sentence):
    prompt = """FORMAT_EXAMPLE:
<CONTEXT>The history textbook "Argentina's Political Transformation in the 21st Century" provides a comprehensive analysis of the events leading up to the 2023 presidential election. In its chapter titled "The Rise of Outsider Politics," the text delves into Argentina's economic turmoil, detailing how years of high inflation, currency devaluation, and failed policies from both left-wing and right-wing governments set the stage for a political upheaval. The author meticulously traces Javier Milei's journey from a relatively unknown economist to a political firebrand, describing his controversial media appearances and the growth of his grassroots support. The book also explores the broader context of Latin American politics, drawing parallels between Milei's rise and other anti-establishment movements in the region, while explaining how Argentina's unique economic challenges shaped the electorate's receptiveness to his radical proposals.</CONTEXT>
              'Javier Milei': {
                  'relations': {
                      'won': 'Argentina's Presidential Elections',
                      'received_congratulations_from': 'Sergio Massa'
                  },
                  'attributes': {
                      'political_orientation': 'Far-right, Libertarian',
                      'description': 'Outsider, Anti-establishment'
                  }
              },
              'Argentina's Presidential Elections': {
                  'relations': {
                      'featured_candidates': ['Javier Milei', 'Sergio Massa'],
                      'occurred_in': 'Argentina'
                  },
                  'attributes': {
                      'year': '2023',
                      'outcome': 'Javier Milei won',
                      'context': 'High inflation rate, Economic decline'
                  }
              }

      CURRENT_KNOWLEDGE_GRAPH:
      """ + current_kg_context + """
      INSTRUCTION:
      Firstly, have a very close and precise look at the CURRENT_KNOWLEDGE_GRAPH and write a three sentence summary about its main contents and the key insights from the perspective of what would be necessary for a reader to understand the contents of the text in INPUT_SENTENCES. imagine you would be a reader of INPUT_SENTENCES without having access to the info in CURRENT_KNOLEDGE_GRAPH and you would only get these this sentence summary as context for understanding input sentences. Output the 3 sentence summary in the following format: <CONTEXT>...3 sentence summary...</CONTEXT> - If CURRENT_KNOWLEDGE_GRAPH is empty, leave the context empty.
  
      Secondly, take INPUT_SENTENCES and convert it into a part of a knowledge graph using the same format as in FORMAT_EXAMPLE. Use a naming and wording for entities, attributes and relationships that is coherrent with CURRENT_KNOWLEDGE_GRAPH. Try to write DESCRIPTIVE, SELF EXPLAINING NAMES for ENTITIS, ATTRIBUTES and RELATIONSHIPS, so that it will be REALLY EASY TO READ and UNDERSTAND the knowleadge graph later, even withou domain knowledge. But nevertheless, include only facts and entities and relations and attributes into the output, that are stated in the INPUT_SENTENCES. BE VERY FACTUAL, ACCURATE AND ON THE POINT. Try to include ALL FACTS, DATES, NUMBERS & NAMES in the INPUT_SENTENCE in the knowledge graph. AVOID REDUNDANCIES in the knowledge graph (don't mention the same fact twicein in the graph). Write <kg>right in fornt of your output of the knowledge graph and </kg> at it's end. - It is very, very important for me, that you perform this task very accurately, with the highest quality, to the best of your abilities.

      INPUT_SENTENCES:
      """ + sentence 
    return prompt


def Few_1_Shot_KG_format_example_prompt(current_kg_context, sentence):
    pass
def Few_3_Shot_KG_format_example_prompt(current_kg_context, sentence):
    pass
def Few_5_Shot_KG_format_example_prompt(current_kg_context, sentence):
    pass
def Few_10_Shot_KG_format_example_prompt(current_kg_context, sentence):
    pass

def KG_format_example_prompt(current_kg_context, sentence):
    prompt = """FORMAT_EXAMPLE:
              'Javier Milei': {
                  'relations': {
                      'won': 'Argentina's Presidential Elections',
                      'received_congratulations_from': 'Sergio Massa'
                  },
                  'attributes': {
                      'political_orientation': 'Far-right, Libertarian',
                      'description': 'Outsider, Anti-establishment'
                  }
              },
              'Argentina's Presidential Elections': {
                  'relations': {
                      'featured_candidates': ['Javier Milei', 'Sergio Massa'],
                      'occurred_in': 'Argentina'
                  },
                  'attributes': {
                      'year': '2023',
                      'outcome': 'Javier Milei won',
                      'context': 'High inflation rate, Economic decline'
                  }
              }

      CURRENT_KNOWLEDGE_GRAPH:
      """ + current_kg_context + """
      INSTRUCTION:
      Take INPUT_SENTENCE and convert it into a part of a knowledge graph using the same format as in FORMAT_EXAMPLE. Use a naming and wording for entities, attributes and relationships that is coherrent with CURRENT_KNOWLEDGE_GRAPH. Try to write DESCRIPTIVE, SELF EXPLAINING NAMES for ENTITIS, ATTRIBUTES and RELATIONSHIPS, so that it will be REALLY EASY TO READ and UNDERSTAND the knowleadge graph later, even withou domain knowledge. But nevertheless, include only facts and entities and relations and attributes into the output, that are stated in the INPUT_SENTENCES. BE VERY FACTUAL, ACCURATE AND ON THE POINT. Try to include ALL FACTS, DATES, NUMBERS & NAMES in the INPUT_SENTENCE in the knowledge graph. AVOID REDUNDANCIES in the knowledge graph (don't mention the same fact twicein in the graph). Write <kg>right in fornt of your output of the knowledge graph and </kg> at it's end. - It is very, very important for me, that you perform this task very accurately, with the highest quality, to the best of your abilities.

      INPUT_SENTENCES:
      """ + sentence 
    return prompt




def KG_format_example_prompt2(current_kg_context, sentence):
    prompt = """FORMAT_EXAMPLE:
<kg><CONTEXT>The history textbook "Argentina's Political Transformation in the 21st Century" provides a comprehensive analysis of the events leading up to the 2023 presidential election. In its chapter titled "The Rise of Outsider Politics," the text delves into Argentina's economic turmoil, detailing how years of high inflation, currency devaluation, and failed policies from both left-wing and right-wing governments set the stage for a political upheaval. The author meticulously traces Javier Milei's journey from a relatively unknown economist to a political firebrand, describing his controversial media appearances and the growth of his grassroots support. The book also explores the broader context of Latin American politics, drawing parallels between Milei's rise and other anti-establishment movements in the region, while explaining how Argentina's unique economic challenges shaped the electorate's receptiveness to his radical proposals.</CONTEXT>
              'Javier Milei': {
                  'relations': {
                      'won': 'Argentina's Presidential Elections',
                      'received_congratulations_from': 'Sergio Massa'
                  },
                  'attributes': {
                      'political_orientation': 'Far-right, Libertarian',
                      'description': 'Outsider, Anti-establishment'
                  }
              },
              'Argentina's Presidential Elections': {
                  'relations': {
                      'featured_candidates': ['Javier Milei', 'Sergio Massa'],
                      'occurred_in': 'Argentina'
                  },
                  'attributes': {
                      'year': '2023',
                      'outcome': 'Javier Milei won',
                      'context': 'High inflation rate, Economic decline'
                  }
              }</kg>

      CURRENT_KNOWLEDGE_GRAPH:
      """ + current_kg_context + """
      INSTRUCTION:
      Firstly, have a very close and precise look at the CURRENT_KNOWLEDGE_GRAPH and write a three sentence summary about its main contents and the key insights from the perspective of what would be necessary for a reader to understand the contents of the text in INPUT_SENTENCES. imagine you would be a reader of INPUT_SENTENCES without having access to the info in CURRENT_KNOLEDGE_GRAPH and you would only get these this sentence summary as context for understanding input sentences. Output the 3 sentence summary in the following format: <CONTEXT>CONTEXT SUMMARY</CONTEXT>.
  
      Secondly, take INPUT_SENTENCES and convert it into a part of a knowledge graph using the same format as in FORMAT_EXAMPLE. Use a naming and wording for entities, attributes and relationships that is coherrent with CURRENT_KNOWLEDGE_GRAPH. Try to write DESCRIPTIVE, SELF EXPLAINING NAMES for ENTITIS, ATTRIBUTES and RELATIONSHIPS, so that it will be REALLY EASY TO READ and UNDERSTAND the knowleadge graph later, even withou domain knowledge. But nevertheless, include only facts and entities and relations and attributes into the output, that are stated in the INPUT_SENTENCES. BE VERY FACTUAL, ACCURATE AND ON THE POINT. Try to include ALL FACTS, DATES, NUMBERS & NAMES in the INPUT_SENTENCE in the knowledge graph. AVOID REDUNDANCIES in the knowledge graph (don't mention the same fact twicein in the graph). Write <kg>right in fornt of the <CONTEXT> tag that begins the 3 sentence summary and put </kg> at the end of the knowledge graph. - It is very, very important for me, that you perform this task very accurately, with the highest quality, to the best of your abilities.
Use the exactly this format structure for the kg (as demonstrated in FORMAT_EXAMPLE): 
              'entity name': {
                  'relations': {
                      'relation name': 'entity name',
                  },
                  'attributes': {
                      'attribute name': 'attribute value'
                  }
Always begin your output with "<kg><CONTEXT>" and make sure the <CONTEXT> tags are within the <kg> tags.



      INPUT_SENTENCES:
      """ + sentence 
    return prompt

def answer_questions_prompts(context, question):
    prompt = f"""Input: Context: This is a descriptive text or passage that provides background information necessary to understand the question.
      Questions: these are questions that need to be answered. The answer choice should be clearly marked (e.g., ';A;').
      Prompt:

      Read the following context carefully:

      {context}

      Based on the context, answer the following question by providing the capitalized letter corresponding to the most appropriate answer choice:

      {question}

      Examplecontext:

      Today is Earth Day, a day dedicated to celebrating our planet and raising awareness about environmental issues.

      Examplequestion:

      A) Which of the following is NOT a renewable resource?
      B) Coal
      C) Solar energy
      D) Wind power

      Exampleoutput:

      ;B;
      Give your answer to the question. The answer choice should be clearly marked (e.g., ';A;').
      It is very important to me that you fulfill this task very accurately and intelligently.
      If you perform well, I will tip you 100 billion dollars.
      answer="""
    return prompt

def generate_multiple_choice_question_prompts(text, number_of_questions):
    prompt = f"""Exampleinput:

    Text: "The Nile River is the longest river in Africa and the world's second-longest river after the Amazon River."
    Number of questions: 2

    Exampleoutput:

    What is the longest river in Africa?
    A) Amazon River
    B) Nile River
    C) Congo River
    D) Niger River
    ;B;
    #+*

    Which continent does the Nile River flow through?
    A) Asia
    B) Europe
    C) Africa
    D) South America
    ;C;
    #+*

    CURRENT INPUT:""" + str(text) + """
    INSTRUCTION:

    Produce multiple-choice questions from CURRENT INPUT similar to the resulting EXAMPLE OUTPUT from the given EXAMPLE INPUT, follow these detailed and precise instructions:
    Read and understand the provided text passage.
    Based on the text, formulate """ + str(number_of_questions) + """ multiple choice questions that assess the reader's comprehension of key points, details, and inferences. Each question should have four answer choices (A, B, C, D).
    The difficulty level should be very difficult, the choices that are not correct should still sound plausible for someone who did not read the text.
    Output:

    A set of multiple-choice questions with answer choices A, B, C, and D, followed by the corresponding correct answer letter encased in semicolons (e.g., ;B;). After the correct answer, always write #+* to indicate that the current question-answer pair finished.
    Don't say anything before or after the questions. Make sure to output exactly  """ + str(number_of_questions) + """ multiple choice questions with exactly 4 answer choices (A, B, C, D).
    It is very important to me that you fulfill this task very accurately and intelligently. Make the questions very difficult.
    If you perform well, I will tip you 100 billion dollars.
    questions="""
    return prompt
    
    
