

# Installs bufbuild via brew if it's not already installed
.PHONY: deps-bufbuild
deps-bufbuild:
	@command -v buf > /dev/null || brew install buf

.PHONY: deps
deps: deps-bufbuild

.PHONY: generate
generate:
	protoc examples/googleapis/google/cloud/vision/v1/*.proto \
		--proto_path=../api-common-protos/ --proto_path=. \
		--python_gapic_out=gen/

.PHONY: clean
clean:
	rm -rf gen
