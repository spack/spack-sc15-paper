name = spack-sc15
tex_args = -shell-escape

# LaTeX diff command
latexdiff = latexdiff-vc --git -c review-process/latexdiff.cfg -r submitted

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
	scripts/require-clean-work-tree "make diff" *.tex
# cat ARES usecase document to end of usecases, to make it look new to latexdiff.
	sed -i~ 's/\\input{usecase-ares}//' usecases.tex
	cat usecase-ares.tex >> usecases.tex
	rm usecase-ares.tex
# Diff all the files
	$(latexdiff) *.tex;
	for file in *.tex; do \
		diff_file=`echo $$file | sed 's/.tex$$/-diffsubmitted.tex/'` && mv $$diff_file $$file; \
	done
# Make a PDF of the diff
	make $(name).pdf
	mv $(name).pdf $(name)-diff.pdf
# Restore deleted ARES use case and restore all files to current revision
	touch usecase-ares.tex
	git checkout *.tex
