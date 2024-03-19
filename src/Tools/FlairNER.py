import flair
from flair.data import Sentence

flair_ner = flair.models.SequenceTagger.load('ner')

def extract_entities(text):
    # Create a Flair Sentence
    sentence = Sentence(text)

    # Run NER on the sentence
    flair_ner.predict(sentence)

    # Initialize lists to store head and tail entities
    head_entities = []
    tail_entities = []

    # Extract entities and their types
    for entity in sentence.get_spans('ner'):
        if entity.tag == 'PER':
            head_entities.append(entity.text)
        else:
            tail_entities.append(entity.text)

    # Create a list of dictionaries containing head and tail entities
    result = [{"head": head, "tail": tail} for head, tail in zip(head_entities, tail_entities)]

    return result

    