import os

from premai import Prem
from dotenv import load_dotenv


load_dotenv()

client = Prem(
    api_key=os.getenv("PREMAI_API_KEY"),
)


system_prompt = "You are an helpful assistant, optimized for RAG. Please answer the user question, based on the given context. But avoid sentences like 'based on the given context' in the response."

messages = [
    {"role": "user",
        "content": "How does the NIS 2 Directive (Directive (EU) 2022/2555) ensure a high common level of cybersecurity across the Union, and what are the specific obligations for Member States in terms of national cybersecurity strategies?"}
]

project_id = 4455


# Create completion
response = client.chat.completions.create(
    system_prompt=system_prompt,
    project_id=project_id,
    messages=messages,
)

print('\033[94m' + messages[0]['content'] + '\033[0m')
print('\033[96m' + response.choices[0].message.content + '\033[0m')
