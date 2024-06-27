import os
from dotenv import load_dotenv, dotenv_values 
from langchain_openai import OpenAI

load_dotenv()
api_key = os.getenv("api_key")

llm = OpenAI(
    openai_api_key = api_key
)

llm.invoke("Write a very short poem")