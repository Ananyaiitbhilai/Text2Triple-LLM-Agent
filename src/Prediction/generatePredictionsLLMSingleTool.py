import json
import sys
from ..SystemLLM.LLMsingleTool import process_command

# Function to extract triples for each context in eval.json and create pred.json
def generate_pred_json(eval_file_path, pred_file_path):
    # Load the evaluation data from eval.json
    with open(eval_file_path, 'r') as file:
        eval_data = json.load(file)
    
    # Initialize a list to hold the modified data with extracted triples
    modified_data = []
    
    # Iterate over each item in the evaluation data
    for item in eval_data:
        context = item['context']
        # Prepare the command with the context
        command = f"Can you please give triples for {context}"
        # Use the process_command function to predict the extracted triples
        extracted_triplets = process_command(command)
        # Append the extracted triples to the item under the 'triples' key
        item['triples'] = extracted_triplets
        # Append the modified item to the modified_data list
        modified_data.append(item)
    
    # Write the modified data with extracted triples to pred.json
    with open(pred_file_path, 'w') as file:
        json.dump(modified_data, file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <eval_file_path> <pred_file_path>")
        sys.exit(1)
    
    eval_file_path = sys.argv[1]
    pred_file_path = sys.argv[2]
    generate_pred_json(eval_file_path, pred_file_path)