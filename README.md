# AI Agent

This project implements an AI agent system with a Streamlit-based web UI and a FastAPI-powered API. It utilizes a SQLite database for data storage and includes scripts for agent logic, web interface, and API endpoints.

## Features

- AI agent logic implemented in `agent.py`.
- Web interface using Streamlit (`webui.py`).
- API endpoints provided by FastAPI (`api.py`).
- SQLite database setup with `sample.db` and `sample.sql`.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jeffreychan1/ai-agent.git
   cd ai-agent
   ```

2. Install the required Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running with Ollama and Qwen2.5-7B

To run the agent using the [Qwen2.5-7B](https://ollama.com/library/qwen2:7b) model locally with [Ollama](https://ollama.com):

1. **Install Ollama**  
   Follow the installation guide for your platform: [https://ollama.com/download](https://ollama.com/download)

2. **Pull the Qwen2.5-7B model**  
   Run the following command to download the model:
   ```bash
   ollama pull qwen2:7b
   ```

## Database Setup

Create a SQLite database named `sample.db` and initialize it using the provided `sample.sql` script:

```bash
sqlite3 sample.db < sample.sql
```

This will create the necessary tables and populate them with initial records.

## Web Interface with Streamlit

The Streamlit-based web UI is provided in `webui.py`. To launch the web interface:

```bash
streamlit run webui.py
```

This will start a local web server and open the application in your default browser.

## API with FastAPI

The FastAPI application is defined in `api.py`. To run the API server:

```bash
fastapi dev api.py
```

This will start the FastAPI server with automatic reload enabled. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## License

This project is licensed under the MIT License.

## 📚 Related Article

Check out the full story behind this project on Hashnode:  
👉 [My Own Private AI Agent](https://jeffreychan.hashnode.dev/my-own-private-ai-agent)
