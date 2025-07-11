import asyncio
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
import platform

load_dotenv()
print("Loading environment variables...")
embeddings = OpenAIEmbeddings(api_key=os.environ.get("OPENAI_API_KEY", "No API key found"))
print(f"Initialized embeddings with API key: {bool(os.environ.get('OPENAI_API_KEY'))}")
vectorstore = PineconeVectorStore.from_existing_index(index_name="campaign-trends", embedding=embeddings)
print("Vector store initialized.")
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, api_key=os.environ.get("OPENAI_API_KEY", "No API key found"))
print("Initialized language model.")

class IdeaGenerationAgent:
    def __init__(self, llm):
        self.llm = llm

    async def generate_idea(self, query):
        print(f"Generating idea for query: {query}")
        prompt = ChatPromptTemplate.from_template("Suggest a creative product idea for an e-commerce campaign based on: {query}")
        chain = prompt | self.llm | StrOutputParser()
        return await chain.ainvoke({"query": query})

class TrendRetrievalAgent:
    def __init__(self, vectorstore):
        self.vectorstore = vectorstore

    async def retrieve_trends(self, query):
        print(f"Retrieving trends for query: {query}")
        results = vectorstore.similarity_search(query, k=3)
        print(f"Retrieved {len(results)} trends.")
        return results

class OptimizationAgent:
    def __init__(self, llm):
        self.llm = llm

    async def optimize_campaign(self, idea, trends):
        print(f"Optimizing campaign for idea: {idea}")
        trend_text = "\n".join([doc.page_content for doc in trends])
        prompt = ChatPromptTemplate.from_template("Optimize a campaign for: {idea} using trends: {trends}. Suggest channels and strategy.")
        chain = prompt | self.llm | StrOutputParser()
        return await chain.ainvoke({"idea": idea, "trends": trend_text or "No trends available"})

async def main():
    print("Initializing agents...")
    idea_agent = IdeaGenerationAgent(llm)
    trend_agent = TrendRetrievalAgent(vectorstore)
    optimize_agent = OptimizationAgent(llm)

    query = "eco-friendly products"  # Default query
    print(f"Processing query: {query}")
    idea = await idea_agent.generate_idea(query)
    trends = await trend_agent.retrieve_trends(query)
    campaign = await optimize_agent.optimize_campaign(idea, trends)

    print(f"Idea: {idea}")
    print(f"Trends: {[doc.page_content for doc in trends]}")
    print(f"Campaign Plan: {campaign}")

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())