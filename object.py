from pygame.sprite import Sprite, collide_rect
from pygame.draw import rect
from pygame import Surface
from pygame.image import load
from pygame.transform import scale
from pyganim import PygAnimation


SPEED = 20
GRAVITY = 2
JUMP_POWER = 5

# animation

ANIMATION_DELAY = 1
line_1 = 'data/паук/стоит/'
end = '.png'


def add_sprite(name, lens):
    sprites = []
    for i in range(1, lens):
        sprites.append(name + str(i) + end)
    return sprites


def Work(anim, speed=ANIMATION_DELAY):
    data = []
    for i in anim:
        data.append((i, speed))
    return data

#hero
ANIMATION_HERO_STAY_LEFT = add_sprite('data/паук/стоит/паук_стоит_налево_', 3)
ANIMATION_HERO_STAY_RIGHT = add_sprite('data/паук/стоит/паук_стоит_направо_', 3)
ANIMATION_HERO_JUMP_RIGHT = add_sprite('data\паук\прыжок\прыжок_направо_', 6)
ANIMATION_HERO_JUMP_LEFT = add_sprite('data\паук\прыжок\прыжок_налево_', 6)
ANIMATION_HERO_BIGJUMP_LEFT = add_sprite('data\паук\прыжок над пропастью\большой_прыжок_налево_', 9)
ANIMATION_HERO_BIGJUMP_RIGHT = add_sprite('data\паук\прыжок над пропастью\большой_прыжок_направо_', 9)
ANIMATION_HERO_LOSE_RIGHT = add_sprite('data\паук\проиграл\направо\проигрыш_направо_', 24)
ANIMATION_HERO_LOSE_LEFT = add_sprite('data\паук\проиграл\налево\проигрыш_налево_', 24)
ANIMATION_HERO_CLIMP_LEFT = add_sprite('data\паук\по стене\карабкается_по_стене_налево_', 4)
ANIMATION_HERO_CLIMP_RIGHT = add_sprite('data\паук\по стене\карабкается_по_стене_направо_', 4)
ANIMATION_HERO_TAKE_LEFT = add_sprite('data\паук\бросок\бросок_налево_', 3)
ANIMATION_HERO_GO_LEFT = add_sprite('data\паук\бежит\паук_бежит_налево_', 5)
ANIMATION_HERO_GO_RIGHT = add_sprite('data\паук\бежит\паук_бежит_направо_', 5)
ANIMATION_HERO_FALL_RIGHT = ['data\паук\прыжок\прыжок_направо_3.png']
ANIMATION_HERO_FALL_LEFT = ['data\паук\прыжок\прыжок_налево_3.png']

#enemy1
ANIMATION_ENEMY1_STAY_RIGHT = add_sprite('data\враги\грибной паук\паук_стоит_направо_', 3)
ANIMATION_ENEMY1_STAY_LEFT = add_sprite('data\враги\грибной паук\паук_стоит_налево_', 3)
ANIMATION_ENEMY1_GO_LEFT = add_sprite('data\враги\грибной паук\паук_идет_налево_', 4)
ANIMATION_ENEMY1_GO_RIGHT = add_sprite('data\враги\грибной паук\паук_идет_направо_', 4)
ANIMATION_ENEMY1_DIE_RIGHT = add_sprite('data\враги\грибной паук\паук_связан_направо_', 3)
ANIMATION_ENEMY1_DIE_LEFT = add_sprite('data\враги\грибной паук\паук_связан_налево_', 3)

#enemy2
ANIMATION_ENEMY2_STAY = add_sprite('data\враги\ёж\ёж_', 3)

