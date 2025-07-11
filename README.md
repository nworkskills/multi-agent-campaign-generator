# Multi-Agent Campaign Generator

## Overview
Welcome to the **Multi-Agent Campaign Generator**, a cutting-edge demonstration of artificial intelligence (AI) leveraging multi-agent systems and generative AI to craft personalized e-commerce campaign plans. This project features three specialized agents—Idea Generation Agent, Trend Retrieval Agent, and Optimization Agent—working collaboratively to create innovative marketing strategies tailored to current market trends. Built with Python, Docker, and advanced AI tools like OpenAI, Pinecone, and LangChain, this demo is designed to educate and inspire developers, students, business professionals, and trainers. It now includes a REST API for production-ready integration, accessible via a new `main.py` script.

## Purpose
- **Demonstrate Multi-Agent Collaboration:** Showcase how multiple AI agents can work together to solve complex problems.
- **Teach Key Concepts:** Provide hands-on learning in data ingestion, trend retrieval, campaign optimization, asynchronous programming with asyncio, and REST API development.
- **Highlight Real-World Applications:** Illustrate practical use cases in e-commerce, with scalability for other industries.
- **Encourage Innovation:** Inspire users to adapt this framework for their own projects or businesses.

## Benefits
- **Educational Value:** Offers a step-by-step guide for learning AI, multi-agent systems, and API integration, ideal for students and developers.
- **Business Impact:** Enables e-commerce businesses to launch targeted campaigns, boosting sales and market relevance.
- **Future-Ready Skills:** Equips users with skills aligned with the growing $6T e-commerce market and $47.1B AI agent market by 2030.

## Architecture
### Components
- **Idea Generation Agent:** Utilizes the OpenAI API to generate creative product ideas (e.g., "Eco-friendly reusable water bottles") based on user queries. This agent leverages generative AI to spark innovation, ensuring campaigns start with unique, market-relevant concepts.
- **Trend Retrieval Agent:** Queries a Pinecone vector store to fetch up-to-date e-commerce trends (e.g., "Sustainable products up 25%") using vector embeddings for semantic similarity search. It grounds the campaign in real-world data.
- **Optimization Agent:** Employs LangChain to synthesize inputs from the Idea and Trend Agents, optimizing the campaign with suggested channels (e.g., "Instagram ads, eco-blogs") and strategies. It uses generative AI to refine and personalize the plan.
- **Gradio UI:** Provides an interactive web interface for real-time query input and output visualization, enhancing user engagement.
- **REST API (via `main.py`):** Offers a production-ready endpoint (`/generate/{query}`) for programmatic access to campaign generation, ideal for integration into business workflows.

### Flow
- Agents share data via a LangChain memory module, enabling seamless collaboration.
- Asynchronous processing with asyncio ensures efficient, non-blocking execution.
- The system produces a JSON-formatted campaign plan, displayed in the Gradio UI, terminal, or accessible via the REST API.

### Deployment
- **Containerized with Docker:** Ensures portability and consistency across environments.
- **Optional Enhancements:** Includes a REST API and advanced Gradio UI for production-ready interactivity.

## Tree Structure of Files
```
multi-agent-campaign-generator/
├── campaign_generator/
│   ├── ingest_campaign_data.py      # Script to ingest trend data into Pinecone
│   ├── campaign_generator.py        # Main script with agent definitions and execution
│   ├── main.py                      # REST API script for campaign generation
│   ├── app.py                       # Gradio UI script for interactive demo
│   ├── campaign_data.csv            # Sample dataset with 30 e-commerce trends
│   ├── .env                         # Environment file for API keys
│   ├── Dockerfile                   # Docker configuration for containerization
│   └── requirements.txt             # List of Python dependencies
├── README.md                        # This documentation file
└── LICENSE                          # MIT License file
```

