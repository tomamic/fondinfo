#!/usr/bin/env python3
import sys
sys.path.append('../../examples/')

from knightdom import KnightDom
from boardgame_g2d import BoardGameGui

def main():
    game = KnightDom(6)
    gui = BoardGameGui(game)
    gui.main_loop()
    
if __name__ == '__main__':
    main()
