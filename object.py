from pygame.sprite import Sprite, collide_rect
from pygame.draw import rect
from pygame import Surface
from pygame.image import load
from pygame.transform import scale


SPEED = 20
GRAVITY = 2
JUMP_POWER = 5

class Enemy(Sprite):
    def __init__(self, x, y, width=50, height=50):
        Sprite.__init__(self)
        #self.image = load('data/паук/стоит/паук_стоит_направо_1.png')
        self.image = Surface((width, height))
        self.image.fill((0, 200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.yvel = 0
        self.xvel = 0
        self.onGround = False

    def new_coord(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self, left, right, up, platforms):

        # лево право
        if left:
            self.xvel = -SPEED
        if right:
            self.xvel = SPEED
        if not (left or right):
            self.xvel = 0

        # прыжок
        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

    def collide(self, xvel, yvel, platforms):
        for pl in platforms:
            if collide_rect(self, pl):
                #self.serf = True
                if yvel > 0:
                    self.onGround = True
                    self.rect.bottom = pl.rect.top
                if yvel < 0:
                    self.yvel = 0
                    self.rect.top = pl.rect.bottom
                if xvel < 0:
                    self.yvel = 0
                    self.rect.left = pl.rect.right
                if xvel > 0:
                    self.yvel = 0
                    self.rect.right = pl.rect.left

'''
    def AI(self, hero):
        if -100 < hero.x - self.x < 100:
            if -100 < hero.y - self.y < 100:
                if self.
                self.update
'''
class Player(Sprite):
    def __init__(self, x, y, width=50, height=50):
        Sprite.__init__(self)
        #self.image = load('data/паук/стоит/паук_стоит_направо_1.png')
        self.image = Surface((width, height))
        self.image.fill((0, 200, 0))
        self.rect = self.image.get_rect()
        self.spawn = '#'
        self.level = 5
        self.rect.x = x
        self.rect.y = y
        self.yvel = 0
        self.xvel = 0
        self.onGround = False
        self.count = 0
        self.jump = False
        self.serf = False

    def new_coord(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self, left, right, up, platforms, teleports):

        # лево право
        if left or right:
            if self.serf:
                if left:
                    self.yvel = -SPEED
                if right:
                    self.yvel = SPEED
            else:
                if left:
                    self.xvel = -SPEED
                if right:
                    self.xvel = SPEED
        else:
            if self.serf:
                self.yvel = 0
            else:
                self.xvel = 0
                '''
        if self.serf and (left or right) and up:
            self.serf = False
            if left:
                self.xvel = -SPEED
            if right:
                self.xvel = SPEED '''

        # прыжок
        if not self.onGround:
            if self.yvel < 50:
                self.yvel += GRAVITY
            if up and self.count < 1 and self.yvel > 0:
                self.count += 1
                self.yvel += -JUMP_POWER**2

        #реализовать лазание по крыше
        if up and self.onGround:
            self.jump = True
            self.onGround = False
            self.serf = False
            self.yvel = -JUMP_POWER**2

        self.onGround = False
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        answer = self.teleport(self.xvel, 0, teleports)
        if answer:
            self.teleport(0, self.yvel, teleports)


    def collide(self, xvel, yvel, platforms):
        for pl in platforms:
            if collide_rect(self, pl):
                if pl.name == '-':
                    self.count = 0
                    #self.serf = True
                    if yvel > 0:
                        #self.serf = False
                        self.onGround = True
                        self.rect.bottom = pl.rect.top
                    if yvel < 0:
                        #self.onGround = False
                        #self.serf = False
                        self.yvel = 0
                        self.rect.top = pl.rect.bottom
                    if xvel < 0:
                        self.yvel = 0
                        self.rect.left = pl.rect.right
                    if xvel > 0:
                        self.yvel = 0
                        self.rect.right = pl.rect.left


    def teleport(self, xvel, yvel, teleport):
        for pl in teleport:
            if collide_rect(self, pl):
                if yvel > 0:
                    self.onGround = True
                    self.rect.bottom = pl.rect.top
                if yvel < 0:
                    self.rect.top = pl.rect.bottom
                if xvel < 0:
                    self.rect.left = pl.rect.right
                if xvel > 0:
                    self.rect.right = pl.rect.left

                if pl.name == '^':
                    self.level += pl.move
                    self.spawn = '@'
                    return True

                if pl.name == 'v':  # проблема с ебаным телепортом не решена
                    self.level -= pl.move
                    self.spawn = '#'
                    return True

class Background(Sprite):
    def __init__(self, x, y, filename):
        Sprite.__init__(self)
        self.image = scale(load(filename), (int(720), int(720)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Platform(Sprite):
    def __init__(self, x, y, width, height):
        Sprite.__init__(self)
        self.name = '-'
        self.image = Surface((width, height))
        self.image.fill((200, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Teleport_A(Sprite):
    def __init__(self, x, y, width, height, move=1):
        Sprite.__init__(self)
        self.name = '^'
        self.move = move
        self.image = Surface((width, height))
        self.image.fill((0, 100, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, move):
        self.move = move


class Teleport_B(Sprite):
    def __init__(self, x, y, width, height, move=1):
        Sprite.__init__(self)
        self.name = 'v'
        self.move = move
        self.image = Surface((width, height))
        self.image.fill((0, 0, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, move):
        self.move = move
