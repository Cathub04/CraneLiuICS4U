import pygame
import sys
import random
from threading import Timer
from pygame import mixer

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREY = pygame.Color(150, 150, 150)

pygame.init()

# Preparation
screen_width = 1200
screen_height = 600
level = 500
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
    character[0][i] = pygame.transform.scale_by(character[0][i], 0.65)
for i in range(8):
    character[1].append(pygame.image.load(("./src/jump" + str(i + 1) + ".png")))
    character[1][i] = pygame.transform.scale_by(character[1][i], 0.30)
text_start = FONT.render("Press Space to start >>>", False, BLACK, None)
text_end1 = FONT.render("You die...", False, BLACK, None)
text_end2 = FONT.render("Press return to restart >>>", False, BLACK, None)
heart = 3
hearticon = pygame.transform.scale_by(pygame.image.load("./src/heart.png"), 0.5)
score = 0
score_count = False
bar = pygame.transform.scale_by(pygame.image.load("./src/bar.png"), 1)

# shield_light = pygame.transform.scale(pygame.image.load("./src/light.png"),
#                                       [character[0][0].get_height(), character[0][0].get_height()])
# prop = []
# prop.append(pygame.image.load("./src/light.png"))


# Music
mixer.init()
mixer.music.load('./src/music.mp3')
mixer.music.play()
mixer.music.set_volume(0.2)
jumpsound = pygame.mixer.Sound('./src/jumpsound.mp3')
monstersound = pygame.mixer.Sound('./src/monstersound.mp3')
monstersound.set_volume(0.7)
jumpsound.set_volume(2.5)


# Enemy
e1 = pygame.image.load('./src/slime1.png')
e2 = pygame.image.load('./src/slime2.png')
enemy = [e1, e2]
for i in range(len(enemy)):
    enemy[i] = pygame.transform.scale(enemy[i], [100, 100])
e_ran = 0
e_change = 0


# Timer & status & change
game_status = False
r_time = 0
run_status = False
j_time = 0
old_j_time = 0
j_change = 0
e_time = 0
looph = level - enemy[e_ran].get_height()
v_change = 0
bg_change = 0


# Functions
def add_enemy():
    global e_ran, e_change, e_time, r_time, looph, v_change, score, score_count
    e_timer = Timer(0.03, add_enemy)
    e_timer.start()
    if e_change == 0:
        e_ran = random.randrange(2)
    if e_change < -screen_width:
        e_change = 0
        score_count = False
    else:
        e_change -= 20

    if screen_width + e_change < 500 and not score_count:
        score += 100
        score_count = True

    if looph + enemy[e_ran].get_height() < level - 300:
        v_change += 15
    elif looph >= level - enemy[e_ran].get_height():
        v_change -= 15
        monstersound.play()

    looph += v_change
    if not game_status:
        e_timer.cancel()
        return


def run():
    global r_time, screen_width, looph, game_status, heart, e_ran, e_change
    r_timer = Timer(0.07, run)
    r_timer.start()
    if not run_status:
        r_timer.cancel()
        return
    r_time += 1
    if is_collide(character[0][r_time % 10], enemy[e_ran],
                  [500, level - character[0][r_time % 10].get_height()], [screen_width + e_change, looph], 25, 50):
        e_ran = random.randrange(2)
        e_change = 0
        heart -= 1
        return


def jump():
    global j_time, run_status, old_j_time, j_change, game_status, heart, e_ran, e_change
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
    if is_collide(character[1][j_time % 8], enemy[e_ran],
                  [500, level - character[1][j_time % 8].get_height() + j_change],
                  [screen_width + e_change, looph], 25, 50):
        e_ran = random.randrange(2)
        e_change = 0
        heart -= 1
        return


def is_collide(p1, p2, p1pos, p2pos, v_space, h_space):
    # (surface1, surface2, [x, y], [x, y])
    #   p1.left  > p2.right                       p1.right < p2.left
    if (p1pos[0] + v_space > p2pos[0] + p2.get_width()) or (p1pos[0] + p1.get_width() < p2pos[0] + v_space) \
            or (p1pos[1] + p1.get_height() < p2pos[1] + h_space) or (p1pos[1] + h_space > p2pos[1] + p2.get_height()):
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


def life():
    global heart, game_status
    if heart == 3:
        screen.blit(hearticon, [10, 10])
        screen.blit(hearticon, [110, 10])
        screen.blit(hearticon, [210, 10])
    elif heart == 2:
        screen.blit(hearticon, [10, 10])
        screen.blit(hearticon, [110, 10])
    elif heart == 1:
        screen.blit(hearticon, [10, 10])
    else:
        game_status = False


# def prop():
#     # p_ran = random.randrange
#

screen.blit(background[0], [0, 0])
screen.blit(text_start, [200, 100])

# Main loop

while True:
    pygame.time.Clock().tick(45)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and game_status:
                if run_status:
                    run_status = False
                    jump()
                    jumpsound.play()

            if not game_status:
                game_status = True
                time_status = True
                run_status = True
                run()
                add_enemy()
                scroll_bg()

        key = pygame.key.get_pressed()
        if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
            time_status = False
            run_status = False
            game_status = False
            pygame.quit()
            sys.exit()

    screen.blit(background[0], [0 + bg_change, 0])
    screen.blit(background[1], [screen_width + bg_change, 0])
    if game_status:
        if not run_status:
            screen.blit(character[1][j_time % 8], [500, level - character[1][j_time % 8].get_height() + j_change])
            # screen.blit(shield_light, [500 - 20, level - character[1][j_time % 8].get_height() + j_change - 20])
        else:
            screen.blit(character[0][r_time % 10], [500, level - character[0][r_time % 10].get_height()])
            # screen.blit(shield_light, [500, level - character[0][r_time % 10].get_height()])
        screen.blit(enemy[e_ran], [screen_width + e_change, looph+25])
        text_score = FONT.render(("Score: %d" % score), False, BLACK, None)
        screen.blit(text_score, [screen_width - text_score.get_width() - 20, 10])
    elif r_time == 0:
        screen.blit(text_start, [200, 100])
    else:
        screen.blit(text_end1, [200, 100])
        screen.blit(text_end2, [200, 170])

    screen.blit(bar, [(screen_width-bar.get_width())/2, level])
    life()
    pygame.display.update()


# END
