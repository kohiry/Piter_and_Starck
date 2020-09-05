from pygame.sprite import Sprite, collide_rect
from pygame.draw import rect
from pygame import Surface
from pygame.image import load
from pygame.transform import scale
from pyganim import PygAnimation
from random import choice
from pygame.font import Font
from pygame.draw import rect
from pygame import mixer
mixer.init()


SPEED = 1
GRAVITY = 1
JUMP_POWER = 4


# animation

ANIMATION_DELAY = 150
line_1 = 'data/паук/стоит/'
end = '.png'


def add_sprite(name, lens):
    sprites = []
    for i in range(1, lens):
        sprites.append(name + str(i) + end)
    return sprites


def Work(anim, speed=ANIMATION_DELAY, correct=None):
    data = []
    if correct == True:
        speed = 500
    for i in anim:
        data.append((i, speed))
    return data

#hero
ANIMATION_HERO_STAY_LEFT = add_sprite('data/паук/стоит/паук_стоит_налево_', 3)
ANIMATION_HERO_STAY_RIGHT = add_sprite('data/паук/стоит/паук_стоит_направо_', 3)
ANIMATION_HERO_JUMP_RIGHT = add_sprite('data\паук\прыжок\прыжок_направо_', 4)
ANIMATION_HERO_JUMP_LEFT = add_sprite('data\паук\прыжок\прыжок_налево_', 4)
ANIMATION_HERO_BIGJUMP_LEFT = add_sprite('data\паук\прыжок над пропастью\большой_прыжок_налево_', 9)
ANIMATION_HERO_BIGJUMP_RIGHT = add_sprite('data\паук\прыжок над пропастью\большой_прыжок_направо_', 9)
ANIMATION_HERO_LOSE_RIGHT = add_sprite('data\паук\проиграл\направо\проигрыш_направо_', 24)
ANIMATION_HERO_LOSE_LEFT = add_sprite('data\паук\проиграл\налево\проигрыш_налево_', 24)
ANIMATION_HERO_CLIMP_LEFT = add_sprite('data\паук\по стене\карабкается_по_стене_налево_', 4)
ANIMATION_HERO_CLIMP_RIGHT = add_sprite('data\паук\по стене\карабкается_по_стене_направо_', 4)
ANIMATION_HERO_TAKE_LEFT = add_sprite('data\паук\бросок\бросок_налево_', 3)
ANIMATION_HERO_GO_LEFT = add_sprite('data\паук\бежит\паук_бежит_налево_', 9)
ANIMATION_HERO_GO_RIGHT = add_sprite('data\паук\бежит\паук_бежит_направо_', 9)
ANIMATION_HERO_GO_STRIKE_RIGHT = add_sprite('data\паук\стреляет\бежит\паук_стреляет_бежит_направо_', 9)
ANIMATION_HERO_GO_STRIKE_LEFT = add_sprite('data\паук\стреляет\бежит\паук_стреляет_бежит_налево_', 9)
ANIMATION_HERO_STRIKE_LEFT = add_sprite('data\паук\стреляет\стоит\паук_стреляет_стоит_налево_', 3)
ANIMATION_HERO_STRIKE_RIGHT = add_sprite('data\паук\стреляет\стоит\паук_стреляет_стоит_направо_', 3)
ANIMATION_HERO_FALL_RIGHT = ['data\паук\прыжок\прыжок_направо_1.png']
ANIMATION_HERO_FALL_LEFT = ['data\паук\прыжок\прыжок_налево_1.png']


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

# титры
ANIMATION_AFTER_WORDS = add_sprite('data\\ТИТРЫ\КАДРЫ\\', 49)


