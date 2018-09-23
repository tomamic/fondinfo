#!/usr/bin/env python3

##import cppyy
##cppyy.include("lightsout.cpp")
##from cppyy.gbl import LightsOut

from boardgames import LightsOut

import sys
sys.path.append('../../examples/')
from boardgame_g2d import BoardGameGui

game = LightsOut(4, 5, 5)
gui = BoardGameGui(game)
gui.main_loop()
