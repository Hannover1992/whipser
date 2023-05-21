import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
lists = openai.Model.list()
print(lists)