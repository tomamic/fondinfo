import pygame

def center(rect: (int, int, int, int)) -> (int, int):
    x, y, w, h = rect
    return x + w // 2, y + h // 2

def htree(screen, rect: (int, int, int, int), level: int):
    x, y, w, h = rect
    if level == 0 or w < 3 or h < 3:
        return
    if level % 2 == 0:
        rect1 = x, y, w // 2, h
        rect2 = x + w // 2, y, w // 2, h
    else:
        rect1 = x, y, w, h // 2
        rect2 = x, y + h // 2, w, h // 2

    pygame.draw.line(screen, (255, 255, 255),
                     center(rect1), center(rect2))
    htree(screen, rect1, level - 1)
    htree(screen, rect2, level - 1)

level = int(input('level? '))  ## -1 = infinite
side = 600

pygame.init()
screen = pygame.display.set_mode((side, side))
htree(screen, (0, 0, side, side), level)
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
