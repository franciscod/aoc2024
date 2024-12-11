TODAY = $(shell date +"%e")
YEAR = 2024

today: $(TODAY)/Makefile

times:
	echo '# Advent of Code 2024' > README.md
	echo '```' >> README.md
	curl "https://adventofcode.com/$(YEAR)/leaderboard/self" \
	  -H 'cookie: session=$(shell cat cookie)' | htmlq -t pre >> README.md
	echo '```' >> README.md

$(TODAY)/Makefile:
	mkdir -p $(TODAY)
	ln -sr Makefile_day $(TODAY)/Makefile
	ln -sr lib.py $(TODAY)/lib.py
	cp skel.py $(TODAY)/solve.py
