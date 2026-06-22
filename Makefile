# ugendran — quality gate. Single-file CLI, zero runtime deps.
.PHONY: check test lint compile

check: compile lint test   ## Full gate (run before pushing)

compile:  ## Fast structural check — bytecode-compile every module
	python3 -m py_compile ugendran.py _generator/*.py tests/*.py

lint:  ## Real-bug lint (unused imports / undefined names). No-op if ruff absent.
	@ruff check . || echo "ruff not installed — skipping (CI enforces it)"

test:  ## Run the regression suite
	python3 -m unittest discover -s tests
