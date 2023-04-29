from os import environ
import openai
from playground.utils.paths import get_absolute_repo_root
from playground.utils.secret import get_local_secrets


def set_environment_variables(
    openai_api_key:str,
) -> None:
    environ["OPENAI_API_KEY"] = openai_api_key


def setup_environment_from_local(path:str = None) -> None:
    if not path:
        path = get_absolute_repo_root()

    secrets = get_local_secrets(path / "secrets.yaml")

    set_environment_variables(
        openai_api_key=secrets["api_key"].get_secret(),
    )

    openai.api_base = secrets["api_base"].get_secret()
    openai.api_type = "azure"
    openai.api_version = secrets["api_version"].get_secret()

