# `openapi-parser` — OpenAPI Specs Merger

Generates a merged OpenAPI 3.0 JSON specs by fetching and combining multiple OpenAPI sources — [`coingecko-pro`](https://docs.coingecko.com/openapi/6584ea6ce07e130056b1af99) and [`geckoterminal`](https://docs.coingecko.com/openapi/6585013ec2907b0031346aa4).

## How it Works

```sh
openapi-parser
├── Makefile
├── README.md
├── app
│   ├── __init__.py
│   ├── docs  # 👈 OpenAPI specs (default and merged)
│   ├── main.py  # 👈 Main logic
│   └── utils.py
└── main.py
```

1. **Fetches** individual OpenAPI specs using unique IDs from [ReadMe API references](https://docs.coingecko.com/docs/useful-links#pro-api-swagger-json).
2. **Merges** the specs:
    - Uses [`docs/default.json`](./app/docs/default.json) as the base.
    - Combines `paths` from both sources, adding an `/onchain` prefix to `geckoterminal` paths.
    - Merges `components/schemas` from both sources.
3. **Outputs** the merged OpenAPI spec as [`docs/coingecko.json`](./app/docs/coingecko.json).

## Usage

```bash
make run
```

### Output

```sh
./app/docs/coingecko.json  # 👈 Merged OpenAPI JSON ready for client generation
```
