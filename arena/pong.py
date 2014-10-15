from sys import stdin
from arena import Character, Arena

class PongArena(Arena):
    LEFT, RIGHT = 0, 1
    
    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self._points = [0, 0]

    def score(self, side: int, val: int):
        self._points[side] += val

    def points(self) -> (int, int):
        return self._points[0], self._points[1]


class Ball(Character):
    
    def __init__(self, arena: PongArena, x: int, y: int):
        self._x, self._y = x, y
        self._dx, self._dy = 16, 12
        self._w, self._h = 20, 20
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()

        self._x += self._dx
        if not 0 <= self._x < arena_w - self._w:
            self.score()
            self.bounce_h(arena_w, 0)
            
        self._y = self._y + self._dy
        if not 0 <= self._y < arena_h - self._h:
            self.bounce_v(arena_h, 0)

    def bounce_h(self, obstacle_at_right: int, obstacle_at_left: int):
        if self._dx > 0:
            self._x = 2 * (obstacle_at_right - self._w) - self._x
        else:
            self._x = 2 * obstacle_at_left - self._x
        self._dx = -self._dx

    def bounce_v(self, obstacle_below: int, obstacle_above: int):
        if self._dy > 0:
            self._y = 2 * (obstacle_below - self._h) - self._y
        else:
            self._y = 2 * obstacle_above - self._y
        self._dy = -self._dy
            
    def score(self):
        if self._dx > 0:
            self._arena.score(PongArena.LEFT, 1)
        else:
            self._arena.score(PongArena.RIGHT, 1)
                
    def hit(self, other: Character):
        x1, y1, w1, h1 = other.rect()
        self.bounce_h(x1, x1 + w1)

    def symbol(self) -> int:
        return 0

    def rect(self) -> (int, int, int, int):
        return (self._x, self._y, self._w, self._h)


class Paddle:
    SPEED = 8

    def __init__(self, arena: PongArena, x: int, y: int):
        self._x, self._y = x, y
        self._w, self._h = 5, 50
        self._dy = 0
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        self._y += self._dy
        if self._y < 0:
            self._y = 0
        elif self._y > arena_h - self._h:
            self._y = arena_h - self._h

    def hit(self, other: Character):
        other.bounce_h(self._x, self._x + self._w)

    def go_up(self):
        self._dy = -self.SPEED
        
    def go_down(self):
        self._dy = self.SPEED

    def stay(self):
        self._dy = 0

    def symbol(self) -> int:
        return 0
        
    def rect(self) -> (int, int, int, int):
        return (self._x, self._y, self._w, self._h)
        

class AutoPaddle(Paddle):
    def __init__(self, arena: PongArena, x: int, y: int, amplitude: int):
        super().__init__(arena, x, y)
        self._ymin, self._ymax = y, y + amplitude
        self._dy = self.SPEED // 2

    def move(self):
        if not (self._ymin <= self._y + self._dy < self._ymax):
            self._dy = -self._dy
        self._y += self._dy


if __name__ == '__main__':
    arena = PongArena(600, 400)
    Ball(arena, 300, 200)
    paddle = Paddle(arena, 100, 200);
    AutoPaddle(arena, 200, 50, 250);
    AutoPaddle(arena, 500, 200, 100);
    AutoPaddle(arena, 400, 50, 100);
    print(arena)

    for line in stdin:
        if line.strip() == 'w':
            paddle.go_up()
        elif line.strip() == 's':
            paddle.go_down()
        else:
            paddle.stay()

        arena.move_all()
        print(arena)
        print(arena.points())
