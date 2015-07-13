name = spack-paper-sc15
tex_args = -shell-escape
latexdiff = latexdiff-vc --git -c review-process/latexdiff.cfg

$(name).pdf: *.tex *.cls *.bib
	pdflatex $(tex_args) $(name)
	bibtex $(name)
	pdflatex $(tex_args) $(name)
	pdflatex $(tex_args) $(name)

clean:
	rm -f *.out *.aux *.toc *.log *.bbl *.blg $(name).pdf
	rm -f *.ent *.synctex.gz *.rai *.cpt
	rm -f *Graph.pdf *Graph.dot *Graph.log
	rm -f *-diffsubmitted.tex
	rm -rf _minted-*

diff:
	rm -f *-diffsubmitted.tex
	scripts/require-clean-work-tree "make diff"
	for file in *.tex; do \
		$(latexdiff) -r submitted $$file; \
		diff_file=`echo $$file | sed 's/.tex$$/-diffsubmitted.tex/'` && mv $$diff_file $$file; \
	done
