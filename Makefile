

# Installs bufbuild via brew if it's not already installed
.PHONY: deps-bufbuild
deps-bufbuild:
	@command -v buf > /dev/null || brew install buf

# Install Python Poetry if it's not already installed
.PHONY: deps-poetry
deps-poetry:
	@command -v poetry > /dev/null || brew install poetry

.PHONY: deps
deps: deps-bufbuild deps-poetry

.PHONY: generate-widgets-v1-dataclasses
generate-widgets-v1-dataclasses:
	@mkdir -p examples/simple-types/gen || true
	@protoc ./examples/simple-types/proto/widgets/v1/*.proto \
		--python_gapic_out=examples/simple-types/gen \
		--python_gapic_opt=python-gapic-templates=$(shell pwd)/templates/dataclasses
	@autoimport examples/simple-types/gen
	@black examples/simple-types/gen --target-version py311
	@ruff examples/simple-types/gen --fix

.PHONY: clean
clean:
	rm -rf gen
	rm -rf examples/simple-types/gen
