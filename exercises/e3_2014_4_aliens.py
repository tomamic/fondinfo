import pygame

class Alien:
    SPEED = 5
    PATH_W = 150

    def __init__(self, x0: int, y0: int):
        self._x = x0
        self._y = y0
        self._xmin = x0
        self._dx = self.SPEED

    def move(self):
        new_x = self._x + self._dx
        if self._xmin <= new_x < self._xmin + self.PATH_W:
            self._x = new_x
        else:
            self._dx = -self._dx
            self._y += self.SPEED

    def pos_x(self):
        return self._x

    def pos_y(self):
        return self._y


pygame.init()                     # Prepare pygame
screen = pygame.display.set_mode((320, 240))
clock = pygame.time.Clock()       # To set game speed
image = pygame.image.load('../arena/ball.png')

aliens = [Alien(40, 40), Alien(80, 80), Alien(120, 40)]

playing = True
while playing:
    for e in pygame.event.get():  # Handle events: mouse, keyb etc.
        if e.type == pygame.QUIT: playing = False
    screen.fill((255, 255, 255))  # Draw background 

    for a in aliens:
        a.move()                # Apply game logic
        screen.blit(image, (a.pos_x(), a.pos_y()))   # Draw foreground

    pygame.display.flip()         # Surface ready, show it!
    clock.tick(30)                # Wait 1/30 seconds
pygame.quit()                     # Close the window