#enemy3
ANIMATION_ENEMY3_STAY_LEFT = add_sprite('data\враги\тентаклемонстр\тентакли_налево_', 5)
ANIMATION_ENEMY3_STAY_RIGHT = add_sprite('data\враги\тентаклемонстр\тентакли_направо_', 5)
ANIMATION_ENEMY3_GO_RIGHT = add_sprite('data\враги\тентаклемонстр\схвачен_тентаклями_направо_', 9)
ANIMATION_ENEMY3_GO_LEFT = add_sprite('data\враги\тентаклемонстр\схвачен_тентаклями_налево_', 9)
ANIMATION_ENEMY3_DIE_LEFT = add_sprite('data\враги\тентаклемонстр\тентакли_спрятались_налево_', 4)
ANIMATION_ENEMY3_DIE_RIGHT = add_sprite('data\враги\тентаклемонстр\тентакли_спрятались_направо_', 4)

#Tony Stark
ANIMATION_TONY = add_sprite('data\Тони\тони_', 3)

#BOSS
ANIMATION_BOSS_STAY_LEFT = add_sprite('data\враги\королева\королева_стоит_налево_', 3)
ANIMATION_BOSS_STAY_RIGHT = add_sprite('data\враги\королева\королева_стоит_направо_', 3)
ANIMATION_BOSS_GO_LEFT = add_sprite('data\враги\королева\королева_идет_налево_', 5)
ANIMATION_BOSS_GO_RIGHT = add_sprite('data\враги\королева\королева_идет_направо_', 5)
ANIMATION_BOSS_DIE_LEFT = add_sprite('data\враги\королева\королева_связана_налево_', 3)
ANIMATION_BOSS_DIE_RIGHT = add_sprite('data\враги\королева\королева_связана_направо_', 3)



