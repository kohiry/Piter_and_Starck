import pygame
import classes
import random

"_____________________________________________"
bullets = []
enemys = []
"_____________________________________________"
xy = [1, 330]
width = 60
height = 60
speed = 11
hero = classes.Hero(xy, width, height, speed)
"_____________________________________________"

def enemy_add(width):
    xy = [random.randint(1, width), 320]
    width_enemy = 60
    height = 70
    speed = 5
    enemys.append(classes.Enemy(xy, width_enemy, height, speed))

"_____________________________________________"

def attack_ball():  # выстрел
    speed_ball = 20
    x_ball = hero.xy[0] + hero.width//2
    y_ball = hero.xy[1] + hero.height//2
    bullets.append(classes.Attack([x_ball, y_ball], hero.width//4, speed_ball, hero.front))
    return True

"_____________________________________________"
#([500, 330], 60, 60, 8)
