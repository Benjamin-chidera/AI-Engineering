from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY_LANGCHAIN = os.getenv("OPENAI_API_KEY_LANGCHAIN")

client = OpenAI(api_key=OPENAI_API_KEY_LANGCHAIN)


def main_analysis(prompt:str):
    response = client.responses.create(
        model="gpt-3.5-turbo",
        input= [
            {
                "role": "system",
                "content": "You are a helpful assistant that provides semantic analysis of text. Respond with either Positive, Negative or Neutral."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.output[0].content[0].text # type: ignore


if __name__ == '__main__':
    talk = input("Enter your text: ")
    response = main_analysis(talk)
    print(response)