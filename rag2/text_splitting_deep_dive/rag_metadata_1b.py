from dotenv import load_dotenv
load_dotenv()

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# Initialize the embedding model
embedding = OpenAIEmbeddings(
    model="text-embedding-ada-002",  # Ensure this is a valid OpenAI embedding model
)

# Load the vector store
db = Chroma(persist_directory="db/chroma_store_metadata", embedding_function=embedding)

# Query the vector store
query = input("Enter query: ")

retriever = db.as_retriever(
    search_type="similarity",  # Use "similarity" for Chroma
    search_kwargs={"k": 30}  # Retrieve the top 30 most relevant documents
)

# Retrieve relevant documents
relevant_docs = retriever.get_relevant_documents(query)

# Print the relevant documents
for doc in relevant_docs:
    print(doc.page_content)
    print(doc.metadata)  # Print metadata for each document