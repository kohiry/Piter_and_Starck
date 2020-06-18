from pygame.sprite import Sprite, collide_rect
from pygame.draw import rect
from pygame import Surface
from pygame.image import load
from pygame.transform import scale
from settings import SIZE


SPEED = 20
GRAVITY = 1
JUMP_POWER = 20


class Player(Sprite):
    def __init__(self, x, y, width=50, height=50):
        Sprite.__init__(self)
        #self.image = load('data/паук/стоит/паук_стоит_направо_1.png')
        self.image = Surface((width, height))
        self.image.fill((0, 200, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.yvel = 0
        self.side = 0
        self.onGround = False

    def new_coord(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self, side, up, platforms):
        # лево право
        if side != 0:
            self.rect.x += SPEED * side

        # прыжок
        if not self.onGround:
            self.yvel += GRAVITY
        if up and self.onGround:
            self.onGround = False
            self.yvel = -JUMP_POWER


        #self.onGround = False
        self.rect.y += self.yvel
        self.side = side
        self.collide(0, self.side, platforms)
        self.collide(self.yvel, 0, platforms)
        print(side, '|', self.yvel, '|', self.onGround)

    def collide(self, yvel, side, platforms):
        for pl in platforms:
            if collide_rect(self, pl):


                if yvel > 0:
                    self.yvel = 0
                    self.onGround = True
                    self.rect.bottom = pl.rect.top
                elif yvel < 0:
                    self.rect.top = pl.rect.bottom
                # лаганно презимляется
                if self.yvel < 20:
                    if side == -1:
                        self.rect.left = pl.rect.right
                    elif side == 1:
                        self.rect.right = pl.rect.left
                elif self.onGround:
                    self.yvel = 0


                    #self.yvel = 0



class Background(Sprite):
    def __init__(self, x, y, filename):
        Sprite.__init__(self)
        self.image = scale(load(filename), (int(1080//1.52), int(1080//1.52)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, side):
        pass

class Platform(Sprite):
    def __init__(self, x, y, width, height):
        Sprite.__init__(self)
        self.image = Surface((width, height))
        self.image.fill((200, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, side):
        pass
