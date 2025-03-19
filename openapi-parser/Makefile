VENV = .venv
MAIN = main.py
PACKAGE = app
CONFIG = .config

all: venv

venv: $(VENV)/bin/activate

$(VENV)/bin/activate: ./$(CONFIG)/requirements.txt
	@python3 -m venv $(VENV)
	@./$(VENV)/bin/pip install -r ./$(CONFIG)/requirements.txt
	@./$(VENV)/bin/pre-commit install --config=./$(CONFIG)/.pre-commit-config.yaml

%:
	@:

command: venv
	@./$(VENV)/bin/$(filter-out $@,$(MAKECMDGOALS))

run: venv
	@./$(VENV)/bin/python3 $(MAIN) $(filter-out $@,$(MAKECMDGOALS))

lint: venv
	@./$(VENV)/bin/pycodestyle --ignore=E501 $(PACKAGE) $(MAIN)
	@./$(VENV)/bin/pylint --rcfile=./$(CONFIG)/.pylintrc $(PACKAGE) $(MAIN)
	@./$(VENV)/bin/mypy --config-file=./$(CONFIG)/.mypy.ini $(PACKAGE) $(MAIN)

test: venv
	@./$(VENV)/bin/pytest

clean:
	@if [ -d $(VENV) ]; then \
		./$(VENV)/bin/pyclean . || true; \
	fi

fclean: clean
	@rm -rf $(VENV) .mypy_cache/ .pytest_cache/

re: fclean all

.PHONY: all venv command run lint test clean fclean re
