from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
import copy
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma

get_pdf = PyPDFLoader("AI_Engineer_Roadmap_Clean.pdf")

loaded_pdf = get_pdf.load()

copied_pdf = copy.deepcopy(loaded_pdf)

# chunk the document
text_splitter = CharacterTextSplitter(separator=" ", chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(copied_pdf)

# print(len(docs))

# print(docs[1].page_content)

# embending the document
embending = OpenAIEmbeddings(
    model="text-embedding-ada-002",
)
# create the vector store
db = Chroma.from_documents(
    docs, embending, persist_directory="db/chroma_store"
)

# Note: this section loads the env, loads the PDF, chunks the document, embed the document and create the vector store.