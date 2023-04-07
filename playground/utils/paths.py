"""
Module that provide functions to navigate paths in the current project
"""
from pathlib import Path

DEPTH = 3


def get_absolute_repo_root() -> Path:
    """
    Get the root of the current repo
    :return:
    """
    current_file_path = Path(__file__)
    repo_path = current_file_path

    for _ in range(DEPTH):
        repo_path = repo_path.parent

    return repo_path.absolute()
