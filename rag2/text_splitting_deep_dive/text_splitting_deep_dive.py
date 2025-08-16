from dotenv import load_dotenv
load_dotenv()

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader
import copy
from langchain.text_splitter import (CharacterTextSplitter, 
                                    #  SentenceTransformersTokenTextSplitter, 
                                     TokenTextSplitter, 
                                     RecursiveCharacterTextSplitter)
from langchain.vectorstores import Chroma

# Load the PDF
get_pdf = PyPDFLoader("AI_Engineer_Roadmap_Clean.pdf")
loaded_pdf = get_pdf.load()

# Make a copy of the loaded documents
copied_pdf = copy.deepcopy(loaded_pdf)

# Chunk the document while preserving metadata

# character text splitter
text_splitter = CharacterTextSplitter(separator=" ", chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(copied_pdf)

# sentence text splitter
# text_splitter_sentence = SentenceTransformersTokenTextSplitter(chunk_size=1000, chunk_overlap=0)
# docs_sentence = text_splitter_sentence.split_documents(copied_pdf)

# print(docs_sentence)

# token text splitter
text_splitter_token = TokenTextSplitter(chunk_size=1000, chunk_overlap=0)
docs_token = text_splitter_token.split_documents(copied_pdf)

# print(docs_token)

# recursive character text splitter
text_splitter_recursive = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs_recursive = text_splitter_recursive.split_documents(copied_pdf)

print(docs_recursive)

# Initialize the embedding model
embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002",  # Ensure this is a valid OpenAI embedding model
)

# Create the vector store with metadata
db = Chroma.from_documents(
    docs_recursive, embeddings, persist_directory="db/chroma_store_metadata"
)

print("Vector store with metadata created successfully!")