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
  Perform a brief yet intelligent & thorough analysis (20 to 40 words) of the textÃÂÃÂÃÂÃÂ¢ÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂs writing style, rhythm, genre, and more, carefully considering the distinctive features that typify its literary and communicative approach. Reflect on the following aspects:

  Format and Genre: How does the text situate itself within specific genres or sub-genres such as epic, tragedy, comedy, tragicomedy, mystery, thriller, horror, romance, speculative fiction (including fantasy, science fiction, and dystopian), magical realism, young adult (YA), childrenÃÂÃÂÃÂÃÂ¢ÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂs literature, flash fiction, creative nonfiction, biographical works, poetry (sonnet, haiku, free verse), historical narrative, legal or medical analysis, academic journal, self-help, how-to guides, or culinary reviews?
  Writing Style: Which terms best describe the text's style? Is it formal, informal, academic, conversational, ornate, sparse, lyrical, dry, satirical, or colloquial? Does it utilize rich figurative language, complex syntactic structures, discipline-specific terminology, or maintain simplicity and clarity?
  Rhythm and Flow: Evaluate the pacing and smoothness of the text. Does it engage with rapid, succinct sentences, or unfold through leisurely, intricate phrasing? How does the rhythm align with the genre and content, shaping the overall effect and engagement of the piece?
  Tone and Voice: Determine the dominant tone (e.g., hopeful, cynical, impartial, authoritative, whimsical, grave, sarcastic) and the nature of the authorial voice (e.g., intimate, distant, introspective, enthusiastic). How do these elements enrich the textÃÂÃÂÃÂÃÂ¢ÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂs unique character?
Comparison and Guidance for Writers: How could a literature expert concisely convey the text's stylistic essence to an author wishing to replicate this style in new works across diverse topics? Emphasize critical stylistic features such as sentence structure, lexicon, tone, and the implementation of narrative techniques or rhetorical devices that are quintessential for capturing the styleÃÂÃÂÃÂÃÂ¢ÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂs core.
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

    You are given an INPUT_TEXT which is a sample from the beginning of a scientific paper, a book, a blog post, a website article, or a similar piece of writing. Your task is to analyze this text and extract the following information, if present, and format it as specified:

    1. Title Extraction:
       - Carefully examine the INPUT_TEXT to identify the title. Titles are often prominently displayed at the beginning, perhaps in a larger or bolder font, or set apart from the main text.
       - If you find a title, output it within <TITLE> tags like this: <TITLE>Extracted Title Here</TITLE>.
       - If no title is apparent, simply skip this step and do not output anything for the title.

       Example:
       If the input text starts with:
       "
    **The Impact of Artificial Intelligence on Modern Healthcare**

    In recent years, the field of healthcare has witnessed...
    "

        Your output should be:
        <TITLE>The Impact of Artificial Intelligence on Modern Healthcare</TITLE>

    2. Author Extraction:
       - Look for names of authors, which might be listed near the title or at the beginning of a paper's introduction.
       - If you find author names, output them within <AUTHORS> tags, separating multiple authors with semicolons, like this: <AUTHORS>First Name1 Last Name1; First Name2 Last Name2; ...</AUTHORS>.
       - If no authors are found, skip this step.

       Example:
        If the input text includes:
        "
        ...
        By John Smith, Maria Garcia, and Alice Johnson
        Department of Computer Science...
        "

        Your output should be:
        <AUTHORS>John Smith; Maria Garcia; Alice Johnson</AUTHORS>

    3. Genre and Style Analysis:
       - After extracting the title and authors (if found), perform a detailed analysis of the text's genre and writing style.
       - **Genre:** Determine the genre or sub-genre of the text. Output the genre within <GENRE> tags. Use a comma-separated list if multiple genres apply.
          - Consider the following list of genres, but also use your judgment to classify the text appropriately if it doesn't fit neatly into these categories:
              -  Epic, Tragedy, Comedy, Tragicomedy, Mystery, Thriller, Horror, Romance, Speculative Fiction (including Fantasy, Science Fiction, Dystopian), Magical Realism, Young Adult (YA), Children's Literature, Flash Fiction, Creative Nonfiction, Biographical Works, Poetry (Sonnet, Haiku, Free Verse), Historical Narrative, Legal Analysis, Medical Analysis, Academic Journal, Self-Help, How-To Guides, Culinary Reviews.

       Example:
        If the input text is clearly from a scientific paper about a new medical treatment, your output might be:
        <GENRE>Medical Analysis, Academic Journal</GENRE>

       - **Style:** Describe the writing style in a few sentences (around 20-40 words). Output this description within <STYLE> tags.
          - Consider these aspects of style:
              - **Formality:** Is it formal, informal, academic, conversational?
              - **Language:** Is it ornate, sparse, lyrical, dry, satirical, colloquial? Does it use figurative language, complex sentences, or specialized terminology?
              - **Rhythm:** Is the pacing fast or slow? Are sentences short and direct or long and complex?
              - **Tone:** Is the tone hopeful, cynical, impartial, authoritative, whimsical, grave, sarcastic?
              - **Voice:** Is the authorial voice intimate, distant, introspective, enthusiastic?

       Example:
        If the input text uses formal language, complex sentences, and specialized terminology in an objective tone, your output might be:
        <STYLE>The writing style is formal and academic, employing specialized terminology and complex sentence structures. The tone is objective and impartial, characteristic of scholarly research papers.</STYLE>

    Here are a few complete examples demonstrating the full extraction process for different types of text:

    Example 1:

    INPUT_TEXT:
    "
    **Unveiling the Mysteries of the Deep Sea: A Journey into the Unknown**
    *By Dr. Emily Carter and Prof. James Williams*

    The ocean's depths have long captivated the human imagination. In this book, we embark on a thrilling...
    "

    OUTPUT:
    <TITLE>Unveiling the Mysteries of the Deep Sea: A Journey into the Unknown</TITLE>
    <AUTHORS>Dr. Emily Carter; Prof. James Williams</AUTHORS>
    <GENRE>Creative Nonfiction, Science</GENRE>
    <STYLE>The style is engaging and slightly informal, aimed at a broad audience interested in science. The tone is enthusiastic and adventurous, reflecting the book's exploratory nature.</STYLE>

    Example 2:

    INPUT_TEXT:
    "
    The efficacy of blockchain technology in securing digital identities.
    Robert Miller; Sarah Chen; David Lee
    In recent years, digital identity theft has become an increasingly...
    "

    OUTPUT:
    <TITLE>The efficacy of blockchain technology in securing digital identities.</TITLE>
    <AUTHORS>Robert Miller; Sarah Chen; David Lee</AUTHORS>
    <GENRE>Academic Journal, Technology</GENRE>
    <STYLE>The style is formal and academic, utilizing technical jargon related to blockchain and digital security. The tone is objective and analytical, typical of scholarly research.</STYLE>

    Example 3:

    INPUT_TEXT:
    "
    The Enchanted Forest: A Tale of Friendship and Magic
    Once upon a time, in a land far, far away, there lived a young girl named Lily...
    "

    OUTPUT:
    <TITLE>The Enchanted Forest: A Tale of Friendship and Magic</TITLE>
    <GENRE>Children's Literature, Fantasy</GENRE>
    <STYLE>The style is simple, imaginative, and uses narrative language suitable for children. The tone is whimsical and inviting, characteristic of a fairy tale.</STYLE>
    
    Example 4:
    
    INPUT_TEXT:
    "
    **Mindful Cooking: Recipes to Nourish Body and Soul**
    *By Sarah Johnson*

    Welcome to the world of mindful cooking! In this book, we'll explore how to transform your kitchen into a sanctuary of peace and nourishment. This is more than just a cookbook; it's a guide to cultivating a deeper connection with yourself and the food you eat. Each recipe is crafted not only to delight your taste buds but also to enhance your well-being. Let's begin our journey with a simple yet profound recipe: the Gratitude Bowl. Ingredients: 1 cup of quinoa, 2 cups of mixed greens, 1 avocado, a handful of cherry tomatoes, and a sprinkle of your favorite seeds. Preparation: Start by cooking the quinoa according to package instructions. While it simmers, take a moment to reflect on the journey of each ingredient from farm to table. As you chop the vegetables, focus on their colors and textures, engaging all your senses. Once the quinoa is cooked, combine all ingredients in a bowl. Before you enjoy, take a deep breath and express gratitude for the nourishment before you. This practice not only enriches your meal but also nurtures your soul.
    "

    OUTPUT:
    <TITLE>Mindful Cooking: Recipes to Nourish Body and Soul</TITLE>
    <AUTHORS>Sarah Johnson</AUTHORS>
    <GENRE>Self-Help, Culinary</GENRE>
    <STYLE>The style is warm, inviting, and instructional, blending culinary guidance with mindfulness practices. The tone is gentle and encouraging, aimed at readers seeking both physical and spiritual nourishment through cooking.</STYLE>

    Example 5:

    INPUT_TEXT:
    "
    **The Galactic Federation: A New Era**
    *By Alex Rivera*

    Chapter 1: The Awakening

    The year is 2342. Humanity has finally achieved interstellar travel, and with it, the long-awaited contact with the Galactic Federation, a conglomerate of advanced alien civilizations. Our story begins on Neo-Earth, a terraformed planet orbiting a distant star. Here, amidst towering cities and lush alien landscapes, a young cadet named Jax is about to embark on a journey that will change the course of history. Jax, with his unparalleled piloting skills and a thirst for adventure, has always dreamed of exploring the stars. Little does he know that his acceptance into the Federation's elite training program is just the first step on a path fraught with danger, intrigue, and discovery. As he navigates the challenges of the academy, Jax forms alliances with cadets from across the galaxy, each with their own unique abilities and backgrounds. Together, they must unravel a conspiracy that threatens the very fabric of the Federation. Their mission will take them to uncharted territories, where they will encounter ancient mysteries and face adversaries more powerful than they could ever imagine.
    "

    OUTPUT:
    <TITLE>The Galactic Federation: A New Era</TITLE>
    <AUTHORS>Alex Rivera</AUTHORS>
    <GENRE>Science Fiction</GENRE>
    <STYLE>The style is narrative-driven and immersive, characteristic of science fiction adventures. It employs vivid descriptions of futuristic settings and hints at a larger, unfolding plot. The tone is adventurous and slightly ominous, setting the stage for a story filled with exploration and conflict.</STYLE>

    Now, here is the INPUT_TEXT you provided, and you will analyze it accordingly:

    INPUT_TEXT:
    """ + input_text + """
    Analyze the INPUT_TEXT according to the above INSTRUCTIONS and provide the output in the specified format:
    """
    
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
      MAKE the kg after </CONTEXT> in OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES as detailed, long and extensive as possible within the contraint of staying factual w.r.t. the INPUT_SENTENCES! LONG AND DETAILED! 
      INPUT_SENTENCES:
      """ + sentence +"\nOUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES:"
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




