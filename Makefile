name=paper

$(name).pdf: *.tex *.cls *.bib
	pdflatex $(name)
	bibtex $(name)
	pdflatex $(name)
	pdflatex $(name)

clean:
	rm -f *.out *.aux *.toc *.log *.bbl *.blg $(name).pdf
	rm -f *.ent *.synctex.gz
