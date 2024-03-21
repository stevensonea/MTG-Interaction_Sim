# Author: Ethan Stevenson
# Purpose: To learn how machine learning can read text following a tutorial found at https://towardsdatascience.com/machine-learning-text-processing-1d5a2d638958

"""
There are 4 steps when it comes to Text Processing
    1) Data Preprocessing
        - Tokenization: converting sentences to words
        - Removing unnecessary punctuation (tags)
        - Removing stop words: words that do not have specific sematic (ex. "the", "is")
        - Stemming: reducing words to their root by dropping unecessary characters. Doing this removes inflection
        - Lemmatization: removes inflection by determining parts of speech
"""

# The Natural Language ToolKit does most of the text preprocessing 
import nltk
from nltk.tokenize import word_tokenize

#This function tokenizes the sentence
tokens = word_tokenize("The quick brown fox jumps over the lazy dog")
print(tokens)

nltk.download('stopwords')