class Enemy(Sprite):
    def __init__(self, x, y, width=216, height=220):
        Sprite.__init__(self)
        #self.image = load('data/паук/стоит/паук_стоит_направо_1.png')
        self.image = Surface((width, height))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.yvel = 0
        self.xvel = 0
        self.side = 1
        self.isdie = False
        self.helth = 3
        self.onGround = False

        #animation
        self.AnimeEnemyStayLeft = PygAnimation(Work(ANIMATION_ENEMY1_STAY_LEFT))
        self.AnimeEnemyStayRight = PygAnimation(Work(ANIMATION_ENEMY1_STAY_RIGHT))
        self.AnimeEnemyGoLeft = PygAnimation(Work(ANIMATION_ENEMY1_GO_LEFT))
        self.AnimeEnemyGoRight = PygAnimation(Work(ANIMATION_ENEMY1_GO_RIGHT))
        self.AnimeEnemyDieLeft = PygAnimation(Work(ANIMATION_ENEMY1_DIE_LEFT))
        self.AnimeEnemyDieRight = PygAnimation(Work(ANIMATION_ENEMY1_DIE_RIGHT))


        # on
        self.AnimeEnemyStayLeft.play()
        self.AnimeEnemyStayRight.play()
        self.AnimeEnemyGoLeft.play()
        self.AnimeEnemyGoRight.play()
        self.AnimeEnemyDieLeft.play()
        self.AnimeEnemyDieRight.play()

    def AI(self, hero, platforms):
        if hero.rect.x <= self.rect.x + 1000 and hero.rect.x > self.rect.x + self.rect.width-1:
            self.update(False, True, platforms)
        elif hero.rect.x >= self.rect.x - 1000 and hero.rect.x < self.rect.x - self.rect.width-1:
            self.update(True, False, platforms)
        else:
            self.update(False, False, platforms)

    def update(self, left, right, platforms):
        # лево право
        #self.image.set_colorkey((0, 255, 0))
        self.image.fill((0, 255, 0))
        if not self.isdie:
            if left:
                self.xvel = -SPEED * 0.5
                self.side = -1
                #self.AnimeEnemyGoLeft.blit(self.image, (0, 0))
            if right:
                self.xvel = SPEED * 0.5
                self.side = 1
                #self.AnimeEnemyGoRight.blit(self.image, (0, 0))
            if not (left or right):
                self.xvel = 0
                #if self.side == 1:
                    #self.AnimeEnemyStayRight.blit(self.image, (0, 0))
                #elif self.side == -1:
                    #self.AnimeEnemyStayLeft.blit(self.image, (0, 0))
        #else:
            #if self.side == 1:
                #self.AnimeEnemyDieRight.blit(self.image, (0, 0))
            #elif self.side == -1:
                #self.AnimeEnemyDieLeft.blit(self.image, (0, 0))

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
    def __init__(self, x, y, width=400, height=400):
        Sprite.__init__(self)
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

        #animation
        self.AnimeEnemyStayLeft = PygAnimation(Work(ANIMATION_BOSS_STAY_LEFT))
        self.AnimeEnemyStayRight = PygAnimation(Work(ANIMATION_BOSS_STAY_RIGHT))
        self.AnimeEnemyGoLeft = PygAnimation(Work(ANIMATION_BOSS_GO_LEFT))
        self.AnimeEnemyGoRight = PygAnimation(Work(ANIMATION_BOSS_GO_RIGHT))
        self.AnimeEnemyDieLeft = PygAnimation(Work(ANIMATION_BOSS_DIE_LEFT))
        self.AnimeEnemyDieRight = PygAnimation(Work(ANIMATION_BOSS_DIE_RIGHT))


        # on
        self.AnimeEnemyStayLeft.play()
        self.AnimeEnemyStayRight.play()
        self.AnimeEnemyGoLeft.play()
        self.AnimeEnemyGoRight.play()
        self.AnimeEnemyDieLeft.play()
        self.AnimeEnemyDieRight.play()


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

        #self.image.set_colorkey((0, 255, 0))
        self.image.fill((0, 255, 0))
        if not self.isdie:
            if left:
                self.xvel = -SPEED * 0.5
                self.side = -1
                #self.AnimeEnemyGoLeft.blit(self.image, (0, 0))
            if right:
                self.xvel = SPEED * 0.5
                self.side = 1
                #self.AnimeEnemyGoRight.blit(self.image, (0, 0))
            if not (left or right):
                self.xvel = 0
                #if self.side == 1:
                    #self.AnimeEnemyStayRight.blit(self.image, (0, 0))
                #elif self.side == -1:
                    #self.AnimeEnemyStayLeft.blit(self.image, (0, 0))
        #else:
            #if self.side == 1:
                #self.AnimeEnemyDieRight.blit(self.image, (0, 0))
            #elif self.side == -1:
                #self.AnimeEnemyDieLeft.blit(self.image, (0, 0))

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
        self.eat = 0

        self.onGround = False

        ANIMATION_ENEMY3_STAY_LEFT = add_sprite('data\враги\тентаклемонстр\тентакли_налево_', 5)
        ANIMATION_ENEMY3_STAY_RIGHT = add_sprite('data\враги\тентаклемонстр\тентакли_направо_', 5)
        ANIMATION_ENEMY3_GO_RIGHT = add_sprite('data\враги\тентаклемонстр\схвачен_тентаклями_направо_', 9)
        ANIMATION_ENEMY3_GO_LEFT = add_sprite('data\враги\тентаклемонстр\схвачен_тентаклями_налево_', 9)
        ANIMATION_ENEMY3_DIE_LEFT = add_sprite('data\враги\тентаклемонстр\тентакли_спрятались_налево_', 4)
        ANIMATION_ENEMY3_DIE_RIGHT = add_sprite('data\враги\тентаклемонстр\тентакли_спрятались_направо_', 4)

        #animation
        self.AnimeEnemyStayLeft = PygAnimation(Work(ANIMATION_ENEMY3_STAY_LEFT))
        self.AnimeEnemyStayRight = PygAnimation(Work(ANIMATION_ENEMY3_STAY_RIGHT))
        self.AnimeEnemyGoLeft = PygAnimation(Work(ANIMATION_ENEMY3_GO_RIGHT))
        self.AnimeEnemyGoRight = PygAnimation(Work(ANIMATION_ENEMY3_GO_LEFT))
        self.AnimeEnemyDieLeft = PygAnimation(Work(ANIMATION_ENEMY3_DIE_LEFT))
        self.AnimeEnemyDieRight = PygAnimation(Work(ANIMATION_ENEMY3_DIE_RIGHT))

        #on
        self.AnimeEnemyStayLeft.play()
        self.AnimeEnemyStayRight.play()
        self.AnimeEnemyGoLeft.play()
        self.AnimeEnemyGoRight.play()
        self.AnimeEnemyDieLeft.play()
        self.AnimeEnemyDieRight.play()


    def new_coord(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def AI(self, hero, platforms):
        pass  # тут будет катсцена

    def update(self, left, right):
        pass

    def die(self):
        self.isdie = True  # включу запутанного моба
        self.xvel = 0
        self.yvel = 0


class Player(Sprite):
    def __init__(self, x, y, width=140, height=200):
        Sprite.__init__(self)
        #self.image = load('data/паук/стоит/паук_стоит_направо_1.png')
        self.image = Surface((width, height))
        self.rect = self.image.get_rect()
        self.spawn = '@'
        self.level = 9
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
        self.image.set_colorkey((0, 0, 0))

        self.AnimeStayLeft = PygAnimation(Work(ANIMATION_HERO_STAY_LEFT))
        self.AnimeStayRight = PygAnimation(Work(ANIMATION_HERO_STAY_RIGHT))
        self.AnimeGoRight = PygAnimation(Work(ANIMATION_HERO_GO_RIGHT))
        self.AnimeGoLeft = PygAnimation(Work(ANIMATION_HERO_GO_LEFT))
        self.AnimeJumpRight = PygAnimation(Work(ANIMATION_HERO_JUMP_RIGHT))
        self.AnimeJumpLeft = PygAnimation(Work(ANIMATION_HERO_JUMP_LEFT))
        self.AnimeFallLeft = PygAnimation(Work(ANIMATION_HERO_FALL_RIGHT))
        self.AnimeFallRight = PygAnimation(Work(ANIMATION_HERO_FALL_RIGHT))

        # on
        self.AnimeStayLeft.play()
        self.AnimeStayRight.play()
        self.AnimeGoRight.play()
        self.AnimeGoLeft.play()
        self.AnimeJumpRight.play()
        self.AnimeJumpLeft.play()
        self.AnimeFallLeft.play()
        self.AnimeFallRight.play()

    def new_coord(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self, left, right, up, platforms, teleports, tree, enemy, use, screen, BOSS, monster):
        # animation
        self.image.set_colorkey((0, 255, 0))
        self.image.fill((0, 255, 0))
        # лево право
        if left or right:
            if left and right:
                self.xvel = 0
            elif left:
                self.xvel = -SPEED
                self.side = -1
            elif right:
                self.xvel = SPEED
                self.side = 1
            if up:
                if self.side == 1:
                    self.AnimeJumpRight.blit(self.image, (-90, -90))
                elif self.side == -1:
                    self.AnimeJumpLeft.blit(self.image, (-90, -90))
            else:
                if left and right:
                    self.AnimeStayRight.blit(self.image, (-90, -90))
                elif left:
                    self.AnimeGoLeft.blit(self.image, (-90, -90))
                elif right:
                    self.AnimeGoRight.blit(self.image, (-90, -90))

        else:
            self.xvel = 0
            if up:
                if self.side == 1:
                    self.AnimeJumpRight.blit(self.image, (-90, -90))
                elif self.side == -1:
                    self.AnimeJumpLeft.blit(self.image, (-90, -90))
            else:
                if not self.onGround:
                    if self.side == 1:
                        self.AnimeFallRight.blit(self.image, (-90, -90))
                    elif self.side == -1:
                        self.AnimeFallLeft.blit(self.image, (-90, -90))
                else:
                    if self.side == 1:
                        self.AnimeStayRight.blit(self.image, (-90, -90))
                    else:
                        self.AnimeStayLeft.blit(self.image, (-90, -90))
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
            if self.level == 69:
                if BOSS.helth >= 1:
                    self.helth -= 1

                    if BOSS.xvel >= 0:
                        self.rect.x += SPEED * 4
                    else:
                        self.rect.x += -(SPEED * 4)

    def enemys(self, enemy):
        for pl in enemy:
            if collide_rect(self, pl):
                if not pl.isdie:
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
