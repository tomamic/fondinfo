'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

class Actor(object):
    '''Interface to be implemented by each game character'''
    
    def move(self):
        '''Called by Arena, at the actor's turn'''
        raise NotImplementedError('Abstract method')

    def collide(self, other):
        '''Called by Arena, when the actor collides with another one
        Args:
            other: Actor -- the other actor involved in the collision
        '''
        raise NotImplementedError('Abstract method')

    def rect(self):
        '''Return the rectangle containing the actor, as a 4-tuple of ints
        Returns:
            (int, int, int, int) -- (left, top, width, height)
        '''
        raise NotImplementedError('Abstract method')

    def symbol(self):
        '''Return (0, 0) or the (x, y) position of current sprite in a
           larger image, containing more sprites
        Returns:
            (int, int) -- the position of current sprite
        '''
        raise NotImplementedError('Abstract method')


class Arena(object):
    '''A generic 2D game, with a given size in pixels and a list of actors'''

    def __init__(self, width, height):
        '''Create an arena, with given dimensions
        Args:
            width: int -- width in pixels
            height: int -- height in pixels
        '''
        self._w, self._h = width, height
        self._actors = []

    def add(self, a):
        '''Register an actor into this arena
        Args:
            a: Actor
        '''
        if a not in self._actors:
            self._actors.append(a)

    def remove(self, a):
        '''Cancel an actor from this arena
        Args:
            a: Actor
        '''
        if a in self._actors:
            self._actors.remove(a)

    def move_all(self):
        '''Move all actors (through their own move method).
        After each single move, collisions are checked and
        The collide methods of both colliding actors are called
        '''
        for a in self.actors():
            previous_pos = a.rect()
            a.move()
            if a.rect() != previous_pos:
                for other in reversed(self.actors()):
                    # reversed order, so actors drawn on top of others
                    # (towards the end of the cycle) are checked first
                    if other is not a and self.check_collision(a, other):
                        a.collide(other)
                        other.collide(a)

    def check_collision(self, a1, a2):
        '''Check two actors for mutual collision
        (bounding-box collision detection)
        Args:
            a1 -- The first actor to check
            a2 -- The second actor
        Returns:
            bool -- Collision value
        '''
        x1, y1, w1, h1 = a1.rect()
        x2, y2, w2, h2 = a2.rect()
        return (y2 < y1 + h1 and y1 < y2 + h2
            and x2 < x1 + w1 and x1 < x2 + w2)

    def actors(self):
        '''Return a copy of the list of actors
        Returns:
            list[Actor] -- the registerd actors
        '''
        return list(self._actors)

    def size(self):
        '''Return the size of the arena as a 2-tuple of ints
        Returns:
            (int, int) -- (width, height)
        '''
        return (self._w, self._h)
