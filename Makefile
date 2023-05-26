PYs=$(shell ls [a-z]*.py)
HTMLs=$(PYs:.py=.html)

all: $(HTMLs) 

%.html: %.py
	python3 $< > $@
