from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Chat model
chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Prompt with placeholders
messages = [
    (
        "system",
        "You are a helpful assistant that translates {language_1} to {language_2}. Translate the user sentence.",
    ),
    ("human", "{user_sentence}"),
]

prompt_chat = ChatPromptTemplate.from_messages(messages)

# Parser for plain text output
parser = StrOutputParser()

# Chain
chain = prompt_chat | chat | parser 

check = chain.stream({
    "language_1": "english",
    "language_2": "french",
    "user_sentence": "I love programming. Sing a song about it"
})

# Streaming the response
for chunk in check:
    print(chunk, end="", flush=True)

print()  # final newline
