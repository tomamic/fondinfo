import pygame

cols = int(input('Cols? '))
rows = int(input('Rows? '))

WIDTH, HEIGHT = 600, 400
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

w, h = WIDTH / cols, HEIGHT / rows
delta_blue, delta_green = 0, 0
if cols > 1:
    delta_blue = 255.0 / (cols - 1)
if rows > 1:
    delta_green = 255.0 / (rows - 1)

for y in range(rows):
    for x in range(cols):
        color = 0, int(delta_green * y), int(delta_blue * x)
        rect = int(w * x), int(h * y), int(w - 1), int(h - 1)
        pygame.draw.rect(screen, color, rect)

pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
