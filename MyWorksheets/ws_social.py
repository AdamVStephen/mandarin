#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
ws-social.py : Mandarin worksheets for social vocabulary
"""

from manws import TestPhrase, Worksheet
import sys

import pdb

testPhrases = []
testPhrases.append(TestPhrase('她没有男朋右' , 'She does not have a boyfriend'))
testPhrases.append(TestPhrase('李老师没有弟弟', 'Teacher Li does not have a younger brother'))
testPhrases.append(TestPhrase('洗手间在这儿马', 'Is the bathroom here?'))
testPhrases.append(TestPhrase('没有洗手间这儿', 'There is no bathroom here'))
testPhrases.append(TestPhrase('老师在那儿', 'The teacher is over there'))

def make_worksheets():
    category = 'social'
    wh = Worksheet(testPhrases, wsfile='%s-hanzi.tex' % category, giveHanzi=True)
    wp = Worksheet(testPhrases, wsfile='%s-pinyin.tex' % category, givePinyin=True)
    wx = Worksheet(testPhrases, wsfile='%s-xpinyin.tex' % category, giveXpinyin=True)
    we = Worksheet(testPhrases, wsfile='%s-english.tex' % category, giveEnglish=True)
    ww = Worksheet(testPhrases, wsfile='%s-all.tex' % category, giveHanzi = True, givePinyin=True, giveXpinyin=True, giveEnglish=True)
    wa = Worksheet(testPhrases, wsfile='%s-answers.tex' % category, giveAnswers=True)
        
if __name__ == '__main__':
    make_worksheets()
