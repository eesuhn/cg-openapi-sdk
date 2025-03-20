#!/bin/bash

ROOT=$(dirname "$(readlink -f "$0")")

DEFAULT_OUT="out"
DEFAULT_GEN="python"
DEFAULT_CONF="default-config.json"

show_help() {
    cat << EOF
Usage: $0 [command] [options]

Commands:
generate  Generates code using the OpenAPI Generator
clean     Removes all files in the output directory except .gitkeep

Options:
--out=OUT    Output directory for generated code (default: $DEFAULT_OUT)
--gen=GEN    Generator name (default: $DEFAULT_GEN)
--conf=CONF  OpenAPI Generator config file (default: $DEFAULT_CONF)
--help       Display help message
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

OUT=${OUT:-$DEFAULT_OUT}
GEN=${GEN:-$DEFAULT_GEN}
CONF=${CONF:-$DEFAULT_CONF}

while [[ $# -gt 0 ]]; do
    case $1 in
        --out=*)
            OUT="${1#*=}"
            ;;
        --gen=*)
            GEN="${1#*=}"
            ;;
        --conf=*)
            CONF="${1#*=}"
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

OUT="$ROOT/$OUT"

clean() {
    if [[ -d "$OUT" ]]; then
        find "$OUT" -mindepth 1 -not -name '.gitkeep' -exec rm -rf {} \; 2>/dev/null
    fi
}

debloat() {
    rm -rf \
        "$OUT/.github" \
        "$OUT/.gitlab-ci.yml" \
        "$OUT/.travis.yml" \
        "$OUT/git_push.sh"
}

generate() {
    openapi-generator generate \
        -i "$ROOT/openapi-parser/app/docs/coingecko.json" \
        -g "$GEN" \
        -o "$OUT" \
        -c "$ROOT/openapi-config/$CONF"
    debloat
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
