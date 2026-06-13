# ==============================================================================
# timm.fyi - Minimal Task Runner
# ==============================================================================

SHELL    := /bin/bash
GIT_ROOT := $(shell git rev-parse --show-toplevel 2>/dev/null)
PORT     := 8080

GISTS    ?= $(HOME)/gists
# slug:gistdir:mdfile — curated gist READMEs imported as Tools pages (make tools)
TOOLS := konfig:konfig:,konfig.md ezr:ezr:,ezr.md kah-lua:kah-lua:,kah.md \
         lithp:lithp:,lithp.md luamine:luamine:,luamine.md luk:luk:,luk.md \
         repltut:repltut:,Repltut.md
# gist-only lines dropped before conversion (shields badges, screenshot, Files TOC)
STRIP := img.shields.io|gist.github.com/user-attachments|qr-image|\*\*Files:\*\*

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

tools: ## build Tools index + subpages from curated gist READMEs (needs pandoc)
	@command -v pandoc >/dev/null || { echo "need pandoc: brew install pandoc"; exit 1; }
	@idx=$$(mktemp); \
	 printf '<h1>Tim Menzies<br><small>tools</small></h1>\n<p>small, self-contained software tools. each page is a README imported from its gist via <code>make tools</code>.</p>\n<div class="tools-list">\n' > $$idx; \
	 for t in $(TOOLS); do \
	   slug=$${t%%:*}; rest=$${t#*:}; dir=$${rest%%:*}; md=$${rest#*:}; \
	   src="$(GISTS)/$$dir/$$md"; \
	   [ -f "$$src" ] || { echo "  SKIP missing $$src"; continue; }; \
	   grep -vaE '$(STRIP)' "$$src" \
	     | sed -E 's/\[([^]]+)\]\(([^):/]+)\)/\1/g' \
	     | pandoc -f gfm -t html --syntax-highlighting=none --template etc/tool.html \
	         --metadata title="$$slug" -o tool-$$slug.html; \
	   desc=$$(awk -F'|' -v s="$$slug" '$$1==s{print $$2;f=1} END{exit !f}' etc/tools.txt 2>/dev/null) \
	     || desc=$$(awk '/^### /{f=1;next} f{if($$0 ~ /^[[:space:]]*$$/ || $$0 ~ /^</)next; gsub(/[`*]/,""); print; exit}' "$$src"); \
	   printf '<h2><a href="tool-%s.html">%s</a></h2>\n<p>%s</p>\n' "$$slug" "$$slug" "$$desc" >> $$idx; \
	   echo "  built tool-$$slug.html"; \
	 done; \
	 printf '</div>\n' >> $$idx; \
	 pandoc -f html -t html --template etc/tool.html --metadata title="Tools" -o tools.html $$idx; \
	 rm -f $$idx; echo "  built tools.html"

clean: ## remove macOS junk + tmp files
	@find . -name '.DS_Store' -delete
	@find . -name '*~' -delete
	@find . -name '#*#' -delete

sh: ## launch dev shell with banner + parent/dir prompt
	@-echo -e $(CLS)$(cYELLOW); \
	  command -v figlet >/dev/null && figlet -W -f slant fyi || echo "fyi"; \
	  echo -e $(cRESET)
	@-bash --rcfile $(GIT_ROOT)/etc/bashrc -i
