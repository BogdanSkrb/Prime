import pygame as pg
import random

from objects.abs_objects import GameObject

class Being(GameObject):
    image_path = r'beings\human_being.png'

    def __init__(self, screen):
        super().__init__(screen)
        self._rect.x = random.choice([int(i) for i in range(0, self._screen.width, 10)])
        self._rect.y = random.choice([int(i) for i in range(0, self._screen.height, 10)])
