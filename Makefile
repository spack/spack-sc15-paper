name = paper
tex_args = -shell-escape

$(name).pdf: *.tex *.cls *.bib
	make clean
	pdflatex $(tex_args) $(name)
	bibtex $(name)
	pdflatex $(tex_args) $(name)
	pdflatex $(tex_args) $(name)

clean:
	rm -f *.out *.aux *.toc *.log *.bbl *.blg $(name).pdf
	rm -f *.ent *.synctex.gz *.rai *.cpt
	rm -f *Graph.pdf *Graph.dot *Graph.log
