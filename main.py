from dotenv import load_dotenv
load_dotenv()

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain ,SimpleSequentialChain, SequentialChain

import streamlit as st

st.title("Chat with your own Data")

llm = OpenAI(temperature=0.7)
chat_llm = ChatOpenAI(temperature=0.7,model_name="gpt-3.5-turbo")