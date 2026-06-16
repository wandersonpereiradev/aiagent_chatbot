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

  ### Extração do conteúdo
def extract_text_pdf(file_path):
  loader = PyMuPDFLoader(file_path)
  doc = loader.load()
  content = "\n".join([page.page_content for page in doc])
  return content

### Indexação e recuperação
def config_retriever(folder_path="content"):
  # Carregar documentos
  docs_path = Path("content")
  pdf_files = [f for f in docs_path.glob("*.pdf")]

  if len(pdf_files) < 1:
    st.error("Nenhum arquivo PDF carregado")
    st.stop()

  loaded_documents = [extract_text_pdf(pdf) for pdf in pdf_files]

   # Divisão em pedaços de texto / Split
  text_splitter = RecursiveCharacterTextSplitter(
      chunk_size=1000,
      chunk_overlap=200
  )
  chunks = []
  for doc in loaded_documents:
      chunks.extend(text_splitter.split_text(doc))

  # Embeddings
  embedding_model = "BAAI/bge-m3" #sentence-transformers/all-mpnet-base-v2

  embeddings = HuggingFaceEmbeddings(model_name=embedding_model)

  # Armazenamento
  vectorstore = FAISS.from_texts(chunks, embedding=embeddings)

  vectorstore.save_local('index_faiss')

  # Configurando o recuperador de texto / Retriever
  retriever = vectorstore.as_retriever(
      search_type='mmr',
      search_kwargs={'k':3, 'fetch_k':4}
  )

  return retriever
