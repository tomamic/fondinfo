#!/usr/bin/env python3

import cppyy
cppyy.include("lightsout.hpp")
cppyy.include("fifteen.hpp")
from cppyy.gbl import LightsOut, Fifteen

##from boardgames import LightsOut, Fifteen

import sys
sys.path.append('../../examples/')
from boardgame_g2d import gui_play

##game = LightsOut(4, 5, 5)
game = Fifteen(3, 3)
gui_play(game)
