import g2d
from actor import Actor, Arena

class Wall(Actor):
    def __init__(self, pos, size):
        self._pos = pos
        self._size = size
        
    def move(self, arena):
        return
    
    def pos(self):
        return self._pos
    
    def size(self):
        return self._size
    
    def sprite(self):
        return 

class Ball(Actor):
    def __init__(self, pos):
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._dx, self._dy = 4, 0
        
    def move(self, arena):
        arena_w, arena_h = arena.size()
        keys = arena.current_keys()
        
        for other in arena.collisions():
            ox, oy = other.pos()
            ow, oh = other.size()
            if isinstance(other, Wall) and self._dy >= 0:
                self._y = oy - self._h
                self._dy = 0
                if "ArrowUp" in keys:
                    self._dy = -20
        
        self._x = (self._x + self._dx) % arena_w
        self._y += self._dy
        
        self._dy += 1
    
    def pos(self):
        return self._x, self._y
    
    def size(self):
        return self._w, self._h
    
    def sprite(self):
        return

def tick():
    g2d.clear_canvas()
    
    for a in arena.actors():
        g2d.draw_rect(a.pos(), a.size())
        
    arena.tick(g2d.current_keys())

arena = Arena((480, 360))
b = Ball((100, 50))
arena.spawn(b)

arena.spawn(Wall((0, 340), (480, 20)))

w1 = Wall((250, 250), (100, 20))
arena.spawn(w1)

g2d.init_canvas(arena.size())
g2d.main_loop(tick)