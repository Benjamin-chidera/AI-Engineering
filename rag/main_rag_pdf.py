from langchain_community.document_loaders import PyPDFLoader
import copy

loader_pdf = PyPDFLoader("AI_Engineer_Roadmap_Clean.pdf")
pages_pdf = loader_pdf.load()

pages_pdf_cut = copy.deepcopy(pages_pdf)

joined_text = " ".join(pages_pdf_cut[0].page_content.split())

for i in pages_pdf_cut:
    i.page_content = " ".join(pages_pdf_cut[0].page_content.split())
    
    
print(pages_pdf_cut)