import pygame
import sys
import random
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
FONT = pygame.font.SysFont("monospace", 50)
character = []
for i in range(10):
    character.append(pygame.image.load(("./src/run" + str(i + 1) + ".png")))
text_start = FONT.render("Press any key to start >>>", False, WHITE, None)

# Enemy
e1 = pygame.image.load('./src/purpmon.png')
e2 = pygame.image.load('./src/pinkmon.png')
enemy = [e1, e2]
for i in range(len(enemy)):
    enemy[i] = pygame.transform.scale(enemy[i], [100, 100])
e_ran = 0
e_change = 0


# Timer
r_time = 0
game_status = False
time = 0
time_status = False


# Functions
def add_enemy(t):
    global e_ran, e_change
    if e_change == 0:
        e_ran = random.randrange(2)
    if t * 100 / 7 / 3 > 0:
        screen.blit(enemy[e_ran], [1200 + e_change, 530])
    if e_change < -1200:
        e_change = 0
    else:
        e_change -= 30


def run():
    global r_time
    r_timer = Timer(0.07, run)
    r_timer.start()
    screen.blit(background, [0, 0])
    screen.blit(character[r_time % 10], [500, 420])
    add_enemy(r_time)
    if not time_status:
        r_timer.cancel()
        return
    r_time += 1


screen.blit(background, [0, 0])
screen.blit(text_start, [200, 100])

# Main loop
while True:
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if not game_status:
                game_status = True
                time_status = True
                run()
                # codes

        key = pygame.key.get_pressed()
        if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
            time_status = False
            pygame.quit()
            sys.exit()
    pygame.display.update()
# END
