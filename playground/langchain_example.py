import openai
from langchain.llms import AzureOpenAI

from playground.utils.secret import get_local_secrets


secrets = get_local_secrets()
# your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_base = secrets["api_base"].get_secret()
openai.api_type = "azure"
# this may change in the future
openai.api_version = "2022-12-01"


llm = AzureOpenAI(
    temperature=0.9,
    openai_api_key=secrets["api_key"].get_secret(),
    deployment_name="text-davinci-003",
)
