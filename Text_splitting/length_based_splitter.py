from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader, PyPDFLoader

loader = TextLoader('D:/Lang Chain/Test Models/RAG/Document_loaders/text_loader.txt', encoding='utf-8')
docs = loader.load()

#print(docs[0].page_content)

splitter = CharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=5,
    separator=''
)

result = splitter.split_text(docs[0].page_content)
#print(result)


loader_2 = PyPDFLoader('D:/Lang Chain/Test Models/RAG/Text_splitting/random.pdf')
docs_2 = loader_2.load()

result_2 = splitter.split_documents(docs_2)
print(result_2[1])