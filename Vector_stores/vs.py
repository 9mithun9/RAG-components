# %% [markdown]
# # My Project Title
# This is a markdown cell in Colab-style.

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

from langchain_core.documents import Document

documents = [
    Document(
        page_content="Climate change is a long-term alteration of temperature and typical weather patterns in a place.",
        metadata={"topic": "Climate Change"}
    ),
    Document(
        page_content="AI enables computers and machines to mimic human intelligence and perform tasks like problem-solving.",
        metadata={"topic": "Artificial Intelligence"}
    ),
    Document(
        page_content="The Great Wall of China was built to protect Chinese states against invasions and raids from nomadic groups.",
        metadata={"topic": "The Great Wall of China"}
    ),
    Document(
        page_content="Electric vehicles use electric motors powered by batteries, reducing carbon emissions significantly.",
        metadata={"topic": "Electric Vehicles"}
    ),
    Document(
        page_content="The human brain is a complex organ responsible for thought, memory, emotion, and sensory processing.",
        metadata={"topic": "The Human Brain"}
    ),
    Document(
        page_content="Photosynthesis is the process used by plants to convert light energy into chemical energy.",
        metadata={"topic": "Photosynthesis"}
    ),
    Document(
        page_content="Space exploration involves investigating outer space using astronomy, space technology, and spacecraft.",
        metadata={"topic": "Space Exploration"}
    ),
    Document(
        page_content="COVID-19 affected global health systems and economies, highlighting the need for preparedness and vaccines.",
        metadata={"topic": "COVID-19 Pandemic"}
    ),
    Document(
        page_content="Ancient Egypt was a civilization known for pyramids, hieroglyphics, and a deep belief in the afterlife.",
        metadata={"topic": "Ancient Egypt"}
    ),
    Document(
        page_content="Blockchain is a decentralized ledger system that records transactions in a secure and transparent way.",
        metadata={"topic": "Blockchain Technology"}
    ),
]


vector_store = Chroma(
    embedding_function=OpenAIEmbeddings(),
    persist_directory='chroma_db',
    collection_name='sample'
)

vector_store.add_documents(documents)
print(vector_store.get(include=['embeddings','metadatas']))
