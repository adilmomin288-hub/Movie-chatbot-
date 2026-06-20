import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from sentence_transformers import SentenceTransformer
from huggingface_hub import InferenceClient

load_dotenv()

class LocalEmbeddings:
    def __init__(self):
        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def embed_documents(self, texts):
        return self.model.encode(texts).tolist()

    def embed_query(self, text):
        return self.model.encode(text).tolist()

    def __call__(self, text):
        if isinstance(text, list):
            return self.embed_documents(text)
        return self.embed_query(text)

st.set_page_config(
    page_title="Movie Chatbot",
    page_icon="🎬"
)

st.title("🎬 Movie Chatbot")

embeddings = LocalEmbeddings()

db = FAISS.load_local(
    "vector_store/faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

question = st.text_input("Ask About Movies")

if question:

    docs = db.similarity_search(question, k=3)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

    client = InferenceClient(
        provider="featherless-ai",
        api_key=token
    )

    response = client.chat_completion(
        messages=[
            {"role": "system", "content": "You are a movie expert."},
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion:\n{question}"
            },
        ],
        model="mistralai/Mistral-7B-Instruct-v0.2",
        max_tokens=200,
    )

    answer = response.choices[0].message.content

    st.write(answer)
