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
        self.isdie = False
        self.helth = 3
        self.onGround = False

    def AI(self, hero, platforms):
        if hero.rect.x <= self.rect.x + 200 and hero.rect.x > self.rect.x + self.rect.width-1:
            self.update(False, True, platforms)
        elif hero.rect.x >= self.rect.x - 200 and hero.rect.x < self.rect.x - self.rect.width-1:
            self.update(True, False, platforms)
        else:
            self.update(False, False, platforms)

    def update(self, left, right, platforms):
        # лево право
        if not self.isdie:
            if left:
                self.xvel = -SPEED * 0.5
            if right:
                self.xvel = SPEED * 0.5
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

    def die(self):
        self.isdie = True  # включу запутанного моба
        self.xvel = 0
        self.yvel = 0


class Boss(Sprite):
    def __init__(self, x, y, width=400, height=300):
        Sprite.__init__(self)
        #self.image = load('data/паук/стоит/паук_стоит_направо_1.png')
        self.image = Surface((width, height))
        self.image.fill((0, 200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.yvel = 0
        self.xvel = 0
        self.isdie = False
        self.helth = 3
        self.onGround = False

    def new_coord(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def AI(self, hero, platforms):
        if hero.rect.x <= self.rect.x + 1000 and hero.rect.x > self.rect.x + self.rect.width-1:
            self.update(False, True, platforms)
        elif hero.rect.x >= self.rect.x - 1000 and hero.rect.x < self.rect.x:
            self.update(True, False, platforms)
        else:
            self.update(False, False, platforms)

    def update(self, left, right, platforms):
        # лево право
        if not self.isdie:
            if left:
                self.xvel = -SPEED * 0.5
            if right:
                self.xvel = SPEED * 0.5
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

    def die(self):
        self.isdie = True  # включу запутанного моба
        self.xvel = 0
        self.yvel = 0


class Ball(Sprite):
    def __init__(self, x, y, side, r=20):
        Sprite.__init__(self)
        self.image = Surface((r, r))
        self.image.fill((125, 125, 125))
        self.rect = self.image.get_rect()
        self.side = side
        self.rect.x = x
        self.rect.y = y
        self.yvel = 0
        self.xvel = 0
        self.die = False
        #self.ball =

    def update(self, platforms, enemys, BOSS):
        # лево право
        if self.side == -1:
            self.xvel = -SPEED * 4
        if self.side == 1:
            self.xvel = SPEED * 4

        self.rect.x += self.xvel
        self.collide(platforms, enemys, BOSS)
        self.rect.y += self.yvel

    def collide(self, platforms, enemys, BOSS):
        for pl in platforms:
            if collide_rect(self, pl):
                self.kill()
                self.die = True
        for pl in enemys:
            if collide_rect(self, pl):
                pl.helth -= 1
                if pl.helth < 0:
                    pl.die()
                self.die = True
                self.kill()
                break
        if collide_rect(self, BOSS):

            BOSS.helth -= 1
            if BOSS.helth < 0:
                BOSS.die()
            self.kill()
            self.die = True


class Monster(Sprite):
    def __init__(self, x, y, width=400, height=600):
        Sprite.__init__(self)
        #self.image = load('data/паук/стоит/паук_стоит_направо_1.png')
        self.image = Surface((width, height))
        self.image.fill((0, 200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.yvel = 0
        self.xvel = 0
        self.isdie = False
        self.helth = 3
        self.onGround = False

    def new_coord(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def AI(self, hero, platforms):
        pass

    def update(self, left, right, platforms):
        # лево право
        if not self.isdie:
            if left:
                self.xvel = -SPEED * 0.5
            if right:
                self.xvel = SPEED * 0.5
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

    def die(self):
        self.isdie = True  # включу запутанного моба
        self.xvel = 0
        self.yvel = 0


class Player(Sprite):
    def __init__(self, x, y, width=50, height=50):
        Sprite.__init__(self)
        #self.image = load('data/паук/стоит/паук_стоит_направо_1.png')
        self.image = Surface((width, height))
        self.image.fill((0, 200, 0))
        self.rect = self.image.get_rect()
        self.spawn = '@'
        self.level = 10
        self.rect.x = x
        self.rect.y = y
        self.side = 1
        self.yvel = 0
        self.xvel = 0
        self.onGround = False
        self.count = 0
        self.helth = 3
        self.jump = False
        self.serf = False
        self.trees = set()

    def new_coord(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self, left, right, up, platforms, teleports, tree, enemy, use, screen, BOSS, monster):

        # лево право
        if left or right:
            if left:
                self.xvel = -SPEED
                self.side = -1
            if right:
                self.xvel = SPEED
                self.side = 1
        else:
            self.xvel = 0

        # прыжок
        if not self.onGround:
            #if self.yvel < 50:
            self.yvel += GRAVITY
            '''
            if up and self.count < 1 and self.yvel > 0 and self.onGround:
                print(1)
                self.count += 1
                self.yvel += -JUMP_POWER**2'''

        if up and self.onGround and not self.serf:
            self.jump = True
            self.onGround = False
            self.yvel = -JUMP_POWER**2


        self.onGround = False
        self.serf = False
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        answer = self.teleport(self.xvel, 0, teleports, BOSS)
        if not answer:
            self.teleport(0, self.yvel, teleports, BOSS)

        self.enemys(enemy)

        self.Boss(BOSS)

        self.monsters(monster)

        return self.wooden(tree, use, screen)

    def monsters(self, monster):
        for pl in monster:
            if collide_rect(self, pl):
                self.respawn_new()
                break

    def respawn_new(self):
        self.spawn = '@'
        self.level -= 1
        self.helth -= 1

    def respawn(self):
        self.spawn = '@'
        self.level = 1
        self.trees = set()

    def Boss(self, BOSS):
        if collide_rect(self, BOSS):
            if BOSS.helth >= 1:
                self.helth -= 1

                if BOSS.xvel >= 0:
                    self.rect.x += SPEED * 4
                else:
                    self.rect.x += -(SPEED * 4)

    def enemys(self, enemy):
        for pl in enemy:
            if collide_rect(self, pl):
                self.helth -= 1

                if pl.xvel >= 0:
                    self.rect.x += SPEED * 4
                else:
                    self.rect.x += -(SPEED * 4)
                    print(pl.xvel)
                break


    def collide(self, xvel, yvel, platforms):
        for pl in platforms:
            if collide_rect(self, pl):
                if pl.name == '-':
                    self.count = 0
                    #self.serf = True
                    if yvel > 0:
                        self.serf = False
                        self.onGround = True
                        self.rect.bottom = pl.rect.top
                    if yvel < 0:
                        self.yvel = 0
                        self.rect.top = pl.rect.bottom
                    if xvel < 0:
                        self.yvel = -SPEED
                        self.onGround = True
                        self.serf = True
                        self.jump = False
                        self.rect.left = pl.rect.right
                    if xvel > 0:
                        self.yvel = -SPEED
                        self.onGround = True
                        self.serf = True
                        self.jump = False
                        self.rect.right = pl.rect.left


    def wooden(self, tree, use, screen):
        for pl in tree:
            if collide_rect(self, pl):  # текст не отобравжается
                if use:
                    pl.use()
                if pl.die:
                    self.trees.add(pl)
                    return False
                return True


    def teleport(self, xvel, yvel, teleport, BOSS):
        for pl in teleport:
            if collide_rect(self, pl):
                if pl == Teleport_COME:
                    pl.BOSS_live(BOSS)

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

                if pl.name == '!':  # проблема с ебаным телепортом не решена
                    self.level = pl.move
                    self.spawn = '@'
                    return True

                if pl.name == '?':  # проблема с ебаным телепортом не решена
                    if pl.boss:
                        break
                    else:
                        self.level = pl.move
                        self.spawn = '%'
                        return True

class Background(Sprite):
    def __init__(self, x, y, filename):
        Sprite.__init__(self)
        self.image = scale(load(filename), (int(720), int(720)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Tree(Sprite):
    def __init__(self, x, y, filename_True, filename_False):
        Sprite.__init__(self)
        self.image = scale(load(filename_True), (int(720), int(720)))
        self.filename_False = filename_False
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.die = False

    def use(self):  # теперь ягоды с дерева собраны
        self.image = scale(load(self.filename_False), (int(720), int(720)))
        self.die = True


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

class Teleport_BOSS(Sprite):
    def __init__(self, x, y, width, height):
        Sprite.__init__(self)
        self.name = '!'
        self.move = 69

        self.image = Surface((width, height))
        self.image.fill((100, 0, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



class Teleport_COME(Sprite):
    def __init__(self, x, y, width, height):
        Sprite.__init__(self)
        self.name = '?'
        self.move = 10
        self.boss = True
        self.image = Surface((width, height))
        self.image.fill((0, 100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        def BOSS_live(self, Boss):
            if Boss.helth <= 0:
                self.boss = False

class Monster_platform(Sprite):
    def __init__(self, x, y, width, height, move=1):
        Sprite.__init__(self)
        self.name = '_'
        self.move = move
        self.image = Surface((width, height))
        self.image.fill((0, 100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
