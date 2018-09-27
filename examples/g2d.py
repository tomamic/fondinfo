#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html

@link    https://www.brython.info/static_doc/en/intro.html
@link    https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API
'''

try:
    import pygame
except:
    import subprocess, sys
    subprocess.call([sys.executable, "-m", "pip", "install", "pygame"])
    import pygame

import sys
from tkinter import Tk, messagebox, simpledialog

_tkmain = Tk()
_tkmain.wm_withdraw() #to hide the main window

_canvas = None
_keydown, _keyup = None, None
_mousedown, _mouseup = None, None

def init_canvas(size: (int, int)):
    '''Set size of first CANVAS and return it'''
    global _canvas
    pygame.init()
    _canvas = pygame.display.set_mode(size)
    _canvas.fill((255, 255, 255))

def fill_canvas(color: (int, int, int)) -> None:
    _canvas.fill(color)

def update_canvas() -> None:
    pygame.display.update()

def draw_line(color: (int, int, int), pt1: (int, int), pt2: (int, int)) -> None:
    pygame.draw.line(_canvas, color, pt1, pt2)

def draw_circle(color: (int, int, int), center: (int, int), radius: int) -> None:
    pygame.draw.circle(_canvas, color, center, radius)

def draw_rect(color: (int, int, int), rectangle: (int, int, int, int)) -> None:
    pygame.draw.rect(_canvas, color, rectangle)

def draw_text(txt: str, color: (int, int, int), pos: (int, int), size: int) -> None:
    font = pygame.font.SysFont('freesansbold', size)
    surface = font.render(txt, True, color) ##, (255, 255, 255))
    _canvas.blit(surface, pos)

def draw_text_centered(txt: str, color: (int, int, int), pos: (int, int), size: int) -> None:
    font = pygame.font.SysFont('freesansbold', size)
    surface = font.render(txt, True, color) ##, (255, 255, 255))
    w, h = surface.get_size()
    _canvas.blit(surface, (pos[0] - w // 2, pos[1] - h // 2))

def load_image(url: str) -> pygame.Surface:
    return pygame.image.load(url)

def draw_image(image: pygame.Surface, pos: (int, int)) -> None:
    _canvas.blit(image, pos)

def draw_image_clip(image: pygame.Surface, rect: (int, int, int, int), area: (int, int, int, int)) -> None:
    x0, y0, w0, h0 = area
    x1, y1, w1, h1 = rect
    if w0 == w1 and h0 == h1:
        _canvas.blit(image, rect, area=area)
    else:
        cropped = pygame.Surface((w0, h0), pygame.SRCALPHA)
        cropped.blit(image, (0, 0), area=area)
        scaled = pygame.transform.smoothscale(cropped, (w1, h1))
        _canvas.blit(scaled, (x1, y1))

def load_audio(url: str) -> pygame.mixer.Sound:
    return pygame.mixer.Sound(url)
    
def play_audio(audio: pygame.mixer.Sound, loop=False) -> None:
    audio.play(-1 if loop else 0)
    
def pause_audio(audio: pygame.mixer.Sound) -> None:
    audio.stop()

def alert(message: str) -> None:
    messagebox.showinfo(" ", message)

def confirm(message: str) -> bool:
    return messagebox.askokcancel(" ", message)

def prompt(message: str) -> str:
    return simpledialog.askstring(" ", message, parent=_tkmain)

def handle_keyboard(keydown, keyup):
    global _keydown, _keyup
    _keydown, _keyup = keydown, keyup

def handle_mouse(mousedown, mouseup):
    global _mousedown, _mouseup
    _mousedown, _mouseup = mousedown, mouseup

def web_key(key: int) -> str:
    word = pygame.key.name(key)
    word = word[0].upper() + word[1:]
    if len(word) == 1 and word.isalpha():
        word = "Key" + word
    elif len(word) == 1 and word.isdigit():
        word = "Digit" + word
    elif word in ("Up", "Down", "Right", "Left"):
        word = "Arrow" + word
    return word

def main_loop(update=None, millis=100) -> None:
    clock = pygame.time.Clock()
    while True:
        for e in pygame.event.get():
            # print(e)
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYDOWN and _keydown:
                _keydown(web_key(e.key))
            elif e.type == pygame.KEYUP and _keyup:
                _keyup(web_key(e.key))
            elif e.type == pygame.MOUSEBUTTONDOWN and _mousedown:
                _mousedown(e.pos, e.button - 1)
            elif e.type == pygame.MOUSEBUTTONUP and _mouseup:
                _mouseup(e.pos, e.button - 1)
        if update:
            update()
        pygame.display.flip()
        clock.tick(1000/millis)
    exit()

def exit() -> None:
    pygame.quit()
    sys.exit()
