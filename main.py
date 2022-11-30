import pygame
import sys
import random
# import threading

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREY = pygame.Color(150, 150, 150)

game_status = False


pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Game")
background = pygame.image.load('background.png')

screen.fill(background)

while True:
    for event in pygame.event.get():
        if not game_status:
            game_status = True
            # codes

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    '''
    background = [terrain1, terrain1, terrain2, terrain2, terrain2, terrain1]
    screen = create_graphics_screen()
    for i in range(6):
        screen.blit(background[i], (i*10, 0))
    playerpos = 3
    screen.blit(playerimage, (playerpos*10, 0))
    '''
    pygame.display.update()

# END
