

# Installs bufbuild via brew if it's not already installed
.PHONY: deps-bufbuild
deps-bufbuild:
	@command -v buf > /dev/null || brew install buf

.PHONY: deps
deps: deps-bufbuild

.PHONY: generate-widgets-v1-dataclasses
generate-widgets-v1-dataclasses:
	mkdir examples/simple-types/gen || true
	protoc ./examples/simple-types/proto/widgets/v1/*.proto \
		--python_gapic_out=examples/simple-types/gen \
		--python_gapic_opt=python-gapic-templates=$(shell pwd)/templates/dataclasses

.PHONY: generate-google-vision-v1
generate-google-vision-v1:
	protoc examples/googleapis/google/cloud/vision/v1/*.proto \
		--proto_path=../api-common-protos/ --proto_path=. \
		--python_gapic_out=gen/

.PHONY: clean
clean:
	rm -rf gen
	rm -rf examples/simple-types/gen
