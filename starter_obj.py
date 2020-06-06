import pygame
import classes
import random


#sprite_hero = classes.Sprites_hero()
"_____________________________________________"
width_window = 500
height_window = 500
background = classes.Map(width_window, height_window, 10)  #все фоны
"_____________________________________________"
bullets = []
enemys = []
"_____________________________________________"
click = False
exit_menu = classes.Button(width_window // 2, height_window // 2, "Выход")
"_____________________________________________"
width_h = 50
height_h = 50
speed = 10
is_jump = False
xy = [1, height_window - int(height_h + 110)]  #320
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
