from llama_cpp import Llama
import re
import json
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from ..Tools.REBEL import extract_text_triplets_rebel


callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

llm = Llama(model_path="<path of your LLM (gguf format)>",  
n_ctx=2048,
n_gpu_layers=-1,
n_batch=512,
callback_manager=callback_manager,
verbose=True)


prompt_template = '''<s>[INST] <<SYS>>
Assistant is an expert JSON builder designed to assist with a wide range of tasks.

Assistant is able to trigger actions for User by responding with JSON strings that contain "action" and "action_input" parameters.

The available action to Assistant is:
- "extract_text_triplets": Useful for when Assistant is asked to extract triplets from a given text.
  - To use the extract_triplets tool, Assistant should respond like so:
    {{"action": "extract_text_triplets_rebel", "action_input": "Your text here"}}

Here are some previous conversations between the Assistant and User:

User: Hey how are you today?
Assistant: I'm good thanks, how are you?
User: Can you extract all the triplets from this text: "Gràcia is a district of the city of Barcelona, Spain."
Assistant: {{"action": "extract_text_triplets_rebel", "action_input": "Gràcia is a district of the city of Barcelona, Spain."}}
User: Also give triples for "obama was US president"
Assistant: {{"action": "extract_text_triplets_rebel", "action_input": "obama was US president"}}


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
        if responseJson['action'] == 'extract_text_triplets_rebel':
            extracted_triplets = extract_text_triplets_rebel(responseJson['action_input'])
            return extracted_triplets   
    except Exception as e:
        print(e)
    # No json match, just return response
    return response