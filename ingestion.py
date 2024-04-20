## pipenv install llama-index-vector-stores-pinecone
## pipenv install pinecone-client
## pipenv install llama-index-llms-openai
## pipenv install llama-index-embeddings-openai

import os
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.llms import openai
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import download_loader, ServiceContext, VectorStoreIndex, StorageContext
from llama_index.vector_stores.pinecone import PineconeVectorStore
# from llama_index.legacy.vector_stores import PineconeVectorStore
import pinecone





load_dotenv()

if __name__ == "__main__":
    print ("Going to ingest pinecone documentation...")
    # print (f"{os.environ['PINECONE_API_KEY']}")
    # print (f"{os.environ}")
