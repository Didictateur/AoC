YEAR ?= 2020
DAY ?= 1

all:
	@ocamlc -o main.x str.cma parse.ml $(YEAR)/$(DAY)/main.ml
	@echo "Year: $(YEAR), day: $(DAY)\n"
	@echo "Part 1"
	@echo "Test: $$(./main.x "test" "1")"
	@echo "Final: $$(./main.x "final" "1")"
	@echo "\nPart 2"
	@echo "Test: $$(./main.x "test" "2")"
	@echo "Final: $$(./main.x "final" "2")"

clean:
	@rm -f *.cmi *.cmo *.cmx *.x
	@rm -rf **/**/*.cmi **/**/*.cmo **/**/*.cmx **/**/*.x
	@clear