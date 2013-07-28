from sys import stdin
from arena import Actor, Arena, Piece

class Ball(Actor):
    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._dx, self._dy = 1, 1
        self._arena = arena
        arena.add_actor(self)

    def move(self):
        new_x = self._x + self._dx
        if new_x < 0:
            self._arena.score_points(self._arena.RIGHT, 1)
            self._dx = -self._dx
        elif new_x >= self._arena.width:
            self._arena.score_points(self._arena.LEFT, 1)
            self._dx = -self._dx
        new_y = self._y + self._dy
        if not (0 <= new_y < self._arena.height):
            self._dy = -self._dy

        what = self._arena.get(self._x + self._dx, self._y + self._dy)
        if what != None:
            what.actor.interact(self)
            self._dx = -self._dx
        self._x += self._dx
        self._y += self._dy
        
    def interact(self, other: Actor):
        pass

    @property
    def pieces(self):
        return [Piece(self._x, self._y, 0, '*', self)]


class Paddle:
    UP, STAY, DOWN = -1, 0, +1
    INITIAL_LENGTH = 3

    def __init__(self, arena, x, y):
        self._length = Paddle.INITIAL_LENGTH
        self._x, self._y = x, y
        self._dy = 0
        self._arena = arena
        arena.add_actor(self)

    def move(self):
        if self._dy != 0:
            if self._dy == -1:
                new_y = self._y - 1
            else:
                new_y = self._y + self._length
            if 0 <= new_y < self._arena.height:
                what = self._arena.get(self._x, new_y)
                if what == None:
                    self._y += self._dy
                    
    def interact(self, other: Actor):
        pass

    def set_direction(self, dy):
        self._dy = dy

    @property
    def pieces(self):
        return [Piece(self._x, self._y + i, 0, '|', self)
                for i in range(self._length)]


class AutoPaddle(Paddle):
    def __init__(self, arena, x, y):
        super().__init__(arena, x, y)
        self._turn = 0

    def move(self):
        self._turn += 1
        if self._turn % 3 == 0: return
        
        middle = self._y + (self._length // 2)
        half_width = self._arena.width // 2
        for piece in self._arena.pieces:
            if piece.symbol == '*' and abs(self._x - piece.x) < half_width:
                if piece.y < middle:
                    self.set_direction(-1)
                elif piece.y > middle:
                    self.set_direction(+1)
        super().move()


class PongArena(Arena):
    LEFT, RIGHT = 0, 1
    
    def __init__(self, width, height):
        super().__init__(width, height)
        self._points = [0, 0]

    def score_points(self, side, val):
        self._points[side] += val

    def get_points(self, side):
        return self._points[side]


if __name__ == '__main__':
    arena = PongArena(51, 19)
    Ball(arena, 15, 6)
    paddle = Paddle(arena, 4, 9);
    AutoPaddle(arena, 0, 9);
    AutoPaddle(arena, 46, 9);
    AutoPaddle(arena, 50, 9);
    print(arena)

    COMMANDS = {'w': Paddle.UP, 's': Paddle.DOWN}
    for line in stdin:
        direction = COMMANDS.get(line.strip(), Paddle.STAY)
        paddle.set_direction(direction)

        arena.move_all()
        print(arena)
        print(arena.get_points(0), arena.get_points(1))
