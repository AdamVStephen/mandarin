%.pdf : %.dvi
	dvipdf $<

%.dvi : %.tex
	latex $<
	latex $<

ALL:=lesson-yi.pdf

all : $(ALL)

clean :
	rm -f *.aux *.log *~
