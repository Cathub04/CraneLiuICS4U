import pygame
import sys

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREY = pygame.Color(150, 150, 150)

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Game")

screen.fill(BLACK)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

# END
