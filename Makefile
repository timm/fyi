PYs=$(shell ls [a-z]*.py)
HTMLs=$(PYs:.py=.html)

all: $(HTMLs) 

%.html: %.py
	python3 $< > $@

put:
	git commit -am saving; git push; git status
