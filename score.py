import pygame
from setting import *

class Score:
    
    def __init__ (self, red, blue):
        self.red = red
        self.blue = blue
        self.font = pygame.font.SysFont('Arial', 40)
        self.redscore = self.font.render(str(self.red), True, RED)
        self.bluescore = self.font.render(str(self.blue), True, BLUE)
    
    def update (self, red, blue):
        self.red += red
        self.blue += blue
        self.redscore = self.font.render(str(self.red), True, RED)
        self.bluescore = self.font.render(str(self.blue), True, BLUE)

    def draw(self, surface):
        w = self.redscore.get_width()
        h = self.redscore.get_height()
        surface.blit(self.redscore, ((200-w)//2,(WINDOW_HEIGHT-h)//2))
        w = self.bluescore.get_width()
        h = self.bluescore.get_height()
        surface.blit(self.bluescore, (800 + (200-w)//2,(WINDOW_HEIGHT-h)//2))