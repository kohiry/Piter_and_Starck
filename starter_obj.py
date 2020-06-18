import object
from pygame.sprite import Group
from settings import BACK_SIZE
from level import level1


group_draw = Group()


HERO = object.Player(10, 10)
platforms = []
x_hero, y_hero = 0, 0


def make_level(level):
    x, y = 0, 0
    lens = 43
    #width =
    for row in level:
        for col in row:
            if col == '-':
                pl = object.Platform(x, y, lens, lens)
                group_draw.add(pl)
                platforms.append(pl)
            if col == '@':
                HERO.new_coord(x, y)
            if col == '1':
                group_draw.add(object.Background(x, y, 'data/фоны/начало.png'))
                pl = object.Platform(x, y, lens, lens)
                group_draw.add(pl)
                platforms.append(pl)
            if col == '2':
                group_draw.add(object.Background(x, y, 'data/фоны/горизонталь_1.png'))
                pl = object.Platform(x, y, lens, lens)
                group_draw.add(pl)
                platforms.append(pl)
            x += lens
        y += lens
        x = 0

make_level(level1)
group_draw.add(HERO)
