# AI Agent - SafeBank Customer Support Chatbot 🤖

## Overview

This project is an AI-powered chatbot agent designed to answer questions about a fictional bank called **SafeBank**.

The chatbot uses a document-based knowledge approach, where answers are generated based on the information available in the provided bank manual:

```
content/manual-safebank.pdf
```

The main goal of this project is to demonstrate the implementation of an AI Agent capable of retrieving information from a knowledge base and generating accurate responses using a Large Language Model (LLM).

The application simulates a customer support assistant that can help users with questions related to:

* Banking products
* Account information
* Services
* Policies
* Procedures
* Frequently asked questions

---

# Project Structure

```
AIAGENT_CHATBOT/
│
├── content/
│   └── manual-safebank.pdf
│
├── .env
├── app.py
└── requirements.txt
```

---

# Files Description

| File                          | Description                                                                   |
| ----------------------------- | ----------------------------------------------------------------------------- |
| `.env`                        | Stores environment variables, including the Groq API Key                      |
| `app.py`                      | Main application containing the chatbot interface and AI agent implementation |
| `requirements.txt`            | List of Python dependencies required to run the project                       |
| `content/manual-safebank.pdf` | Knowledge base document used by the chatbot to answer user questions          |

---

# Technologies Used

## Python

Python is the main programming language used to develop the AI Agent.

It is responsible for:

* Application logic
* Document processing
* AI workflow orchestration
* User interaction handling

---

## Streamlit

Streamlit is used to create the chatbot web interface.

It provides:

* Interactive chat experience
* User input handling
* Display of generated responses
* Simple web application deployment

---

## LangChain

LangChain is used as the framework for building the AI workflow.

It provides components for:

* Connecting the application with the LLM
* Creating prompts
* Managing document retrieval
* Building the RAG pipeline

The chatbot uses LangChain to combine user questions with relevant information retrieved from the knowledge base.

---

## Retrieval-Augmented Generation (RAG)

The project uses the RAG architecture to improve the accuracy of responses.

The workflow is:

1. The user sends a question through the chatbot.
2. The system searches the SafeBank manual for relevant information.
3. The retrieved content is added to the LLM prompt.
4. The LLM generates a response based on the retrieved knowledge.

This approach reduces hallucinations by grounding answers in a trusted source document.

---

## Groq API

The project uses Groq as the Large Language Model provider.

The application requires a Groq API Key to communicate with the LLM.

Groq provides high-performance inference for AI models, enabling fast chatbot responses.

---

## python-dotenv

The project uses `python-dotenv` to load environment variables from the `.env` file.

The required environment variable is:

```env
GROQ_API_KEY
```

This key authenticates requests made to the Groq API.

---

# How the AI Agent Works

The chatbot workflow follows these steps:

1. The user enters a question in the Streamlit chatbot interface.
2. The application processes the user request.
3. The system searches the SafeBank PDF document for relevant information.
4. The retrieved context is combined with the user question.
5. The prompt is sent to the Groq LLM.
6. The generated answer is displayed to the user.

---

# Installation and Setup

## 1. Clone the repository

Clone this repository:

```bash
git clone <repository-url>
```

Navigate into the project folder:

```bash
cd AIAGENT_CHATBOT
```

---

# 2. Create and activate a virtual environment

Creating a virtual environment is recommended to isolate project dependencies.

Create the environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

# 3. Install project dependencies

All required dependencies are listed in the:

```
requirements.txt
```

file.

Install them using:

```bash
pip install -r requirements.txt
```

This command installs all required libraries, including:

* Streamlit
* LangChain
* Groq integration libraries
* Document processing dependencies
* AI and data processing packages

---

# 4. Configure Groq API Key

This project requires a Groq API Key to access the Large Language Model.

## Creating a Groq Account

1. Access the Groq platform:

```
https://console.groq.com/
```

2. Create an account or sign in.

3. After authentication, navigate to:

```
Dashboard → API Keys
```

4. Click:

```
Create API Key
```

5. Enter a name for your API Key.

6. Generate and copy the key.

⚠️ Keep your API Key secure. Never commit it to GitHub or expose it publicly.

---

## Configure the `.env` file

Create or edit the `.env` file in the project root directory:

```
AIAGENT_CHATBOT/
│
├── .env
├── app.py
└── requirements.txt
```

Add the following variable:

```env
GROQ_API_KEY=your_api_key_here
```

Replace:

```
your_api_key_here
```

with the API Key generated in Groq.

Example:

```env
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxx
```

---

# 5. Run the Application

Inside the project root directory, execute:

```bash
python -m streamlit run app.py
```

After starting, Streamlit will provide a local URL similar to:

```
http://localhost:8501
```

Open this URL in your browser to access the chatbot.

---

# Example Usage

The chatbot can answer questions related to the fictional SafeBank documentation.

Examples:

```
What documents are required to open an account?
```

```
How can I request a new banking service?
```

```
What are the available account types?
```

The answers are generated based on the information contained in:

```
content/manual-safebank.pdf
```

---

# License

This project is intended for educational and demonstration purposes related to:

* Artificial Intelligence Agents
* Generative AI
* Large Language Models
* Retrieval-Augmented Generation (RAG)
* AI-powered customer support systems
