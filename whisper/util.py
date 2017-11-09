"""



"""

import pandas as pd

def parse_arguments(args):
    pass

def identify_cols(data):

    # Create empty dictionary and lists for dimensions and measures
    column_data_types = {}
    dimensions = []
    measures = []

    # Populate a dictionary with columns and data types
    for i in data.columns.values:
        column_data_types[i] = str(data[i].dtype)

    # Identify the datatypes in each column and split them into categorical dimensions or continuous measures
    for key, value in column_data_types.items():
        if value in ['int64', 'float64', 'timedelta[ns]']:
            measures.append(key)
        if value in ['object', 'datetime64']:
            dimensions.append(key)

    return dimensions, measures

