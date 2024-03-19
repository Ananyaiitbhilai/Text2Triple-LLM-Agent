import json
import sys

# Function to calculate precision, recall, and F1 score
def calculate_scores(tp, total_golden, total_prediction):
    precision = tp / total_prediction if total_prediction > 0 else 0
    recall = tp / total_golden if total_golden > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    return precision, recall, f1

# Function to process the files and calculate the scores, considering extras
def evaluate_predictions_corrected(golden_file, prediction_file):
    # Load the golden truths and predictions
    with open(golden_file, 'r') as f:
        golden_data = json.load(f)
    with open(prediction_file, 'r') as f:
        prediction_data = json.load(f)

    tp = 0
    extras = 0

    # Convert golden data and prediction data into dictionaries for easier access
    golden_dict = {item['id']: set(tuple(triple.items()) for triple in item['triples']) for item in golden_data}
    prediction_dict = {item['id']: set(tuple(triple.items()) for triple in item['triples']) for item in prediction_data}

    # Iterate over each instance in the golden data to calculate true positives
    for id, golden_triples in golden_dict.items():
        prediction_triples = prediction_dict.get(id, set())
        tp += len(golden_triples & prediction_triples)

    # Calculate extras in prediction
    for id, prediction_triples in prediction_dict.items():
        if id not in golden_dict:
            extras += len(prediction_triples)
        else:
            unmatched_triples = prediction_triples - golden_dict[id]
            print(unmatched_triples)
            extras += len(unmatched_triples)

    # Calculate micro scores
    total_golden = sum(len(triples) for triples in golden_dict.values())
    total_prediction = sum(len(triples) for triples in prediction_dict.values())
    precision_micro, recall_micro, f1_micro = calculate_scores(tp, total_golden, total_prediction)

    # Calculate macro scores
    total_items = len(golden_dict)
    precision_macro, recall_macro, f1_macro = 0, 0, 0
    for id, golden_triples in golden_dict.items():
        prediction_triples = prediction_dict.get(id, set())
        tp = len(golden_triples & prediction_triples)
        precision, recall, _ = calculate_scores(tp, len(golden_triples), len(prediction_triples))
        precision_macro += precision
        recall_macro += recall
    precision_macro /= total_items
    recall_macro /= total_items
    f1_macro = 2 * (precision_macro * recall_macro) / (precision_macro + recall_macro) if (precision_macro + recall_macro) > 0 else 0

    return {
        'micro': {
            'precision': precision_micro,
            'recall': recall_micro,
            'f1': f1_micro
        },
        'macro': {
            'precision': precision_macro,
            'recall': recall_macro,
            'f1': f1_macro
        },
        'true_positives': tp,
        'extras': extras
    }

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <path to golden truth file> <path to prediction file>")
        sys.exit(1)

    golden_file_path = sys.argv[1]
    prediction_file_path = sys.argv[2]

    scores = evaluate_predictions_corrected(golden_file_path, prediction_file_path)
    print("Micro Scores:", scores['micro'])
    print("Macro Scores:", scores['macro'])
    print("Extras:", scores['extras'])