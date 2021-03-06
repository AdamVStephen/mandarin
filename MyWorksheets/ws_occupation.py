#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
ws_occupation.py : Mandarin worksheets relating to work/occupation
"""
import pdb
import sys

from manws import TestPhrase, Worksheet

testPhrases = []
testPhrases.append(TestPhrase('医院在这儿马' , 'Is the hospital over there?'))
testPhrases.append(TestPhrase('你的姐姐在饭馆' , 'Your older sister is in the restaurant'))

def make_worksheets():
    category = 'occupation'
    wh = Worksheet(testPhrases, wsfile='%s-hanzi.tex' % category, giveHanzi=True)
    wp = Worksheet(testPhrases, wsfile='%s-pinyin.tex' % category, givePinyin=True)
    wx = Worksheet(testPhrases, wsfile='%s-xpinyin.tex' % category, giveXpinyin=True)
    we = Worksheet(testPhrases, wsfile='%s-english.tex' % category, giveEnglish=True)
    ww = Worksheet(testPhrases, wsfile='%s-all.tex' % category, giveHanzi = True, givePinyin=True, giveXpinyin=True, giveEnglish=True)
    wa = Worksheet(testPhrases, wsfile='%s-answers.tex' % category, giveAnswers=True)
        
if __name__ == '__main__':
    make_worksheets()
