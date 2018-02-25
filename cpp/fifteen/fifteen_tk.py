#!/usr/bin/env python3
import sys
sys.path.append('../../examples/')

from fifteen import Fifteen
from boardgame_tk import BoardGameGui

def main():
    game = Fifteen(3, 2)
    gui = BoardGameGui(game)
    gui.mainloop()
    
if __name__ == '__main__':
    main()
