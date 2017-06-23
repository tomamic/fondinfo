#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html

@link    https://www.brython.info/static_doc/en/intro.html
@link    https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API
'''

import pygame

K_LEFT, K_UP, K_RIGHT, K_DOWN = 276, 273, 275, 274

canvas = None
onkeydown = None
onkeyup = None

def canvas_init(size: (int, int)):
    '''Set size of first CANVAS and return it'''
    global canvas
    pygame.init()
    canvas = pygame.display.set_mode(size)

def canvas_fill(color: (int, int, int)) -> None:
    canvas.fill(color)

def draw_line(color: (int, int, int), pt1: (int, int), pt2: (int, int)) -> None:
    pygame.draw.line(canvas, color, pt1, pt2)

def draw_circle(color: (int, int, int), center: (int, int), radius: int) -> None:
    pygame.draw.circle(canvas, color, center, radius)

def draw_rect(color: (int, int, int), rectangle: (int, int, int, int)) -> None:
    pygame.draw.rect(canvas, color, rectangle)

def draw_text(txt: str, color: (int, int, int), pos: (int, int), size: int) -> None:
    font = pygame.font.SysFont('sans-serif', size)
    surface = font.render(txt, True, color)
    canvas.blit(surface, pos)

def image_load(url: str) -> pygame.Surface:
    return pygame.image.load(url)

def image_blit(image: pygame.Surface, pos: (int, int), area: (int, int, int, int)=None) -> None:
    canvas.blit(image, pos, area)

def image_blit_scaled(image: pygame.Surface, pos: (int, int, int, int), area: (int, int, int, int)=None) -> None:
    x, y, w, h = pos
    scaled = scale(image, (w, h))
    canvas.blit(scaled, pos, area)

def audio_load(url: str) -> pygame.mixer.Sound:
    return pygame.mixer.Sound(url)
    
def audio_play(audio: pygame.mixer.Sound, loop=False) -> None:
    audio.play(-1 if loop else 0)
    
def audio_pause(audio: pygame.mixer.Sound) -> None:
    audio.stop()

def handle_keyboard(keydown, keyup):
    global onkeydown, onkeyup
    onkeydown, onkeyup = keydown, keyup

def web_key(key: int) -> str:
    result = ""
    word = pygame.key.name(key)
    word = word[0].upper() + word[1:]
    if len(word) == 1 and word.isalpha():
        word = "Key" + word
    elif len(word) == 1 and word.isdigit():
        word = "Digit" + word
    elif word in ("Up", "Down", "Right", "Left"):
        word = "Arrow" + word
    result = word + result
    return result

def set_interval(update, millis: float) -> None:
    global playing
    playing = True
    clock = pygame.time.Clock()
    while playing:
        for e in pygame.event.get():
            # print(e)
            if e.type == pygame.QUIT:
                pygame.quit()
                playing = False
                return
            elif e.type == pygame.KEYDOWN and onkeydown:
                onkeydown(web_key(e.key))
            elif e.type == pygame.KEYUP and onkeyup:
                onkeyup(web_key(e.key))
        update()
        pygame.display.flip()
        clock.tick(1000/millis)
     
def clear_interval(timer=None):
    global playing
    playing = False
