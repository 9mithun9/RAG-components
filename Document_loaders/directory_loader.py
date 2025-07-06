from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
    path='D:\Lang Chain\Test Models\RAG\Document_loaders\Books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for documents in docs:
    print(documents.metadata)