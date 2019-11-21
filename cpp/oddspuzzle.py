#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import cppyy
cppyy.include("oddspuzzle.cpp")
from cppyy.gbl import OddsPuzzle

import sys
sys.path.append('../examples/')
from boardgamegui import gui_play

game = OddsPuzzle(4, 3)
gui_play(game)
