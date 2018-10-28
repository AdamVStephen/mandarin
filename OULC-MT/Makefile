%.pdf : %.dvi
	dvipdf $<

%.dvi : %.tex
	latex $<
	latex $<

ALL:=lesson-yi.pdf vocabulary.pdf

all : $(ALL)

clean :
	rm -f *.aux *.log *~
