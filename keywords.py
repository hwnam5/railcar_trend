from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama
from langchain_ollama import ChatOllama

def get_keywords(article : str):
    llm = ChatOllama(model = "llama3.1:latest")
    prompt = ChatPromptTemplate.from_messages([
        ("system", 
         "Bring me the keywords from the article below in korean. Output only keywords in the result prompt and avoid any other words. The keywords mentioned here should not contain any spaces buy Separate words with spaces."),
        ("user", "{input}")
    ])
    chain = prompt | llm | StrOutputParser()

    return chain.invoke({"input": article})