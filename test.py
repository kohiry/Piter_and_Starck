import pygame
pygame.init()
import starter_obj
from screeninfo import get_monitors


size = width, height = 900, 500
#size = width, height = get_monitors()[0].width, get_monitors()[0].height
screen = pygame.display.set_mode(size)
#screen = pygame.display.set_mode((0, 0), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
pygame.display.set_caption('Gay game')

White = (255, 255, 255)
Black = (0, 0, 0)
is_jump = False
attack = False

def draw():
    if attack:
        for i in starter_obj.bullets:  #отрисовка всех болл-паутин
            i.draw(screen)
    starter_obj.hero.draw(screen)
    pygame.draw.line(screen, Black, (0, 390),  (width, 390), 2)


running = True
while running:
    pygame.time.Clock().tick(60)
    pygame.mouse.set_visible(True)  # скрывает мышь
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:  # создание новой болл-паутины
                if len(starter_obj.bullets) < 4:
                    speed_ball = 15
                    x_ball = starter_obj.hero.xy[0] + starter_obj.hero.width//2
                    y_ball = starter_obj.hero.xy[1] + starter_obj.hero.height//2
                    starter_obj.bullets.append(starter_obj.attack_ball([x_ball, y_ball], starter_obj.hero.width//4, speed_ball, starter_obj.hero.front))
                    attack = True

    keys = pygame.key.get_pressed()  # движения персонажей под зажим

    if keys[pygame.K_a] and starter_obj.hero.xy[0] > 0 and keys[pygame.K_SPACE]:
        if not is_jump:
            is_jump = True
        starter_obj.hero.move_x_a()  # при зажиме прыжок идёт с движение
    if keys[pygame.K_a] and starter_obj.hero.xy[0] > 0:
        starter_obj.hero.move_x_a()  #границы джвижения

    if keys[pygame.K_d] and starter_obj.hero.xy[0] < width - starter_obj.hero.width and keys[pygame.K_SPACE]:
        starter_obj.hero.move_x_d()
        if not is_jump:
            is_jump = True   # при зажиме прыжок идёт с движение
    if keys[pygame.K_d] and starter_obj.hero.xy[0] < width - starter_obj.hero.width:
        starter_obj.hero.move_x_d() #границы джвижения

    if attack:  # движение болл-паутины
        for i in starter_obj.bullets:
            if 0 < i.xy[0] < width:
                i.move()
            else:
                starter_obj.bullets.pop(starter_obj.bullets.index(i))

    if keys[pygame.K_SPACE]:  #реакция на нажатие пробела
        if not is_jump:
            is_jump = True
    if is_jump:  #реализация прыжка
        if starter_obj.hero.jump() == 'End':
            is_jump = False
        pygame.time.Clock().tick(60)

    screen.fill(White)
    draw()
    pygame.display.flip()

pygame.quit()

# иногда реально ненавижу git hub, снова для нового коммита
