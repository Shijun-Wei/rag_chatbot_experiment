import os 
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_classic.chains import RetrievalQA

class RAGChatbot:
    def __init__(self, api_key, document_path):
        # 1. Setup API Key
        os.environ["GOOGLE_API_KEY"] = api_key
        
        # 2. Load the Data correctly
        loader = TextLoader(document_path, encoding='utf-8')
        # You MUST call .load() to get the list of Documents
        documents = loader.load() 
        
        # 3. Split the Documents (Pass the list 'documents', not 'loader')
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        self.texts = text_splitter.split_documents(documents)
        
        # 4. Create Vector Store
        embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
        self.vector_db = FAISS.from_documents(self.texts, embeddings)
        
        # 5. Initialize LLM
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)
        
        # 6. Create Retrieval Chain
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=self.vector_db.as_retriever(search_kwargs={"k": 3})
        )

    def get_response(self, user_query):
        try:
            # Using invoke() is the modern standard for chains
            result = self.qa_chain.invoke({"query": user_query})
            return result["result"]
        except Exception as e:
            return f"Error processing query: {str(e)}"