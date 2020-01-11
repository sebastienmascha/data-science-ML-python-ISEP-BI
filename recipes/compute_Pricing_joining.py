# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
datafinitiElectronicsProductsPricingData = dataiku.Dataset("DatafinitiElectronicsProductsPricingData")
datafinitiElectronicsProductsPricingData_df = datafinitiElectronicsProductsPricingData.get_dataframe()
processing_joining = dataiku.Dataset("Processing_joining")
processing_joining_df = processing_joining.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
datafinitiElectronicsProductsPricingData_df = datafinitiElectronicsProductsPricingData_df.drop(columns=['id',
 'brand',
 'categories',
 'dateAdded',
 'dateUpdated',
 'ean',
 'imageURLs',
 'keys',
 'manufacturer',
 'manufacturerNumber',
 'name',
 'primaryCategories',
 'sourceURLs',
 'upc',
 'weight',
 'col_26',
 'col_27',
 'col_28',
 'col_29',
 'col_30'])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Compute recipe outputs
pricing_joining_df = pd.merge(processing_joining_df.astype(object), datafinitiElectronicsProductsPricingData_df.astype(object), how='left', on=[
 'asins'])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
pricing_joining = dataiku.Dataset("Pricing_joining")
pricing_joining.write_with_schema(pricing_joining_df)