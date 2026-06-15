# ==============================================================================
# timm.fyi - Minimal Task Runner
# ==============================================================================

SHELL    := /bin/bash
GIT_ROOT := $(shell git rev-parse --show-toplevel 2>/dev/null)
PORT     := 8080

CLS     := '\033[H\033[J'
cRESET  := '\033[0m'
cYELLOW := '\033[1;33m'

help: ## show help
	@awk 'BEGIN{FS=":.*##"} \
	      /^[a-zA-Z_%\/.~$$-]+:.*##/ \
	      {printf "  \033[36m%-20s\033[0m %s\n",$$1,$$2}' \
	      $(MAKEFILE_LIST)

push: ## commit with prompted msg and push
	@read -p "Reason? " msg; \
	 git commit -am "$$msg"; git push; git status

wc: ## show word counts (site.css strips :{} before count)
	@printf "site.css: %s words\n" $$(tr -d ':{}' < site.css | wc -w)
	@printf "main pages:\n"
	@for f in index.html research.html teaching.html higher_way.html irl.html; do \
	   printf "  %-22s %s lines\n" $$f $$(wc -l < $$f); \
	 done

links: ## check for dead local refs in HTML
	@for f in *.html; do \
	  grep -oE '(href|src)="[^"]+"' $$f \
	  | sed 's/.*"\([^"]*\)".*/\1/' \
	  | grep -vE '^(https?:|mailto:|tel:|#|URL$$)' \
	  | sed 's/#.*//' \
	  | sort -u \
	  | while read ref; do \
	      [ -z "$$ref" ] && continue; \
	      [ -e "$$ref" ] || echo "MISSING: $$f -> $$ref"; \
	    done; \
	done

# DOOT = gists root (dir holding the konfig-style gists). env wins.
DOOT ?= $(HOME)/gists
# SKIP = retired/experimental gist slugs to leave OUT of the catalog.
# (gist API has no folders, so old/ gists still return -- exclude here.)
SKIP ?= ape,dot-files,preci0us,ranger,ruler,tests4mop,tinypythonclasses,tricks

.PHONY: tools
tools: ## render gist catalog -> tools/ (needs $(DOOT)/gistsite + pandoc)
	@python3 -B $(DOOT)/gistsite/gistsite.py -o tools -c ../site.css --skip $(SKIP)
	@echo "rendered -> tools/  (review, then: make push)"

clean: ## remove macOS junk + tmp files
	@find . -name '.DS_Store' -delete
	@find . -name '*~' -delete
	@find . -name '#*#' -delete

sh: ## launch dev shell with banner + parent/dir prompt
	@-echo -e $(CLS)$(cYELLOW); \
	  command -v figlet >/dev/null && figlet -W -f slant fyi || echo "fyi"; \
	  echo -e $(cRESET)
	@-bash --rcfile $(GIT_ROOT)/etc/bashrc -i
