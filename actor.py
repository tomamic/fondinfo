#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

Point = "tuple[int, int]"

class Actor:
    '''Interface to be implemented by each game character.
    '''
    def move(self, arena: "Arena"):
        '''Called by Arena, at the actor's turn.
        '''
        raise NotImplementedError("Abstract method")

    def pos(self) -> Point:
        '''Return the position (x, y) of the actor (left-top corner).
        '''
        raise NotImplementedError("Abstract method")

    def size(self) -> Point:
        '''Return the size (w, h) of the actor.
        '''
        raise NotImplementedError("Abstract method")

    def sprite(self) -> Point:
        '''Return the position (x, y) of current sprite,
        if it is contained in a larger image, with other sprites;
        Otherwise, simply return None.
        '''
        raise NotImplementedError("Abstract method")


class Arena():
    '''A generic 2D game, with a given size in pixels and a list of actors.
    '''
    def __init__(self, size: Point):
        '''Create an arena, with given dimensions in pixels.
        '''
        self._w, self._h = size
        self._count = 0
        self._turn = None
        self._actors = []
        self._curr_keys = self._prev_keys = tuple()
        self._collisions = {}

    def spawn(self, a: Actor):
        '''Register an actor into this arena.
        Actors are blitted in their order of registration.
        '''
        if a not in self._actors:
            self._actors.append(a)

    def kill(self, a: Actor):
        '''Removes an actor from this arena.
        '''
        if a in self._actors:
            self._actors.remove(a)

    def tick(self, keys=tuple()):
        '''Move all actors (through their own act method).
        '''
        actors = list(self._actors)
        self._detect_collisions(actors)
        self._prev_keys = self._curr_keys
        self._curr_keys = keys
        for a in reversed(actors):
            self._turn = a
            a.move(self)

        self._count += 1

    def _detect_collisions(self, actors):
        self._collisions = {a:[] for a in actors}
        # divide the arena in tiles, for efficient collision detection
        tile = 40
        nx, ny = (self._w + tile - 1) // tile,  (self._h + tile - 1) // tile
        cells = [set() for _ in range(nx * ny)]
        for i, a in enumerate(actors):
            x, y, w, h = map(round, a.pos() + a.size())
            for tx in range(x // tile, 1 + (x + w) // tile):
                for ty in range(y // tile, 1 + (y + h) // tile):
                    if 0 <= tx < nx and 0 <= ty < ny:
                        cells[ty * nx + tx].add(i)
        for i in reversed(range(len(actors))):
            a1 = actors[i]
            neighs = set()
            x, y, w, h = map(round, a1.pos() + a1.size())
            for tx in range(x // tile, 1 + (x + w) // tile):
                for ty in range(y // tile, 1 + (y + h) // tile):
                    if 0 <= tx < nx and 0 <= ty < ny:
                        neighs |= cells[ty * nx + tx]
            for j in reversed(sorted(list(neighs))):
                a2 = actors[j]
                if self.check_collision(a1, a2):
                    self._collisions[a1].append(a2)

    def check_collision(self, a1: Actor, a2: Actor) -> bool:
        '''Check the two actors (args) for mutual collision (bounding-box
        collision detection). Return True if colliding, False otherwise.
        '''
        x1, y1, w1, h1 = a1.pos() + a1.size()
        x2, y2, w2, h2 = a2.pos() + a2.size()
        return (a1 is not a2
            and y2 < y1 + h1 and y1 < y2 + h2
            and x2 < x1 + w1 and x1 < x2 + w2)
    
    def collisions(self) -> list[Actor]:
        '''Get the list of actors colliding with the actor `a`'''
        return self._collisions.get(self._turn, [])

    def actors(self) -> list:
        '''Return a copy of the list of actors.
        '''
        return list(self._actors)

    def size(self) -> Point:
        '''Return the size (w, h) of the arena.
        '''
        return (self._w, self._h)

    def count(self) -> int:
        '''Return the total count of ticks (or frames).
        '''
        return self._count

    def current_keys(self) -> "tuple[str, ...]":
        '''Return the currently pressed keys, as a tuple of strs.
        '''
        return self._curr_keys

    def previous_keys(self) -> "tuple[str, ...]":
        '''Return the keys pressed at last tick, as a tuple of strs.
        '''
        return self._prev_keys
