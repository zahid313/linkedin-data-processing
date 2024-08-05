from dotenv import load_dotenv
import os
from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrap_linkedin_profile
# from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

if __name__ == "__main__":
    load_dotenv()
    ollama_api_url = os.getenv("OLLAMA_API_URL")
    ollama_api_key = os.getenv("OLLAMA_API_KEY")

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    llm = ChatOllama(model="phi3", base_url=ollama_api_url, api_key=ollama_api_key)
    chain = summary_prompt_template | llm | StrOutputParser()
    linkedin_data  = scrap_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/zahid-ali-1735049/",
        mock=True
    )
    res = chain.invoke(input={"information": linkedin_data})

    print(res)