def KG_format_example_prompt_many_examples_long_document(current_kg_context, sentence):
    prompt = """OUTPUT_FORMAT_EXAMPLE_1:
CURRENT_KNOWLEDGE_GRAPH:
'Argentina': {
    'relations': {
        'experienced': 'Economic Turmoil',
        'saw_rise_of': 'Public Discontent'
    },
    'attributes': {
        'description': 'South American nation',
        'economic_status': 'High inflation, Currency devaluation'
    }
},
'Economic Turmoil': {
    'relations': {
        'affected': 'Argentina',
        'led_to': 'Public Discontent'
    },
    'attributes': {
        'period': 'Years leading up to 2023',
        'impact': 'Widespread economic hardship'
    }
},
'Public Discontent': {
    'relations': {
        'resulted_in': 'Desire for Political Change'
    },
    'attributes': {
        'cause': 'Failed policies from traditional parties'
    }
}

INPUT_SENTENCES:
"The 2023 Argentine presidential election marked a pivotal moment in the nation's history. Javier Milei, an economist known for his radical libertarian views and fiery rhetoric, secured a landslide victory. His win was a significant departure from traditional politics, unseating the long-dominant Peronist party."

OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES:
<kg><CONTEXT>Previously, Argentina faced prolonged economic challenges that led to widespread public dissatisfaction with traditional political parties. The populace's desire for significant change set the stage for outsider candidates to gain prominence. Understanding this context is essential to grasp the impact of the 2023 election results.</CONTEXT>
                  'Javier Milei': {
                      'relations': {
                          'won': "Argentina's Presidential Election 2023",
                          'unseated': 'Peronist Party'
                      },
                      'attributes': {
                          'occupation': 'Economist',
                          'political_orientation': 'Radical Libertarian',
                          'description': 'Known for fiery rhetoric'
                      }
                  },
                  "Argentina's Presidential Election 2023": {
                      'relations': {
                          'featured_candidates': ['Javier Milei', 'Peronist Party Candidate'],
                          'represented': 'Departure from Traditional Politics'
                      },
                      'attributes': {
                          'year': '2023',
                          'outcome': 'Javier Milei won by landslide',
                          'significance': 'Pivotal moment in nationÃÂÃÂs history'
                      }
                  },
                  'Peronist Party': {
                      'relations': {
                          'was_unseated_by': 'Javier Milei'
                      },
                      'attributes': {
                          'status': 'Long-dominant political party'
                      }
                  }
</kg>

OUTPUT_FORMAT_EXAMPLE_2:
CURRENT_KNOWLEDGE_GRAPH:
'Stars': {
    'relations': {
        'form_from': 'Nebulae',
        'evolve_through': 'Stellar Lifecycle'
    },
    'attributes': {
        'composition': 'Hydrogen and helium gases',
        'formation_process': 'Gravitational collapse'
    }
},
'Nebulae': {
    'relations': {
        'are_birthplaces_of': 'Stars'
    },
    'attributes': {
        'description': 'Clouds of gas and dust in space'
    }
}

INPUT_SENTENCES:
"Most stars, including our Sun, are found along the main sequence, a continuous band on the Hertzsprung-Russell diagram where stars spend the majority of their lifetimes fusing hydrogen into helium. Above the main sequence lie the red giants and supergiants, massive stars that have exhausted the hydrogen in their cores and expanded in size. Below the main sequence are white dwarfs, the dense remnants of low-mass stars that have shed their outer layers."

OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES:
<kg><CONTEXT>Earlier, we discussed how stars form from nebulae and begin their evolutionary journey. This process leads to various stages in a star's life, each characterized by different physical properties. Having this background helps in understanding their placement on the Hertzsprung-Russell diagram.</CONTEXT>
                  'Main Sequence Stars': {
                      'relations': {
                          'are_found_on': 'Hertzsprung-Russell Diagram',
                          'include': 'Our Sun'
                      },
                      'attributes': {
                          'process': 'Fusing hydrogen into helium',
                          'lifetime_phase': 'Majority of starsÃÂÃÂ lifespans'
                      }
                  },
                  'Red Giants and Supergiants': {
                      'relations': {
                          'lie_above': 'Main Sequence on Hertzsprung-Russell Diagram',
                          'evolved_from': 'Stars that exhausted core hydrogen'
                      },
                      'attributes': {
                          'size': 'Expanded',
                          'stage': 'Advanced stellar evolution'
                      }
                  },
                  'White Dwarfs': {
                      'relations': {
                          'lie_below': 'Main Sequence on Hertzsprung-Russell Diagram',
                          'are_remnants_of': 'Low-mass stars'
                      },
                      'attributes': {
                          'description': 'Dense and compact',
                          'process': 'Shed outer layers'
                      }
                  },
                  'Hertzsprung-Russell Diagram': {
                      'relations': {
                          'plots': ['Luminosity', 'Temperature'],
                          'shows': ['Main Sequence', 'Red Giants', 'White Dwarfs']
                      },
                      'attributes': {
                          'type': 'Graphical tool in astrophysics'
                      }
                  }
</kg>


OUTPUT_FORMAT_EXAMPLE_3:
CURRENT_KNOWLEDGE_GRAPH:
'Nutrients': {
    'relations': {
        'classified_into': ['Macronutrients', 'Micronutrients']
    },
    'attributes': {
        'definition': 'Substances needed for growth and health'
    }
},
'Macronutrients': {
    'relations': {
        'include': ['Proteins', 'Carbohydrates', 'Fats']
    },
    'attributes': {
        'required_in': 'Large amounts'
    }
},
'Fats': {
    'relations': {
        'divided_into': ['Saturated Fats', 'Unsaturated Fats']
    },
    'attributes': {
        'function': 'Energy storage, Cell structure'
    }
}

INPUT_SENTENCES:
"Omega-3 fatty acids are essential nutrients critical for maintaining heart and brain health. These polyunsaturated fats cannot be synthesized by the human body and must be obtained through diet. The three primary types are ALA, EPA, and DHA."

OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES:
<kg><CONTEXT>Previously, we learned about the different types of fats within macronutrients, specifically focusing on saturated and unsaturated fats. Understanding the role of unsaturated fats sets the foundation for exploring essential fatty acids that the body needs but cannot produce.</CONTEXT>
                  'Omega-3 Fatty Acids': {
                      'relations': {
                          'are_types_of': 'Polyunsaturated Fats',
                          'include': ['ALA', 'EPA', 'DHA'],
                          'must_be_obtained_from': 'Diet'
                      },
                      'attributes': {
                          'essential_nutrient': True,
                          'health_benefits': ['Heart health', 'Brain health'],
                          'cannot_be_synthesized_by_body': True
                      }
                  },
                  'ALA': {
                      'relations': {
                          'is_a': 'Type of Omega-3 Fatty Acid'
                      },
                      'attributes': {
                          'full_name': 'Alpha-linolenic acid'
                      }
                  },
                  'EPA': {
                      'relations': {
                          'is_a': 'Type of Omega-3 Fatty Acid'
                      },
                      'attributes': {
                          'full_name': 'Eicosapentaenoic acid'
                      }
                  },
                  'DHA': {
                      'relations': {
                          'is_a': 'Type of Omega-3 Fatty Acid'
                      },
                      'attributes': {
                          'full_name': 'Docosahexaenoic acid'
                      }
                  }
</kg>

OUTPUT_FORMAT_EXAMPLE_4:
CURRENT_KNOWLEDGE_GRAPH:
'Lady Isabella': {
    'relations': {
        'betrothed_to': 'Sir Reginald',
        'resides_in': 'Meadowbrook'
    },
    'attributes': {
        'status': 'Noblewoman',
        'reputation': 'Fairest in the land'
    }
},
'Sir Reginald': {
    'relations': {
        'engaged_to': 'Lady Isabella',
        'planning': 'Lavish Celebration'
    },
    'attributes': {
        'status': 'Nobleman',
        'lineage': 'Esteemed'
    }
},
'Meadowbrook': {
    'relations': {
        'is_home_to': ['Lady Isabella', 'Sir Reginald']
    },
    'attributes': {
        'description': 'Quaint hamlet adorned with spring blossoms'
    }
}

INPUT_SENTENCES:
"Yet, her heart belonged to Marcus, a poet of humble birth whose verses stirred her very soul. As spring blossoms adorned the countryside, whispers of their secret affection spread like wildfire. Under the moon's soft glow, Isabella and Marcus exchanged tokens of their forbidden love, each meeting fraught with both joy and despair."

OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES:
<kg><CONTEXT>Previously, Lady Isabella was betrothed to Sir Reginald, a match that pleased their families and society. The setting is the idyllic Meadowbrook, where appearances and social expectations hold great importance. This context is crucial to understanding the conflict arising from Isabella's true feelings.</CONTEXT>
                  'Lady Isabella': {
                      'relations': {
                          'in_love_with': 'Marcus',
                          'exchanged_tokens_with': 'Marcus'
                      },
                      'attributes': {
                          'emotional_state': 'Torn between duty and love',
                          'description': 'Fairest in the land'
                      }
                  },
                  'Marcus': {
                      'relations': {
                          'loves': 'Lady Isabella',
                          'wrote_verses_for': 'Lady Isabella'
                      },
                      'attributes': {
                          'occupation': 'Poet',
                          'birth_status': 'Humble',
                          'talent': 'Verses that stir the soul'
                      }
                  },
                  'Secret Affection': {
                      'relations': {
                          'between': ['Lady Isabella', 'Marcus'],
                          'became_known_as': 'Whispers spreading like wildfire'
                      },
                      'attributes': {
                          'nature': 'Forbidden love',
                          'emotions': ['Joy', 'Despair']
                      }
                  },
                  'Meetings': {
                      'relations': {
                          'occurred_under': "Moon's soft glow",
                          'involved': ['Lady Isabella', 'Marcus']
                      },
                      'attributes': {
                          'tokens_exchanged': True,
                          'emotional_tension': True
                      }
                  }
</kg>


      INSTRUCTION:
Firstly, **carefully examine the CURRENT_KNOWLEDGE_GRAPH provided below**. Then, **write a concise three-sentence summary** that captures the main contents and key insights of the CURRENT_KNOWLEDGE_GRAPH. This summary should provide essential background information that a reader would need to understand the INPUT_SENTENCES, especially if they have no prior access to the CURRENT_KNOWLEDGE_GRAPH. The summary should focus on events, entities, and relationships that **precede or provide context to the INPUT_SENTENCES**. **Use clear and accessible language**. Output the summary in the following format: **<CONTEXT>CONTEXT SUMMARY</CONTEXT>**.

Secondly, **convert the INPUT_SENTENCES into a segment of a knowledge graph**, using the same format as in the OUTPUT_FORMAT_EXAMPLE. Use naming and wording for entities, attributes, and relationships that are **consistent with the CURRENT_KNOWLEDGE_GRAPH**. Ensure that the names are **descriptive and self-explanatory**, making the knowledge graph easy to read and understand, even without domain knowledge. Include only the **facts, entities, relations, and attributes that are explicitly stated in the INPUT_SENTENCES**. **Be factual, accurate, and concise**. Include **all facts, dates, numbers, and names** from the INPUT_SENTENCES in the knowledge graph. **Avoid redundancies** (do not mention the same fact twice in the graph).

Always begin your output with **"<kg><CONTEXT>"** and make sure the **<CONTEXT>** tags are within the **<kg>** tags, and the context summary is closed with a </CONTEXT> tag. Close the knowledge graph with **"</kg>"**.

Use the exact format structure for the knowledge graph as demonstrated in the OUTPUT_FORMAT_EXAMPLE:
                  'entity name': {
                      'relations': {
                          'relation name': 'entity name',
                      },
                      'attributes': {
                          'attribute name': 'attribute value'
                      }
                  }

Make sure to output **ONLY** the context summary and the knowledge graph in **exactly this format**, as described above, in the section **OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES**. Ensure it represents **ALL KNOWLEDGE from INPUT_SENTENCES** in the knowledge graph format as demonstrated in the OUTPUT_FORMAT_EXAMPLEs.
MAKE the kg after </CONTEXT> in OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES as detailed, long and extensive as possible within the contraint of staying factual w.r.t. the INPUT_SENTENCES! LONG AND DETAILED! 

**It is very important that you perform this task accurately and with the highest quality, following the instructions precisely.**

CURRENT_KNOWLEDGE_GRAPH:
""" + current_kg_context + """
INPUT_SENTENCES:
""" + sentence + """
OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES:"""
    return prompt







