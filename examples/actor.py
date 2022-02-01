#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

class Actor():
    '''Interface to be implemented by each game character.
    '''
    def act(self, arena: "Arena"):
        '''Called by Arena, at the actor's turn.
        '''
        raise NotImplementedError('Abstract method')

    def collide(self, other: "Actor", arena: "Arena"):
        '''Called by Arena, at the actor's turn.
        '''
        raise NotImplementedError('Abstract method')

    def pos(self) -> (int, int):
        '''Return the position (x, y) of the actor (left-top corner).
        '''
        raise NotImplementedError('Abstract method')

    def size(self) -> (int, int):
        '''Return the size (w, h) of the actor.
        '''
        raise NotImplementedError('Abstract method')

    def sprite(self) -> (int, int):
        '''Return the position (x, y) of current sprite,
        if it is contained in a larger image, with other sprites;
        Otherwise, simply return None.
        '''
        raise NotImplementedError('Abstract method')


class Arena():
    '''A generic 2D game, with a given size in pixels and a list of actors.
    '''
    def __init__(self, size: (int, int)):
        '''Create an arena, with given dimensions in pixels.
        '''
        self._w, self._h = size
        self._count = 0
        self._actors = []
        self._spawned = []
        self._killed = []
        self._curr_keys = self._prev_keys = tuple()

    def spawn(self, a: Actor):
        '''Register an actor into this arena.
        Actors are blitted in their order of registration.
        '''
        self._spawned.append(a)

    def kill(self, a: Actor):
        '''Removes an actor from this arena.
        '''
        self._killed.append(a)

    def tick(self, keys=tuple()):
        '''Move all actors (through their own act method).
        '''
        self._prev_keys = self._curr_keys
        self._curr_keys = keys
        for a in reversed(self._actors):
            a.act(self)

        for a1 in reversed(self._actors):
            for a2 in reversed(self._actors):
                if self.check_collision(a1, a2):
                    a1.collide(a2, self)

        self._actors = [a for a in self._actors + self._spawned
                        if a not in self._killed]
        self._spawned = []
        self._killed = []
        self._count += 1

    def check_collision(self, a1: Actor, a2: Actor) -> bool:
        '''Check the two actors (args) for mutual collision (bounding-box
        collision detection). Return True if colliding, False otherwise.
        '''
        x1, y1, w1, h1 = a1.pos() + a1.size()
        x2, y2, w2, h2 = a2.pos() + a2.size()
        return (a1 is not a2
            and y2 < y1 + h1 and y1 < y2 + h2
            and x2 < x1 + w1 and x1 < x2 + w2)

    def actors(self) -> list:
        '''Return a copy of the list of actors.
        '''
        return list(self._actors)

    def size(self) -> (int, int):
        '''Return the size (w, h) of the arena.
        '''
        return (self._w, self._h)

    def count(self) -> int:
        '''Return the total count of ticks (or frames).
        '''
        return self._count

    def current_keys(self) -> "tuple[str]":
        '''Return the currently pressed keys, as a tuple of strs.
        '''
        return self._curr_keys

    def previous_keys(self) -> "tuple[str]":
        '''Return the keys pressed at last tick, as a tuple of strs.
        '''
        return self._prev_keys
