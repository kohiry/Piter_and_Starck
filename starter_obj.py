import pygame
import classes
import random
from screeninfo import get_monitors

"_____________________________________________"

#sprite_hero = classes.Sprites_hero()

"_____________________________________________"
width_window = 800
height_window = 800
background = classes.Map(width_window, height_window, 10)  #все фоны
"_____________________________________________"
bullets = []
enemys = []
"_____________________________________________"
click = False
exit_menu = classes.Button(get_monitors()[0].width // 2 - 100, get_monitors()[0].height // 2, "Выход")
"_____________________________________________"
width_h = 50
height_h = 50
speed = 10
is_jump = False
xy = [0, 550]  #320
hero = classes.Hero(xy, width_h, height_h, speed)
"_____________________________________________"

def enemy_add(width_en):
    width_enemy = 60
    height_enemy = 70
    xy = [random.randint(1, width_en), 410 - height_enemy]
    speed = 5
    enemys.append(classes.Enemy(xy, width_enemy, height_enemy, speed))

"_____________________________________________"

def attack_ball():  # выстрел
    speed_ball = 20
    x_ball = hero.xy[0] + hero.width//2
    y_ball = hero.xy[1] + hero.height//2
    bullets.append(classes.Attack([x_ball, y_ball], hero.width//5, speed_ball, hero.front))
    return True


"_____________________________________________"
blocks = []
blocks.append(classes.Platform(0, 650, 1000, 50))
"_____________________________________________"
