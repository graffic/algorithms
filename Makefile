KATAS=cracking_interview euler hackerrank intro_algorithms leetcode misc

all: clean $(KATAS)

clean:
	rm -f .coverage

$(KATAS):
	pytest --cov=. --cov-append $@

.PHONY: clean $(KATAS)