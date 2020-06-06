import pygame
pygame.init()
import starter_obj
import random
from screeninfo import get_monitors


#size = width, height = starter_obj.width_window, starter_obj.height_window
size = width, height = 1000, 1000
#screen = pygame.display.set_mode(size)
screen = pygame.display.set_mode((0, 0), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
pygame.display.set_caption('Gay game')

White = (255, 255, 255)
Black = (0, 0, 0)
menu = -1

attack = False
my_font = "pixle_font.ttf"


def AI():
    for i in starter_obj.enemys:
        i.AI(starter_obj.hero)

def spider_check(screen):  # паучье чутьё
    around = 200
    max_len = 500
    for enemy in starter_obj.enemys:
        if max_len >= abs(enemy.xy[0] - starter_obj.hero.xy[0]) >= around:
            starter_obj.hero.check(screen)
            break


def camera():
    pass


def draw():
    global running
    #menu(screen, width, height, my_font)  # типо меню
    if menu == 1:
        running = starter_obj.exit_menu.draw(screen, starter_obj.click)
    else:
        starter_obj.background.draw(screen, width)
        if attack:
            for i in starter_obj.bullets:  #отрисовка всех болл-паутин
                i.draw(screen)
        starter_obj.hero.draw(screen)
        for i in starter_obj.enemys:
            i.draw(screen)
            if i.hp <= 0:
                starter_obj.enemys.pop(starter_obj.enemys.index(i))
        spider_check(screen)  # запускает паучье чутьё


running = True
while running:
    #starter_obj.enemy.damages = False
    pygame.time.Clock().tick(60)
    pygame.mouse.set_visible(True)  # скрывает мышь

    AI()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:  # создание новой болл-паутины
                if starter_obj.attack_ball():
                    attack = True
            if event.key == pygame.K_e:  #создаём врагов для отладки
                starter_obj.enemy_add(width)
            if event.key == pygame.K_SPACE:
                if not starter_obj.is_jump:
                    starter_obj.is_jump = True
            if event.key == pygame.K_ESCAPE:  #создаём врагов для отладки
                menu *= -1


        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if menu == 1:
                    if starter_obj.exit_menu.rect().collidepoint(event.pos):
                        starter_obj.click = True
                else:
                    if starter_obj.attack_ball():
                        attack = True


    keys = pygame.key.get_pressed()  # движения персонажей под зажим\

    if keys[pygame.K_a] or keys[pygame.K_RIGHT] or keys[pygame.K_LEFT] or keys[pygame.K_d]:
        starter_obj.hero.action = True
    else:
        starter_obj.hero.action = False

    if keys[pygame.K_a] and starter_obj.hero.xy[0] > 0 and keys[pygame.K_SPACE]:  #pygame.K_LEFT
        if not starter_obj.is_jump:
            starter_obj.is_jump = True
        starter_obj.hero.move_x_a()  # при зажиме прыжок идёт с движение

    elif keys[pygame.K_LEFT] and starter_obj.hero.xy[0] > 0 and keys[pygame.K_SPACE]:  #pygame.K_LEFT
        if not starter_obj.is_jump:
            starter_obj.is_jump = True
        starter_obj.hero.move_x_a()  # при зажиме прыжок идёт с движение

    if keys[pygame.K_a] and starter_obj.hero.xy[0] > 0:
        starter_obj.hero.move_x_a()  #границы джвижения

    elif keys[pygame.K_LEFT] and starter_obj.hero.xy[0] > 0:
        starter_obj.hero.move_x_a()  #границы джвижения

    if keys[pygame.K_d] and starter_obj.hero.xy[0] < width - starter_obj.hero.width and keys[pygame.K_SPACE]:
        starter_obj.hero.move_x_d()
        if not starter_obj.is_jump:
            starter_obj.is_jump = True   # при зажиме прыжок идёт с движение

    elif keys[pygame.K_RIGHT] and starter_obj.hero.xy[0] < width - starter_obj.hero.width and keys[pygame.K_SPACE]:
        starter_obj.hero.move_x_d()
        if not starter_obj.is_jump:
            starter_obj.is_jump = True   # при зажиме прыжок идёт с движение

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

    if starter_obj.is_jump:  #реализация прыжка
        if starter_obj.hero.jump() == 'End':
            starter_obj.is_jump = False

    screen.fill(Black)
    camera()
    draw()
    pygame.display.flip()

pygame.quit()

# иногда реально ненавижу git hub, снова для нового коммита
