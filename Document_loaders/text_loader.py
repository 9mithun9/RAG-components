from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(
    model = "gpt-4o"
)

loader = TextLoader('D:/Lang Chain/Test Models/RAG/Document_loaders/text_loader.txt', encoding='utf-8')
docs = loader.load()

print(docs[0].page_content)

str_parser = StrOutputParser()
prompt = PromptTemplate(
    template="Generate an encrypted quize from the text below: \n {text}",
    input_variables=['text']
)

chain = prompt | model | str_parser

result = chain.invoke({'text': docs[0].page_content})
print(result)



