%.pdf : %.dvi
	dvipdf $<

%.dvi : %.tex
	latex $<
	latex $<

ut-english.tex ut-hanzi.tex ut-pinyin.tex ut-xpinyin.tex ut-answers.tex: manws.py template.py
	./manws.py

social-hanzi.tex social-pinyin.tex social-xpinyin.tex social-english.tex social-answers.tex : ws-social.py
	./ws-social.py

SUFFICES := hanzi pinyin xpinyin english answers all

SOCIAL=social-hanzi.tex social-pinyin.tex social-xpinyin.tex social-english.tex social-answers.tex social-all.tex

SOCIAL_PDF=$(patsubst %.tex,%.pdf, $(SOCIAL))

OCCUPATION_STUB=occupation

OCCUPATION=$(foreach suffix, $(SUFFICES), $(addsuffix -$(suffix).tex, $(OCCUPATION_STUB)))

$(OCCUPATION) : ./ws-occupation.py
	python3 $<

OCCUPATION_PDF=$(patsubst %.tex,%.pdf, $(OCCUPATION))

ALL:=ut-english.pdf ut-hanzi.pdf ut-pinyin.pdf ut-xpinyin.pdf ut-answers.pdf $(SOCIAL_PDF)

social : $(SOCIAL_PDF)

occupation : $(OCCUPATION_PDF)
	echo $(OCCUPATION_PDF)

all : $(ALL)

clean :
	rm -f *.aux *.log *~ *.dvi

sterile :
	rm -f *.aux *.log *~ *.pdf *.dvi
