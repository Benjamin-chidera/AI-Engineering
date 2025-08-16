from dotenv import load_dotenv
import os

load_dotenv()

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser



# embed the documents
# Initialize the embedding model
embedding = OpenAIEmbeddings(
    model="text-embedding-ada-002",
)

llm = ChatOpenAI(model="gpt-3.5-turbo") # type: ignore

# load the documents from chroma store
db = Chroma(persist_directory="db/chroma_store_web_scraping", embedding_function=embedding)

query = input("Enter query: ")


# retrieve the documents
docs = db.as_retriever(
    search_type="similarity",  # Use "similarity" instead of "similarity_score_threshold"
    search_kwargs={"k": 30},
)

relevant_docs = docs.invoke(query)


# for doc in relevant_docs:
#     print(doc.page_content)


text = (
    f"""
        Here are some documents that might be helpful to answer the question:

    {query}
    
    {[docs.page_content for docs in relevant_docs]}
    
        Please provide an answer based only on the proviede documents. If the answer is not found in the documents, please reply i don't know.
    """
)

message = [
    ("system", "You are a helpful assistant that answers questions based on the provided documents."),
    
    ("human", "{text}")
]

str = StrOutputParser()

chat = ChatPromptTemplate.from_messages(message)

result = chat | llm | str

res = result.invoke(
    {
        "text": text,
    }
)

print(res)