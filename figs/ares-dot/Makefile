
PDFS=ares.pdf \
	 legend.pdf

all: $(PDFS)

%.pdf: %.dot
	dot -Tpdf < $^ > $@

clean:
	rm $(PDFS)
