#!/usr/bin/env python3

##import cppyy
##cppyy.include("lightsout.cpp")
##cppyy.include("fifteen.cpp")
##from cppyy.gbl import LightsOut, Fifteen

from boardgames import LightsOut, Fifteen

import sys
sys.path.append('../../examples/')
from boardgame_g2d import BoardGameGui

##game = LightsOut(4, 5, 5)
game = Fifteen(3, 3)
gui = BoardGameGui(game)
gui.main_loop()
