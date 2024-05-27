from premai import Prem

client = Prem(
    api_key=""
)


system_prompt = "You are an helpful assistant, optimized for RAG. Please answer the user question, based on the given context. Be But avoid sentences like 'based on the given context' in the response."

messages = [
    {"role": "user", "content": "What measures are proposed to ease the burden of proof for injured persons in complex cases involving pharmaceuticals, smart products, or AI-enabled products?"}
]

project_id = 4455

repositories = dict(
  ids=[1961], 
  similarity_threshold=0.3,
  limit=5
)

# Create completion
response = client.chat.completions.create(
    system_prompt=system_prompt,
    project_id=project_id,
    messages=messages,
    repositories=repositories,
)

print('\033[94m' + messages[0]['content'] + '\033[0m')
print('\033[96m' + response.choices[0].message.content + '\033[0m')
