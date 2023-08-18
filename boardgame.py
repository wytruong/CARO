import pygame
from setting import *
from emptycell import Emptycell

class Boardgame:

    def __init__ (self):
        self.width = 600
        self.height = 600
        self.size = 30
        self.x = 200
        self.y = 0
        self.board = []
        self.over = [0,0]
        self.prev = [-1,-1]
        for i in range(self.width // self.size):
            row = []
            for j in range(self.height // self.size):
                row.append(0)
            self.board.append(row)

    def draw(self, surface):

        if (self.prev[0] != -1):
            pygame.draw.rect(surface, GREEN, (self.x + self.size*self.prev[0], self.y + self.size * self.prev[1], self.size, self.size))
        
        for i in range(self.width // self.size):
            for j in range(self.height // self.size):
                cell = Emptycell(self.size, self.x + self.size*j, self.y + self.size*i, BLACK)
                cell.draw(surface)
                match self.board[i][j]:
                    case 1:
                        cell.fill(surface, RED)
                    case 2:
                        cell.fill(surface, BLUE)        

    def move(self, player):
        x, y = pygame.mouse.get_pos()
        x = (x - self.x) // self.size
        y = (y - self.y) // self.size
        if (0 <= x and x < self.width // self.size and 0 <= y and  y < self.height // self.size):
            if (self.board[y][x] == 0):
                self.board[y][x] = player
            self.prev = [x,y]
        self.checkWin(x,y,player)
        return (player % 2) + 1
            
    def checkWin(self, x, y, player):
        #check horizontal
        px = x 
        res = 0
        while (px>=0):
            if (self.board[y][px] == player):
                px -= 1
                res += 1
            else: break
        px = x + 1
        while (px< self.width // self.size):
            if (self.board[y][px] == player):
                px += 1
                res += 1
            else: break
        if (res>=5): 
            self.over = (1,player)
        #check vertical
        py = y
        res = 0
        while (py>=0):
            if (self.board[py][x] == player):
                py -= 1
                res += 1
            else: break
        py = y + 1
        while (py < self.height // self.size):
            if (self.board[py][x] == player):
                py += 1
                res += 1  
            else: break
        if (res>=5): 
            self.over = (1, player)