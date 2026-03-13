from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2")

response = llm.invoke("Explain diffusion models in simple terms")

print(response)