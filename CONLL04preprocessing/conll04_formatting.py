import json
import logging
import os



# Define your dataset paths
dataset_paths = {
    "train": "data/conll04/train.json",
    "dev": "data/conll04/dev.json",
    "test": "data/conll04/test.json",
    
  
}

# Define your output paths
output_paths = {
    "train": "data/datasets/conll04/train_triples.json",
    "dev": "data/datasets/conll04/dev_triples.json",
    "test": "data/datasets/conll04/test_triples.json",
  
}

mapping = {'Kill': 'killed by', 'Live_In': 'residence', 'Located_In': 'location', 'OrgBased_In': 'headquarters location', 'Work_For': 'employer'}
mapping_types = {'Peop': '<peop>', 'Org': '<org>', 'Other': '<other>', 'Loc': '<loc>'}

def generate_triples(filepath, output_path):
    """Generate triples and save them to a specified file."""
    logging.info("Generating examples from = %s", filepath)
    triples_data = []

    with open(filepath) as json_file:
        f = json.load(json_file)
        for id_, row in enumerate(f):
            triplets = ''
            prev_head = None
            row_triples = []
            for relation in row['relations']:
                head_entity = ' '.join(row['tokens'][row['entities'][relation['head']]['start']:row['entities'][relation['head']]['end']])
                tail_entity = ' '.join(row['tokens'][row['entities'][relation['tail']]['start']:row['entities'][relation['tail']]['end']])
                triple = {
                    'head': head_entity,
                    'type': mapping[relation['type']],
                    'tail': tail_entity
                }
                row_triples.append(triple)

                if prev_head == relation['head']:
                    triplets += f' {mapping_types[row["entities"][relation["head"]]["type"]]} ' + ' '.join(row['tokens'][row['entities'][relation['tail']]['start']:row['entities'][relation['tail']]['end']]) + f' {mapping_types[row["entities"][relation["tail"]]["type"]]} ' + mapping[relation['type']]
                elif prev_head == None:
                    triplets += '<triplet> ' + ' '.join(row['tokens'][row['entities'][relation['head']]['start']:row['entities'][relation['head']]['end']]) + f' {mapping_types[row["entities"][relation["head"]]["type"]]} ' + ' '.join(row['tokens'][row['entities'][relation['tail']]['start']:row['entities'][relation['tail']]['end']]) + f' {mapping_types[row["entities"][relation["tail"]]["type"]]} ' + mapping[relation['type']]
                    prev_head = relation['head']
                else:
                    triplets += ' <triplet> ' + ' '.join(row['tokens'][row['entities'][relation['head']]['start']:row['entities'][relation['head']]['end']]) + f' {mapping_types[row["entities"][relation["head"]]["type"]]} ' + ' '.join(row['tokens'][row['entities'][relation['tail']]['start']:row['entities'][relation['tail']]['end']]) + f' {mapping_types[row["entities"][relation["tail"]]["type"]]} ' + mapping[relation['type']]
                    prev_head = relation['head']
            text = ' '.join(row['tokens'])
            triples_data.append({
                "title": str(row["orig_id"]),
                "context": text,
                "id": str(row["orig_id"]),
                "triplets_sentence": triplets,
                "triples": row_triples,
            })

    # Save the generated triples to the specified output path
    with open(output_path, 'w') as outfile:
        json.dump(triples_data, outfile, indent=4)

# Generate and save triples for each dataset split
for split in ['train', 'dev', 'test']:
    generate_triples(dataset_paths[split], output_paths[split])