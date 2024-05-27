from premai import Prem

client = Prem(
    api_key=""
)

messages = [
    {"role": "user", "content": "What are the proposed changes to the limitations on making compensation claims, such as the threshold for property damage and the period of liability for manufacturers?"},
]
project_id = 4455

# Create completion
response = client.chat.completions.create(
    project_id=project_id,
    messages=messages,
)

print(response.choices)
