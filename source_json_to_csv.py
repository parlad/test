import json
import csv
import chardet

def extract_json_to_csv(input_file, output_file, columns_to_extract):
    # Detect the encoding of the input file
    with open(input_file, 'rb') as f:
        result = chardet.detect(f.read())

    # Open the input file with the detected encoding
    with open(input_file, encoding=result['encoding']) as f:
        data = json.load(f)

    # Create the output CSV file and write the column headers
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(columns_to_extract)

        # Extract the specified columns from the JSON data and write them to the CSV file
        for item in data:
            row = [item[column] for column in columns_to_extract]
            writer.writerow(row)
    
    print(f"CSV file '{output_file}' successfully created!")

# Example usage of the function
columns_to_extract = ['column1', 'column2', 'column3']
extract_json_to_csv('input_file.json', 'output_file.csv', columns_to_extract)
