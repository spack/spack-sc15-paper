name = spack-sc15
tex_args = -shell-escape

# LaTeX diff command
latexdiff = latexdiff-vc --git -c review-process/latexdiff.cfg -r shepherd.2

figures = \
	figs/concretization.pdf \
	figs/overhead/overhead.pdf \
	figs/overhead/build-time.pdf \
	figs/ares-dot/ares-fig.pdf \
	figs/concretization-overhead/concretization-times.pdf

$(name).pdf: *.tex *.cls *.bib $(figures)
	pdflatex $(tex_args) $(name)
	bibtex $(name)
	pdflatex $(tex_args) $(name)
	pdflatex $(tex_args) $(name)

clean:
	rm -f *.out *.aux *.toc *.log *.bbl *.blg $(name).pdf
	rm -f *.ent *.synctex.gz *.rai *.cpt
	rm -f *Graph.pdf *Graph.dot *Graph.log
	rm -f *-diffshepherd.2.tex
	rm -rf _minted-*

diff:
	rm -f *-diffshepherd.2.tex
	scripts/require-clean-work-tree "make diff" *.tex
# include new files directly in the old files (latexdiff doesn't seem to see them otherwise)
#	sed -i~ -e '/\\input{usecase-ares}/ {' -e 'r usecase-ares.tex' -e 'r limitations.tex' -e 'd' -e '}' usecases.tex
#	sed -i~ -e 's/\\input{limitations}//' spack-sc15.tex
# Diff all the files
	files=`\ls *.tex` && \
	$(latexdiff) *.tex && \
	for file in $$files; do \
		diff_file=`echo $$file | sed 's/.tex$$/-diffshepherd.2.tex/'` && mv $$diff_file $$file; \
	done
# Make a PDF of the diff
	make $(name).pdf
	mv $(name).pdf $(name)-diff.pdf
# Restore deleted ARES use case and restore all files to current revision
	git checkout *.tex
