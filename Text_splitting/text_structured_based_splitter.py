from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, PyPDFLoader

loader = TextLoader('D:/Lang Chain/Test Models/RAG/Text_splitting/random.txt', encoding ="utf-8")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
)

chunk = splitter.split_text(docs[0].page_content)
#print(chunk)

##........................pyPDFLoader..............................................
loader_2 = PyPDFLoader('D:/Lang Chain/Test Models/RAG/Text_splitting/random.pdf')
docs_2 = loader_2.load()

chunk_2 = splitter.split_documents(docs_2)
print(chunk_2[0])

