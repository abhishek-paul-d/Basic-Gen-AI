import os 
from dotenv import load_dotenv
load_dotenv()

from langchain_community.llms import Ollama

from langchain_community.llms import ollama

import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


##Langsmith tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

##Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistan. Please respond to the question asked by the user"),
        ("user","Question:{question}")

    ]
)

## Streamlit Framework

st.title("Langchain Demo with Gemma:2b Model")
input_text=st.text_input("What question do you have?")


## Ollama Gemma  Model
def run_chat_interface():
    """Runs the chatbot interface using Streamlit.
    
    This function initializes the Ollama model, sets up the output parser,
    and defines the chat prompt template. It then creates a simple Streamlit
    UI with a text input field and displays the model's response.
    
    Args:
        None
        
    Returns:
        None
    """
    llm = Ollama(model="gemma:2b")
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    if input_text:
        st.write(chain.invoke({"question": input_text}))


# Run the chat interface
run_chat_interface()
