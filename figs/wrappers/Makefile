

wrapper-overhead.pdf: wrapper-overhead.py overhead.yaml
	./wrapper-overhead.py
	pdfcrop	wrapper-overhead.pdf
	mv wrapper-overhead-crop.pdf wrapper-overhead.pdf

clean:
	rm -f wrapper-overhead.pdf
