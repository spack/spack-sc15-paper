TEX_NAME=paper

.PHONY: $(TEX_NAME).pdf clean

all: $(TEX_NAME).pdf

$(TEX_NAME).pdf:
	latexmk -lualatex $(TEX_NAME).tex

clean:
	latexmk -C $(TEX_NAME).tex
	rm -f *.ent *.synctex.gz
