%.pdf : %.dvi
	dvipdf $<

%.dvi : %.tex
	latex $<
	latex $<

ALL:=lesson-yi.pdf lesson-er.pdf lesson-san.pdf lesson-si.pdf vocabulary.pdf dictation.pdf


all : $(ALL)

clean :
	rm -f *.aux *.log *~
