PYs=$(wildcard [a-z]*.py)
HTMLs=$(PYs:.py=.html)

all: $(HTMLs) 

%.html: %.py
	python3 -B $< > $@

put:
	git commit -am saving; git push; git status