class After_words(Sprite):
    def __init__(self, end):
        Sprite.__init__(self)
        self.image = Surface((960, 4062))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.end = end
        self.animation = []
        for i in ANIMATION_AFTER_WORDS:
            self.animation.append(load(i).convert())
        self.animcount = 0


    def play(self, BACK):
        BACK.play(-1)

    def update(self):
        self.animcount += 1
        self.image.blit(self.animation[self.animcount // 8], (0, 0))
        if self.animcount >= 383:
            self.animcount = 0
        if self.rect.y +  + 4062 <= self.end:
            return False
        else:
            self.rect.y -= 1
            return True


class Sound:
    def __init__(self):
        # audio
        self.BACK_AUDIO = mixer.Sound(file=r'Sound\basic_back.wav')
        self.FIGHT_AUDIO = mixer.Sound(file=r'Sound/fight.wav')
        self.DAMAGE_AUDIO = mixer.Sound(file=r'Sound/hock.wav')
        self.STRIKE_AUDIO = mixer.Sound(file=r'Sound/strike.wav')
        self.TAKE_AUDIO = mixer.Sound(file=r'Sound/take_barries.wav')
        self.BACK2_AUDIO = mixer.Sound(file=r'Sound/back_water.wav')
        self.STEP_AUDIO = mixer.Sound(file=r'Sound/step.wav')
        self.STEP2_AUDIO = mixer.Sound(file=r'Sound/step2.wav')
        self.BACK_AFTER_WORDS = mixer.Sound(file=r'Sound/Back_after_words.wav')
        self.SPIDER_AUDIO = [
            mixer.Sound(file=r'Sound/spider_01.wav'),
            mixer.Sound(file=r'Sound/spider_02.wav'),
            mixer.Sound(file=r'Sound/spider_03.wav'),
            mixer.Sound(file=r'Sound/spider_04.wav'),
            mixer.Sound(file=r'Sound/spider_05.wav'),
            mixer.Sound(file=r'Sound/spider_06.wav')
        ]
        self.BUTTON = mixer.Sound(file=r'Sound/button.wav')

        self.DAMAGE_AUDIO.set_volume(0.2)
        self.STRIKE_AUDIO.set_volume(0.1)
        self.TAKE_AUDIO.set_volume(0.5)


class Enemy(Sprite):
    def __init__(self, x, y, width=108, height=110):
        Sprite.__init__(self)
        #self.image = load('data/паук/стоит/паук_стоит_направо_1.png')
        self.image = Surface((width, height))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.SPIDER_AUDIO = Sound().SPIDER_AUDIO
        self.rect.x = x
        self.rect.y = y
        self.yvel = 0
        self.xvel = 0
        self.side = 1
        self.isdie = False
        self.helth = 10
        self.onGround = False
        self.damage = False

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
        if self.damage:
            if hero.rect.x >= self.rect.x and hero.rect.x > self.rect.x + self.rect.width-1:
                self.update(False, True, platforms)
            elif hero.rect.x <= self.rect.x and hero.rect.x < self.rect.x:
                self.update(True, False, platforms)
            else:
                self.update(False, False, platforms)
        else:
            if hero.rect.x <= self.rect.x + 1000 and hero.rect.x > self.rect.x + self.rect.width-1:
                self.update(False, True, platforms)
            elif hero.rect.x >= self.rect.x - 1000 and hero.rect.x < self.rect.x:
                self.update(True, False, platforms)
            else:
                self.update(False, False, platforms)

    def update(self, left, right, platforms):
        # лево право
        SPEED = 2
        self.image.set_colorkey((0, 255, 0))
        self.image.fill((0, 255, 0))
        if not self.isdie:
            if left:
                self.xvel = -SPEED  * 0.5
                self.side = -1
                self.AnimeEnemyGoLeft.blit(self.image, (0, 0))
            if right:
                self.xvel = SPEED * 0.5
                self.side = 1
                self.AnimeEnemyGoRight.blit(self.image, (0, 0))
            if not (left or right):
                self.xvel = 0
                if self.side == 1:
                    self.AnimeEnemyStayRight.blit(self.image, (0, 0))
                elif self.side == -1:
                    self.AnimeEnemyStayLeft.blit(self.image, (0, 0))
        else:
            if self.side == 1:
                self.AnimeEnemyDieRight.blit(self.image, (0, 0))
            elif self.side == -1:
                self.AnimeEnemyDieLeft.blit(self.image, (0, 0))

        # прыжок
        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

    def hit(self):
        choice(self.SPIDER_AUDIO).play()

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
        self.SPIDER_AUDIO = Sound().SPIDER_AUDIO
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

    def hit(self):
        choice(self.SPIDER_AUDIO).play()

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


class Ball:
    def __init__(self, x, y, side, r=20):
        self.damage_audio = Sound().DAMAGE_AUDIO
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
        SPEED = 20
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
                self.damage_audio.play()
                pl.helth -= 1
                pl.damage = True
                pl.hit()
                if pl.helth < 0:
                    pl.die()
                self.die = True
                self.kill()
                break
        if collide_rect(self, BOSS):
            BOSS.hit()
            BOSS.helth -= 1
            if BOSS.helth < 0:
                BOSS.die()
            self.kill()
            self.die = True

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Monster(Sprite):
    def __init__(self, x, y, width=400, height=500):
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

    def AI(self, hero):
        self.image.set_colorkey((0, 255, 0))
        self.image.fill((0, 255, 0))
        if collide_rect(self, hero):
            hero.films()
            if hero.side == 1:
                self.AnimeEnemyGoLeft.blit(self.image, (0, 0))
            elif hero.side == -1:
                self.AnimeEnemyGoRight.blit(self.image, (0, 0))
            else:
                self.AnimeEnemyStayLeft.blit(self.image, (0, 0))
        else:
            hero.film = False
            self.AnimeEnemyStayLeft.blit(self.image, (0, 0))

    def die(self):
        self.isdie = True  # включу запутанного моба
        self.xvel = 0
        self.yvel = 0


class Player(Sprite):
    def __init__(self, x, y, width=105, height=117):
        Sprite.__init__(self)
        self.TAKE_AUDIO = Sound().TAKE_AUDIO
        self.STEP_AUDIO = Sound().STEP_AUDIO
        self.STEP2_AUDIO = Sound().STEP2_AUDIO
        self.image = Surface((width, height))
        self.rect = self.image.get_rect()
        self.spawn = '@'
        self.level = 0
        self.rect.x = x
        self.rect.y = y
        self.film = False
        self.side = 1
        self.yvel = 0
        self.gift = False
        self.audio_step_count = 0
        self.xvel = 0
        self.onGround = False
        self.count = 0
        self.helth = 3
        self.fight = False
        self.jump = False
        self.serf = False
        self.trees = set()
        self.image.set_colorkey((0, 0, 0))
        self.animationR = []
        self.animationL = []
        for i in ANIMATION_HERO_LOSE_RIGHT:
            #im = load(i).convert_alpha()  # ВТФ почему я не могу конвертировать
            self.animationR.append(load(i))
        for i in ANIMATION_HERO_LOSE_LEFT:
            #im = load(i).convert_alpha()
            self.animationL.append(load(i))
        self.animcount = 0

        self.data_wh = {
            'go': (105, 117),
            'strike': (99, 108),
            'stay': (76, 108),
            'jump': (88, 90),
            'climb': (47, 144),
            'go_strike': (120, 117),
            'die': (127, 109)

        }


        self.AnimeGoStrikeRight = PygAnimation(Work(ANIMATION_HERO_GO_STRIKE_RIGHT))
        self.AnimeGoStrikeLeft = PygAnimation(Work(ANIMATION_HERO_GO_STRIKE_LEFT))
        self.AnimeStrikeRight = PygAnimation(Work(ANIMATION_HERO_STRIKE_RIGHT))
        self.AnimeStrikeLeft = PygAnimation(Work(ANIMATION_HERO_STRIKE_LEFT))

        self.AnimeStayLeft = PygAnimation(Work(ANIMATION_HERO_STAY_LEFT))
        self.AnimeStayRight = PygAnimation(Work(ANIMATION_HERO_STAY_RIGHT))
        self.AnimeGoRight = PygAnimation(Work(ANIMATION_HERO_GO_RIGHT))
        self.AnimeGoLeft = PygAnimation(Work(ANIMATION_HERO_GO_LEFT))
        self.AnimeJumpRight = PygAnimation(Work(ANIMATION_HERO_JUMP_RIGHT))
        self.AnimeJumpLeft = PygAnimation(Work(ANIMATION_HERO_JUMP_LEFT))
        self.AnimeClimbRight = PygAnimation(Work(ANIMATION_HERO_CLIMP_RIGHT))
        self.AnimeClimbLeft = PygAnimation(Work(ANIMATION_HERO_CLIMP_LEFT))

        # on
        self.AnimeGoStrikeRight.play()
        self.AnimeGoStrikeLeft.play()
        self.AnimeStrikeRight.play()
        self.AnimeStrikeLeft.play()
        self.AnimeClimbRight.play()
        self.AnimeClimbLeft.play()
        self.AnimeStayLeft.play()
        self.AnimeStayRight.play()
        self.AnimeGoRight.play()
        self.AnimeGoLeft.play()
        self.AnimeJumpRight.play()
        self.AnimeJumpLeft.play()

    def new_coord(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def films(self):
        self.film = True
        self.xvel = 0
        self.yvel = 0

    def resize(self, name):
        self.image = Surface(self.data_wh[name])
        self.image.set_colorkey((0, 255, 0))
        self.image.fill((0, 255, 0))

    def update(self, left, right, up, platforms, teleports, tree, enemy, use, screen, BOSS, monster, strike):
        global SPEED
        # animation
        self.image.set_colorkey((0, 255, 0))
        self.image.fill((0, 255, 0))
        print(strike)
        # лево право
        if not self.film:
            if left or right:
                if self.audio_step_count != 1 and self.onGround:
                    self.audio_step_count = 1
                    self.STEP_AUDIO.play(-1)
                    self.STEP2_AUDIO.play(-1)
                elif not self.onGround:
                    self.audio_step_count = 0
                    self.STEP_AUDIO.stop()
                    self.STEP2_AUDIO.stop()
                if left and right:
                    self.xvel = 0
                    SPEED = 1
                elif left or right:
                    if SPEED < 5:
                        SPEED += 1
                    if left:
                        self.xvel = -SPEED
                        self.side = -1
                    elif right:
                        self.xvel = SPEED
                        self.side = 1
                if up and not self.serf:
                    if self.side == 1:
                        self.resize('jump')
                        self.AnimeJumpRight.blit(self.image, (0, 0))
                    elif self.side == -1:
                        self.resize('jump')
                        self.AnimeJumpLeft.blit(self.image, (0, 0))
                elif self.serf:
                    if left and right:
                        if self.side == 1:
                            self.resize('jump')
                            self.AnimeJumpRight.blit(self.image, (0, 0))
                        elif self.side == -1:
                            self.resize('jump')
                            self.AnimeJumpLeft.blit(self.image, (0, 0))
                    elif left:
                        self.resize('climb')
                        self.AnimeClimbLeft.blit(self.image, (0, 0))
                    elif right:
                        self.resize('climb')
                        self.AnimeClimbRight.blit(self.image, (0, 0))
                else:
                    if left and right and self.onGround and strike:
                        self.resize('strike')
                        self.AnimeStrikeRight.blit(self.image, (0, 0))
                    if left and right and self.onGround:
                        self.resize('stay')
                        self.AnimeStayRight.blit(self.image, (0, 0))
                    elif left and right and not self.onGround:
                        if self.side == 1:
                            self.resize('jump')
                            self.AnimeJumpRight.blit(self.image, (0, 0))
                        elif self.side == -1:
                            self.resize('jump')
                            self.AnimeJumpLeft.blit(self.image, (0, 0))
                    elif left and self.onGround and strike:
                        self.resize('go_strike')
                        self.AnimeGoStrikeLeft.blit(self.image, (0, 0))
                    elif left and self.onGround and not strike:
                        self.resize('go')
                        self.AnimeGoLeft.blit(self.image, (0, 0))
                    elif right and self.onGround and strike:
                        self.resize('go_strike')
                        self.AnimeGoStrikeRight.blit(self.image, (0, 0))
                    elif right and self.onGround and not strike:
                        self.resize('go')
                        self.AnimeGoRight.blit(self.image, (0, 0))
                    else:
                        if not (left and right):
                            if self.side == 1:
                                self.resize('jump')
                                self.AnimeJumpRight.blit(self.image, (0, 0))
                            elif self.side == -1:
                                self.resize('jump')
                                self.AnimeJumpLeft.blit(self.image, (0, 0))

            else:
                self.xvel = 0
                SPEED = 1
                self.audio_step_count = 0
                self.STEP_AUDIO.stop()
                self.STEP2_AUDIO.stop()
                if up:
                    if self.side == 1:
                        self.resize('jump')
                        self.AnimeJumpRight.blit(self.image, (0, 0))
                    elif self.side == -1:
                        self.resize('jump')
                        self.AnimeJumpLeft.blit(self.image, (0, 0))
                else:
                    if not self.onGround:
                        if self.side == 1:
                            self.resize('jump')
                            self.AnimeJumpRight.blit(self.image, (0, 0))
                        elif self.side == -1:
                            self.resize('jump')
                            self.AnimeJumpLeft.blit(self.image, (0, 0))
                    else:
                        if self.side == 1 and strike:
                            self.resize('strike')
                            self.AnimeStrikeRight.blit(self.image, (0, 0))
                        elif self.side == 1 and not strike:
                            self.resize('stay')
                            self.AnimeStayRight.blit(self.image, (0, 0))
                        elif self.side == -1 and strike:
                            self.resize('strike')
                            self.AnimeStrikeLeft.blit(self.image, (0, 0))
                        elif self.side == -1 and not strike:
                            self.resize('stay')
                            self.AnimeStayLeft.blit(self.image, (0, 0))

        else:
            self.resize('die')
            self.animcount += 1
            end = 183
            if self.side == -1:
                self.image.blit(self.animationR[self.animcount // 8], (0, 0))
                if self.animcount >= end:
                    self.animcount = 0
            elif self.side == 1:
                self.image.blit(self.animationL[self.animcount // 8], (0, 0))
                if self.animcount >= end:
                    self.animcount = 0
        # прыжок
        if not self.onGround:
            #if self.yvel < 50:
            self.yvel += GRAVITY

            if up and self.count < 1 and self.yvel > 0 and not self.onGround and not self.film:
                self.count += 1
                self.yvel = -JUMP_POWER**2

        if up and self.onGround and not self.serf and not self.film:
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

        self.fight_find(enemy)

        return self.wooden(tree, use, screen)

    def monsters(self, monster):
        for pl in monster:
            if collide_rect(self, pl):
                #self.respawn_new()
                break

    def fight_find(self, enemy):
        for i in enemy:
            if not i.isdie:
                if (i.rect.x <= self.rect.x and self.rect.x - i.rect.x <= 1200) or (i.rect.x >= self.rect.x and i.rect.x - self.rect.x <= 1200):
                    if (i.rect.y <= self.rect.y and self.rect.y - i.rect.y <= 200) or (i.rect.y >= self.rect.y and i.rect.y - self.rect.y <= 200):
                        self.fight = True
                        break
                    else:
                        self.fight = False
                else:
                    self.fight = False
            else:
                self.fight = False
        else:
            self.fight = False

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
                    break


    def collide(self, xvel, yvel, platforms):
        for pl in platforms:
            if collide_rect(self, pl):
                if pl.name == '-':
                    #self.serf = True
                    if yvel > 0:
                        self.serf = False
                        self.onGround = True
                        self.count = 0
                        self.rect.bottom = pl.rect.top
                    if yvel < 0:
                        self.yvel = 0
                        self.onGround = False
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
                    self.TAKE_AUDIO.play()
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
        self.image = load(filename).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Tree(Sprite):
    def __init__(self, x, y, filename_True, filename_False):
        Sprite.__init__(self)
        self.image = load(filename_True).convert()
        self.filename_False = filename_False
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.die = False

    def use(self):  # теперь ягоды с дерева собраны
        self.image = load(self.filename_False).convert()
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


class Button(Sprite):
    def __init__(self, x, y, width, height, name, who=None, tag=True):
        Sprite.__init__(self)
        self.who = who
        self.name = name
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.image = Surface((width, height))
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.tag = tag
        self.image.fill((255, 255, 255))
        self.rect.x = x
        self.rect.y = y
        self.number = [str(i) for i in range(1, 13)]
        if self.name in self.number:
            self.image.blit(load(f'data\\КПК\\1\\ячейки пустые\\ячейка_{self.name}_выкл.png').convert(), (0, 0))

        elif self.name == 'Exit':
            self.image.blit(load('data\\МЕНЮ\\кнопка_выход_выкл.png').convert(), (0, 0))
        elif self.name == 'Play':
            self.image.blit(load('data\\МЕНЮ\\кнопка_новая_игра_выкл.png').convert(), (0, 0))
        elif self.name == 'Settings':
            self.image.blit(load('data\\МЕНЮ\\кнопка_настройки_выкл.png').convert(), (0, 0))
        elif self.name == 'Shop':
            self.image.blit(load('data\\МЕНЮ\\кнопка_магазин_выкл.png').convert(), (0, 0))

    def mouse(self, around):
        if around:
            self.image.fill(self.BLACK)
            if self.name in self.number:
                self.image.blit(load(f'data\\КПК\\1\\ячейки пустые\\ячейка_{self.name}_выкл.png').convert(), (0, 0))
            elif self.name == 'Exit':
                self.image.blit(load('data\\МЕНЮ\\кнопка_выход_выкл.png').convert(), (0, 0))
            elif self.name == 'Play':
                self.image.blit(load('data\\МЕНЮ\\кнопка_новая_игра_выкл.png').convert(), (0, 0))
            elif self.name == 'Settings':
                self.image.blit(load('data\\МЕНЮ\\кнопка_настройки_выкл.png').convert(), (0, 0))
            elif self.name == 'Shop':
                self.image.blit(load('data\\МЕНЮ\\кнопка_магазин_выкл.png').convert(), (0, 0))

            font = Font('pixle_font.ttf', 72)
            txt = font.render(self.name, 1, self.WHITE)
            text_x = self.width // 2 - txt.get_width() // 2
            text_y = self.height // 2 - txt.get_height() // 2
            text_w = txt.get_width()
            text_h = txt.get_height()
            if self.tag:
                self.image.blit(txt, (text_x, text_y))
                rect(self.image, self.WHITE, (self.rect.x+3, self.rect.y+3, self.rect.width-3, self.rect.height-3), 3)
        else:
            self.image.fill(self.WHITE)
            if self.name in self.number:
                self.image.blit(load(f'data\\КПК\\1\\ячейки пустые\\ячейка_{self.name}_вкл.png').convert(), (0, 0))
            elif self.name == 'Exit':
                self.image.blit(load('data\\МЕНЮ\\кнопка_выход_вкл.png').convert(), (0, 0))
            elif self.name == 'Play':
                self.image.blit(load('data\\МЕНЮ\\кнопка_новая_игра_вкл.png').convert(), (0, 0))
            elif self.name == 'Settings':
                self.image.blit(load('data\\МЕНЮ\\кнопка_настройки_вкл.png').convert(), (0, 0))
            elif self.name == 'Shop':
                self.image.blit(load('data\\МЕНЮ\\кнопка_магазин_вкл.png').convert(), (0, 0))

            font = Font('pixle_font.ttf', 72)
            txt = font.render(self.name, 1, self.BLACK)
            text_x = self.width // 2 - txt.get_width() // 2
            text_y = self.height // 2 - txt.get_height() // 2
            text_w = txt.get_width()
            text_h = txt.get_height()
            if self.tag:
                self.image.blit(txt, (text_x, text_y))
                rect(self.image, self.BLACK, (self.rect.x+3, self.rect.y+3, self.rect.width-3, self.rect.height-3), 3)
