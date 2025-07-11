from fastapi import FastAPI
from fastapi.responses import JSONResponse
import asyncio
from campaign_generator import IdeaGenerationAgent, TrendRetrievalAgent, OptimizationAgent, llm, vectorstore

app = FastAPI()


@app.get("/generate/{query}")
async def generate_campaign_api(query: str):
    idea_agent = IdeaGenerationAgent(llm)
    trend_agent = TrendRetrievalAgent(vectorstore)
    optimize_agent = OptimizationAgent(llm)

    idea = await idea_agent.generate_idea(query)
    trends = await trend_agent.retrieve_trends(query)
    campaign = await optimize_agent.optimize_campaign(idea, trends)

    return JSONResponse({
        "idea": idea,
        "trends": [doc.page_content for doc in trends],
        "campaign_plan": campaign
    })

# Run with: uvicorn app:app --reload
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)