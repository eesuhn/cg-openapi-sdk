VENV = .venv
MAIN = main.py
PACKAGE = app
CONFIG = .config

all: venv

venv: $(VENV)/bin/activate

$(VENV)/bin/activate: ./$(CONFIG)/requirements.txt
	@python3 -m venv $(VENV)
	@./$(VENV)/bin/pip install -r ./$(CONFIG)/requirements.txt
	@bun install

run: venv
	@./$(VENV)/bin/python3 $(MAIN)

lint: venv
	@./$(VENV)/bin/pylint --rcfile=./$(CONFIG)/.pylintrc $(PACKAGE) $(MAIN)
	@./$(VENV)/bin/mypy --config-file=./$(CONFIG)/.mypy.ini $(PACKAGE) $(MAIN)

clean:
	@if [ -d $(VENV) ]; then \
		./$(VENV)/bin/pyclean . || true; \
	fi

fclean: clean
	@rm -rf $(VENV) .mypy_cache/

re: fclean all

doc-lint: venv
	@bunx redocly lint $(PACKAGE)/docs/coingecko.json

.PHONY: all venv run lint clean fclean re doc-lint
