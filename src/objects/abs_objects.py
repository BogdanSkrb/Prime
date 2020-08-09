import pygame as pg

from services.resources import ResourcesService

class GameObject:
    image_path = None

    def __init__(self, screen):
        self._screen = screen
        self._image = pg.image.load(ResourcesService(self.get_image_path()).path).convert_alpha()
        self._rect = self._image.get_rect()

    def get_image_path(self):
        if self.image_path is not None:
            return self.image_path
        raise ValueError('image_path is not set')

    def render(self):
        self._screen.blit(self._image, self._rect)