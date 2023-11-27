import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo", # gpt-4-1106-preview
  messages=[
    {"role": "system", "content": "You provide answer, solutions, documentation, insights, code review and engage in pair programming."},
    {"role": "user", "content": "List and describe the solid principles. You will demonstrate how the solid principles can be represented in category theory. You will then demonstrate provide examples for each of the SOLID principles by providing code examples in python, and in another way that achieves the same result but using a functional style to demonstrate how category theory is able to achieve the same result using functions as first class objects."}
  ]
)

print(completion.choices[0].message.content)
