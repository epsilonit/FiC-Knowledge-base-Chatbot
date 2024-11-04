from langchain_community.document_loaders import DirectoryLoader
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
import os
from langchain.text_splitter import TokenTextSplitter

OPENAI_APIKEY = os.environ['OPENAI_APIKEY']


def build_vector_store():
    loader = DirectoryLoader('./ccp')
    docs = loader.load()
    text_splitter = TokenTextSplitter(model_name='gpt-4o',
                                      chunk_size=700,
                                      chunk_overlap=350)
    splits = text_splitter.split_documents(docs)

    embeddings_model = OpenAIEmbeddings(api_key=OPENAI_APIKEY,
                                        model='text-embedding-3-large',
                                        max_retries=150,
                                        chunk_size=700,
                                        show_progress_bar=False)

    vectorstore = Chroma.from_documents(documents=splits,
                                        embedding=embeddings_model,
                                        persist_directory="./kb_chroma_db")

# build_vector_store()
