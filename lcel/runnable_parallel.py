from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)



chat_temp = ChatPromptTemplate.from_template('''
                                             
  Suggest three of the best intermidiate-level {programming_language} books
  
  Answer only by listing the books.                                           
                                             ''')

chat_temp_projects = ChatPromptTemplate.from_template("""
  
  Suggest three intresting {programming_language} projects suitable for intermediate-level programmers.
  
  Answer only by listing the projects.                                                    
                                                      """)

string_parser = StrOutputParser()

chain_books = chat_temp | chat | string_parser
chain_projects = chat_temp_projects | chat | string_parser

chain_parallel = RunnableParallel({"books": chain_books, "projects": chain_projects})

response = chain_parallel.invoke({"programming_language": "Python"})
print(response)

chain_parallel.get_graph().print_ascii()