import pygame
from pygame.locals import *

import settings
from objects.beings import being


class Screen:
    def __init__(self):
        self.size = settings.WIDTH, settings.HEIGHT
        self._display = pygame.display.set_mode(
            self.size, 
            pygame.RESIZABLE
        )

    def blit(self, *args):
        return self._display.blit(*args)

    def fill(self):
        return self._display.fill((30, 30, 30))


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
 
    def on_init(self):
        pygame.init()
        self.screen = Screen()
        self._running = True

        self.object_list = [being.Being(self.screen)]
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    
    def on_loop(self):
        pass

    
    def on_render(self):
        self.screen.fill()
        for o in self.object_list:
            o.render()
        
        pygame.display.flip()
            


    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()