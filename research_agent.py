import os
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from tools import find_github_link, clone_repo, explain_repo


llm = OllamaLLM(model="llama3.2")

embeddings = OllamaEmbeddings(model="nomic-embed-text")

db = Chroma(
    persist_directory="./vectordb",
    embedding_function=embeddings
)

retriever = db.as_retriever()

query = input("Ask about the paper: ")

docs = retriever.invoke(query)

context = "\n\n".join([doc.page_content for doc in docs])

print("\nChecking for GitHub implementation...\n")

with open("paper_text.txt", "r", encoding="utf-8") as f:
    paper_text = f.read()
repo = find_github_link(paper_text)

if repo:
    print("GitHub repository found:")
    print(repo)

    print("\nCloning repository...\n")

    repo_name = repo.split("/")[-1]

    print(clone_repo(repo))

    print("\nAnalyzing repository...\n")

    instructions = explain_repo(repo_name)

    print(instructions)

    with open("repo_instructions.txt", "w", encoding="utf-8") as f:
        f.write(instructions)

else:
    print("No official repository found.\n")
    
    prompt = f"""
Generate a PyTorch implementation skeleton for the following ML method.

Method description:
{context}
"""
    
    print(llm.invoke(prompt))
