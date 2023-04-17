import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntesityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# download nltk corpus(first time only)
import nltk
nltk.download('all')

#load the amazon review dataset

df -  pd.read_csv('https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/amazon.csv')