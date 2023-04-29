"""
Utility for handling secrets
"""
from dataclasses import dataclass
import yaml

from playground.utils.paths import get_absolute_repo_root


@dataclass
class Secret:
    """
    Class to obfuscate secrets, so that there are no accidental prints
    """

    _secret: str

    def get_secret(self) -> str:
        """
        Return the contents of the secret
        :return:
        """
        return self._secret

    def __repr__(self):
        return "<REDACTED>"

    def __str__(self):
        return self.__repr__()


def get_local_secrets(file_name: str = "secrets.yaml") -> dict[str:Secret]:
    """
    Helper method to read the local secrets in the repo root
    :param file_name:
    :return:
    """
    repo_root = get_absolute_repo_root()
    contents = yaml.safe_load((repo_root / file_name).read_text())

    return {k: Secret(v) for k, v in contents.items()}
