from pathlib import Path


def create_folders():
    folders = [
        "models",
        "outputs",
        "logs",
        "cache"
    ]

    for folder in folders:
        Path(folder).mkdir(exist_ok=True)
