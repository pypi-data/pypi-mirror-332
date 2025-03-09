# Makefile

SPHINXOPTS      ?=
SPHINXBUILD     ?= sphinx-build
SOURCEDIR       = docs/_source
BUILDDIR	= docs/_build
AUTOBUILDOPTS   = --host 127.0.0.1 --port 8000 --ignore "*.swp" --ignore "*.swx"
GETTEXT_BUILD   = gettext_build
UPDATE_LOCALE   = sphinx-intl update -p $(BUILDDIR)/locale/gettext -d $(SOURCEDIR)/locale -l
PO_FILES	= $(wildcard docs/_source/locale/*/LC_MESSAGES/*.po)
MSGATTRIB       = msgattrib
#LANGUAGES       = am ar bg bn ca cak cs cy da de el en eo es et eu fa fi fil fr he hi hr hu id it ja ko lkt lt lv mk mr ms ne nl no pl pt ro ru si sk sl sq sr sv ta te th tr uk ur vi zh
LANGUAGES       = en es

.PHONY: check help html livehtml clean_sphinx clean gettext_build update_locale build_html all copy clean_po latex pdf ebook prepress

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  clean                Remove all build files and directories (including translations)"
	@echo "  all                  Clean and make all targets"
	@echo "  gettext_build        Build localisation strings for translation"
	@echo "  update_locale        Update localisation"
	@echo "  update_locale_<lang> Update localisation for <lang>"
	@echo "  html                 Build the HTML documentation for all languages"
	@echo "  html_<lang>          Build HTML documentation for <lang>"
	@echo "  latex                Build the documentation using LaTeX for all languages"
	@echo "  latex_<lang>         Build the documentation using LaTeX for <lang>"
	@echo "  pdf                  Build the PDF documentation using LaTeX for all languages"
	@echo "  pdf_<lang>           Build the PDF documentation using LaTeX for <lang>"
	@echo "  ebook                Reduce size of PDF for eBook"
	@echo "  prepress             Reduce size of PDF for prepess"
	@echo "  index                Copy static docs/index.html to docs/_build/html/index.html"
	@echo "  translations         Translate from English"

all: clean gettext_build update_locale html index latex pdf ebook prepress

check:
	@for po in $(PO_FILES); do \
		echo "Checking $$po..."; \
		msgfmt --check --output-file=- "$$po" || exit 1; \
	done

index:
	mkdir -p docs/_build/html
	cp -p docs/index.html docs/_build/html/index.html

clean:
	for file in $(PO_FILES); do \
	    $(MSGATTRIB) --no-obsolete -o $$file $$file; \
	done
	cd docs && make clean
	find $(SOURCEDIR) -type f -name "*.mo" -delete
	rm -rf $(BUILDDIR)/*

gettext_build:
	$(SPHINXBUILD) -b gettext -c $(SOURCEDIR) -d $(BUILDDIR)/doctrees/$(GETTEXT_BUILD) $(SOURCEDIR) $(BUILDDIR)/locale/gettext

update_locale:
	@pids="" ; \
	for lang in $(LANGUAGES); do \
	    ( echo "Updating locale for $$lang..." ; $(UPDATE_LOCALE) $$lang ) & pids="$$pids $$!" ; \
	done ; \
	for pid in $$pids; do \
	    wait $$pid ; \
	done

update_locale_%:
	$(UPDATE_LOCALE) $*

html: index
	@for lang in $(LANGUAGES); do \
	    echo "Building HTML documentation for $$lang..."; \
	    $(SPHINXBUILD) -b html -d $(BUILDDIR)/doctrees -D language=$$lang $(SOURCEDIR) $(BUILDDIR)/html/$$lang; \
	done

html_%: gettext_build
	$(SPHINXBUILD) -b html -d $(BUILDDIR)/doctrees -D language=$* -c $(SOURCEDIR) $(SOURCEDIR) $(BUILDDIR)/html/$*/

latex:
	@for lang in $(LANGUAGES); do \
		echo "Building LaTeX documentation for $$lang..."; \
		$(SPHINXBUILD) -b latex -d $(BUILDDIR)/doctrees -D language=$$lang -Dlatex_engine=xelatex $(SOURCEDIR) $(BUILDDIR)/latex/$$lang; \
	done

latex_%:
	$(SPHINXBUILD) -b latex -d $(BUILDDIR)/doctrees -D language=$* -Dlatex_engine=xelatex $(SOURCEDIR) $(BUILDDIR)/latex/$*/; \

pdf: latex
	@for lang in $(filter-out ar he ja,$(LANGUAGES)); do \
		echo "Building PDF documentation for $$lang..."; \
		$(MAKE) -C $(BUILDDIR)/latex/$$lang ; \
	done

pdf_%:
	$(MAKE) -C $(BUILDDIR)/latex/$* ; \

ebook: latex pdf
	gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -q \
		-o docs/_build/latex/en/transpolibre-ebook-en.pdf \
		docs/_build/latex/en/transpolibre.pdf
	gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -q \
		-o docs/_build/latex/es/transpolibre-ebook-es.pdf \
		docs/_build/latex/es/transpolibre.pdf

prepress: latex pdf
	gs -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress -q \
		-o docs/_build/latex/en/transpolibre-prepress-en.pdf \
		docs/_build/latex/en/transpolibre.pdf
	gs -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress -q \
		-o docs/_build/latex/es/transpolibre-prepress-es.pdf \
		docs/_build/latex/es/transpolibre.pdf

translations:
	echo "Not implemented"
