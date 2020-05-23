from pathlib import Path


def join_base_path(path):
    return Path(__file__).parent.parent.joinpath(path)