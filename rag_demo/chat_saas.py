import os

from premai import Prem
from dotenv import load_dotenv


load_dotenv()

client = Prem(api_key=os.environ["PREMAI_API_KEY"])


system_prompt = "You are a helpful assistant, optimized for RAG. Please answer the user question, based on the given context. But avoid sentences like 'based on the given context' in the response. Try to use the context, as much as you can, but again: AVOID USING SENTENCES THAT CONTAIN THE WORD 'CONTEXT'"

messages = [
    {
        "role": "user",
        "content": "What is the key feature of ChatEval compared to other evaluation strategies?"
    }
]

project_id = 4508


# Create completion
response = client.chat.completions.create(
    system_prompt=system_prompt,
    project_id=project_id,
    messages=messages,
)

print('\033[94m' + messages[0]['content'] + '\033[0m')
print('\033[96m' + response.choices[0].message.content + '\033[0m')
