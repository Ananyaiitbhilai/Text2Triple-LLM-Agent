import json
import os

# List of file paths for the files you want to process
file_paths = ['data/datasets/conll04/test_triples.json']

# List of output directories for each file
output_file_paths = ['data/datasets/conll04/conll04_eval.json']

for file_path, output_file_path in zip(file_paths, output_file_paths):
    # Ensure the output directory exists
    output_directory = os.path.dirname(output_file_path)
    os.makedirs(output_directory, exist_ok=True)
    
    with open(file_path, 'r') as input_file:
        data = json.load(input_file)
        
        # Initialize a list to hold all extracted data
        all_extracted_data = []
        
        # Assuming data is a list of dictionaries, we iterate over each item
        for item in data:
            # Extract the required information from each item
            extracted_data = {
                'title': item['title'],
                'context': item['context'],
                'id': item['id']
            }
            # Add the extracted data to the list
            all_extracted_data.append(extracted_data)
            
        # Write all the extracted information to the specified output file path
        with open(output_file_path, 'w') as output_file:
            json.dump(all_extracted_data, output_file, indent=4)

print("Extraction and storage complete.")