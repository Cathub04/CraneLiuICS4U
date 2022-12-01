import pygame
import sys
import random
from threading import Timer
from pygame import mixer
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
background = [pygame.image.load('./src/bg.jpeg'), pygame.image.load('./src/bg.jpeg')]
for i in range(len(background)):
    background[i] = pygame.transform.scale(background[i], [screen_width, screen_height])
clock = pygame.time.Clock()

FONT = pygame.font.SysFont("monospace", 50)
character = [[], []]
for i in range(10):
    character[0].append(pygame.image.load(("./src/run" + str(i + 1) + ".png")))
for i in range(8):
    character[1].append(pygame.image.load(("./src/jump" + str(i + 1) + ".png")))
    character[1][i] = pygame.transform.scale_by(character[1][i], 0.5)
text_start = FONT.render("Press any key to start >>>", False, WHITE, None)


#music
mixer.init()
mixer.music.load('./src/music.mp3')
mixer.music.play()

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
bg_change = 0
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
    if looph < 250:
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


def is_collide(p1, p2, p1pos, p2pos):
    # (surface1, surface2, [x, y], [x, y])
    #   p1.left  > p2.right                       p1.right < p2.left
    if (p1pos[0] > p2pos[0] + p2.get_width()) or (p1pos[0] + p1.get_width() < p2pos[0]) \
            or (p1pos[1] + p1.get_height() < p2pos[1]) or (p1pos[1] > p2pos[1] + p2.get_height()):
        #       p1.down < p2.top                           p1.top > p2.down
        return False
    else:
        return True


def scroll_bg():
    global bg_change
    s_timer = Timer(0.01, scroll_bg)
    s_timer.start()
    bg_change -= 3
    if bg_change == -screen_width:
        bg_change = 0
    if not game_status:
        s_timer.cancel()
        return


screen.blit(background[0], [0, 0])
screen.blit(text_start, [200, 100])

# Main loop

while True:
    pygame.time.Clock().tick(45)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if not game_status:
                game_status = True
                time_status = True
                run_status = True
                run()
                add_enemy()
                scroll_bg()

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

    screen.blit(background[0], [0 + bg_change, 0])
    screen.blit(background[1], [screen_width + bg_change, 0])
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