def KG_format_example_prompt_many_examples(current_kg_context, sentence): 
    prompt = """OUTPUT_FORMAT_EXAMPLE_1:

INPUT_SENTENCES:
"The 2023 Argentine presidential election marked a pivotal moment in the nation's history. Javier Milei, an economist known for his radical libertarian views and fiery rhetoric, secured a landslide victory. His win was a significant departure from traditional politics, unseating the long-dominant Peronist party."

OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES:
<kg><CONTEXT>The 2023 Argentine presidential election represented a transformative moment in the nationÃÂs history. Javier Milei, a radical libertarian economist known for his passionate rhetoric, achieved a resounding victory. This outcome ended the Peronist partyÃÂs longstanding political dominance.</CONTEXT>
                  'Javier Milei': {
                      'relations': {
                          'won': "Argentina's Presidential Election 2023",
                          'unseated': 'Peronist Party'
                      },
                      'attributes': {
                          'occupation': 'Economist',
                          'political_orientation': 'Radical Libertarian',
                          'description': 'Known for fiery rhetoric'
                      }
                  },
                  "Argentina's Presidential Election 2023": {
                      'relations': {
                          'featured_candidates': ['Javier Milei', 'Peronist Party Candidate'],
                          'represented': 'Departure from Traditional Politics'
                      },
                      'attributes': {
                          'year': '2023',
                          'outcome': 'Javier Milei won by landslide',
                          'significance': 'Pivotal moment in nationÃÂs history'
                      }
                  },
                  'Peronist Party': {
                      'relations': {
                          'was_unseated_by': 'Javier Milei'
                      },
                      'attributes': {
                          'status': 'Long-dominant political party'
                      }
                  }
</kg>

OUTPUT_FORMAT_EXAMPLE_2:

INPUT_SENTENCES:
"Most stars, including our Sun, are found along the main sequence, a continuous band on the Hertzsprung-Russell diagram where stars spend the majority of their lifetimes fusing hydrogen into helium. Above the main sequence lie the red giants and supergiants, massive stars that have exhausted the hydrogen in their cores and expanded in size. Below the main sequence are white dwarfs, the dense remnants of low-mass stars that have shed their outer layers."

OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES:
<kg><CONTEXT>Stars predominantly reside along the main sequence, spending most of their existence fusing hydrogen into helium. Red giants and supergiants appear above this band once their core hydrogen is depleted and they have expanded. White dwarfs are found below, representing the dense remains of low-mass stars that have lost their outer layers.</CONTEXT>
                  'Main Sequence Stars': {
                      'relations': {
                          'are_found_on': 'Hertzsprung-Russell Diagram',
                          'include': 'Our Sun'
                      },
                      'attributes': {
                          'process': 'Fusing hydrogen into helium',
                          'lifetime_phase': 'Majority of starsÃÂ lifespans'
                      }
                  },
                  'Red Giants and Supergiants': {
                      'relations': {
                          'lie_above': 'Main Sequence on Hertzsprung-Russell Diagram',
                          'evolved_from': 'Stars that exhausted core hydrogen'
                      },
                      'attributes': {
                          'size': 'Expanded',
                          'stage': 'Advanced stellar evolution'
                      }
                  },
                  'White Dwarfs': {
                      'relations': {
                          'lie_below': 'Main Sequence on Hertzsprung-Russell Diagram',
                          'are_remnants_of': 'Low-mass stars'
                      },
                      'attributes': {
                          'description': 'Dense and compact',
                          'process': 'Shed outer layers'
                      }
                  },
                  'Hertzsprung-Russell Diagram': {
                      'relations': {
                          'plots': ['Luminosity', 'Temperature'],
                          'shows': ['Main Sequence', 'Red Giants', 'White Dwarfs']
                      },
                      'attributes': {
                          'type': 'Graphical tool in astrophysics'
                      }
                  }
</kg>


OUTPUT_FORMAT_EXAMPLE_3:

INPUT_SENTENCES:
"Omega-3 fatty acids are essential nutrients critical for maintaining heart and brain health. These polyunsaturated fats cannot be synthesized by the human body and must be obtained through diet. The three primary types are ALA, EPA, and DHA."

OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES:
<kg><CONTEXT>Omega-3 fatty acids are vital for heart and brain health. They are polyunsaturated fats that humans cannot produce, necessitating dietary intake. Key forms include ALA, EPA, and DHA.</CONTEXT>
                  'Omega-3 Fatty Acids': {
                      'relations': {
                          'are_types_of': 'Polyunsaturated Fats',
                          'include': ['ALA', 'EPA', 'DHA'],
                          'must_be_obtained_from': 'Diet'
                      },
                      'attributes': {
                          'essential_nutrient': True,
                          'health_benefits': ['Heart health', 'Brain health'],
                          'cannot_be_synthesized_by_body': True
                      }
                  },
                  'ALA': {
                      'relations': {
                          'is_a': 'Type of Omega-3 Fatty Acid'
                      },
                      'attributes': {
                          'full_name': 'Alpha-linolenic acid'
                      }
                  },
                  'EPA': {
                      'relations': {
                          'is_a': 'Type of Omega-3 Fatty Acid'
                      },
                      'attributes': {
                          'full_name': 'Eicosapentaenoic acid'
                      }
                  },
                  'DHA': {
                      'relations': {
                          'is_a': 'Type of Omega-3 Fatty Acid'
                      },
                      'attributes': {
                          'full_name': 'Docosahexaenoic acid'
                      }
                  }
</kg>

OUTPUT_FORMAT_EXAMPLE_4:

INPUT_SENTENCES:
"Yet, her heart belonged to Marcus, a poet of humble birth whose verses stirred her very soul. As spring blossoms adorned the countryside, whispers of their secret affection spread like wildfire. Under the moon's soft glow, Isabella and Marcus exchanged tokens of their forbidden love, each meeting fraught with both joy and despair."

OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES:
<kg><CONTEXT>Lady Isabella loved Marcus, a modest poet whose poetry profoundly moved her. Their secret romance gained notoriety as springÃÂs blossoms adorned the landscape. By moonlight, they exchanged tokens of affection, mingling happiness with sorrow.</CONTEXT>
                  'Lady Isabella': {
                      'relations': {
                          'in_love_with': 'Marcus',
                          'exchanged_tokens_with': 'Marcus'
                      },
                      'attributes': {
                          'emotional_state': 'Torn between duty and love',
                          'description': 'Fairest in the land'
                      }
                  },
                  'Marcus': {
                      'relations': {
                          'loves': 'Lady Isabella',
                          'wrote_verses_for': 'Lady Isabella'
                      },
                      'attributes': {
                          'occupation': 'Poet',
                          'birth_status': 'Humble',
                          'talent': 'Verses that stir the soul'
                      }
                  },
                  'Secret Affection': {
                      'relations': {
                          'between': ['Lady Isabella', 'Marcus'],
                          'became_known_as': 'Whispers spreading like wildfire'
                      },
                      'attributes': {
                          'nature': 'Forbidden love',
                          'emotions': ['Joy', 'Despair']
                      }
                  },
                  'Meetings': {
                      'relations': {
                          'occurred_under': "Moon's soft glow",
                          'involved': ['Lady Isabella', 'Marcus']
                      },
                      'attributes': {
                          'tokens_exchanged': True,
                          'emotional_tension': True
                      }
                  }
</kg>


      INSTRUCTION:
Firstly, write a concise three-sentence summary that captures the main contents and key insights of the INPUT_SENTENCES. This summary should provide essential background information based solely on the INPUT_SENTENCES. The summary should focus on the most important events, entities, and relationships mentioned in the INPUT_SENTENCES, using clear and accessible language. Output the summary in the following format: <CONTEXT>CONTEXT SUMMARY</CONTEXT>.

Secondly, convert the INPUT_SENTENCES into a segment of a knowledge graph, using the same format as in the OUTPUT_FORMAT_EXAMPLE. Use naming and wording for entities, attributes, and relationships that are consistent and descriptive. Include only the facts, entities, relations, and attributes that are explicitly stated in the INPUT_SENTENCES. Be factual, accurate, and concise. Include all facts, dates, numbers, and names from the INPUT_SENTENCES in the knowledge graph. Avoid redundancies.

Always begin your output with "<kg><CONTEXT>" and make sure the <CONTEXT> tags are within the <kg> tags, and the context summary is closed with a </CONTEXT> tag. Close the knowledge graph with "</kg>".

Use the exact format structure for the knowledge graph as demonstrated in the OUTPUT_FORMAT_EXAMPLE:
                  'entity name': {
                      'relations': {
                          'relation name': 'entity name',
                      },
                      'attributes': {
                          'attribute name': 'attribute value'
                      }
                  }

Make sure to output ONLY the context summary and the knowledge graph in exactly this format, as described above, in the section OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES. Ensure it represents ALL KNOWLEDGE from INPUT_SENTENCES in the knowledge graph format as demonstrated in the OUTPUT_FORMAT_EXAMPLEs.

It is very important that you perform this task accurately and with the highest quality, following the instructions precisely.

INPUT_SENTENCES:
""" + sentence + """
OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES:"""
    return prompt




