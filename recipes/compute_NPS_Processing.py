# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
preProcessing = dataiku.Dataset("PreProcessing")
preProcessing_df = preProcessing.get_dataframe()

nps_Processing_df = preProcessing_df.copy()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
names = nps_Processing_df['name']
names = list(set(names))
name0 = nps_Processing_df['name'][1000]
print(name0)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
my_dict = {}
number_of_occurence = 0
detractors = 0
liability = 0
promoter = 0
for i in range (0, len(names)):
    if names[i] not in my_dict:
        name = names[i]
        for j in range(len(preProcessing_df) ):
            if (preProcessing_df['reviews.rating'][j] == 5) & (preProcessing_df['name'][j] == name):
                promoter+=1
                number_of_occurence+=1
            elif (preProcessing_df['reviews.rating'][j] == 4) & (preProcessing_df['name'][j] == name):
                liability +=1
                number_of_occurence += 1
            elif (preProcessing_df['reviews.rating'][j] < 4) & (preProcessing_df['name'][j] == name):
                detractors +=1
                number_of_occurence+=1

        promoter_score = promoter/number_of_occurence
        detractor_score = detractors/number_of_occurence
        #print(promoter_score - detractor_score)
        my_dict[name] = promoter_score - detractor_score
        number_of_occurence = 0
        detractors = 0
        liability = 0
        promoter = 0
  #  elif names[i] in my_dict:
        #print(my_dict.get(names[i]))

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
nps_Processing_df['NPS'] = nps_Processing_df['name'].apply(lambda x: my_dict.get(x))

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
nps_Processing = dataiku.Dataset("NPS_Processing")
nps_Processing.write_with_schema(nps_Processing_df)