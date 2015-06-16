'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

class Actor:
    '''Interface to be implemented by each game character'''
    
    def move(self):
        '''Called by Arena, at the actor's turn'''
        raise NotImplementedError('Abstract method')

    def collide(self, other: 'Actor'):
        '''Called by Arena, when the actor collides with another one
        Args:
          other -- the other actor involved in the collision
        '''
        raise NotImplementedError('Abstract method')

    def symbol(self) -> int:
        '''Return 0, or the index of current image'''
        raise NotImplementedError('Abstract method')

    def rect(self) -> (int, int, int, int):
        '''Return the rectangle containing the actor,
        as a 4-tuple of ints (left, top, width, height)'''
        raise NotImplementedError('Abstract method')


class Arena:
    '''A generic 2D game, with a given size in pixels and a list of actors'''

    def __init__(self, width: int, height: int):
        '''Create an arena, with given dimensions

        Args:
          width -- width in pixels
          height -- height in pixels'''
        self._w, self._h = width, height
        self._actors = []

    def add(self, a: Actor):
        '''Register an actor into this arena'''
        if a not in self._actors:
            self._actors.append(a)

    def remove(self, a: Actor):
        '''Cancels an actor from this arena'''
        if a in self._actors:
            self._actors.remove(a)

    def move_all(self):
        '''Move all actors (through their own move method).
        After each single move, collisions are checked and
        The collide methods of both colliding actors are called
        '''
        for a in self.actors():
            a.move()
            for other in reversed(self._actors):
                # reversed order, so actors drawn on top of others
                # (towards the end of the cycle) are checked first
                if self.check_collision(a, other):
                    a.collide(other)
                    other.collide(a)

    def check_collision(self, a1: Actor, a2: Actor) -> bool:
        '''Check two actors for mutual collision
        (bounding-box collision detection)

        Args:
          a1 -- The first actor to check
          a2 -- The second actor
        '''
        
        x1, y1, w1, h1 = a1.rect()
        x2, y2, w2, h2 = a2.rect()
        return (a1 is not a2
            and y2 < y1 + h1 and y1 < y2 + h2
            and x2 < x1 + w1 and x1 < x2 + w2)

    def actors(self) -> list:
        '''Return a copy of the list of actors'''
        return list(self._actors)

    def size(self) -> (int, int):
        '''Return the size of the arena as a 2-tuple of ints (w, h)'''
        return (self._w, self._h)
