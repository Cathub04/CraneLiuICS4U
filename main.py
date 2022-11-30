import pygame
import sys
import threading

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREY = pygame.Color(150, 150, 150)
character = pygame.

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Game")

screen.fill(BLACK)
def start()
class scene:

while True:
    for event in pygame.event.get():
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
