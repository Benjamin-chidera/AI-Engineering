from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)



chat_temp = ChatPromptTemplate.from_template('''
                                             
  What are the most important tools a {job_title} needs?
  
  Answer only by listing the tools.                                           
                                             ''')

chat_temp_strategy = ChatPromptTemplate.from_template("""
                                                      
  Considering the tools provided, develop a strategy for effectively learning and mastering them:
  {tools}                                                    
                                                      """)


string_parser = StrOutputParser()

chain_tools = chat_temp | chat | string_parser | {"tools": RunnablePassthrough()}

chat_strategy = chat_temp_strategy | chat | string_parser


chat_response = chain_tools.invoke({"job_title": "Software Engineer"})

# print(chat_response)
chat_strategy_response = chat_strategy.invoke({"tools": chat_response})

# print(chat_strategy_response)

chain_combine = chain_tools | chat_strategy
print(chain_combine.invoke({"job_title": "Software Engineer"}))

chain_combine.get_graph().print_ascii()