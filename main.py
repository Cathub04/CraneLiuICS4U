import pygame
import sys
# import threading

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREY = pygame.Color(150, 150, 150)

game_status = False

pygame.init()

screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Game")
background = pygame.image.load('./src/background.jpeg')
background = pygame.transform.scale(background, [screen_width, screen_height])

screen.blit(background, [0, 0])

while True:
    for event in pygame.event.get():
        if not game_status:
            game_status = True
            # codes

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

# END
