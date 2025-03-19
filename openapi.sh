#!/bin/bash

ROOT=$(dirname "$(readlink -f "$0")")

DEFAULT_TARGET="out"
DEFAULT_LANGUAGE="python"

show_help() {
    cat << EOF
Usage: $0 [command] [options]

Commands:
clean     Clean the target directory
generate  Generate code using OpenAPI generator

Options:
--target=DIR      Target directory (default: $DEFAULT_TARGET)
--language=LANG   Generator language (default: $DEFAULT_LANGUAGE)
--help            Display this help message
EOF
    exit 0
}

if [[ $# -gt 0 ]]; then
    case $1 in
        clean|generate)
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
LANGUAGE=${LANGUAGE:-$DEFAULT_LANGUAGE}

while [[ $# -gt 0 ]]; do
    case $1 in
        --target=*)
            TARGET="${1#*=}"
            ;;
        --language=*)
            LANGUAGE="${1#*=}"
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
        find "$TARGET" -mindepth 1 -not -name '.gitkeep' -delete 2>/dev/null || find "$TARGET" -mindepth 1 -not -name '.gitkeep' -exec rm -rf {} \; 2>/dev/null
    fi
}

generate() {
    openapi-generator generate \
        -i "$ROOT/openapi-parser/app/docs/coingecko.json" \
        -g "$LANGUAGE" \
        -o "$TARGET" \
        -c "$ROOT/openapi-config/cg-python.json"
    rm -rf "$TARGET/.github" "$TARGET/.gitlab-ci.yml"
}

case $COMMAND in
    clean)
        clean
        ;;
    generate)
        generate
        ;;
    "")
        echo "Error: No command specified."
        echo "Usage: $0 [clean|generate] [options]"
        echo "Use --help for more information"
        ;;
esac
