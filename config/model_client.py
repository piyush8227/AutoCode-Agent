import os
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constants import MODEL, OPENAI_API_KEY

load_dotenv()

api_key = os.getenv(OPENAI_API_KEY)

def get_model_client():
    if not api_key:
        print(f"Please enter a valid {OPENAI_API_KEY} key")
    
    model_client = OpenAIChatCompletionClient(model=MODEL, api_key=api_key)
    return model_client