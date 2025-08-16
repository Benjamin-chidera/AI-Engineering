from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters.character import CharacterTextSplitter

loader_docx = Docx2txtLoader("Introduction_to_Data_and_Data_Science.docx")

page_docx = loader_docx.load()

for i in range(len(page_docx)):
    page_docx[i].page_content = " ".join(page_docx[i].page_content.split())
    
    
char_splitter = CharacterTextSplitter(separator=" ", chunk_size=500, chunk_overlap=0)

pages_char_split = char_splitter.split_documents(page_docx)

# print(len(pages_char_split))

print(pages_char_split[16].page_content)