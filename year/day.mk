TODAY = $(shell pwd | cut -d/ -f 7-9)
EDITOR = nvim

edit2: solve2.py
	$(EDITOR) $<
	
solve2.py: solve.py
	cp $< $@

input: input.txt
input.txt:
	curl 'https://adventofcode.com/$(TODAY)/input' \
	  -H 'cookie: session=$(shell cat ../../../../cookie)' > input.txt

level: level.html
.PHONY: level.html
level.html:
	curl "https://adventofcode.com/$(TODAY)" \
	  -H 'cookie: session=$(shell cat ../../../../cookie)' > level.html

ans1:
	curl "https://adventofcode.com/$(TODAY)/answer" \
	  -H 'cookie: session=$(shell cat ../../../../cookie)' \
	  --data-raw 'level=1&answer=$(shell head -1)'

ans2:
	curl "https://adventofcode.com/$(TODAY)/answer" \
	  -H 'cookie: session=$(shell cat ../../../../cookie)' \
	  --data-raw 'level=2&answer=$(shell head -1)'
		

today:
	echo $(TODAY)

t1:
	python3 solve.py test.txt

s1:
	python3 solve.py input.txt

t2:
	python3 solve2.py test.txt

s2:
	python3 solve2.py input.txt
