import os
import shutil
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

# Reset vector database
if os.path.exists("./vectordb"):
    shutil.rmtree("./vectordb")

# Load PDF
loader = PyPDFLoader("papers/diffusion.pdf")
documents = loader.load()

# Clean unicode
for doc in documents:
    doc.page_content = doc.page_content.encode("utf-8", "ignore").decode()

# Save full paper text for GitHub detection
full_text = "\n".join(doc.page_content for doc in documents)

with open("paper_text.txt", "w", encoding="utf-8") as f:
    f.write(full_text)

# Split text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

# Embeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# Store vector DB
db = Chroma.from_documents(
    chunks,
    embeddings,
    persist_directory="./vectordb"
)

db.persist()

print("Paper indexed successfully!")