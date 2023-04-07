import openai

from playground.utils.secret import get_local_secrets

secrets = get_local_secrets()

openai.api_key = secrets["api_key"].get_secret()
openai.api_base = secrets[
    "api_base"
].get_secret()  # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = "azure"
openai.api_version = "2022-12-01"  # this may change in the future

deployment_name = "text-davinci-003"  # This will correspond to the custom name you chose for your deployment when you deployed a model.

# Send a completion call to generate an answer
print("Sending a test completion job")
start_phrase = "Write a tagline for an ice cream shop. "
response = openai.Completion.create(
    engine=deployment_name, prompt=start_phrase, max_tokens=10
)
text = response["choices"][0]["text"].replace("\n", "").replace(" .", ".").strip()
print(start_phrase + text)
