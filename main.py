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
    enemy[i] = pygame.transform.scale(enemy[i], [150, 150])
e_ran = 0
e_change = 0


# Timer
r_time = 0
game_status = False
e_time = 0
time = 0
time_status = False
run_status = False


# Functions
looph = 530
v_change= random.randint(-15,15)
def add_enemy():
    global e_ran, e_change, e_time, r_time
    e_timer = Timer(0.07, add_enemy)
    e_timer.start()
    if e_change == 0:
        e_ran = random.randrange(2)
    if e_change < -screen_width:
        e_change = 0
    else:
        e_change -= 30
    if not time_status:
        e_timer.cancel()
        return


def run():
    global r_time
    r_timer = Timer(0.07, run)
    r_timer.start()
    if not run_status:
        r_timer.cancel()
        return
    r_time += 1


def is_coincide(p1, p2, p1cell, p2cell):
    # a.down >= b.top or a.top <= b.down or a.left <= b.right or a.right >= left
    if p1[0] + p1cell < p2[0] or p1[0] > p2[0] + p2cell or p1[1] > p2[1] + p2cell or p1[1] + p1cell < p2[1]:
        return False
    else:
        return True


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
                run_status = True
                run()
                add_enemy()
                # codes
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                run_status = False

        key = pygame.key.get_pressed()
        if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
            time_status = False
            run_status = False
            pygame.quit()
            sys.exit()

    screen.blit(background, [0, 0])
    if game_status:
        screen.blit(character[r_time % 10], [500, 420])
        screen.blit(enemy[e_ran], [1200 + e_change, 530])
    else:
        screen.blit(text_start, [200, 100])

    pygame.display.update()
# END
