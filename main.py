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
FONT = pygame.font.SysFont("monospace", 50)
character = []
for i in range(10):
    character.append(pygame.image.load(("./src/run" + str(i + 1) + ".png")))
text_start = FONT.render("Press any key to start >>>", False, WHITE, None)

e1 = pygame.image.load('./src/purpmon.png')
e2 = pygame.image.load('./src/pinkmon.png')
enemy = [e1,e2]


# Timer
r_time = 0
game_status = False
time = 0
time_status = False


# Functions
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


class nonplayer:

    def __init__(self,enemy,height,speed):
        self.enemy = enemy
        self.speed = speed
        self.pos = enemy.get_rect().move(0,height)
    def move(self):
        self.pos = self.movs.move(0,self.speed)
        if self.pos.right > 1200:
            self.pos.left = 0







def to_quit():
    global time_status
    time_status = False
    pygame.quit()
    sys.exit()


screen.blit(background, [0, 0])
screen.blit(text_start, [200, 100])

# Main loop
while True:
    pygame.time.Clock().tick(10)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if not game_status:
                game_status = True
                time_status = True
                run()
                # codes

            if event.key == pygame.K_ESCAPE:
                to_quit()

        if event.type == pygame.QUIT:
            to_quit()
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
