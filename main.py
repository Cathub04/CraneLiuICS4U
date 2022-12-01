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
background = pygame.image.load('./src/background.jpeg').convert()
background2 = 0
background3 = background.get_width()
background = pygame.transform.scale(background, [screen_width, screen_height])
clock = pygame.time.Clock()

FONT = pygame.font.SysFont("monospace", 50)
character = [[], []]
for i in range(10):
    character[0].append(pygame.image.load(("./src/run" + str(i + 1) + ".png")))
for i in range(8):
    character[1].append(pygame.image.load(("./src/jump" + str(i + 1) + ".png")))
    character[1][i] = pygame.transform.scale_by(character[1][i], 0.5)
text_start = FONT.render("Press any key to start >>>", False, WHITE, None)

# Enemy
e1 = pygame.image.load('./src/purpmon.png')
e2 = pygame.image.load('./src/pinkmon.png')
enemy = [e1, e2]
for i in range(len(enemy)):
    enemy[i] = pygame.transform.scale(enemy[i], [120, 120])
e_ran = 0
e_change = 0


# Timer
game_status = False
r_time = 0
run_status = False
j_time = 0
old_j_time = 0
j_change = 0
e_time = 0
looph = 530
v_change = 0
# time = 0
# time_status = False


# Functions
def add_enemy():
    global e_ran, e_change, e_time, r_time, looph, v_change
    e_timer = Timer(0.025, add_enemy)
    e_timer.start()
    if e_change == 0:
        e_ran = random.randrange(2)
    if e_change < -screen_width:
        e_change = 0
    else:
        e_change -= 15
    if looph < 350:
        v_change += 15
    elif looph >= 530:
        v_change -= 15
    looph += v_change
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


def jump():
    global j_time, run_status, old_j_time, j_change
    j_timer = Timer(0.025, jump)
    j_timer.start()
    if j_time - old_j_time == 32:
        run_status = True
        j_timer.cancel()
        old_j_time = j_time
        run()
        return
    if j_time % 32 < 16:
        j_change -= 20
    else:
        j_change += 20
    j_time += 1


def is_coincide(p1, p2, p1cell, p2cell):
    # a.down >= b.top and a.top <= b.down and a.left <= b.right and a.right >= left
    if p1[0] + p1cell < p2[0] or p1[0] > p2[0] + p2cell or p1[1] > p2[1] + p2cell or p1[1] + p1cell < p2[1]:
        return False
    else:
        return True


def backgroundwin():
    screen.blit(background, (background2, 0))
    screen.blit(background, (background3, 0))
    pygame.display.update()


screen.blit(background, [0, 0])
screen.blit(text_start, [200, 100])

# Main loop
speed = 10
back = True
while True:
    backgroundwin()
    clock.tick(speed)
    background2 -= 1.4
    background3 -= 1.4
    if background2 < background.get_width()*-1:
        background2 = background.get_width()
    if background3 < background.get_width()*-1:
        background3 = background.get_width()

    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if not game_status:
                game_status = True
                time_status = True
                run_status = True
                run()
                add_enemy()

            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                if run_status:
                    run_status = False
                    jump()

        key = pygame.key.get_pressed()
        if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
            time_status = False
            run_status = False
            pygame.quit()
            sys.exit()

    screen.blit(background, [0, 0])
    if game_status:
        if not run_status:
            screen.blit(character[1][j_time % 8], [500, 420 + j_change])
        else:
            screen.blit(character[0][r_time % 10], [500, 420])
        screen.blit(enemy[e_ran], [1050 + e_change, looph])
    else:
        screen.blit(text_start, [200, 100])

    pygame.display.update()
# END
