from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
import copy
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma

# embending the document
embending = OpenAIEmbeddings(
    model="text-embedding-ada-002",
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
    
    
# Note: this section loads the env, calls the openAI embedding API, loads the vector store, and retrieves the relevant documents.