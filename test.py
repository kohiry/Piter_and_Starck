import pygame
pygame.init()
import starter_obj
from screeninfo import get_monitors


size = width, height = 800, 600
#size = width, height = get_monitors()[0].width, get_monitors()[0].height
screen = pygame.display.set_mode(size)
#screen = pygame.display.set_mode((0, 0), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
pygame.display.set_caption('Gay game')

White = (255, 255, 255)
Black = (0, 0, 0)
is_jump = False


def draw():
    pygame.time.Clock().tick(60)
    starter_obj.hero.draw(screen)
    pygame.draw.line(screen, Black, (0, 360),  (800, 360), 2)


running = True
while running:
    pygame.mouse.set_visible(True)  # скрывает мышь
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and starter_obj.hero.xy[0] > 0 and keys[pygame.K_SPACE]:
        if not is_jump:
            is_jump = True
        starter_obj.hero.move_x_a()
    if keys[pygame.K_a] and starter_obj.hero.xy[0] > 0:
        starter_obj.hero.move_x_a()

    if keys[pygame.K_d] and starter_obj.hero.xy[0] < width - starter_obj.hero.width and keys[pygame.K_SPACE]:
        starter_obj.hero.move_x_d()
        if not is_jump:
            is_jump = True
    if keys[pygame.K_d] and starter_obj.hero.xy[0] < width - starter_obj.hero.width:
        starter_obj.hero.move_x_d()

    if keys[pygame.K_SPACE]:
        if not is_jump:
            is_jump = True
    if is_jump:
        if starter_obj.hero.jump() == 'End':
            is_jump = False
        pygame.time.Clock().tick(60)

    screen.fill(White)
    draw()
    pygame.display.flip()

pygame.quit()

# иногда реально ненавижу git hub, снова для нового коммита
