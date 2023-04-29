from langchain.llms import AzureOpenAI

from playground.utils.azure_openai import setup_environment_from_local
setup_environment_from_local()


llm = AzureOpenAI(
    temperature=0,
    deployment_name="text-davinci-003",
)

response = llm("What day is it today?")
print(response)