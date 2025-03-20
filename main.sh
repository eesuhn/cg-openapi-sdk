#!/bin/bash

ROOT=$(dirname "$(readlink -f "$0")")

DEFAULT_TARGET="out"
DEFAULT_GENERATOR="python"
DEFAULT_CONFIG="default-config.json"

show_help() {
    cat << EOF
Usage: $0 [command] [options]

Commands:
generate  Generate code using OpenAPI generator
clean     Clean the target directory

Options:
--target=TARGET   Target directory (default: $DEFAULT_TARGET)
--generator=GEN   Generator (default: $DEFAULT_GENERATOR)
--config=CONFIG   Configuration file (default: $DEFAULT_CONFIG)
--help            Display this help message
EOF
    exit 0
}

if [[ $# -gt 0 ]]; then
    case $1 in
        generate|clean)
            COMMAND=$1
            shift
            ;;
        --help)
            show_help
            ;;
        *)
            echo "Error: Unknown command: $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
fi

TARGET=${TARGET:-$DEFAULT_TARGET}
GENERATOR=${GENERATOR:-$DEFAULT_GENERATOR}
CONFIG=${CONFIG:-$DEFAULT_CONFIG}

while [[ $# -gt 0 ]]; do
    case $1 in
        --target=*)
            TARGET="${1#*=}"
            ;;
        --generator=*)
            GENERATOR="${1#*=}"
            ;;
        --config=*)
            CONFIG="${1#*=}"
            ;;
        --help)
            show_help
            ;;
        *)
            echo "Error: Unknown parameter: $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
    shift
done

TARGET="$ROOT/$TARGET"

clean() {
    if [[ -d "$TARGET" ]]; then
        find "$TARGET" -mindepth 1 -not -name '.gitkeep' -exec rm -rf {} \; 2>/dev/null
    fi
}

generate() {
    openapi-generator generate \
        -i "$ROOT/openapi-parser/app/docs/coingecko.json" \
        -g "$GENERATOR" \
        -o "$TARGET" \
        -c "$ROOT/openapi-config/$CONFIG"
    rm -rf \
        "$TARGET/.github" \
        "$TARGET/.gitlab-ci.yml" \
        "$TARGET/.travis.yml" \
        "$TARGET/git_push.sh"
}

case $COMMAND in
    generate)
        generate
        ;;
    clean)
        clean
        ;;
    "")
        echo "Error: No command specified."
        echo "Usage: $0 [generate|clean] [options]"
        echo "Use --help for more information"
        ;;
esac
