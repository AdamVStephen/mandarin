#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

pageBreak = r'''\vfill\eject'''

docHeader = r'''
\documentclass{article}
% Margin control
\usepackage[a4paper, total={7in, 11in}]{geometry}
% For Chinese support, recommended by Chou : augmented with xpinyin by sobenlee@gmail.com
\usepackage{CJKutf8}
% For xpinyin
\usepackage{xpinyin}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
% From Chou
\usepackage{ucs} 
\usepackage[encapsulated]{CJK}
% Font choices
% bsmi limited - lacks certain characters
%\newcommand{\myfont}{bsmi} % or {stheiti}, etc
% gbsn recommended from sobenlee@gmail.com in xpinyin documentation
\newcommand{\myfont}{gbsn} % or {stheiti}, etc
%
% \tiny
% \scriptsize
% \footnotesize
% \small
% \normalsize
% \large
% \Large
% \LARGE
% \huge
\Huge
% For Exam/Question support taken from en.wikibooks.org/wiki/LaTeX/List\_Structures
\usepackage{tasks}
\usepackage{exsheets}
\SetupExSheets[question]{type=exam}
% Personal macros
\newcommand{\cvoc}[1]{#1 & \xpinyin*{#1} }
\newcommand{\cvct}[3]{#1 & \xpinyin*{#1} & \pinyin{#2} & #3 \\ \hline}
\newcommand{\cvctp}[4]{#1 & \xpinyin*{#1} & \pinyin{#2} & #3 & #4 \\ \hline}
% For dictation box setup (todo : write a python generator)


%\newcommand{\cvctp}[4]{#1 & \xpinyin*{#1} & \pinyin{#2} & #3 & #4 \\ \hline}
% xpe = xpinyin : english
\newcommand{\xpe}[2]{\xpinyin*{#1} : #2}

\begin{document} 
\begin{CJK}{UTF8}{\myfont} 
'''

docFooter = r'''
\end{CJK} 
\end{document}
'''
