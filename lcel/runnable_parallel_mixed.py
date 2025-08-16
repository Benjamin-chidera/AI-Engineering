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

chat_tem_time = ChatPromptTemplate.from_template("""
  
 I am an intermediate-level programmer.  
 
 Consider the following literature:
 {books}
 
 Also, consider the following projects:
 {projects}
 
 Roughly how much time would it take to read the books and complete the projects?                                             
                                                      """)

string_parser = StrOutputParser()

chain_books = chat_temp | chat | string_parser
chain_projects = chat_temp_projects | chat | string_parser

chain_parallel = RunnableParallel({"books": chain_books, "projects": chain_projects})
chain_time = RunnableParallel({"books": chain_books, "projects": chain_projects}) | chat_tem_time | chat | string_parser

response = chain_parallel.invoke({"programming_language": "Python"})

chain_time_response = chain_time.invoke({
  "programming_language": "Python",
  "books": chain_books
})

print("Books and Projects:", chain_time_response)

chain_parallel.get_graph().print_ascii()