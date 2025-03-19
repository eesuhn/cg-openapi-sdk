#!/bin/bash

ROOT=$(dirname $(readlink -f $0))
TARGET="$ROOT/cg-python"

clean() {
    if [ -d "$TARGET" ]; then
        find $TARGET -mindepth 1 -not -name '.gitkeep' -exec rm -rf {} +
    fi
}

generate() {
    openapi-generator generate \
        -i $ROOT/openapi-parser/app/docs/merged.json \
        -g python \
        -o $TARGET \
        -c $ROOT/config.json
    rm -rf $TARGET/.github $TARGET/.gitlab-ci.yml
}

case $1 in
    clean)
        clean
        ;;
    generate)
        generate
        ;;
    *)
        ;;
esac
