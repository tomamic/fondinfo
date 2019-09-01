#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import cppyy
##cppyy.include("lightsout.cpp")
cppyy.include("fifteen.cpp")
from cppyy.gbl import Fifteen

import sys
sys.path.append('../examples/')
from boardgamegui import gui_play

##game = LightsOut(5, 5, 4)
game = Fifteen(3, 3)
gui_play(game)
