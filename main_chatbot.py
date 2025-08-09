from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY_LANGCHAIN = os.getenv("OPENAI_API_KEY_LANGCHAIN")

client = OpenAI(api_key=OPENAI_API_KEY_LANGCHAIN)

def main_chatbot(prompt: str):
   completion = client.responses.create(
        model="gpt-3.5-turbo",
        input=[
            {
                "role": "system",
                "content": "you are Marv, a chatbot that reluctantly answers questions with sarcastic responses."
            },
            {
                "role": "user",
                "content": prompt
            }
        ] 
        )
      
   return completion.output[0].content[0].text # type: ignore
    



    
talk = main_chatbot("I just got a dog, what should I do with it?")
print(talk)