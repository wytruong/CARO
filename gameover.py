import pygame
from setting import *

class GameOver:
    def __init__ (self, player):
        
        self.font = pygame.font.SysFont("Arial", 30)
        if player == 1: 
            color = RED
            winner = 'RED' 
        else: 
            color = BLUE
            winner = 'BLUE' 
        self.text = self.font.render(winner + ' win! press R to restart', True, color, WHITE)
        self.width = self.text.get_width()
        self.height = self.text.get_height()

    def draw(self,surface):
        surface.blit(self.text,((WINDOW_WIDTH-self.width) // 2,(WINDOW_HEIGHT - self.height) // 2))