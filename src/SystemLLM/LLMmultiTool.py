from llama_cpp import Llama
import re
import json
import sys
import os
from dotenv import load_dotenv
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from src.Tools.multiToolRE import extract_text_triplets
from src.Tools.FlairNER import extract_entities

load_dotenv()

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

llm = Llama(model_path=os.getenv("LLM_MODEL_PATH"),  
n_ctx=2048,
n_gpu_layers=-1,
n_batch=512,
callback_manager=callback_manager,
verbose=True)

prompt_template = '''<s>[INST] <<SYS>>
Assistant is an expert JSON builder designed to assist with a wide range of tasks.

Assistant is able to trigger actions for User by responding with JSON strings that contain "action" and "action_input" parameters.

The available actions to Assistant are:

- "extract_text_triplets": Useful when Assistant is asked to extract triplets from a given text.
  - To use the extract_triplets tool, Assistant should respond like so:
    {{"action": "extract_text_triplets", "action_input": "Your text here"}}

- "extract_entities": Useful when Assistant is asked to extract entities from a given text.
  - To use the extract_triplets tool, Assistant should respond like so:
    {{"action": "extract_entities", "action_input": "Your text here"}} 

Here are some previous conversations between the Assistant and User:

User: Hey how are you today?
Assistant: I'm good thanks, how are you?
User: Can you extract all the triplets from this text: "Gràcia is a district of the city of Barcelona, Spain."
Assistant: {{"action": "extract_text_triplets", "action_input": "Gràcia is a district of the city of Barcelona, Spain."}}
User: Also give triples for "obama was US president"
Assistant: {{"action": "extract_text_triplets", "action_input": "obama was US president"}}
User: Can you extract all the entities from this text: "Gràcia is a district of the city of Barcelona, Spain."
Assistant: {{"action": "extract_entities", "action_input": "Gràcia is a district of the city of Barcelona, Spain."}}
User: Also give entities for "obama was US president"
Assistant: {{"action": "extract_entities", "action_input": "obama was US president"}}


<</SYS>>

{0}[/INST]'''


def process_command(command):
    # Put user command into prompt
    prompt = prompt_template.format("User: " + command)
    # Send command to the model
    output = llm(prompt, max_tokens=2000, stop=["User:"])
    response = output['choices'][0]['text']

    # try to find json in the response
    try:
        # Extract json from model response by finding first and last brackets {}
        firstBracketIndex = response.index("{")
        lastBracketIndex = len(response) - response[::-1].index("}")
        jsonString = response[firstBracketIndex:lastBracketIndex]
        responseJson = json.loads(jsonString)
        if responseJson['action'] == 'extract_text_triplets':
            extracted_triplets = extract_text_triplets(responseJson['action_input'])
            return extracted_triplets   
        elif responseJson['action'] == 'extract_entities':
            extracted_entities = extract_entities(responseJson['action_input'])
            return extracted_entities   
    except Exception as e:
        print(e)
    # No json match, just return response
    return response
