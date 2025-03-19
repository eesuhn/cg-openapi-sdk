from .utils import (
    get_openapi_json,
    load_json,
    log_json
)
from eesuhn_sdk import (
    print_warning
)


class Main:
    def __init__(self) -> None:
        self.geckoterminal = self.get_gt_json()
        self.coingecko_pro = self.get_pro_json()
        self.merge_oas_docs()

    def get_gt_json(
        self
    ) -> dict:
        return get_openapi_json(
            jsonId="6585013ec2907b0031346aa4"
        )

    def get_pro_json(
        self
    ) -> dict:
        return get_openapi_json(
            jsonId="6584ea6ce07e130056b1af99"
        )

    def merge_oas_docs(
        self
    ) -> None:
        merged_docs = load_json(
            filename="app/docs/default.json"
        )
        merged_docs["paths"] = self.merge_paths()
        merged_docs["components"]["schemas"] = self.merge_schemas()
        log_json(
            data=merged_docs,
            filename="docs/merged"
        )

    def merge_paths(
        self
    ) -> dict:
        paths = {}
        for path, item in self.coingecko_pro.get("paths", {}).items():
            if path in paths:
                print_warning(f"Duplicate path {path} found. Overwriting with coingecko-pro version.")
            paths[path] = item
        for path, item in self.geckoterminal.get("paths", {}).items():
            # Prepend '/onchain' to the existing path.
            new_path = "/onchain" + path if not path.startswith("/onchain") else path
            if new_path in paths:
                print_warning(f"Duplicate path {new_path} found. Overwriting with geckoterminal version.")
            paths[new_path] = item
        return paths

    def merge_schemas(
        self
    ) -> dict:
        schemas = {}
        for source in (self.coingecko_pro, self.geckoterminal):
            components = source.get("components", {})
            for key, schema in components.get("schemas", {}).items():
                if key in schemas:
                    print_warning(f"Duplicate schema {key} encountered. Overwriting previous schema.")
                schemas[key] = schema
        return schemas
