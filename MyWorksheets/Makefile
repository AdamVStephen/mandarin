%.pdf : %.dvi
	dvipdf $<

%.dvi : %.tex
	latex $<
	latex $<

ut-english.tex ut-hanzi.tex ut-pinyin.tex ut-xpinyin.tex ut-answers.tex: manws.py template.py
	./manws.py

ALL:=ut-english.pdf ut-hanzi.pdf ut-pinyin.pdf ut-xpinyin.pdf ut-answers.pdf

all : $(ALL)

clean :
	rm -f *.aux *.log *~ *.dvi

sterile :
	rm -f *.aux *.log *~ *.pdf *.dvi
