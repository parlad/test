import json
import csv

def extract_json_to_csv(json_file_path, config_file_path, csv_file_path):
    # Load the configuration data
    with open(config_file_path, 'r') as config_file:
        config_data = json.load(config_file)

    # Open the JSON file for reading
    with open(json_file_path, 'r') as json_file:
        # Load the JSON data
        json_data = json.load(json_file)

        # Open the CSV file for writing
        with open(csv_file_path, 'w', newline='') as csv_file:
            # Create a CSV writer object
            csv_writer = csv.writer(csv_file)

            # Extract the header row from the configuration data
            header = config_data['columns']
            csv_writer.writerow(header)

            # Extract the data rows from the JSON data
            for row in json_data:
                # Extract the selected columns from the row
                selected_row = [row[col] for col in header]
                csv_writer.writerow(selected_row)

    print(f'Successfully extracted selected JSON data to {csv_file_path}!')

# Example usage
json_file_path = 'example.json'
config_file_path = 'config.json'
csv_file_path = 'example.csv'
extract_json_to_csv(json_file_path, config_file_path, csv_file_path)
