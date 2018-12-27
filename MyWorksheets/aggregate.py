#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
aggreagate.py : Mandarin phrases pulled together from themed worksheets
"""

from manws import TestPhrase, Worksheet

from ws_social import testPhrases as socialTestPhrases

if __name__ == '__main__':
    for tp in socialTestPhrases: print(tp)
