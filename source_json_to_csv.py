import json
import csv
import chardet

# Detect the encoding of the file
with open('input_file.json', 'rb') as f:
    result = chardet.detect(f.read())

# Open the file with the detected encoding
with open('input_file.json', encoding=result['encoding']) as f:
    data = json.load(f)

# Define the columns to extract from the JSON data
columns_to_extract = ['column1', 'column2', 'column3']

# Create a CSV file and write the column headers
with open('output_file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(columns_to_extract)

    # Extract the specified columns from the JSON data and write them to the CSV file
    for item in data:
        row = [item[column] for column in columns_to_extract]
        writer.writerow(row)
