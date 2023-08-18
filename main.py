import pygame
from setting import *
from boardgame import Boardgame
from gameover import GameOver
from score import Score

# creat pygame window
pygame.init()

# properties of pygame window
screen = pygame.display.set_mode(WINDOW_SIZE)
# icon = pygame.image.load(ICON)
# pygame.display.set_icon(icon)
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()

gameStatus = 1
PLAYERSCORE = Score(0,0)

while gameStatus!=0:
    
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                gameStatus = 0 

    #init objects
    boardgame = Boardgame()
    playerMove = 1

    # screen gameplay
    running = True
    while running:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False 
                    gameStatus = 0
                case pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        playerMove = boardgame.move(playerMove)
        
        if (boardgame.over[0] == 1): 
            running = False
            if (boardgame.over[1] == 1):
                PLAYERSCORE.update(1,0)
            else: PLAYERSCORE.update(0,1)

        screen.fill(WHITE)

        #update game
        boardgame.draw(screen)
        PLAYERSCORE.draw(screen)

        pygame.display.flip()

        #set fps
        clock.tick(FPS)
    
    # screen gameover
    if (boardgame.over[0] != 0): 
        running = True
        Ev = GameOver(boardgame.over[1])

    while running:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False 
                    gameStatus = 0
                case pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        running = False 

        Ev.draw(screen)

        PLAYERSCORE.draw(screen)
        
        pygame.display.flip()
        
        #set fps
        clock.tick(FPS)
    

pygame.quit()