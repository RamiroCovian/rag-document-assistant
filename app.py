import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

load_dotenv()

# API de Pinecone
pinecone_api_key = os.getenv("PINECONE_API_KEY")

if not pinecone_api_key:
    raise ValueError("PINECONE_API_KEY no está configurada")

# Creando conexion con Pinecone.
pc = Pinecone(api_key=pinecone_api_key)
index = pc.Index("rag-document-assistant")

# Hago llamada a Pinecone para corroborar conexion.
print(index.describe_index_stats())
