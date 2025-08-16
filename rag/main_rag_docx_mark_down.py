from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters.markdown import MarkdownHeaderTextSplitter
from langchain_text_splitters.character import CharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings

loader_docx = Docx2txtLoader("Introduction_to_Data_and_Data_Science_2.docx")

page_docx = loader_docx.load()


md_splitter = MarkdownHeaderTextSplitter(headers_to_split_on= [("Introduction", "Introduction to Data and Data Science"), ("Data Science", "Data Sciences"), ("Analysis", "Ana")])

page_split_md = md_splitter.split_text(page_docx[0].page_content)

# print(page_split_md)

for i in range(len(page_split_md)):
    page_split_md[i].page_content = " ".join(page_split_md[i].page_content.split())
    
char_splitter = CharacterTextSplitter(
    separator=" ", chunk_size=500, chunk_overlap=50
)

page_char_split = char_splitter.split_documents(page_split_md)

embending = OpenAIEmbeddings(model="text-embedding-ada-002")

vector_1 = embending.embed_query(page_char_split[3].page_content)
vector_2 = embending.embed_query(page_char_split[5].page_content)
vector_3 = embending.embed_query(page_char_split[18].page_content)

print(vector_1)