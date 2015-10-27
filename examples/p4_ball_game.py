from p4_ball import Ball
import pygame
pygame.init()                     # Prepare pygame
clock = pygame.time.Clock()       # To set game speed
screen = pygame.display.set_mode((Ball.ARENA_W, Ball.ARENA_H))

balls = [Ball(40, 80), Ball(80, 40)]

playing = True
while playing:
    for e in pygame.event.get():  # Handle events: mouse, keyb etc.
        if e.type == pygame.QUIT:
            playing = False
    screen.fill((255, 255, 255))

    for b in balls:
        b.move()
        pygame.draw.rect(screen, (127, 127, 127), b.rect())

    pygame.display.flip()         # Surface ready, show it!
    clock.tick(30)                # Delay to get 30 fps
pygame.quit()                     # Close the window
