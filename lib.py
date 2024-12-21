from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


def get_or_init_vector_store(model=OpenAIEmbeddings(model="text-embedding-3-small")):
    file_name = str(Path(__file__).parent.resolve() / "data/vector_store")
    try:
        return InMemoryVectorStore.load(file_name, model)
    except FileNotFoundError:
        splits = load_data()
        vector_store = InMemoryVectorStore(model)
        vector_store.add_documents(documents=splits)
        vector_store.dump(file_name)
        return vector_store


def load_data():
    file_name = str(Path(__file__).parent.resolve() / "data/kokoro.txt")
    loader = TextLoader(file_name)
    doc = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=400, chunk_overlap=50, add_start_index=True
    )
    return text_splitter.split_documents(doc)


def retrieve_context(vector_store, input):
    docs = vector_store.similarity_search(input)
    return "\n\n".join(doc.page_content for doc in docs)


def generate_answer(input, context, model=ChatOpenAI(model="gpt-4o-mini")):
    messages = prompt.invoke({"question": input, "context": context})
    response = model.invoke(messages)
    return response.content


prompt = PromptTemplate.from_template(
    """
あなたは日本語の質問に日本語で回答するアシスタントです。以下の文脈に沿って質問に答えてください。答えがわからない場合は「わかりません」とだけ答えてください。回答は最大3文で簡潔にまとめてください。
質問: {question}
文脈: {context}
解答:
"""
)
