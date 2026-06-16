from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from langchain_classic.chains import create_history_aware_retriever, create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Atendimento SafeBank 🤖", page_icon="🤖")
st.title("Atendimento SafeBank")

id_model = "llama-3.3-70b-versatile"
temperature = 0.7
path = "content"

### Carregamento da LLM
def load_llm(id_model, temperature):
  llm = ChatGroq(
    model=id_model,
    temperature=temperature,
    max_tokens=None,
    timeout=None,
    max_retries=2,
  )
  return llm

llm = load_llm(id_model, temperature)

### Exibição do resultado
def show_res(res):
  from IPython.display import Markdown
  if "</think>" in res:
    res = res.split("</think>")[-1].strip()
  else:
    res = res.strip()  # fallback se não houver tag
  display(Markdown(res))