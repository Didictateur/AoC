YEAR = 2024
DAY = 1

all:
	@clear
	@ruby $(YEAR)/$(DAY)/main.rb $(YEAR) $(DAY)

total:
	@clear
	@for day in $(shell ls $(YEAR) | sort -n); do \
		echo "\nDay $$day"; \
		ruby $(YEAR)/$$day/main.rb $(YEAR) $$day; \
	done

latest:
	@clear
	@echo "Day $(shell ls $(YEAR) | sort -n | tail -n 1)\n"
	@ruby $(YEAR)/$(shell ls $(YEAR) | sort -n | tail -n 1)/main.rb $(YEAR) $(shell ls $(YEAR) | sort -n | tail -n 1)