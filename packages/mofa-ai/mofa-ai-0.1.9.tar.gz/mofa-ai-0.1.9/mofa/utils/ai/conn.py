import os
from typing import List
from dotenv import load_dotenv
import instructor

from openai import OpenAI

def create_openai_client(api_key: str=os.getenv("OPENAI_API_KEY"),*args,**kwargs) -> OpenAI:
    client = OpenAI(api_key=api_key,**kwargs)
    return client
def generate_json_from_llm(client, prompt: str, format_class, messages: List[dict] = None, supplement_prompt: str = None, model_name: str = 'gpt-4o-mini') -> str:

    if messages is None:
        messages = [
            {"role": "system",
             "content": "You are a professional Ai assistant"},
            {"role": "user", "content": prompt},
        ]
    if supplement_prompt is not None:
        messages.append({"role": "user", "content": supplement_prompt})
    completion = client.beta.chat.completions.parse(
        model=model_name,
        messages=messages,
        response_format=format_class,
    )
    return completion.choices[0].message.parsed

def structor_llm(env_file:str,messages:list,response_model,model_name:str='gpt-4o',*args,**kwargs):

    load_dotenv(env_file)
    max_loop = 3
    if os.getenv('LLM_API_KEY') is not None:
        os.environ['OPENAI_API_KEY'] = os.getenv('LLM_API_KEY')

    if os.getenv('LLM_BASE_URL',None) is None:
        client = instructor.from_openai(client=OpenAI(api_key=os.environ['OPENAI_API_KEY']))
    else:
        client = instructor.from_openai(client=OpenAI(api_key=os.environ['OPENAI_API_KEY'],base_url=os.getenv('LLM_BASE_URL'),))
    try:
        response = client.chat.completions.create(
            model=os.getenv('LLM_MODEL_NAME','gpt-4o'),
            messages=messages,
            response_model=response_model,
        )
    except Exception as e:
        print(f"Error: {e}")
        response = None
        for i in range(max_loop):
            try:
                response = client.chat.completions.create(
                    model=model_name,
                    messages=messages,
                    response_model=response_model,
                )
                break
            except Exception as e:
                print(f"Retrying... {i+1}/{max_loop} - Error: {e}")
    return response


