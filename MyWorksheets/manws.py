#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
manws.py : MANdarin WorkSheet generator.
"""

import sys

import pdb
from template import docHeader, docFooter, pageBreak

class TestPhrase:
    def __init__(self, hanzi, translation, character_margin=0):
        self.hanzi = hanzi
        self.translation = translation
        self.lhanzi = len(self.hanzi)
        self.ltranslation = len(self.translation.split())
        self.character_margin = character_margin
        self.linewidth = self.lhanzi + self.character_margin

    def giveEnglish(self):
        """Render a table with the English on one line, then lines for Pinyin and Hanzi."""
        s = []
        s.append('\\begin{tabular}{' + '|l' * self.linewidth + '|} \hline')
        s.append('\multicolumn{%d}{|l|}{%s} \\\\ \hline' % (self.linewidth, self.translation))
        s.append(' &' * (self.linewidth-1) + ' \\\\ \hline')
        s.append(' &' * (self.linewidth-1) + ' \\\\ \hline')
        s.append('\end{tabular}')
        return '\n'.join(s)

    def giveHanzi(self):
        """Render a table with the Hanzi on one line, then lines for Pinyin and English."""
        s = []
        s.append('\\begin{tabular}{' + '|l' * self.linewidth + '|} \hline')
        hanziLine = ['%s &' % h for h in self.hanzi[:-1]]
        hanziLine.append('%s' % self.hanzi[-1])
        s.append(''.join(hanziLine) + ' \\\\ \hline')
        s.append(' &' * (self.linewidth-1) + ' \\\\ \hline')
        s.append('\multicolumn{%d}{|l|}{%s} \\\\ \hline' % (self.linewidth, ''))
        s.append('\end{tabular}')
        return '\n'.join(s)

    def givePinyin(self):
        """Render a table with the Pinyin on one line, then lines for Hanzi and English."""
        s = []
        s.append('\\begin{tabular}{' + '|l' * self.linewidth + '|} \hline')
        pinyinLine = ['\\xpinyin*[ratio={2.}]{\color{white}%s} &' % h for h in self.hanzi[:-1]]
        pinyinLine.append('\\xpinyin*[ratio={2.}]{\color{white}%s}' % self.hanzi[-1])
        s.append(''.join(pinyinLine) + ' \\\\ \hline')
        s.append(' &' * (self.linewidth-1) + ' \\\\ \hline')
        s.append('\multicolumn{%d}{|l|}{%s} \\\\ \hline' % (self.linewidth, ''))
        s.append('\end{tabular}')
        return '\n'.join(s)

    def giveXpinyin(self):
        """Render a table with the Hanzi+Pinyin on one line, then a line for English."""
        s = []
        s.append('\\begin{tabular}{' + '|l' * self.linewidth + '|} \hline')
        xpinyinLine = ['\\xpinyin*{%s} &' % h for h in self.hanzi[:-1]]
        xpinyinLine.append('\\xpinyin*{%s}' % self.hanzi[-1])
        s.append(''.join(xpinyinLine) + ' \\\\ \hline')
        s.append('\multicolumn{%d}{|l|}{%s} \\\\ \hline' % (self.linewidth, ''))
        s.append('\end{tabular}')
        return '\n'.join(s)
    
    def giveAnswers(self):
        """Render a table with the English, then the Hanzi + Pinyin"""
        s = []
        s.append('\\begin{tabular}{' + '|l' * self.linewidth + '|} \hline')
        s.append('\multicolumn{%d}{|l|}{%s} \\\\ \hline' % (self.linewidth, self.translation))
        xpinyinLine = ['\\xpinyin*{%s} &' % h for h in self.hanzi[:-1]]
        xpinyinLine.append('\\xpinyin*{%s}' % self.hanzi[-1])
        s.append(''.join(xpinyinLine) + ' \\\\ \hline')
        s.append('\end{tabular}')
        return '\n'.join(s)
    
    def __repr__(self):
        s = []
        s.append('TestPhrase')
        s.append('N of Hanzi Characters : %d' % self.lhanzi)
        s.append('Type of .hanzi : %s' % type(self.hanzi))
        s.append('Type of .hanzi[0] : %s' % type(self.hanzi[0]))
        s.append('Translation Words : %d' % self.ltranslation)
        s.append('Cells to span both : %d' % max(self.lhanzi, self.ltranslation))
        s.append('In English : %s' % self.translation)
        s.append('In Mandarin : %s' % self.hanzi)
        s.append('In Mandarin : %s' % self.hanzi[0])
        s.append(self.giveEnglish())
        s.append(self.giveHanzi())
        s.append(self.givePinyin())
        s.append(self.giveXpinyin())
        s.append(self.giveAnswers())
        return '\n'.join(s)

class Worksheet:
    def __init__(self, phrases, wsfile=None, giveAnswers = False, giveEnglish = False, giveHanzi = False, givePinyin = False, giveXpinyin = False):
        if not (giveEnglish or giveHanzi or givePinyin or giveXpinyin or giveAnswers):
            raise Exception('Must request one of the test modes for Worksheet or it is pointless!')
        self.phrases = phrases
        self.giveAnswers = giveAnswers
        self.giveEnglish = giveEnglish
        self.giveHanzi = giveHanzi
        self.givePinyin = givePinyin
        self.giveXpinyin = giveXpinyin
        if not wsfile:
            wsfile='ws.tex'
        with open(wsfile, 'w') as fh:
            if giveAnswers:
                fh.writelines(self.answerSheet())
            else:
                fh.writelines(self.testPaper())
        
    def testPaper(self):
        doc = []
        doc.append(docHeader)
        doc.append('\Huge')
        for p in self.phrases:
            if self.giveEnglish: doc.append(p.giveEnglish())
            if self.giveHanzi: doc.append(p.giveHanzi())
            if self.givePinyin: doc.append(p.givePinyin())
            if self.giveXpinyin: doc.append(p.giveXpinyin())
            doc.append(docFooter)
        return('\n'.join(doc))

    def answerSheet(self):
        doc = []
        doc.append(docHeader)
         doc.append('\Huge')
        for p in self.phrases:
            if self.giveEnglish: doc.append(p.giveEnglish())
            if self.giveHanzi: doc.append(p.giveHanzi())
            if self.givePinyin: doc.append(p.givePinyin())
            if self.giveXpinyin: doc.append(p.giveXpinyin())
        doc.append(pageBreak)
        for p in self.phrases:
            if self.giveAnswers: doc.append(p.giveAnswers())
        doc.append(docFooter)
        return('\n'.join(doc))
    
    
def ut():
    testPhrases = []
    testPhrases.append(TestPhrase('你好' , 'Hello'))
    for tp in testPhrases:
        print(tp)
    try:
        ws = Worksheet(testPhrases, wsfile='ut.tex')
    except Exception as error:
        print('Correctly caught exception on invalid worksheet')
    else:
        raise Exception('Unit test failed : invalid worksheet did not raise an exception')

    try:
        ws = Worksheet(testPhrases, wsfile='ut-english.tex', giveEnglish=True)
        ws = Worksheet(testPhrases, wsfile='ut-hanzi.tex', giveHanzi=True)
        ws = Worksheet(testPhrases, wsfile='ut-pinyin.tex', givePinyin=True)
        ws = Worksheet(testPhrases, wsfile='ut-xpinyin.tex', giveXpinyin=True)
        ws = Worksheet(testPhrases, wsfile='ut-answers.tex', giveAnswers=True)
    except Exception as error:
        raise Exception('Unexpected exception')
    else:
        pass
        
if __name__ == '__main__':
    ut()