## Files and Their Roles
- **`ingest_campaign_data.py`:** Ingests `campaign_data.csv` into the Pinecone "campaign-trends" index, converting trends into vectorized documents for retrieval.
- **`campaign_generator.py`:** Defines and orchestrates the three agents, executing the campaign generation process with a default query or user input.
- **`main.py`:** Implements a FastAPI REST API with a `/generate/{query}` endpoint, allowing programmatic access to the multi-agent system for production use.
- **`app.py`:** Implements the Gradio UI, offering a web-based interface to interact with the agents, display chats, trends, and visualizations.
- **`campaign_data.csv`:** Contains 30 records of e-commerce trends with `trend`, `description`, and `growth_rate` columns, serving as the knowledge base.
- **`.env`:** Stores sensitive API keys (e.g., `OPENAI_API_KEY`, `PINECONE_API_KEY`) for secure access to third-party services.
- **`Dockerfile`:** Configures the Docker container environment, ensuring consistent deployment.
- **`requirements.txt`:** Lists dependencies (e.g., `langchain`, `openai`, `pinecone-client`, `gradio`, `pandas`, `matplotlib`, `fastapi`, `uvicorn`) for easy setup.

## Sample Data: `campaign_data.csv` (30 Records)
### Content
A CSV file with columns `trend`, `description`, and `growth_rate`, providing a dataset of e-commerce trends.

### Sample Data (First 5 Records)
```
trend,description,growth_rate
Sustainable Packaging,Eco-friendly materials reduce waste,15%
Smart Home Devices,AI-powered home automation,22%
Vegan Cosmetics,Cruelty-free beauty products,18%
Wearable Tech,Fitness trackers and smartwatches,25%
Personalized Gifts,Customized items for holidays,12%
...
```

### Total Records
30 (full list available in the repository—includes trends like "Organic Food," "AR Shopping," etc.).

### Collection Method
Data was aggregated from public e-commerce reports (e.g., Statista, eMarketer) and enhanced with AI-generated trends using OpenAI, collected over June 2025 to simulate real-world market analysis.

### Explanation for Viewers
"I collected this data by combining insights from e-commerce reports with AI-generated trends, mimicking how businesses analyze markets. We’ll ingest it into Pinecone to power our agents, and you can update it with your own data!"