def KG_format_example_prompt_many_examplesplus(current_kg_context, sentence):

    prompt = """
INSTRUCTIONS FOR CREATING KNOWLEDGE GRAPHS FROM TEXT INPUT:

This task involves converting a passage of text (INPUT_SENTENCES) into a concise summary and a knowledge graph (KG) representation. The output must adhere to a specific format and include all facts explicitly stated in the text. Below is a detailed step-by-step guide, followed by multiple examples to demonstrate the required output structure and style.

**KEY INSTRUCTIONS:**

1. **INPUT_SENTENCES:** This is the text you must analyze. It contains information about events, entities, relationships, and attributes.

2. **OUTPUT STRUCTURE:**  
   - **Context Summary (<CONTEXT>):** Write a concise, three-sentence summary that captures the main ideas, events, or concepts in the text. This summary should:
     - Include the most important insights.
     - Focus only on facts explicitly stated in the input.
     - Be clear, factual, and precise.
   - **Knowledge Graph (KG):** Construct a structured knowledge graph using the following format:
     ```
     <kg><CONTEXT>YOUR THREE-SENTENCE SUMMARY HERE</CONTEXT>
                       'Entity Name': {
                           'relations': {
                               'relation_name': 'Entity Name or Value',
                               'another_relation': ['Entity1', 'Entity2']
                           },
                           'attributes': {
                               'attribute_name': 'attribute value',
                               'another_attribute': 'another value'
                           }
                       },
                       'Another Entity': {
                           'relations': {
                               'relation_name': 'Entity or Value'
                           },
                           'attributes': {
                               'attribute_name': 'value'
                           }
                       }
     </kg>
     ```
     - Each entity is enclosed in single quotes.
     - Include both 'relations' and 'attributes' for each entity.
     - Relations link entities or values using descriptive names.
     - Attributes describe key characteristics or properties of entities.

3. **GUIDELINES:**
   - Include all facts, numbers, and entities mentioned in the input text.
   - Ensure every entity in the text is represented with relevant relations and attributes.
   - Avoid inferring information not explicitly stated.
   - Maintain consistent formatting as shown in the examples below.

---

**EXAMPLES:**

**EXAMPLE 1 (History/Politics Domain):**

**INPUT_SENTENCES:**  
"The 2023 Argentine presidential election, held amidst economic turbulence and widespread public discontent, signaled a dramatic shift in the nationÂs political landscape. Javier Milei, a fiercely independent economist celebrated for his radical libertarian views, fiery rhetoric, and unorthodox policy proposals, secured a landmark victory that stunned international observers. Unseating the long-dominant Peronist party, Milei promised to dismantle decades-old structures, introduce sweeping economic reforms, and redefine ArgentinaÂs role on the global stage."

**OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES:**  
<kg><CONTEXT>The 2023 Argentine presidential election marked a transformative moment in the countryÂs history, occurring during significant economic hardship and popular dissatisfaction. Javier Milei, an independent and radical libertarian economist known for fiery rhetoric, won decisively, uprooting entrenched political power. His victory ended the Peronist partyÂs long-standing dominance and signaled a bold new era of economic and political reforms.</CONTEXT>
                  'Javier Milei': {
                      'relations': {
                          'won': "2023 Argentine Presidential Election",
                          'unseated': 'Peronist Party'
                      },
                      'attributes': {
                          'occupation': 'Economist',
                          'political_orientation': 'Radical Libertarian',
                          'description': 'Known for fiery rhetoric and unorthodox proposals',
                          'notability': 'Stunned international observers'
                      }
                  },
                  "2023 Argentine Presidential Election": {
                      'relations': {
                          'featured_candidates': ['Javier Milei', 'Peronist Party Candidate'],
                          'occurred_in': 'Argentina'
                      },
                      'attributes': {
                          'year': '2023',
                          'context': 'Economic turbulence and public discontent',
                          'outcome': 'Javier Milei achieved landmark victory',
                          'significance': 'Dramatic shift in political landscape'
                      }
                  },
                  'Peronist Party': {
                      'relations': {
                          'was_unseated_by': 'Javier Milei'
                      },
                      'attributes': {
                          'description': 'Long-dominant political force in Argentina'
                      }
                  }
</kg>

---

**EXAMPLE 2 (Astronomy Domain):**

**INPUT_SENTENCES:**  
"Most stars, including our Sun, reside along the main sequence of the Hertzsprung-Russell diagram, spending the majority of their lifetimes fusing hydrogen into helium to generate outward pressure balancing gravitational collapse. Above the main sequence glow the red giants and supergiants, massive stars that have depleted their core hydrogen and swollen to enormous sizes, radiating energy across vast distances. Below the main sequence lie the white dwarfs, incredibly dense stellar remnants of low-mass stars that have shed their outer envelopes, leaving behind only their hot, compact cores."

**OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES:**  
<kg><CONTEXT>Stars predominantly inhabit the main sequence on the Hertzsprung-Russell diagram, sustaining themselves by fusing hydrogen into helium. Once their core hydrogen is depleted, some evolve into red giants or supergiants, expanding dramatically and shining brightly above the main sequence. Below it rest the white dwarfs, dense remnants of low-mass stars that have cast off their outer layers.</CONTEXT>
                  'Main Sequence Stars': {
                      'relations': {
                          'are_positioned_on': 'Hertzsprung-Russell Diagram',
                          'include': 'Our Sun'
                      },
                      'attributes': {
                          'primary_energy_source': 'Hydrogen to Helium Fusion',
                          'lifetime_phase': 'Majority of stellar lifespan',
                          'role': 'Balance outward pressure and gravitational collapse'
                      }
                  },
                  'Red Giants and Supergiants': {
                      'relations': {
                          'lie_above': 'Main Sequence',
                          'evolved_from': 'Stars that depleted core hydrogen'
                      },
                      'attributes': {
                          'size': 'Enormous',
                          'energy_output': 'Radiant across vast distances',
                          'evolution_stage': 'Post main-sequence phase'
                      }
                  },
                  'White Dwarfs': {
                      'relations': {
                          'lie_below': 'Main Sequence',
                          'are_remnants_of': 'Low-mass stars'
                      },
                      'attributes': {
                          'description': 'Incredibly dense stellar cores',
                          'origin': 'Formed after shedding outer layers',
                          'state': 'Hot and compact'
                      }
                  },
                  'Hertzsprung-Russell Diagram': {
                      'relations': {
                          'displays': ['Main Sequence Stars', 'Red Giants and Supergiants', 'White Dwarfs']
                      },
                      'attributes': {
                          'type': 'Graphical tool in astrophysics',
                          'parameters_plotted': ['Luminosity', 'Temperature']
                      }
                  }
</kg>

---

**EXAMPLE 3 (Nutrition/Health Domain):**

**INPUT_SENTENCES:**  
"Omega-3 fatty acids are essential polyunsaturated fats that support cardiovascular function, promote cognitive well-being, and help maintain cellular integrity. Humans cannot synthesize these nutrients endogenously, necessitating their acquisition through dietary sources like fatty fish, flax seeds, and walnuts. The three principal types of omega-3sÂALA, EPA, and DHAÂplay unique roles in inflammation modulation, brain development, and overall metabolic health."

**OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES:**  
<kg><CONTEXT>Omega-3 fatty acids are critical, diet-dependent nutrients that bolster heart health, brain function, and cellular maintenance. They cannot be produced by the human body, requiring intake from foods such as fatty fish, flax seeds, and walnuts. The key variantsÂALA, EPA, and DHAÂeach contribute to metabolic balance, inflammatory regulation, and cognitive support.</CONTEXT>
                  'Omega-3 Fatty Acids': {
                      'relations': {
                          'are_types_of': 'Polyunsaturated Fats',
                          'must_be_obtained_from': ['Fatty Fish', 'Flax Seeds', 'Walnuts'],
                          'include': ['ALA', 'EPA', 'DHA']
                      },
                      'attributes': {
                          'essential': True,
                          'health_benefits': ['Cardiovascular support', 'Cognitive well-being', 'Cellular integrity'],
                          'cannot_be_synthesized_by_body': True
                      }
                  },
                  'ALA': {
                      'relations': {
                          'is_a': 'Type of Omega-3 Fatty Acid'
                      },
                      'attributes': {
                          'role': 'Supports metabolic health',
                          'full_name': 'Alpha-linolenic acid'
                      }
                  },
                  'EPA': {
                      'relations': {
                          'is_a': 'Type of Omega-3 Fatty Acid'
                      },
                      'attributes': {
                          'role': 'Modulates inflammation',
                          'full_name': 'Eicosapentaenoic acid'
                      }
                  },
                  'DHA': {
                      'relations': {
                          'is_a': 'Type of Omega-3 Fatty Acid'
                      },
                      'attributes': {
                          'role': 'Supports brain development',
                          'full_name': 'Docosahexaenoic acid'
                      }
                  }
</kg>

---

**EXAMPLE 4 (Literature/Romance Domain):**

**INPUT_SENTENCES:**  
"Within the lush gardens of her familyÂs estate, Lady Isabella longed for Marcus, a humble poet whose verses stirred her soul more profoundly than any courtly speech. As the soft twilight of spring settled over the blossoming orchards, discreet messengers spread whispered tales of their secret trysts. Beneath the moonÂs gentle glow, they exchanged tokens of loveÂpressed flowers, jeweled pendantsÂand vowed unwavering devotion despite the looming specter of social condemnation."

**OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES:**  
<kg><CONTEXT>Lady Isabella, a noblewoman amid luxurious gardens, adored Marcus, a modest poet whose words deeply moved her spirit. Their clandestine romance flourished as springÂs twilight spread across blooming orchards, and secret rumors carried news of their affections. By moonlight, the two lovers shared heartfelt tokens, promising steadfast loyalty despite societyÂs disapproval.</CONTEXT>
                  'Lady Isabella': {
                      'relations': {
                          'in_love_with': 'Marcus',
                          'exchanged_tokens_with': 'Marcus'
                      },
                      'attributes': {
                          'status': 'Noblewoman',
                          'emotional_state': 'Profound longing',
                          'environment': 'Family estateÂs lush gardens'
                      }
                  },
                  'Marcus': {
                      'relations': {
                          'loves': 'Lady Isabella',
                          'inspired': 'Lady IsabellaÂs soul with poetry'
                      },
                      'attributes': {
                          'occupation': 'Poet',
                          'social_origin': 'Humble birth',
                          'talent': 'Verses stirring deep emotion'
                      }
                  },
                  'Secret Romance': {
                      'relations': {
                          'between': ['Lady Isabella', 'Marcus'],
                          'known_through': 'Discreet whispers and messengers'
                      },
                      'attributes': {
                          'nature': 'Forbidden love',
                          'time_frame': 'Spring twilight',
                          'tokens_exchanged': ['Pressed flowers', 'Jeweled pendants']
                      }
                  }
</kg>

---

**EXAMPLE 5 (Mathematics Domain):**

**INPUT_SENTENCES:**  
"In Euclidean geometry, the Pythagorean theorem states that for any right-angled triangle, the square of the hypotenuseÂs length equals the sum of the squares of the other two sides. This relationship, expressed as aÂ² + bÂ² = cÂ², underpins much of classical trigonometry and has countless applications in fields ranging from architecture to navigation. Although attributed to the ancient Greek mathematician Pythagoras, evidence suggests that various civilizations understood this principle long before his time."

**OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES:**  
<kg><CONTEXT>The Pythagorean theorem asserts a fundamental relationship in right-angled triangles: the hypotenuse squared equals the sum of the squares on the other sides. Represented as aÂ² + bÂ² = cÂ², it is integral to Euclidean geometry and underlies key concepts in trigonometry. Though associated with Pythagoras, similar knowledge existed among earlier cultures, influencing mathematics, architecture, and navigation.</CONTEXT>
                  'Pythagorean Theorem': {
                      'relations': {
                          'applies_to': 'Right-angled Triangles',
                          'is_expressed_as': 'aÂ² + bÂ² = cÂ²'
                      },
                      'attributes': {
                          'field': 'Euclidean Geometry',
                          'importance': 'Foundational for trigonometry',
                          'applications': ['Architecture', 'Navigation']
                      }
                  },
                  'Right-angled Triangles': {
                      'relations': {
                          'are_subject_of': 'Pythagorean Theorem'
                      },
                      'attributes': {
                          'defining_property': 'One angle equals 90 degrees'
                      }
                  },
                  'Pythagoras': {
                      'relations': {
                          'is_attributed_with': 'Pythagorean Theorem'
                      },
                      'attributes': {
                          'era': 'Ancient Greek',
                          'reality': 'Principle known earlier by various civilizations'
                      }
                  }
</kg>

---

**EXAMPLE 6 (Physics Domain):**

**INPUT_SENTENCES:**  
"Quantum entanglement is a phenomenon in which two or more particles become intertwined so that their quantum states cannot be described independently, even if they are separated by vast distances. This correlation, a key aspect of quantum mechanics, challenges classical notions of locality and has been experimentally validated through tests such as BellÂs inequality experiments. Today, quantum entanglement underlies emerging technologies like quantum computing, secure quantum communication, and advanced sensing methods."

**OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES:**  
<kg><CONTEXT>Quantum entanglement links the states of multiple particles, making their properties inseparable regardless of distance. This core feature of quantum mechanics defies classical principles and is supported by experimental evidence, notably BellÂs inequality tests. Entanglement underpins cutting-edge applications in quantum computing, secure communications, and sophisticated sensing technologies.</CONTEXT>
                  'Quantum Entanglement': {
                      'relations': {
                          'involves': ['Two or more particles'],
                          'validated_by': "Bell's Inequality Experiments"
                      },
                      'attributes': {
                          'field': 'Quantum Mechanics',
                          'key_characteristic': 'Non-classical correlation over distance',
                          'applications': ['Quantum Computing', 'Secure Quantum Communication', 'Advanced Sensing']
                      }
                  },
                  'Particles': {
                      'relations': {
                          'can_be_entangled_in': 'Quantum Entanglement'
                      },
                      'attributes': {
                          'state': 'Quantum state not independent when entangled'
                      }
                  },
                  "Bell's Inequality Experiments": {
                      'relations': {
                          'test': 'Quantum Entanglement'
                      },
                      'attributes': {
                          'purpose': 'Validate non-local quantum correlations',
                          'implication': 'Contradiction of classical locality'
                      }
                  }
</kg>

---

**ADDITIONAL GUIDANCE:**

- Always begin your output with `<kg><CONTEXT>` and end the context summary with `</CONTEXT>`, that is at max 3 sentences long und uses different words than the input text.
- After the `</CONTEXT>` tag, start listing entities with relations and attributes in the given JSON-like dictionary format.
- Use single quotes for entity names and keys as shown in the examples.
- Ensure that the formatting is consistent and that all tags and quotes are properly closed.
- Include all facts from the INPUT_SENTENCES in either the summary or the KG, or both. The summary is a high-level contextual overview in exactly three sentences. The KG should contain all details available.
- The final output must end with `</kg>`.

MAKE the kg after </CONTEXT> in OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES as detailed, long and extensive as possible! LONG AND DETAILED! 
---

Below is the final section, where the text to process will be placed.

INPUT_SENTENCES:
""" + sentence + """
OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES:
"""
    return prompt







