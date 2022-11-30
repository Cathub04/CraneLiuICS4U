import pygame
import sys
from threading import Timer
# import func

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREY = pygame.Color(150, 150, 150)

pygame.init()

# Preparation
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Game")
background = pygame.image.load('./src/background.jpeg')
background = pygame.transform.scale(background, [screen_width, screen_height])
FONT = pygame.font.SysFont("monospace", 100)
character = []
for i in range(1, 11):
    character.append(pygame.image.load(("./src/run" + str(i) + ".png")))
# print(character)

# Timer
r_time = 0
game_status = False
time = 0
time_status = True


# Functions
def set_timer():
    global time, time_status
    s_timer = Timer(0.0165, set_timer)
    s_timer.start()
    if not time_status:
        s_timer.cancel()
        return
    time += 1


def run():
    global r_time
    r_timer = Timer(0.07, run)
    r_timer.start()
    screen.blit(background, [0, 0])
    screen.blit(character[r_time % 10], [400, 400])
    if not time_status:
        r_timer.cancel()
        return
    r_time += 1


screen.blit(background, [0, 0])
run()

# Main loop
while True:
    pygame.time.Clock().tick(10)
    for event in pygame.event.get():
        if not game_status:
            game_status = True
            # codes

        if event.type == pygame.QUIT:
            time_status = False
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
