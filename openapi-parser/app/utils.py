import requests
import json

from typing import Optional
from pathlib import Path


def get_package_root() -> Path:
    return Path(__file__).parent


def get_openapi_json(
    jsonId: str
) -> dict:
    url = f"https://docs.coingecko.com/openapi/{jsonId}"
    response = requests.get(
        url=url,
        timeout=10
    )
    return response.json()


def load_json(
    filename: str
) -> dict:
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def log_json(
    data: Optional[dict],
    filename: str,
    dest: str = "."
) -> None:
    path = get_package_root() / dest
    filename = f"{filename}.json"
    with open(path / f"{filename}", "w", encoding="utf-8") as f:
        f.write(json.dumps(data, indent=2))


def print_json(
    data: Optional[dict]
) -> None:
    print(json.dumps(data, indent=2))
