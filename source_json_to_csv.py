import json
import csv

def extract_json_to_csv(json_file_path, csv_file_path):
    # Open the JSON file for reading
    with open(json_file_path, 'r') as json_file:
        # Load the JSON data
        json_data = json.load(json_file)

        # Open the CSV file for writing
        with open(csv_file_path, 'w', newline='') as csv_file:
            # Create a CSV writer object
            csv_writer = csv.writer(csv_file)

            # Extract the header row from the JSON data
            header = list(json_data[0].keys())
            csv_writer.writerow(header)

            # Extract the data rows from the JSON data
            for row in json_data:
                csv_writer.writerow(list(row.values()))

    print(f'Successfully extracted JSON data to {csv_file_path}!')

# Example usage
json_file_path = 'example.json'
csv_file_path = 'example.csv'
extract_json_to_csv(json_file_path, csv_file_path)
