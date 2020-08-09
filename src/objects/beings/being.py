import pygame as pg


class Being:
    def __init__(self, screen):
        self._screen = screen

        self._image = pg.image.load(r'src\resources\beings\human_being.png').convert_alpha()
        self._rect = self._image.get_rect()
        self._rect.x = 100
        self._rect.y = 200

    def render(self):
        self._screen.blit(self._image, self._rect)
