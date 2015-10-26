import pygame

values = []

max_val = 0
val = float(input('Val? '))
while val > 0:
    gray = float(input('Gray? '))
    values.append((val, gray))
    if val > max_val:
        max_val = val
    val = float(input('Val? '))

WIDTH, HEIGHT = 600, 400
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

if len(values) > 0:
    w = WIDTH / len(values)
    h = HEIGHT / max_val

    for i in range(len(values)):
        val, gray = values[i]
        rect = int(w * i), int(HEIGHT - h * val), int(w - 1), int(h * val)
        pygame.draw.rect(screen, (gray, gray, gray), rect)
    
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
