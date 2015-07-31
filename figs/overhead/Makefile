
all:
	./overhead.py
	pdfcrop	build-time.pdf
	mv build-time-crop.pdf build-time.pdf
	pdfcrop	overhead.pdf
	mv overhead-crop.pdf overhead.pdf

clean:
	rm -f *.pdf
