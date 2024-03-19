from transformers import pipeline

triplet_extractor_knowgl = pipeline("text2text-generation", model="ibm/knowgl-large")

def extract_text_triplets_knowgl(input_text):
    """
    Extracts triplets from the given text.

    Parameters:
    input_text (str): The text from which to extract triplets.

    Returns:
    list: A list of dictionaries, each representing a triplet with 'head', 'type', and 'tail'.
    """
    extracted_text = triplet_extractor_knowgl.tokenizer.batch_decode([
        triplet_extractor_knowgl(input_text, return_tensors=True, return_text=False)[0]["generated_token_ids"]
    ])
    return extract_triples(extracted_text[0])

def split_spo(input_string):
    pattern = r"\[(.*?)\|\s*(.*?)\s*\|\s*(.*?)\]"
    matches = re.findall(pattern, input_string)
    if matches:
        return matches[0]

def clean_entity(entity_string):
    return entity_string.split("#")[0][1:]

def convert_format(input_text):
    subj, rel, obj = split_spo(input_text)
    return {'head': clean_entity(subj).strip(), 'type': rel,'tail': clean_entity(obj).strip()}

def extract_triples(gen_text):
    gen_text = gen_text.replace("<s><s>", "").replace("</s>", "")
    triples = []
    for triple_text in gen_text.split("$"):
        triples.append(convert_format(triple_text))
    return triples