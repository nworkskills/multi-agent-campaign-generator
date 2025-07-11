import gradio as gr
import asyncio
from campaign_generator import IdeaGenerationAgent, TrendRetrievalAgent, OptimizationAgent, llm, vectorstore
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Global state for chat history
chat_history = []


async def generate_campaign(query, chat_history):
    idea_agent = IdeaGenerationAgent(llm)
    trend_agent = TrendRetrievalAgent(vectorstore)
    optimize_agent = OptimizationAgent(llm)

    idea = await idea_agent.generate_idea(query)
    trends = await trend_agent.retrieve_trends(query)
    campaign = await optimize_agent.optimize_campaign(idea, trends)

    # Update chat history with messages format
    chat_history.append({"role": "user", "content": query})
    chat_history.append({"role": "assistant", "content": campaign})
    return idea, [doc.page_content for doc in trends], campaign, chat_history[-10:]  # Last 5 pairs


async def get_trending_data():
    all_trends = vectorstore.similarity_search("e-commerce trends", k=10)
    df = pd.DataFrame([(t.page_content.split(":")[0], t.metadata.get("growth_rate", "N/A")) for t in all_trends],
                      columns=["Trend", "Growth Rate"])
    return df


async def plot_trends():
    trends = vectorstore.similarity_search("e-commerce trends", k=5)
    rates = [float(t.metadata["growth_rate"].rstrip("%")) for t in trends if "growth_rate" in t.metadata]
    plt.bar([t.page_content.split(":")[0] for t in trends if "growth_rate" in t.metadata], rates)
    plt.title("Top E-Commerce Trend Growth Rates")
    plt.ylabel("Growth Rate (%)")
    plt.xticks(rotation=45)
    return plt


with gr.Blocks(title="Multi-Agent Campaign Generator") as demo:
    gr.Markdown("# Multi-Agent Campaign Generator 🎉")
    gr.Markdown("Generate personalized e-commerce campaigns with AI agents!")

    with gr.Row():
        with gr.Column():
            query_input = gr.Textbox(label="Enter Query (e.g., eco-friendly products)", lines=2)
            submit_btn = gr.Button("Generate Campaign")
            chat_output = gr.Chatbot(label="Recent Chats", height=300, type="messages")
            clear_btn = gr.Button("Clear Chat")

        with gr.Column():
            trend_table = gr.Dataframe(label="Trending E-commerce Insights", interactive=False)
            trend_graph = gr.Plot(label="Trend Growth Visualization")


    def update_trends():
        return asyncio.run(get_trending_data())


    def clear_chat():
        global chat_history
        chat_history = []
        return []


    submit_btn.click(
        fn=lambda x, y: asyncio.run(generate_campaign(x, y)),
        inputs=[query_input, chat_output],
        outputs=[gr.Textbox(label="Idea"), gr.Textbox(label="Trends"), gr.Textbox(label="Campaign Plan"), chat_output]
    ).then(update_trends, outputs=trend_table).then(plot_trends, outputs=trend_graph)

    clear_btn.click(
        fn=clear_chat,
        inputs=None,
        outputs=chat_output
    )

    demo.load(update_trends, outputs=trend_table)
    demo.load(plot_trends, outputs=trend_graph)

# Launch locally with network access, avoiding share tunneling
demo.launch(server_name="0.0.0.0", server_port=7860, share=False)