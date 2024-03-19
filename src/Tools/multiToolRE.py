
from REBEL import extract_text_triplets_rebel
from KnowGL import extract_text_triplets_knowgl


def extract_text_triplets(input_text):
    """
    Extracts triplets from the given text using both Rebel and KnowGL models,
    and ranks the outputs based on some criteria.

    Parameters:
    input_text (str): The text from which to extract triplets.

    Returns:
    list: A list of dictionaries, each representing a triplet with 'head', 'type', and 'tail',
    sorted based on the ranking criteria.
    """
    # Extract triplets using Rebel model
    triplets_rebel = extract_text_triplets_rebel(input_text)
    
    # Extract triplets using KnowGL model
    triplets_knowgl = extract_text_triplets_knowgl(input_text)
    
    # Combine the triplets from both models
    all_triplets = triplets_rebel + triplets_knowgl
    
    unique_triplets = []
    for triplet in all_triplets:
        if triplet not in unique_triplets:
            unique_triplets.append(triplet)
    
    #ranking criteria is based on the length of the triplets
    ranked_triplets = sorted(unique_triplets, key=lambda x: len(x['type']), reverse=True)
    
    return ranked_triplets