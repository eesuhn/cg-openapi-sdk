from .utils import (
    get_openapi_json,
    load_json,
    log_json
)
from eesuhn_sdk import (
    print_error
)


GECKOTERMINAL: str = "6585013ec2907b0031346aa4"
COINGECKO_PRO: str = "6584ea6ce07e130056b1af99"


class Main:
    def __init__(self) -> None:
        self.flag = True
        self.geckoterminal = self.get_gt_json()
        self.coingecko_pro = self.get_pro_json()
        self.merge_oas_docs()

    def get_gt_json(
        self
    ) -> dict:
        return get_openapi_json(GECKOTERMINAL)

    def get_pro_json(
        self
    ) -> dict:
        return get_openapi_json(COINGECKO_PRO)

    def merge_oas_docs(
        self
    ) -> None:
        doc = load_json(
            filename="docs/default"
        )
        doc["paths"] = self.merge_paths()
        doc["components"]["schemas"] = self.merge_schemas()
        if self.flag:
            log_json(
                data=doc,
                filename="docs/coingecko"
            )
        else:
            print_error("Failed to merge OpenAPI docs.")

    def merge_paths(
        self
    ) -> dict:
        paths = {}
        for path, item in self.coingecko_pro.get("paths", {}).items():
            if path in paths:
                print_error(f"Duplicate path {path} found. Overwriting with coingecko-pro version.")
                self.flag = False
            paths[path] = item
        for path, item in self.geckoterminal.get("paths", {}).items():
            # Prepend '/onchain' to the existing path.
            new_path = "/onchain" + path if not path.startswith("/onchain") else path
            if new_path in paths:
                print_error(f"Duplicate path {new_path} found. Overwriting with geckoterminal version.")
                self.flag = False
            paths[new_path] = item
        # Check operationId for conflicts
        operation_ids: dict = {}
        for path, path_item in paths.items():
            for _, v in path_item.items():
                if isinstance(v, dict) and "operationId" in v:
                    operation_id = v["operationId"]
                    if operation_id in operation_ids:
                        print_error(
                            f"Duplicate operationId '{operation_id}' found in {path}. Previous occurrence in {operation_ids[operation_id]}."
                        )
                        self.flag = False
                    else:
                        operation_ids[operation_id] = path
        return paths

    def merge_schemas(
        self
    ) -> dict:
        schemas = {}
        for source in (self.coingecko_pro, self.geckoterminal):
            components = source.get("components", {})
            for key, schema in components.get("schemas", {}).items():
                if key in schemas:
                    print_error(f"Duplicate schema {key} encountered. Overwriting previous schema.")
                    self.flag = False
                schemas[key] = schema
        return schemas
