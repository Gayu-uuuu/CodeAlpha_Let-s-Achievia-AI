#  Let's Achievia AI – Student Support Chatbot

Let's Achievia AI is an intelligent chatbot designed to support students by answering queries with context awareness and conversational memory. It uses Retrieval-Augmented Generation (RAG) to provide accurate, relevant, and natural responses.

---

##  Features

-  Conversational chatbot with memory  
-  Context-aware answers using vector search  
-  Remembers previous interactions within a session  
-  Retrieval-Augmented Generation (RAG) pipeline  
-  Fast responses using Groq LLM API  
-  Simple and interactive web interface  

---

## Tech Stack

- Python  
- Flask  
- ChromaDB (Vector Database)  
- Groq API (LLM)  
- HTML, CSS  

---

##  How It Works

1. User asks a question  
2. Relevant context is retrieved from the vector database  
3. Conversation history is included for better understanding  
4. LLM generates a natural, human-like response  

---

## Retrieval-Augmented Generation (RAG)

Let's Achievia AI uses a Retrieval-Augmented Generation (RAG) approach to improve response accuracy and reliability.

Instead of relying only on the language model, the system retrieves relevant information from a vector database and uses it as context for generating responses.

### RAG Pipeline

1. User submits a query  
2. Query is converted into embeddings  
3. ChromaDB retrieves the most relevant documents  
4. Retrieved context is combined with conversation history  
5. LLM generates a grounded and context-aware response  

###  Why RAG?

- Reduces hallucination  
- Improves factual accuracy  
- Enables domain-specific responses  
- Makes the chatbot more reliable and scalable  

---

##  Project Structure
├── app.py
├── templates/
│ └── vetri.html
├── vectorstore/ (ignored)
├── .env (ignored)
├── .gitignore
└── README.md


---

##  Environment Setup

Create a `.env` file in the root directory and add:


GROQ_API_KEY=your_api_key_here


---

##  Run Locally

Install dependencies:

pip install -r requirements.txt


Run the application:

python app.py


Open in browser:

http://127.0.0.1:5000


---

##  Notes

- `.env` and `vectorstore/` are excluded for security and performance  
- Add your own API key to run the project  
- Vector database must be populated before use  

---

##  Future Improvements

- Multi-user memory support  
- Improved UI/UX  
- Deployment (Render / Vercel / AWS)  
- Voice-enabled interaction
- More Human-like Response

---

##  Acknowledgment

This project was developed as part of an internship to explore real-world applications of LLMs and conversational AI.

---

##  Author

Gayathri S  


