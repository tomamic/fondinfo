#!/usr/bin/env python3
import sys
sys.path.append('../../examples/')

from fifteen import Fifteen
from boardgame_g2d import BoardGameGui

def main():
    game = Fifteen(3, 2)
    gui = BoardGameGui(game)
    gui.main_loop()
    
if __name__ == '__main__':
    main()
