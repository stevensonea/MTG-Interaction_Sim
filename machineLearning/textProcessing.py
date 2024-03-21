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
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

## Step 1: Data Processing ##
#This function tokenizes the sentence
tokens = word_tokenize("The quick brown fox jumps over the lazy dog")
print("After tokenization\n", tokens)

#Now we will remove the stop words
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
tokens = [w for w in tokens if not w in stop_words]
print("After removing stop words\n", tokens)

#Now we will stem the words
porter = PorterStemmer()
stems = []
for t in tokens:
    stems.append(porter.stem(t))
print("After stemming\n", stems)

#Last thing for this step, we lemmatize the stems
lemmatizer = WordNetLemmatizer()
lemmatized = []
for s in stems:
    lemmatized.append(lemmatizer.lemmatize(s))
print("After lemmatization\n", lemmatized)

## Step 2: Feature Extraction ##