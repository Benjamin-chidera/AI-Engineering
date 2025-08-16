from dotenv import load_dotenv
load_dotenv()

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader
import copy
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

# Load the PDF
get_pdf = PyPDFLoader("AI_Engineer_Roadmap_Clean.pdf")
loaded_pdf = get_pdf.load()

# Make a copy of the loaded documents
copied_pdf = copy.deepcopy(loaded_pdf)

# Chunk the document while preserving metadata
text_splitter = CharacterTextSplitter(separator=" ", chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(copied_pdf)

# Initialize the embedding model
embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002",  # Ensure this is a valid OpenAI embedding model
)

# Create the vector store with metadata
db = Chroma.from_documents(
    docs, embeddings, persist_directory="db/chroma_store_metadata"
)

print("Vector store with metadata created successfully!")