import re
import subprocess
import os
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2")

def find_github_link(text):
    """
    Find GitHub repo link inside paper text.
    """

    pattern = r"(https?://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+|github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)"

    matches = re.findall(pattern, text)

    if matches:
        repo = matches[0]

        # remove punctuation from end (., ), etc.)
        repo = repo.rstrip(".,);")

        # ensure https
        if not repo.startswith("http"):
            repo = "https://" + repo

        return repo

    return None


def clone_repo(repo_url):
    """
    Clone GitHub repository if not already cloned.
    """

    repo_name = repo_url.split("/")[-1]

    if os.path.exists(repo_name):
        return f"Repository already exists locally: {repo_name}"

    try:
        subprocess.run(["git", "clone", repo_url], check=True)
        return f"Repository cloned successfully: {repo_name}"

    except Exception as e:
        return f"Error cloning repository: {e}"


def read_repo_files(repo_name):
    """
    Read important repo files (README mainly).
    """

    repo_text = ""

    readme_paths = [
        "README.md",
        "README.txt",
        "readme.md",
    ]

    for file in readme_paths:
        path = os.path.join(repo_name, file)

        if os.path.exists(path):
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                repo_text += f.read()

    return repo_text


def explain_repo(repo_name):
    """
    Use LLM to explain how to run the repository.
    """

    repo_text = read_repo_files(repo_name)

    if repo_text == "":
        return "README file not found. Please check repository manually."

    prompt = f"""
You are an experienced ML engineer.

Explain how to run this GitHub repository.

Include:

1. Environment setup
2. Required packages
3. Dataset preparation
4. Training command
5. Inference command

Repository README:
{repo_text}
"""

    return llm.invoke(prompt)