# Flipkart Product Recommender System

An AI-powered product recommendation chatbot built with Flask, LangChain, and RAG (Retrieval-Augmented Generation) technology.

## Features

- 🤖 AI-powered product recommendations
- 📊 Real-time product reviews and ratings
- 🛍️ Intelligent product search and suggestions
- 💬 Interactive chat interface
- 🎯 Context-aware responses using RAG

## Tech Stack

- **Backend:** Flask (Python)
- **AI/ML:** LangChain, Groq LLM
- **Vector Database:** AstraDB
- **Embeddings:** HuggingFace
- **Frontend:** HTML, CSS, JavaScript

## Setup

### Prerequisites

- Python 3.10+
- AstraDB account
- Groq API key

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd FLIPKART-PRODUCT-RECOMMENDER-SYSTEM-main
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file (copy from `.env.example`):
```bash
ASTRA_DB_API_ENDPOINT=your_endpoint
ASTRA_DB_APPLICATION_TOKEN=your_token
ASTRA_DB_KEYSPACE=your_keyspace
GROQ_API_KEY=your_groq_key
```

5. Run the application:
```bash
python app.py
```

The app will be available at `http://localhost:5000`

## Deployment on Render

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

### Quick Deploy Steps:

1. Push your code to GitHub
2. Go to [render.com](https://render.com)
3. Create a new Web Service
4. Connect your GitHub repository
5. Add environment variables in Render dashboard
6. Deploy!

## Project Structure

```
.
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   └── index.html
├── static/              # CSS and static files
│   └── style.css
├── flipkart/           # Application modules
│   ├── config.py
│   ├── data_ingestion.py
│   ├── data_converter.py
│   └── rag_chain.py
├── data/               # Data files
│   └── flipkart_product_review.csv
└── utils/              # Utility modules
```

## Environment Variables

Required environment variables:

- `ASTRA_DB_API_ENDPOINT` - Your AstraDB endpoint
- `ASTRA_DB_APPLICATION_TOKEN` - AstraDB authentication token
- `ASTRA_DB_KEYSPACE` - AstraDB keyspace name
- `GROQ_API_KEY` - Groq API key for LLM

## License

This project is for educational purposes.

"# flipkart-product-recommender" 
