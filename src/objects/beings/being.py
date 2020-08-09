import pygame as pg

from services.resources import ResourcesService

class Being:
    def __init__(self, screen):
        self._screen = screen
        resources = ResourcesService(r'beings\human_being.png')
        self._image = pg.image.load(resources.path).convert_alpha()
        self._rect = self._image.get_rect()
        self._rect.x = 100
        self._rect.y = 200

    def render(self):
        self._screen.blit(self._image, self._rect)
