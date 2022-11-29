import pygame
import sys
# import threading

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREY = pygame.Color(150, 150, 150)

game_status = False


pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Game")

screen.fill(BLACK)
def start()
class scene:

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
