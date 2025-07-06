from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='D:\Lang Chain\Test Models\RAG\Document_loaders\lgbtq.csv')

docs = loader.load()

print(docs[4].page_content)