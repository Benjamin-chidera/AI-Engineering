from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser

chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

list_instructions = CommaSeparatedListOutputParser().get_format_instructions()

prompt_message = ChatPromptTemplate.from_messages([
    (
        "human", "I've recently adopted a {pet}. Could you suggest some {pet} names? \n" + list_instructions
    )
])

list_output_parser = CommaSeparatedListOutputParser()

chain = prompt_message | chat | list_output_parser

print(chain.invoke({"pet": "dog"}))