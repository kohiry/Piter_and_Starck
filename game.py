import pygame
pygame.init()
import starter_obj
import random
from screeninfo import get_monitors
import menu
import special_action


size = width, height = 900, 500
#size = width, height = get_monitors()[0].width, get_monitors()[0].height
screen = pygame.display.set_mode(size)
#screen = pygame.display.set_mode((0, 0), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
pygame.display.set_caption('Gay game')

White = (255, 255, 255)
Black = (0, 0, 0)
is_jump = False
attack = False
my_font = "pixle_font.ttf"

def draw():
    menu.main(screen, width, height, my_font)
    if attack:
        for i in starter_obj.bullets:  #отрисовка всех болл-паутин
            i.draw(screen)
    starter_obj.hero.draw(screen)
    for i in starter_obj.enemys:
        i.draw(screen)
        if i.hp <= 0:
            starter_obj.enemys.pop(starter_obj.enemys.index(i))
    pygame.draw.line(screen, Black, (0, 390),  (width, 390), 2)
    special_action.spider_check(screen)  # запускает паучье чутьё


running = True
while running:
    #starter_obj.enemy.damages = False
    pygame.time.Clock().tick(60)
    pygame.mouse.set_visible(True)  # скрывает мышь

    special_action.AI()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:  # создание новой болл-паутины
                if starter_obj.attack_ball():
                    attack = True
            if event.key == pygame.K_e:  #создаём врагов для отладки
                starter_obj.enemy_add(width)


        elif event.type == pygame.MOUSEBUTTONDOWN:
             if event.button == 1:
                 if starter_obj.attack_ball():
                     attack = True



    keys = pygame.key.get_pressed()  # движения персонажей под зажим

    if keys[pygame.K_a] and starter_obj.hero.xy[0] > 0 and keys[pygame.K_SPACE]:  #pygame.K_LEFT
        if not is_jump:
            is_jump = True
        starter_obj.hero.move_x_a()  # при зажиме прыжок идёт с движение

    elif keys[pygame.K_LEFT] and starter_obj.hero.xy[0] > 0 and keys[pygame.K_SPACE]:  #pygame.K_LEFT
        if not is_jump:
            is_jump = True
        starter_obj.hero.move_x_a()  # при зажиме прыжок идёт с движение

    if keys[pygame.K_a] and starter_obj.hero.xy[0] > 0:
        starter_obj.hero.move_x_a()  #границы джвижения

    elif keys[pygame.K_LEFT] and starter_obj.hero.xy[0] > 0:
        starter_obj.hero.move_x_a()  #границы джвижения

    if keys[pygame.K_d] and starter_obj.hero.xy[0] < width - starter_obj.hero.width and keys[pygame.K_SPACE]:
        starter_obj.hero.move_x_d()
        if not is_jump:
            is_jump = True   # при зажиме прыжок идёт с движение

    elif keys[pygame.K_RIGHT] and starter_obj.hero.xy[0] < width - starter_obj.hero.width and keys[pygame.K_SPACE]:
        starter_obj.hero.move_x_d()
        if not is_jump:
            is_jump = True   # при зажиме прыжок идёт с движение

    if keys[pygame.K_d] and starter_obj.hero.xy[0] < width - starter_obj.hero.width:
        starter_obj.hero.move_x_d() #границы джвижения

    elif keys[pygame.K_RIGHT] and starter_obj.hero.xy[0] < width - starter_obj.hero.width:
        starter_obj.hero.move_x_d() #границы джвижения

    if attack:  # движение болл-паутины
        for i in starter_obj.bullets:
            if 0 < i.xy[0] < width:
                i.move()
            else:
                starter_obj.bullets.pop(starter_obj.bullets.index(i))
            if len(starter_obj.enemys) > 0:
                for j in starter_obj.enemys:
                    if i.rect().colliderect(j.rect()):  #проверка соприкосновения патрона и врага
                        j.damages = True
                        try:
                            starter_obj.bullets.pop(starter_obj.bullets.index(i))
                        except ValueError:
                            continue

    if keys[pygame.K_SPACE]:  #реакция на нажатие пробела
        if not is_jump:
            is_jump = True

    if is_jump:  #реализация прыжка
        if starter_obj.hero.jump() == 'End':
            is_jump = False

    screen.fill(White)
    draw()
    pygame.display.flip()

pygame.quit()

# иногда реально ненавижу git hub, снова для нового коммита
