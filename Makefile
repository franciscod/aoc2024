TODAY = $(shell date +"%e")

today: $(TODAY)/Makefile

$(TODAY)/Makefile:
	mkdir -p $(TODAY)
	ln -sr Makefile_day $(TODAY)/Makefile
	ln -sr lib.py $(TODAY)/lib.py
	cp skel.py $(TODAY)/solve.py
