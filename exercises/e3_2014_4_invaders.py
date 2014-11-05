import pygame

class Invader:
    W, H = 20, 20
    PATH_WIDTH = 150

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._dx = 5
        self._dy = 5
        self._x0 = x

    def move(self):
        min_x = self._x0
        max_x = self._x0 + self.PATH_WIDTH - self.W
        if min_x <= self._x + self._dx < max_x:
            self._x += self._dx
        else:
            self._dx = -self._dx
            self._y += self._dy

    def rect(self) -> (int, int, int, int):
        return self._x, self._y, self.W, self.H


pygame.init()                     # Prepare pygame
clock = pygame.time.Clock()       # To set game speed
screen = pygame.display.set_mode((320, 240))

invaders = [Invader(40, 40), Invader(80, 80), Invader(120, 40)]

playing = True
while playing:
    for e in pygame.event.get():  # Handle events: mouse, keyb etc.
        if e.type == pygame.QUIT: playing = False
    screen.fill((255, 255, 255))

    for invader in invaders:
        invader.move()
        pygame.draw.rect(screen, (127, 127, 127), invader.rect())

    pygame.display.flip()         # Surface ready, show it!
    clock.tick(30)                # Delay to get 30 fps
pygame.quit()                     # Close the window
