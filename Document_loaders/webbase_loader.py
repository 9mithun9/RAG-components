from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model = "gpt-4o"
)

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Provide me the code for working with files from the text below:\n {text}",
    input_variables=['text']
)

url = 'https://python.langchain.com/docs/integrations/document_loaders/pypdfloader/'
loader = WebBaseLoader(url)
docs = loader.load()

chain = prompt | model | parser
result = chain.invoke({'text':docs[0].page_content})
print(result)


