# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import pandas as pd
import nltk
from nltk.tokenize import *
from nltk.corpus import stopwords
from textblob import TextBlob
from collections import Counter

# Read recipe inputs
preProcessing = dataiku.Dataset("PreProcessing")
preProcessing_df = preProcessing.get_dataframe()

# New dataframe
textProcessing_df = preProcessing_df.copy()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
def polarityCalc(text):
    try:
        return TextBlob(text).sentiment[0]
    except:
        return None

def subjectivityCalc(text):
    try:
        return TextBlob(text).sentiment[1]
    except:
        return None

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
textProcessing_df.insert(23, 'reviews.polarity', preProcessing_df['reviews.text'].apply(polarityCalc))
textProcessing_df.insert(24, 'reviews.subjectivity', preProcessing_df['reviews.text'].apply(subjectivityCalc))

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
textProcessing_df['reviews.polarity'] = textProcessing_df['reviews.polarity'].apply(lambda x: (x+1)*2.5)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
textProcessing_df['reviews.avgRatingPolarity'] = (textProcessing_df['reviews.polarity']+textProcessing_df['reviews.rating'])/2

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
textProcessing = dataiku.Dataset("TextProcessing")
textProcessing.write_with_schema(textProcessing_df)