# Installs bufbuild via brew if it's not already installed
.PHONY: deps-bufbuild
deps-bufbuild:
	@command -v buf > /dev/null || brew install buf

# Install Python Poetry if it's not already installed
.PHONY: deps-poetry
deps-poetry:
	@command -v poetry > /dev/null || brew install poetry
	poetry install

.PHONY: deps
deps: deps-bufbuild deps-poetry


# .PHONY: generate-widgets-v1-dataclasses
# generate-widgets-v1-dataclasses:
# 	@mkdir -p examples/simple-types/gen || true
# 	cd examples/simple-types && buf generate --path widgets/v1/dataclasses --output ../gen
# 	@autoimport examples/simple-types/gen
# 	@black examples/simple-types/gen --target-version py311
# 	@ruff examples/simple-types/gen --fix

.PHONY: clean
clean:
	rm -rf examples/*/gen
