import pygame

class Alien:
    SPEED = 5
    W, H = 20, 20
    PATH_W = 150

    def __init__(self, x0: int, y0: int):
        self._x = x0
        self._y = y0
        self._xmin = x0
        self._dx = self.SPEED

    def move(self):
        xmax = self._xmin + self.PATH_W - self.W
        if self._xmin <= self._x + self._dx <= xmax:
            self._x += self._dx
        else:
            self._dx = -self._dx
            self._y += self.SPEED

    def rect(self):
        return self._x, self._y, self.W, self.H


pygame.init()                     # Prepare pygame
screen = pygame.display.set_mode((320, 240))
clock = pygame.time.Clock()       # To set game speed

aliens = [Alien(40, 40), Alien(80, 80), Alien(120, 40)]

playing = True
while playing:
    for e in pygame.event.get():  # Handle events: mouse, keyb etc.
        if e.type == pygame.QUIT: playing = False
    screen.fill((255, 255, 255))  # Draw background 

    for a in aliens:
        a.move()                # Apply game logic
                                # Draw foreground
        pygame.draw.rect(screen, (127, 127, 127), a.rect())

    pygame.display.flip()         # Surface ready, show it!
    clock.tick(30)                # Wait 1/30 seconds
pygame.quit()                     # Close the window
