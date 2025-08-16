from dotenv import load_dotenv
import os

load_dotenv()

from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma

# Set the USER_AGENT environment variable if not already set
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

urls = ["https://www.apple.com/"]



# Initialize the web loader
loader = WebBaseLoader(urls)

# Load the documents
documents = loader.load()

# Print the loaded documents

# chunk the documents
text_splitter = CharacterTextSplitter(separator=" ", chunk_size=1000, chunk_overlap=0)

docs = text_splitter.split_documents(documents)

# embed the documents
# Initialize the embedding model
embedding = OpenAIEmbeddings(
    model="text-embedding-ada-002",
)

# create the vector store
vector_store = Chroma.from_documents(
    docs, embedding, persist_directory="db/chroma_store_web_scraping"
)