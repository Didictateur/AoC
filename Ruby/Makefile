YEAR = 2024
DAY = 1

all:
	@clear
	@ruby $(YEAR)/$(DAY)/main.rb $(YEAR) $(DAY)

total:
	@clear
	@for day in $(shell ls $(YEAR)); do \
		echo "\nDay $$day"; \
		ruby $(YEAR)/$$day/main.rb $(YEAR) $$day; \
	done

last:
	@clear
	@ruby $(YEAR)/$(shell ls $(YEAR) | tail -n 1)/main.rb $(YEAR) $(shell ls $(YEAR) | tail -n 1)