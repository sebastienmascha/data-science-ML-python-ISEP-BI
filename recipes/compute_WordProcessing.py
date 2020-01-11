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
wordProcessing_df = preProcessing_df.copy()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
def dicoCount(col1):
    dico = dict()
    for i in range(0, len(col1)):
        if col1[i] in dico:
            # append the new number to the existing array at this slot
            dico[col1[i]] += 1
        else:
            # create a new array in this slot
            dico[col1[i]] = 1
    return dico

def dicoAppend(col1, col2):
    dico = dict()
    for i in range(0, len(col1)):
        if col1[i] in dico:
            # append the new number to the existing array at this slot
            dico[col1[i]].append(col2[i])
        else:
            # create a new array in this slot
            dico[col1[i]] = [col2[i]]
    return dico

def classement (col1, i):
    return dict(Counter(dicoCount(col1)).most_common(i))

def dicoToArray(dico, int):
    array = []
    for i in range (0, len(dico[int])):
        array.append(ratings[int][i])
    return array

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
'''mostRelevantComments = classement(textProcessing_df['reviews.numHelpful'], 150)

ratings = dicoAppend(textProcessing_df['reviews.rating'], textProcessing_df['reviews.text'])``

fiveStars = set(dicoToArray(ratings, 5))
fourStars = set(dicoToArray(ratings, 4))
threeStars = set(dicoToArray(ratings, 3))
twoStars = set(dicoToArray(ratings, 2))
oneStar = set(dicoToArray(ratings, 1))'''

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
wordProcessing_df['test'] = 100

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
wordProcessing = dataiku.Dataset("WordProcessing")
wordProcessing.write_with_schema(wordProcessing_df)