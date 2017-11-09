import pandas as pd
from tkinter import filedialog
import time

print("Welcome to the DataWhisperer Data Loader!")
print("Please select a csv file to load for analysis.")
print("")
print("")

# time.sleep(3)

def load_data():

    # Load a csv from a file dialog
    source = filedialog.askopenfilename()
    data = pd.read_csv(source)
    column_types = data.dtypes

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

    return data, dimensions, measures

# Display an ordered list of dimensions and measures
def print_dims_meas(dimensions, measures):
    dimensions.sort()
    measures.sort()
    print("The data set contains the following measures:\n")
    for meas in measures:
        print(meas)
    print("")
    print("The data set contains the following dimensions:\n")
    for dim in dimensions:
        print(dim)
    print("")


data, dimensions, measures = load_data()


print_dims_meas(dimensions, measures)