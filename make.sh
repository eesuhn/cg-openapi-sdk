#!/bin/bash

TARGET="$1"

if [[ "$TARGET" != cg-* ]]; then
    echo "Error: Target must start with 'cg-'"
    exit 1
fi

if [ ! -d "$TARGET" ]; then
    echo "Error: Target directory '$TARGET' not found."
    exit 1
fi

GENERATOR="${TARGET#cg-}"
CONFIG_FILE="${TARGET}.json"

if [ ! -f "openapi-config/$CONFIG_FILE" ]; then
    echo "Error: Config file 'openapi-config/$CONFIG_FILE' not found."
    exit 1
fi

echo "Updating submodules..."
git submodule update --init --recursive

echo "Generating SDK: out='$TARGET', gen='$GENERATOR', conf='$CONFIG_FILE'"
./main.sh generate --out="$TARGET" --gen="$GENERATOR" --conf="$CONFIG_FILE"
