from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
import copy
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# embending the document
embending = OpenAIEmbeddings(
    model="text-embedding-ada-002",
)

llm = ChatOpenAI(
    model="gpt-3.5-turbo"
)

# load the vector store
db = Chroma(persist_directory="db/chroma_store", embedding_function=embending)

query = input("Enter query: ")

retriever = db.as_retriever(
    search_type="similarity",  # Use "similarity" instead of "similarity_score_threshold"
    search_kwargs={"k": 30},  # Corrected to "score_threshold"
)

relevant_docs = retriever.invoke(query)

# print(len(relevant_docs))

for doc in relevant_docs:
    print(doc.page_content)
    
    
combined_input = (
    f"""
    Here are some documents that might be helpful to answer the question:
    
    {query}
    
    {[doc.page_content for doc in relevant_docs]}
    
    Please provide an answer based only on the proviede documents. If the answer is not found in the documents, please reply not in the documents.
    
    """
)
    
message = [
    ("system", "You are a helpful assistant that answers questions based on the provided documents."),
    ("human", "{combined_input}")
]

prompt_temp = ChatPromptTemplate.from_messages(message)

str_output_parser = StrOutputParser()

chained_response = prompt_temp | llm | str_output_parser

response = chained_response.invoke({
    "combined_input": combined_input
})

print(response)
# Note: this section loads the env, calls the openAI embedding API, loads the vector store, and retrieves the relevant documents.