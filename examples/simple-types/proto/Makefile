BUF := fraser
REPOSITORY := simple-types

.PHONY: repo
repo:
	@buf beta registry repository create buf.build/$(BUF)/$(REPOSITORY) --visibility public

.PHONY: gen
gen:
	@buf generate

.PHONY: clean
clean:
	@rm -rf ../gen
