#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import game2d as g2d
from actor import Actor, Arena
from dk_elements import map_elements


class Jumper(Actor):

    def __init__(self, arena, x, y):
        self._w, self._h = 16, 16
        self._speed = 3
        self._max_speed = 3
        self._gravity = 0.4
        self._x, self._y = x, y
        self._dx, self._dy = 0, 0
        self._landed = False
        self._climbing = False
        self._ladder = None
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        self._y += self._dy
        if self._dx != 0 and self._climbing:
            self._climbing = False
            self._dy = 0
        if not (self._landed or self._climbing):
            self._dy += self._gravity
            self._dy = min(self._dy, self._max_speed)

        self._landed = False

        if self._ladder != None:
            bx, by, bw, bh = self.rect()  # jumper's pos
            wx, wy, ww, wh = self._ladder.rect() # ladder's pos
            if not (wy <= by + bh <= wy + wh and wx < bx + bw // 2 < wx + ww):
                if self._climbing:
                    self._y -= self._dy
                else:
                    self._ladder = None

        self._x += self._dx
        if self._x < 0:
            self._x = 0
        elif self._x > arena_w - self._w:
            self._x = arena_w - self._w

    def jump(self):
        if self._landed:
            self._dy = -self._max_speed
            self._landed = False
        
    def go_left(self):
        self._dx = -self._speed
        
    def go_right(self):
        self._dx = +self._speed

    def go_up(self):
        if self._ladder and (self._climbing or self._landed):
            self._climbing = True
            self._dy = -self._speed
        
    def go_down(self):
        if self._ladder and (self._climbing or self._landed):
            self._climbing = True
            self._dy = self._speed

    def stay(self):
        self._dx = 0
        self._dy = 0

    def collide(self, other):
        bx, by, bw, bh = self.rect()  # jumper's pos
        wx, wy, ww, wh = other.rect() # other's pos
        if (isinstance(other, Ladder) and
            wy <= by + bh <= wy + wh and wx < bx + bw // 2 < wx + ww):
            self._ladder = other
        elif isinstance(other, Platform) and not self._climbing:
            if by + bh < wy + wh:
                self._y = wy - bh
                self._landed = True
        elif isinstance(other, Barrel) and wy <= by + bh // 2 <= wy + wh:
            self._arena.remove(self)
        
    def rect(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        if self._climbing:
            return 124, 24
        return 92, 2


class Mario(Jumper):
    pass


class Barrel(Jumper):

    def __init__(self, arena, x, y):
        Jumper.__init__(self, arena, x, y)
        self._w, self._h = 12, 12
        self._speed, self._max_speed = 2, 4
        self.go_right()
        
    def move(self):
        aw, ah = self._arena.size()
        if self._x + self._w >= aw:
            self.go_left()
        elif self._x <= 0:
            self.go_right()
            if self._y + self._h * 2 > ah:
                self._arena.remove(self)
        Jumper.move(self)

    def symbol(self):
        return 66, 256


class Platform(Actor):

    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._w, self._h = 16, 8
        self._arena = arena
        arena.add(self)

    def move(self):
        pass

    def collide(self, other):
        pass
        
    def rect(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return -1, -1

class Ladder(Actor):

    def __init__(self, arena, x, y, h):
        self._x, self._y = x, y
        self._w, self._h = 8, h
        self._arena = arena
        arena.add(self)

    def move(self):
        pass

    def collide(self, other):
        pass
        
    def rect(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return -1, -1

def update():
    arena.move_all()  # Game logic

    g2d.image_blit(background, (0, 0))
    for a in arena.actors():
        x, y, w, h = a.rect()
        xs, ys = a.symbol()
        if xs >= 0 and ys >= 0:
            g2d.image_blit(sprites, (x, y), area=(xs, ys, w, h))
            
def keydown(code):
    if code == "Space":
        mario.jump()
    elif code == "ArrowLeft":
        mario.go_left()
    elif code == "ArrowRight":
        mario.go_right()
    elif code == "ArrowUp":
        mario.go_up()
    elif code == "ArrowDown":
        mario.go_down()

def keyup(code):
    if code in ("ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown"):
        mario.stay()

def main():
    global arena, mario, sprites, background
    
    arena = Arena(224, 256)
    mario = Mario(arena, 50, 230)
    Barrel(arena, 180, 70)
    Barrel(arena, 150, 70)

    for t, x, y, w, h in map_elements:
        if t == "Platform":
            Platform(arena, int(x), int(y))
        elif t == "Ladder":
            Ladder(arena, int(x), int(y), int(h))

    g2d.canvas_init(arena.size())
    sprites = g2d.image_load("dk_sprites.png")
    background = g2d.image_load("dk_background.png")

    g2d.handle_keyboard(keydown, keyup)
    g2d.set_interval(update, 1000 // 30)  # millis
    
main()
