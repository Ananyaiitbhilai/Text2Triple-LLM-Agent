import json
import sys

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def convert_to_dict(data):
    return {item['id']: item for item in data}

def filter_by_common_ids(data1, data2):
    common_ids = set(data1.keys()) & set(data2.keys())
    return [data1[id] for id in common_ids], [data2[id] for id in common_ids]

def filter_triples_string(data):
    return [entry for entry in data if not ('triples' in entry and isinstance(entry['triples'], str))]

def update_triples_type(data, mapping):
    new_data = []
    for obj in data:
        new_obj = {
            "title": obj["title"],
            "context": obj["context"],
            "id": obj["id"],
            "triples": []
        }
        for triple in obj["triples"]:
            for key, value in mapping.items():
                if triple["type"] in value:
                    triple["type"] = key
                    break
            new_obj["triples"].append(triple)
        new_data.append(new_obj)
    return new_data

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python process_json_files.py <prediction_file_path> <golden_file_path> <output_filtered_golden_path> <output_updated_pred_path>")
        sys.exit(1)

    pred_file_path, golden_file_path, output_filtered_golden_path, output_updated_pred_path = sys.argv[1:5]

    # Load the JSON data
    pred_data = load_json(pred_file_path)
    golden_data = load_json(golden_file_path)

    # Convert to dictionaries indexed by 'id'
    pred_data_dict = convert_to_dict(pred_data)
    golden_data_dict = convert_to_dict(golden_data)

    # Filter by common IDs
    common_pred_data, common_golden_data = filter_by_common_ids(pred_data_dict, golden_data_dict)

    # Filter out entries with "triples" as a string
    filtered_pred_data = filter_triples_string(common_pred_data)
    filtered_golden_data = filter_triples_string(common_golden_data)

    #mapping to 5 relation
    mapping =  {'employer': ['derivative work',   'inception', 'instance of', 'owned by', 'owner of', 'part of', 'participant', 
    'participant in', 'performer', 'twinned administrative body','occupation', 'field of this occupation', 'member of political party','work location', 'language used', 'participant in', 'participant','owner of', 'owned by', 'member of', 'notable work', 'instance of', 'interested in',  'office held by head of government', 'chief executive officer', 'educated at', 'subclass of','part of', 'office held by head of state','chairperson', 'executive body', 'industry', 'officeholder', 
    'position held', 'practiced by', 'language of work or name', 'director / manager', 'employer', 'field of work', 
    'language of work or name', 'notable work', 'occupation', 'member of', 'member of political party', 'officeholder',
    'operator', 'position held', 'educated at', 'founded by',
    'product or material produced', 'subsidiary', 'work location', 'author', 
    'office held by head of government', 'used by', 'uses', 'candidacy in election', 'candidate',  'chairperson', 'head of government' ], 
    'headquarters location': ['headquarters location', 'twinned administrative body','applies to jurisdiction', 'legislative body','military branch', 'contains administrative territorial entity', 
    'parent organization', 'operating area','legislative body', 'contains administrative territorial entity', 
    'headquarters location', 'located in the administrative territorial entity', 'ethnic group', 'language used',
    'military branch', 'parent organization', 'applies to jurisdiction'],
    'killed by': ['cause of death', 'perpetrator', 'convicted of', 
    'killed by', 'place of death',  'facet of','date of death',  'main subject', 'place of death', 'facet of', 'significant event'], 'location': ['location',  'capital','continent',  'located in time zone', 'shares border with', 
    'mountain range', 'located in or next to body of water', 'candidate',   'significant place',   'spouse', 'place of publication',  'target','country', 'located in or next to body of water', 'location', 
    'mouth of the watercourse', 'point in time', 'capital', 'capital of', 
    'shares border with', 'tributary', 'diplomatic relation', 'place of publication', 'spouse'], 
    'residence': [ 'place of birth', 'based on' ,  
    'country of citizenship', 'date of birth' , 'has part', 
    'number of participants', 'history of topic',  'place of birth', 
    'country of origin', 'has quality',  
    'significant event','occupant', 'relative', 'residence']}

    # Update the "type" of triples based on the mapping
    updated_pred_data = update_triples_type(filtered_pred_data, mapping)

    # Save the processed data to new JSON files
    save_json(filtered_golden_data, output_filtered_golden_path)
    save_json(updated_pred_data, output_updated_pred_path)

    print("Processed files have been saved.")
 



