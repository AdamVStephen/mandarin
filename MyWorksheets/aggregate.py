#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
aggregate.py : Mandarin phrases pulled together from themed worksheets
"""

from manws import TestPhrase, Worksheet

from ws_occupation import testPhrases as occupationTestPhrases
from ws_social import testPhrases as socialTestPhrases

def ut():
    for tp in occupationTestPhrases: print(tp)
    for tp in socialTestPhrases: print(tp)

if __name__ == '__main__':
    ut()

