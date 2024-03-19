import json
import sys
import os

from src.Tools.REBEL import extract_text_triplets_rebel
from src.Tools.KnowGL import extract_text_triplets_knowgl



def generate_pred_json(extract_triples_function, input_file_path, output_file_path):
    # Read the evaluation file
    with open(input_file_path, 'r') as file:
        data = json.load(file)

    # Process each entry in the evaluation file
    for entry in data:
        context = entry["context"]
        # Extract triplets from the context
        triplets = extract_triples_function(context)
        # Append the extracted triplets to the entry
        entry["triples"] = triplets

    # Write the modified data to a new JSON file
    with open(output_file_path, "w") as outfile:
        json.dump(data, outfile, indent=4)

    print(f"New file '{output_file_path}' created with updated entries.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <function_name> <eval_file_path> <pred_file_path>")
        sys.exit(1)

    function_name = sys.argv[1]
    eval_file_path = sys.argv[2]
    pred_file_path = sys.argv[3]

    # Select the function based on the command-line argument
    if function_name == "extract_text_triplets_knowgl":
        extract_triples_function = extract_text_triplets_knowgl
    elif function_name == "extract_text_triplets_rebel":
        extract_triples_function = extract_text_triplets_rebel
    else:
        print("Invalid function name. Please use 'extract_text_triplets_knowgl' or 'extract_text_triplets_rebel'.")
        sys.exit(1)

    generate_pred_json(extract_triples_function, eval_file_path, pred_file_path)

