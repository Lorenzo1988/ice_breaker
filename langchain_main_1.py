
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import  ChatPromptTemplate


#VARIABLES





if __name__=="__main__":
    # Leggi il contenuto del file pluto.txt
    with open('/ice_breaker/Informazioni.txt', 'r', encoding='utf-8') as file:
        informations = file.read()

    # Specifica il percorso del file


    # Stampare la variabile globale per verificarne il contenuto
    print("Pippo3")
    summary_template=(f"date le informazioni {informations} voglio creare: "
                      f"1. un piccolo summary"
                      f"2. fatti interessanti che la riguardano")

    summary_prompt_template=PromptTemplate(input_variables="informations", template=summary_template)
#    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    llm = ChatOllama(model="phi3")
    chain = summary_prompt_template | llm | StrOutputParser


    response = chain.invoke(input={"informations":informations})
    print(f"il type di response è: {type(response)}")
    print(response)
