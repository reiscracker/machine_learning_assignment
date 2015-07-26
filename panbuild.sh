pandoc --toc -s -N -V geometry:margin=1in --template mytemplate.latex --include-in-header titlesec.tex -o dokumentation.pdf dokumentation.md 
