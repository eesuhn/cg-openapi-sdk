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
    with open(
        get_package_root() / f"{filename}.json",
        "r",
        encoding="utf-8"
    ) as f:
        return json.load(f)


def log_json(
    data: Optional[dict],
    filename: str
) -> None:
    with open(
        get_package_root() / f"{filename}.json",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(json.dumps(data, indent=2))


def print_json(
    data: Optional[dict]
) -> None:
    print(json.dumps(data, indent=2))
