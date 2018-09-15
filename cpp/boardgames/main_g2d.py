#!/usr/bin/env python3

import cppyy, sys

cppyy.include("lightsout.cpp")
from cppyy.gbl import LightsOut

sys.path.append('../../examples/')
from boardgame_g2d import BoardGameGui

game = LightsOut(4, 5, 5)
gui = BoardGameGui(game)
gui.main_loop()
