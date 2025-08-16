from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

# chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)


find_sum = lambda x: sum(x)
runnable = RunnableLambda(lambda x: sum(x))

print(runnable.invoke([1, 2, 3, 4, 5]))