#!/usr/bin/env python3
import sys
sys.path.append('../../examples/')

from boardgames import LightsOut
from boardgame_g2d import BoardGameGui

def main():
    game = LightsOut(4, 5, 5)
    gui = BoardGameGui(game)
    gui.main_loop()
    
if __name__ == '__main__':
    main()