## Setup
### Prerequisites
- Python 3.10+
- Docker Desktop
- Git
- API keys for OpenAI and Pinecone (sign up at [OpenAI](https://platform.openai.com/) and [Pinecone](https://www.pinecone.io/))

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/nworkskills/multi-agent-campaign-generator.git
   cd multi-agent-campaign-generator/campaign_generator
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   PINECONE_API_KEY=your_pinecone_api_key
   ```
4. Build the Docker image:
   ```
   docker build -t multi-agent-campaign-generator .
   ```

## Usage
### Local Execution
- **Ingest Data:**
  ```
  python ingest_campaign_data.py
  ```
  - Expected Output: `Ingested 30 campaign trends.`
- **Run Generator:**
  ```
  python campaign_generator.py
  ```
  - Expected Output: Campaign details (e.g., Idea, Trends, Campaign Plan).
- **Launch Gradio UI:**
  ```
  python app.py
  ```
  - Access at `http://127.0.0.1:7860` (use `server_name="0.0.0.0"` for local network access).
- **Run REST API:**
  ```
  python main.py
  ```
  - Access at `http://0.0.0.0:8080/generate/{query}` (e.g., `http://0.0.0.0:8080/generate/eco-friendly`).
  - Test with: `curl http://0.0.0.0:8080/generate/eco-friendly`

### Docker Commands
- **Build Image (Windows-Compatible):**
  ```
  docker build -t multi-agent-campaign-generator .
  ```
- **Run Ingestion (Windows Absolute Path):**
  ```
  docker run -it --name ingest-container -v C:\Users\asudh\PycharmProjects\pythonProject\campaign_generator\campaign_data.csv:/app/campaign_data.csv -v C:\Users\asudh\PycharmProjects\pythonProject\campaign_generator\.env:/app/.env multi-agent-campaign-generator python ingest_campaign_data.py
  ```
  - Check logs: `docker logs ingest-container`
- **Run Generator (Windows Absolute Path):**
  ```
  docker run -it --name campaign-container -v C:\Users\asudh\PycharmProjects\pythonProject\campaign_generator\campaign_data.csv:/app/campaign_data.csv -v C:\Users\asudh\PycharmProjects\pythonProject\campaign_generator\.env:/app/.env multi-agent-campaign-generator python campaign_generator.py
  ```
  - Check logs: `docker logs campaign-container`
- **Run REST API (Windows Absolute Path):**
  ```
  docker run -it --name api-container -v C:\Users\asudh\PycharmProjects\pythonProject\campaign_generator\campaign_data.csv:/app/campaign_data.csv -v C:\Users\asudh\PycharmProjects\pythonProject\campaign_generator\.env:/app/.env -p 8080:8080 multi-agent-campaign-generator python main.py
  ```
  - Access at `http://localhost:8080/generate/{query}`; check logs: `docker logs api-container`
- **Cleanup:**
  ```
  docker stop ingest-container campaign-container api-container
  docker rm ingest-container campaign-container api-container
  ```

### Notes
- Replace `C:\Users\asudh\PycharmProjects\pythonProject\campaign_generator\` with your absolute path.
- Use `-it` for interactive mode to see output directly; use `-d` for detached mode and check logs later.
- For REST API, ensure port 8080 is open and not in use.

## Gradio UI Details
### What is Gradio?
Gradio is a Python library that creates interactive web interfaces for machine learning models or scripts. It allows users to input data and see outputs in real-time without complex web development.

### How is it Useful?
- Enables rapid prototyping and testing of AI models.
- Provides an accessible interface for non-technical users.
- Supports visualizations (e.g., tables, charts) for better understanding.

### Why Used in This Demo?
- Offers a live, interactive experience for viewers to test queries (e.g., "eco-friendly products").
- Enhances the tutorial with a chat display, trend table, and growth rate graph.
- Can be extended for production with features like user authentication or cloud deployment.

### Advanced Mode for Production
- Add persistent storage (e.g., save campaigns to a database).
- Integrate with cloud services (e.g., AWS) for scalability.
- Implement user authentication and API endpoints for enterprise use.

## Agent Details
### Idea Generation Agent
- **Role:** Uses OpenAI’s generative AI to propose creative product ideas based on user queries.
- **Example:** For "sustainable fashion," it might suggest "recycled fabric jackets."
- **Implementation:** Employs a prompt template and async processing for efficiency.

### Trend Retrieval Agent
- **Role:** Retrieves relevant trends from the Pinecone vector store using semantic search.
- **Example:** Returns "Sustainable Packaging: 15% growth" for "eco-friendly" queries.
- **Implementation:** Leverages vector embeddings and similarity search with a limit of 3 trends.

### Optimization Agent
- **Role:** Synthesizes the idea and trends into a campaign plan using LangChain’s orchestration.
- **Example:** Combines "recycled fabric jackets" with trends to suggest "Instagram ads targeting eco-buyers."
- **Implementation:** Uses a generative prompt and async chaining for optimized output.

## Advantages for E-Commerce Campaigns
- **Personalization:** Tailors campaigns to specific customer segments, increasing conversion rates.
- **Efficiency:** Automates idea generation and strategy planning, saving time and costs.
- **Data-Driven:** Incorporates real-time trends, aligning with market demands (e.g., 25% growth in Wearable Tech).
- **Scalability:** Handles large datasets and multiple campaigns with Docker deployment.

## Other Domains and Applications
- **Healthcare:** Agents could generate personalized treatment plans using patient data and medical trends.
- **Education:** Create customized learning modules based on student performance and educational trends.
- **Finance:** Develop investment strategies using market data and AI-generated insights.
- **Entertainment:** Design personalized content recommendations or event promotions.
- **Manufacturing:** Optimize product designs and marketing based on industry trends.

## License
This project is licensed under the [MIT License](LICENSE), allowing free use, modification, and distribution.

## Contributing
- Fork the repository and submit pull requests.
- Report issues or suggest features via GitHub Issues.
- Join the discussion in the [@bridge_2_success YouTube comments](https://www.youtube.com/...).

## Acknowledgments
- Thanks to OpenAI, Pinecone, and LangChain for their powerful APIs and libraries.
- Inspired by the growing need for AI-driven solutions in e-commerce and beyond.

---

