import pygame
pygame.init()
from screeninfo import get_monitors
from settings import WIDTH, HEIGHT, SIZE, SIDE, UP
from settings import GREEN
from starter_obj import group_draw, HERO, platforms


#size = width, height = 500, 500
#window = pygame.display.set_mode(size)
window = pygame.display.set_mode((0, 0), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
screen = pygame.Surface(SIZE)
#screen = pygame.Surface((400, 400))
pygame.display.set_caption('Gay game')


def draw():
    screen.fill(GREEN)
    group_draw.draw(screen)
    window.blit(screen, ((int(get_monitors()[0].width) - WIDTH) // 2, (int(get_monitors()[0].height) - HEIGHT) // 2))


running = True
while running:
    #starter_obj.enemy.damages = False

    pygame.mouse.set_visible(True)  # скрывает мышь
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()  # движения персонажей под зажим\
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_SPACE]:
        UP = True
    else:
        UP = False
    if keys[pygame.K_a]:
        SIDE = -1
    elif keys[pygame.K_d]:
        SIDE = 1
    else:
        SIDE = 0
    HERO.update(SIDE, UP, platforms)
    draw()
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()

# иногда реально ненавижу git hub, снова для нового коммита
