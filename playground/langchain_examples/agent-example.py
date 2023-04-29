from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import AzureOpenAI

from playground.utils.azure_openai import setup_environment_from_local

setup_environment_from_local()

llm = AzureOpenAI(
    temperature=0,
    deployment_name="text-davinci-003",
)

tools = load_tools(["wikipedia", "llm-math"], llm=llm)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

agent.run("How many humans do you need to stack to equal the height of the statue of liberty?")
