from premai import Prem
from utils import bcolors
import os
from dotenv import load_dotenv

load_dotenv()

client = Prem(
    api_key=os.getenv("PREMAI_API_KEY"),
)

system_prompt = "You are an helpful assistant, optimized for RAG. Please answer the user question, based on the given context. But avoid sentences like 'based on the given context' in the response."

content_messages = [
	"How does the directive propose to handle evidence disclosure and trade secret protection in legal proceedings involving product liability claims?",
	"What measures are proposed to ease the burden of proof for injured persons in complex cases involving pharmaceuticals, smart products, or AI-enabled products?",
	"How does the directive ensure that there is always an EU-based entity that can be held liable for defective products purchased directly from non-EU manufacturers?",
	"In what ways does the proposed directive align with other existing EU legislation, such as the Sale of Goods Act, the Digital Content and Services Directive, and the GDPR?",
	"What are the implications of the directive's provisions for SMEs and start-ups, particularly regarding the balance between fostering innovation and ensuring consumer protection?",
]
bad_content_messages = [
	"What are the proposed changes to the limitations on making compensation claims, such as the threshold for property damage and the period of liability for manufacturers?",
	"How does the proposed directive support the principles of the circular economy, particularly in relation to the liability of products that are remanufactured or substantially modified?"
]

project_id = 4455
temperature = 0.0



for content_message in content_messages:
	messages = [{"role": "user", "content": content_message}]

	response = client.chat.completions.create(
		project_id=project_id,
		messages=messages,
		system_prompt=system_prompt,
		temperature=temperature,
		stream=False
	)
	print(bcolors.OKCYAN + messages[0]['content'] + bcolors.ENDC)
	print(bcolors.OKBLUE + response.choices[0].message.content + bcolors.ENDC)
	print(bcolors.BOLD + \
	      "Similarity scores: " + \
	      ';'.join(str(round(chunk.similarity_score, 2)) for chunk in response.document_chunks) + \
		  bcolors.ENDC)
	print("------------------------------------------------")


for bad_content_message in bad_content_messages:
	messages = [{"role": "user", "content": bad_content_message}]

	response = client.chat.completions.create(
		project_id=project_id,
		messages=messages,
		system_prompt=system_prompt,
		temperature=temperature,
		stream=False
	)
	print(bcolors.OKCYAN + messages[0]['content'] + bcolors.ENDC)
	print(bcolors.FAIL + response.choices[0].message.content + bcolors.ENDC)
	print(bcolors.BOLD + bcolors.WARNING + \
	      "Similarity scores: " + \
		  ';'.join(str(round(chunk.similarity_score, 2)) for chunk in response.document_chunks) + \
		  bcolors.ENDC)
	print("------------------------------------------------")
