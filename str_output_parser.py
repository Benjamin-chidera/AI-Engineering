
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, CommaSeparatedListOutputParser
load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

message = [
   ( "system", "You are an expert in product review." ),
   ("human", "List the main features of the product MacBook Pro, the M5 chip." )
]

propmt_response = llm.invoke(message)

# parser = StrOutputParser()
parser = CommaSeparatedListOutputParser()

response = parser.invoke(propmt_response)

print(response)