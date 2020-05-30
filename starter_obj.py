import pygame
import classes
import random
import sprites

"_____________________________________________"
width_window = 700
height_window = 700
background = sprites.Background(width_window, height_window)  #все фоны
"_____________________________________________"
bullets = []
enemys = []
"_____________________________________________"
width_h = 200
height_h = 200
speed = 11
is_jump = False
xy = [1, height_window - int(height_h + 120)]  #320
hero = classes.Hero(xy, width_h, height_h, speed)
"_____________________________________________"

def enemy_add(width_en):
    width_enemy = 60
    height_enemy = 70
    xy = [random.randint(1, width_en), height_window - int(height_enemy*3.12)]
    speed = 5
    enemys.append(classes.Enemy(xy, width_enemy, height_enemy, speed))

"_____________________________________________"

def attack_ball():  # выстрел
    speed_ball = 20
    x_ball = hero.xy[0] + hero.width//2
    y_ball = hero.xy[1] + hero.height//2
    bullets.append(classes.Attack([x_ball, y_ball], hero.width//15, speed_ball, hero.front))
    return True
