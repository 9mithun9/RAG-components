from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

loader = TextLoader('D:\Lang Chain\Test Models\RAG\Text_splitting\code.txt', encoding='utf-8')
docs = loader.load()

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=550,
    chunk_overlap=0

)

chunk = splitter.split_text(docs[0].page_content)
print(len(chunk))
print(chunk[2])