from langchain_community.document_loaders import PyPDFLoader



loader = PyPDFLoader('D:/Lang Chain/Test Models/RAG/Document_loaders/random.pdf')
docs = loader.load()

print(docs[3])