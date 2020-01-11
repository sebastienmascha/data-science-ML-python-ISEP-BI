# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
nps_Processing = dataiku.Dataset("NPS_Processing")
nps_Processing_df = nps_Processing.get_dataframe()
textProcessing = dataiku.Dataset("TextProcessing")
textProcessing_df = textProcessing.get_dataframe()
wordProcessing = dataiku.Dataset("WordProcessing")
wordProcessing_df = wordProcessing.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Compute recipe outputs
processing_joining_df = pd.merge(textProcessing_df, nps_Processing_df, how='left', on=['id',
 'asins',
 'brand',
 'categories',
 'colors',
 'dateAdded',
 'dateUpdated',
 'dimension',
 'ean',
 'imageURLs',
 'keys',
 'manufacturer',
 'manufacturerNumber',
 'name',
 'primaryCategories',
 'reviews.date',
 'reviews.dateSeen',
 'reviews.doRecommend',
 'reviews.numHelpful',
 'reviews.rating',
 'reviews.sourceURLs',
 'reviews.text',
 'reviews.title',
 'reviews.username',
 'sourceURLs',
 'upc',
 'weight',
 'numberImages'])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
processing_joining = dataiku.Dataset("Processing_joining")
processing_joining.write_with_schema(processing_joining_df)