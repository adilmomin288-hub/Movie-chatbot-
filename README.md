# 🎬 Movie Chatbot using RAG, LangChain, FAISS & Streamlit

## 📌 Project Overview

This project is an AI-powered Movie Chatbot built using Retrieval-Augmented Generation (RAG), LangChain, FAISS Vector Database, OpenAI, and Streamlit.

The chatbot retrieves relevant information from the IMDb Movie Dataset and provides accurate answers to user queries using semantic search and Large Language Models (LLMs).

---

## 🚀 Features

* AI-powered conversational chatbot
* Retrieval-Augmented Generation (RAG)
* Semantic search using FAISS Vector Database
* LangChain integration
* Streamlit web interface
* OpenAI LLM for intelligent responses
* IMDb movie dataset support
* Fast and accurate information retrieval

---

## 🛠️ Technologies Used

* Python
* Streamlit
* LangChain
* OpenAI
* FAISS
* Pandas
* dotenv

---

## 📂 Project Structure

movie-chatbot/

├── app.py

├── rag.py

├── requirements.txt

├── .env

├── data/

│ └── IMDB-Movie-Data.csv

└── faiss_index/

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/movie-chatbot.git

cd movie-chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a `.env` file in the project root directory.

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## 📊 Dataset

This project uses the IMDb Movie Dataset containing information such as:

* Movie Title
* Genre
* Director
* Description
* Rating
* Votes
* Revenue

The dataset is stored inside:

```text
data/IMDB-Movie-Data.csv
```

---

## 🧠 Creating FAISS Vector Database

Run the following command:

```bash
python rag.py
```

This will:

1. Load the IMDb dataset
2. Generate embeddings
3. Create FAISS vector index
4. Save the index locally

---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the browser:

```text
http://localhost:8501
```

---

## 💬 Example Questions

* Who directed Interstellar?
* What is the rating of Inception?
* Tell me about The Dark Knight.
* Which movie has the highest rating?
* Show movies directed by Christopher Nolan.

---

## 🔄 RAG Workflow

User Query

↓

Streamlit Interface

↓

LangChain Retriever

↓

FAISS Similarity Search

↓

Relevant Context Retrieved

↓

OpenAI LLM

↓

Final Response

---

## 📈 Future Enhancements

* PDF Document Support
* Chat History
* User Authentication
* Multi-file Knowledge Base
* HuggingFace Embeddings
* Groq Integration
* Cloud Deployment
* Voice Assistant Support

---

## 👨‍💻 Author

Adil Momin

Cyber Security & AI Enthusiast

---

## 📜 License

This project is developed for educational and learning purposes.
