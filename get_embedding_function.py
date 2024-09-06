from langchain_huggingface import HuggingFaceEmbeddings

from langchain.embeddings import HuggingFaceEmbeddings

def get_embedding_function():
    embeddings = HuggingFaceEmbeddings()
    return embeddings