def knowledge_graph_template_with_many_examples_for_long_documents_plus(current_kg_context, sentence):
    prompt = """
INSTRUCTIONS FOR CREATING KNOWLEDGE GRAPHS FROM TEXT INPUT (LONG DOCUMENTS):

This task involves two main steps and must be done meticulously:

1. You will be provided with:
   - A CURRENT_KNOWLEDGE_GRAPH: This is a segment of a knowledge graph (KG) that has already been generated from previous parts of a longer document. It provides context for what has happened before.
   - INPUT_SENTENCES: This is the new piece of text you need to process and integrate into a knowledge graph form.

2. You must produce the following OUTPUT:
   A) A concise three-sentence summary inside <CONTEXT> tags that captures the main contents and key insights of the CURRENT_KNOWLEDGE_GRAPH. If CURRENT_KNOWLEDGE_GRAPH is empty, provide an easily understandable 3 sentences long summary of the INPUT_SENTENCES that uses different phrases.  
      - This summary should describe what has been established in the CURRENT_KNOWLEDGE_GRAPH so far, providing essential background information that a reader would need before reading the INPUT_SENTENCES.  
      - Think of it as a "Previously in this narrative..." style summary.  
      - Focus on the entities, events, and relationships that were previously stated, using clear and accessible language.  
      - Do not summarize the INPUT_SENTENCES here. Summarize the CURRENT_KNOWLEDGE_GRAPH (i.e., the already established context) in exactly three sentences.
      - Write this summary in the <CONTEXT> tags in a language that is factual and easily understandable for a non expert with a high school degree. It should not be longer than 3 sentences.
     

   B) After completing the <CONTEXT> summary (which describes the previous content), you must convert the INPUT_SENTENCES into a knowledge graph segment, following the format shown in the examples below.  
      - The knowledge graph must represent all factual content from the INPUT_SENTENCES.  
      - Use a similar style and formatting as in the examples.  
      - Remain strictly factual and do not add information that is not present in the INPUT_SENTENCES.  
      - Use consistent naming and wording for entities, attributes, and relationships.  
      - Begin the output with <kg><CONTEXT>, end the context summary with </CONTEXT>, and then list all entities and their relations/attributes. Close with </kg>.

3. OUTPUT FORMAT:
   The output must start with:
   ```
   <kg><CONTEXT>YOUR THREE-SENTENCE SUMMARY OF THE CURRENT_KNOWLEDGE_GRAPH HERE</CONTEXT>
                  'Entity Name': {
                      'relations': {
                          'relation_name': 'Entity or Value',
                          ...
                      },
                      'attributes': {
                          'attribute_name': 'value',
                          ...
                      }
                  },
                  'Another Entity': {
                      ...
                  }
   </kg>
   ```

4. IMPORTANT:  
   - The three-sentence summary inside <CONTEXT> should ONLY summarize the CURRENT_KNOWLEDGE_GRAPH (the previously established knowledge), NOT the INPUT_SENTENCES.  
   - After closing the </CONTEXT> tag, create a detailed knowledge graph from the INPUT_SENTENCES that follows the structure of the examples.
   - The KG after </CONTEXT> should be as detailed as possible while remaining factually accurate. Include all entities, relations, attributes explicitly stated in the INPUT_SENTENCES.


--------------------------------------------
EXAMPLES (These examples show how to handle different domains and how to first provide a context summary of previously established knowledge, then produce the new KG segment from new input):

EXAMPLE 1 (History/Politics, Long Document Scenario):

CURRENT_KNOWLEDGE_GRAPH:
'Argentina': {
    'relations': {
        'experienced': 'Economic Turmoil',
        'saw_rise_of': 'Public Discontent'
    },
    'attributes': {
        'description': 'South American nation',
        'economic_status': 'High inflation, Currency devaluation'
    }
},
'Economic Turmoil': {
    'relations': {
        'affected': 'Argentina',
        'led_to': 'Public Discontent'
    },
    'attributes': {
        'period': 'Years leading up to 2023',
        'impact': 'Widespread economic hardship'
    }
},
'Public Discontent': {
    'relations': {
        'resulted_in': 'Desire for Political Change'
    },
    'attributes': {
        'cause': 'Failed policies from traditional parties'
    }
}

INPUT_SENTENCES:
"The 2023 Argentine presidential election marked a pivotal moment in the nation's history. Javier Milei, an economist known for his radical libertarian views and fiery rhetoric, secured a landslide victory. His win was a significant departure from traditional politics, unseating the long-dominant Peronist party."

OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES:
<kg><CONTEXT>Previously, Argentina struggled with persistent economic difficulties, resulting in widespread public dissatisfaction and a growing demand for change. The nations long-standing political forces had failed to address these issues, setting the stage for new leaders to emerge. This established backdrop of unrest and desire for reform is crucial to understanding the significance of the upcoming 2023 election results.</CONTEXT>
                  'Javier Milei': {
                      'relations': {
                          'won': "2023 Argentine Presidential Election",
                          'unseated': 'Peronist Party'
                      },
                      'attributes': {
                          'occupation': 'Economist',
                          'political_orientation': 'Radical Libertarian',
                          'description': 'Known for fiery rhetoric'
                      }
                  },
                  "2023 Argentine Presidential Election": {
                      'relations': {
                          'featured_candidates': ['Javier Milei', 'Peronist Party Candidate']
                      },
                      'attributes': {
                          'year': '2023',
                          'significance': 'Pivotal moment in nations history',
                          'outcome': 'Landslide victory for Javier Milei',
                          'departure_from': 'Traditional Politics'
                      }
                  },
                  'Peronist Party': {
                      'relations': {
                          'was_unseated_by': 'Javier Milei'
                      },
                      'attributes': {
                          'status': 'Long-dominant political party'
                      }
                  }
</kg>


EXAMPLE 2 (Astronomy, Long Document Scenario):

CURRENT_KNOWLEDGE_GRAPH:
'Stars': {
    'relations': {
        'form_from': 'Nebulae',
        'evolve_through': 'Stellar Lifecycle'
    },
    'attributes': {
        'composition': 'Hydrogen and helium',
        'formation_process': 'Gravitational collapse'
    }
},
'Nebulae': {
    'relations': {
        'are_birthplaces_of': 'Stars'
    },
    'attributes': {
        'description': 'Clouds of gas and dust'
    }
}

INPUT_SENTENCES:
"Most stars, including our Sun, are found along the main sequence, a continuous band on the Hertzsprung-Russell diagram where stars spend the majority of their lifetimes fusing hydrogen into helium. Above the main sequence lie the red giants and supergiants, massive stars that have exhausted the hydrogen in their cores and expanded in size. Below the main sequence are white dwarfs, the dense remnants of low-mass stars that have shed their outer layers."

OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES:
<kg><CONTEXT>Previously, we established that stars originate in nebulae and follow a broad evolutionary path known as the stellar lifecycle. They are primarily composed of hydrogen and helium, collapsing under gravity to ignite nuclear fusion. This foundation helps us understand the subsequent classification and placement of stars on the Hertzsprung-Russell diagram.</CONTEXT>
                  'Main Sequence Stars': {
                      'relations': {
                          'are_found_on': 'Hertzsprung-Russell Diagram',
                          'include': 'Our Sun'
                      },
                      'attributes': {
                          'primary_fusion_process': 'Hydrogen into Helium',
                          'typical_lifespan_phase': 'Majority of a stars life'
                      }
                  },
                  'Red Giants and Supergiants': {
                      'relations': {
                          'lie_above': 'Main Sequence',
                          'evolved_from': 'Stars that exhausted core hydrogen'
                      },
                      'attributes': {
                          'size': 'Expanded',
                          'massive': True
                      }
                  },
                  'White Dwarfs': {
                      'relations': {
                          'lie_below': 'Main Sequence',
                          'are_remnants_of': 'Low-mass stars'
                      },
                      'attributes': {
                          'description': 'Dense remnants',
                          'formation_process': 'Shedding of outer layers'
                      }
                  },
                  'Hertzsprung-Russell Diagram': {
                      'relations': {
                          'displays': ['Main Sequence Stars', 'Red Giants and Supergiants', 'White Dwarfs']
                      },
                      'attributes': {
                          'type': 'Graphical tool in astrophysics',
                          'parameters_plotted': ['Luminosity', 'Temperature']
                      }
                  }
</kg>


EXAMPLE 3 (Nutrition/Health, Long Document Scenario):

CURRENT_KNOWLEDGE_GRAPH:
'Nutrients': {
    'relations': {
        'classified_into': ['Macronutrients', 'Micronutrients']
    },
    'attributes': {
        'definition': 'Essential substances for health'
    }
},
'Macronutrients': {
    'relations': {
        'include': ['Proteins', 'Carbohydrates', 'Fats']
    },
    'attributes': {
        'required_in': 'Large amounts'
    }
},
'Fats': {
    'relations': {
        'divided_into': ['Saturated Fats', 'Unsaturated Fats']
    },
    'attributes': {
        'role': 'Energy storage and structural component of cells'
    }
}

INPUT_SENTENCES:
"Omega-3 fatty acids are essential nutrients critical for maintaining heart and brain health. These polyunsaturated fats cannot be synthesized by the human body and must be obtained through diet. The three primary types are ALA, EPA, and DHA."

OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES:
<kg><CONTEXT>Previously, we recognized that nutrients encompass both macronutrients and micronutrients, and that fats are a key macronutrient category. Among fats, unsaturated types are noted for their importance to health. This understanding sets the stage for examining specific essential fatty acids that must be obtained through dietary sources.</CONTEXT>
                  'Omega-3 Fatty Acids': {
                      'relations': {
                          'are_types_of': 'Polyunsaturated Fats',
                          'must_be_obtained_from': 'Diet',
                          'include': ['ALA', 'EPA', 'DHA']
                      },
                      'attributes': {
                          'essential_nutrient': True,
                          'health_benefits': ['Heart health', 'Brain health'],
                          'cannot_be_synthesized_by_body': True
                      }
                  },
                  'ALA': {
                      'relations': {
                          'is_a': 'Type of Omega-3 Fatty Acid'
                      },
                      'attributes': {
                          'full_name': 'Alpha-linolenic acid'
                      }
                  },
                  'EPA': {
                      'relations': {
                          'is_a': 'Type of Omega-3 Fatty Acid'
                      },
                      'attributes': {
                          'full_name': 'Eicosapentaenoic acid'
                      }
                  },
                  'DHA': {
                      'relations': {
                          'is_a': 'Type of Omega-3 Fatty Acid'
                      },
                      'attributes': {
                          'full_name': 'Docosahexaenoic acid'
                      }
                  }
</kg>


EXAMPLE 4 (Literature/Romance, Long Document Scenario):

CURRENT_KNOWLEDGE_GRAPH:
'Lady Isabella': {
    'relations': {
        'betrothed_to': 'Sir Reginald',
        'resides_in': 'Meadowbrook'
    },
    'attributes': {
        'status': 'Noblewoman',
        'reputation': 'Fairest in the land'
    }
},
'Sir Reginald': {
    'relations': {
        'engaged_to': 'Lady Isabella',
        'planning': 'Lavish Celebration'
    },
    'attributes': {
        'status': 'Nobleman',
        'lineage': 'Esteemed'
    }
},
'Meadowbrook': {
    'relations': {
        'is_home_to': ['Lady Isabella', 'Sir Reginald']
    },
    'attributes': {
        'description': 'A quaint hamlet adorned with spring blossoms'
    }
}

INPUT_SENTENCES:
"Yet, her heart belonged to Marcus, a poet of humble birth whose verses stirred her very soul. As spring blossoms adorned the countryside, whispers of their secret affection spread like wildfire. Under the moon's soft glow, Isabella and Marcus exchanged tokens of their forbidden love, each meeting fraught with both joy and despair."

OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES:
<kg><CONTEXT>Previously, Lady Isabella was formally engaged to Sir Reginald, and both resided in the peaceful setting of Meadowbrook. Their union was anticipated to uphold tradition and societal expectations. This backdrop provides the social and emotional tension that frames Isabellas emerging clandestine feelings.</CONTEXT>
                  'Lady Isabella': {
                      'relations': {
                          'in_love_with': 'Marcus',
                          'exchanged_tokens_with': 'Marcus'
                      },
                      'attributes': {
                          'inner_emotion': 'Profound longing',
                          'previous_engagement': 'Sir Reginald'
                      }
                  },
                  'Marcus': {
                      'relations': {
                          'loves': 'Lady Isabella',
                          'wrote_verses_for': 'Lady Isabella'
                      },
                      'attributes': {
                          'occupation': 'Poet',
                          'birth_status': 'Humble',
                          'artistic_quality': 'Verses that stirred Isabellas soul'
                      }
                  },
                  'Forbidden Love': {
                      'relations': {
                          'involved': ['Lady Isabella', 'Marcus']
                      },
                      'attributes': {
                          'timing': 'Spring blossoms, under the moons glow',
                          'spread_by': 'Whispers like wildfire',
                          'emotions': ['Joy', 'Despair']
                      }
                  },
                  'Tokens of Affection': {
                      'relations': {
                          'exchanged_between': ['Lady Isabella', 'Marcus']
                      },
                      'attributes': {
                          'nature': 'Symbols of forbidden love'
                      }
                  }
</kg>

--------------------------------------------

ADDITIONAL GUIDANCE:

- Always begin your output with `<kg><CONTEXT>` and end the context summary with `</CONTEXT>`.
- The three-sentence context summary must describe only what came before in the CURRENT_KNOWLEDGE_GRAPH, not the INPUT_SENTENCES.
- After the context summary, produce the KG for the INPUT_SENTENCES following the given format.
- Include all facts from INPUT_SENTENCES, absolutely ALL FACTS!
- The final output must end with `</kg>`.


Make sure to output **ONLY** the context summary and the knowledge graph in **exactly this format**, as described above, in the section **OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES**. Ensure it represents **ALL KNOWLEDGE from INPUT_SENTENCES** in the knowledge graph format as demonstrated in the OUTPUT_FORMAT_EXAMPLEs.
MAKE the kg after </CONTEXT> in OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES as detailed, long and extensive as possible within the contraint of staying factual w.r.t. the INPUT_SENTENCES! LONG AND DETAILED! 

**It is very important that you perform this task accurately and with the highest quality, following the instructions precisely.**


CURRENT_KNOWLEDGE_GRAPH:
""" + current_kg_context + """
INPUT_SENTENCES:
""" + sentence + """
OUTPUT_KG_CONSTRUCTED_FROM_INPUT_SENTENCES:
"""
    return prompt


def answer_questions_prompts(context, question):
    prompt = f"""Input: Context: This is a descriptive text or passage that provides background information necessary to understand the question.
      Questions: these are questions that need to be answered. The answer choice should be clearly marked (e.g., ';A;').
      Prompt:

      Read the following context carefully:

      {context}

      Based on the context, answer the following question by providing the capitalized letter corresponding to the most appropriate answer choice:

      {question}

      Example context:

      Today is Earth Day, a day dedicated to celebrating our planet and raising awareness about environmental issues.

      Examplequestion:

      A) Which of the following is NOT a renewable resource?
      B) Coal
      C) Solar energy
      D) Wind power

      Example output:

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
    
    
