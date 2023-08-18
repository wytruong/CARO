import pygame
from setting import *

POINT = [[0,0], [1,0], [1,1], [0,1], [0,0]]

class Emptycell:

    def __init__(self, size, x, y, color):
        self.size = size
        self.x = x
        self.y = y
        self.color = color

    def draw(self,surface):
        x, y = pygame.mouse.get_pos()
        if (self.x < x and x < self.x + self.size and self.y < y and y < self.y + self.size):
            pygame.draw.rect(surface, LIGHT_GREEN, (self.x, self.y, self.size, self.size))

        for i in range(4):
            start = (self.x + self.size * POINT[i][0], self.y + self.size * POINT[i][1])
            end = (self.x + self.size * POINT[i+1][0], self.y + self.size * POINT[i+1][1])
            pygame.draw.line(surface, self.color, start, end)
    
    def fill(self, surface, color):
        pygame.draw.circle(surface, color, (self.x + self.size // 2, self.y + self.size // 2), self.size // 2 - 5)