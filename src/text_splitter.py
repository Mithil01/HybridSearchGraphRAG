from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter

from llama_index.core.node_parser import SemanticSplitterNodeParser
from llama_index.embeddings.openai import OpenAIEmbedding
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()  
import streamlit as st
st.write(
    "Has environment variables been set:",
    os.environ["openai_api_key"] == st.secrets["openai_api_key"],
)
openai_api_key = os.environ['openai_api_key'] 
client = OpenAI(api_key=openai_api_key)


class TextSplitter:

    def load_data(self, directory="./book"):
        docs = SimpleDirectoryReader(directory).load_data()
        embed_model = OpenAIEmbedding(api_key=openai_api_key)
        #node_parser = SentenceSplitter(chunk_size=1200, chunk_overlap=100)
        splitter = SemanticSplitterNodeParser(
                     buffer_size=1, breakpoint_percentile_threshold=95, embed_model=embed_model
                    )
        nodes = splitter.get_nodes_from_documents(docs)
        return nodes