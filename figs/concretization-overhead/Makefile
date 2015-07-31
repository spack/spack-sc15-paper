
pdfs = concretization-times.pdf package-sizes.pdf

all: $(pdfs)

concretization-times.pdf: ./concretization-times.py
	./concretization-times.py
	pdfcrop concretization-times.pdf
	mv concretization-times-crop.pdf concretization-times.pdf

package-sizes.pdf: ./package-sizes.py
	./package-sizes.py
	pdfcrop package-sizes.pdf
	mv package-sizes-crop.pdf package-sizes.pdf


clean:
	rm concretization-times*.pdf
