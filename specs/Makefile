
TARGETS = \
  mpileaks.pdf \
  mpileaks-version.pdf \
  mpileaks-abstract.pdf \
  mpileaks-concrete.pdf \
  rpaths.pdf


all: $(TARGETS)

%.pdf: %.dot
	dot -Tpdf $< -o $@ 2> $*.log
	pdfcrop $@
	mv $*-crop.pdf $@

clean:
	rm -f *.pdf *.log
