import asyncio
import os
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
import pandas as pd
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import platform

load_dotenv()
print("Loading environment variables...")
pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY", "No API key found"))
print(f"Initialized Pinecone client with API key: {bool(os.environ.get('PINECONE_API_KEY'))}")
index_name = "campaign-trends"

print(f"Checking index: {index_name}")
if index_name in pc.list_indexes().names():
    print(f"Deleting existing index: {index_name}")
    pc.delete_index(index_name)
print(f"Creating new index: {index_name}")
pc.create_index(
    name=index_name,
    dimension=1536,
    metric="cosine",
    spec=ServerlessSpec(cloud="aws", region="us-east-1")
)
print(f"Index created: {index_name}")

embeddings = OpenAIEmbeddings(api_key=os.environ.get("OPENAI_API_KEY", "No API key found"))
print(f"Initialized embeddings with API key: {bool(os.environ.get('OPENAI_API_KEY'))}")
vectorstore = PineconeVectorStore.from_existing_index(index_name=index_name, embedding=embeddings)
print("Vector store initialized.")

async def ingest_data(vectorstore):
    print("Starting data ingestion...")
    try:
        df = pd.read_csv("campaign_data.csv", encoding="utf-8", on_bad_lines="skip")
        print(f"Loaded CSV with {len(df)} records: {df.head()}")
        documents = [Document(page_content=f"{row['trend']}: {row['description']}", metadata={"growth_rate": row["growth_rate"]}) for _, row in df.iterrows()]
        print(f"Processed {len(documents)} documents.")
        await vectorstore.aadd_documents(documents)
        print(f"Ingested {len(documents)} campaign trends.")
        await asyncio.sleep(5)  # Ensure index updates
        print("Ingestion completed with 5-second delay.")
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except Exception as e:
        print(f"Error during ingestion: {e}")

async def main():
    print("Running main ingestion process...")
    await ingest_data(vectorstore)

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())