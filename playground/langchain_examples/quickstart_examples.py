from langchain.chains import LLMChain
from langchain.llms import AzureOpenAI
from langchain.prompts import PromptTemplate

from playground.utils.azure_openai import setup_environment_from_local
setup_environment_from_local()


llm = AzureOpenAI(
    temperature=0.9,
    # openai_api_key=secrets["api_key"].get_secret(),
    deployment_name="text-davinci-003",
)

prompt = PromptTemplate(
    input_variables=["product"],
    template="Give me 10 good names for a company that makes {product}?",
)

chain = LLMChain(llm=llm, prompt=prompt)

output = chain.run("colorful balloons")

print(output)