from pygame.sprite import Sprite, collide_rect
from pygame.draw import rect
from pygame import Surface
from pygame.image import load
from pygame.transform import scale
from pyganim import PygAnimation
from random import choice
from pygame.font import Font
from pygame import Rect
from pygame import mixer
from pygame import sprite
from pygame.display import set_mode
from time import process_time
from pygame import HWSURFACE, DOUBLEBUF, FULLSCREEN
from sqlite3  import connect
import add_info_into_config
mixer.init()



set_mode((0, 0), HWSURFACE| DOUBLEBUF| FULLSCREEN)
SPEED = 8
GRAVITY = 1
JUMP_POWER = 5


# animation

ANIMATION_DELAY = 120
line_1 = 'data/паук/стоит/'
end = '.png'


def add_sprite(name, lens, can=True):
    sprites = []
    if can:
        for i in range(1, lens):
            sprites.append(name + str(i) + end)
    else:
        sprites.append(name + end)
    return sprites


def Work(anim, speed=ANIMATION_DELAY, correct=None, speed_coorect=500):
    data = []
    if correct:
        speed = speed_coorect
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
ANIMATION_HERO_TAKE_RIGHT = add_sprite('data\паук\бросок\бросок_направо_', 3)
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

# info
ANIMATION_INFO_SPIDER = add_sprite('data\\КПК\\2\\грибной_паук_', 3)
ANIMATION_INFO_BIGSPIDER = add_sprite('data\\КПК\\2\\грибная_королева_', 3)
ANIMATION_INFO_TENTACLE = add_sprite('data\\КПК\\2\\овраговый_щупалцехват_', 5)
ANIMATION_INFO_PIDOR = add_sprite('data\\КПК\\2\\сучий_жук_', 3)
ANIMATION_INFO_ESJH = add_sprite('data\\КПК\\2\\ёж_', 3)

ANIMATION_INFO_YELLOW = add_sprite('data\\КПК\\2\\жёлтая_ягода', 2, False)
ANIMATION_INFO_BLUE = add_sprite('data\\КПК\\2\\потолочный_гриб', 2, False)
ANIMATION_INFO_LIFE = add_sprite('data\\КПК\\2\\ягода_жизни', 2, False)

ANIMATION_START = add_sprite('data\\ЗАСТАВКА\\', 9)

class BlackTheme:
    def __init__(self):
        #set_mode((0, 0), HWSURFACE| DOUBLEBUF| FULLSCREEN)
        self.count = 0
        self.one_sprite = 2
        self.all_count = 12
        self.black_list = []
        # затемнение для катсцен
        for i in [f'data\\интерфейс\\затенение_{str(j)}.png' for j in range(1, 7)]:
            self.black_list.append(load(i))
        self.black_list_r = self.black_list.copy()

    def zero(self):
        self.count = 0

    def draw(self, screen, reverse=False):
        self.count += 1
        if self.count <= self.all_count-1:
            if reverse:
                screen.blit(self.black_list_r[self.count // self.one_sprite], (0, 0))
            else:
                screen.blit(self.black_list[self.count // self.one_sprite], (0, 0))


class Start(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        #set_mode((0, 0), HWSURFACE| DOUBLEBUF| FULLSCREEN)
        self.image = load('data\\ЗАСТАВКА\\дисклаймер.png').convert_alpha()

        #self.image = load('data\\интерфейс\\иконки и кнопки\\морды\\Питер\\Питер_нейтрал.png')
        self.rect = self.image.get_rect()
        self.old_time = 0
        self.change = True

        self.Anime = PygAnimation(Work(ANIMATION_START))
        self.Anime.play()

    def upd(self, tag):
        if tag:
            self.Anime.blit(self.image, (0, 0))
        else:
            self.image = load('data\\ЗАСТАВКА\\дисклаймер.png').convert_alpha()

class DialogWindowSpawner(Sprite):
    def __init__(self, x, y, name_, number):
        Sprite.__init__(self)
        name, dialog = '', ''
        if name_ == '0':
            name = 'FirstPhraseInDange'
            dialog = 'text_1'
        if name_ == '^':
            name = 'spider'
            dialog = 'text_' + str(number)
        if name_ == 'v':
            name = 'monster'
            dialog = 'text_' + str(number)
        if name_ == '*':
            name = 'Hedgehog'
            dialog = 'text_' + str(number)


        self.name = name
        self.dialog = dialog
        self.image = Surface((2, 550)).convert()
        #self.image = load('data\\интерфейс\\иконки и кнопки\\морды\\Питер\\Питер_нейтрал.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Dialog_Tab(Sprite):
    draw = True
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.data_text = ''
        self.image = load('data\\интерфейс\\диалоговая_полоса.png')
        #set_mode((0, 0), HWSURFACE| DOUBLEBUF| FULLSCREEN)
        self.image.fill((0, 255, 0))
        self.image.set_colorkey((0, 255, 0))
        self.image = load('data\\интерфейс\\диалоговая_полоса.png').convert_alpha()
        #self.image = load('data\\интерфейс\\иконки и кнопки\\морды\\Питер\\Питер_нейтрал.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.who = []
        self.emotion = []
        self.my_phrase = []
        self.phrase = 0
        self.count = 0
        self.bool_killed_sprite = False
        self.old_art = 'piter_neitral'
        self.art_now = 'piter_neitral'
        self.data = {
            1: load('data\\интерфейс\\иконки и кнопки\\морды\\1 Питер_нейтрал.png').convert(),
            2: load('data\\интерфейс\\иконки и кнопки\\морды\\2 Питер_удивлен.png').convert(),
            3: load('data\\интерфейс\\иконки и кнопки\\морды\\3 Питер_напряг.png').convert(),
            4: load('data\\интерфейс\\иконки и кнопки\\морды\\4 Питер_уныние.png').convert(),
            5: load('data\\интерфейс\\иконки и кнопки\\морды\\5 Питер_падла.png').convert(),
            6: load('data\\интерфейс\\иконки и кнопки\\морды\\6 Питер_флирт.png').convert(),
            7: load('data\\интерфейс\\иконки и кнопки\\морды\\7 Питер_убивака_1.png').convert(),
            8: load('data\\интерфейс\\иконки и кнопки\\морды\\8 Питер_убивака_2.png').convert(),
            9: load('data\\интерфейс\\иконки и кнопки\\морды\\9 Питер_обижен.png').convert(),
            10: load('data\\интерфейс\\иконки и кнопки\\морды\\10 Тони_костюм.png').convert(),
            11: load('data\\интерфейс\\иконки и кнопки\\морды\\11 Тони_недоволен.png').convert(),
            12: load('data\\интерфейс\\иконки и кнопки\\морды\\12 Тони_нейтрал.png').convert(),
            13: load('data\\интерфейс\\иконки и кнопки\\морды\\13 Тони_рад.png').convert(),
            14: load('data\\интерфейс\\иконки и кнопки\\морды\\14 грибной_паук.png').convert()
        }
        for i in self.data.keys():
            self.data[i].set_colorkey((0, 255, 0))
        #self.image.blit(self.data['piter_neitral'], (0, 414))  # ещё не перешёл в интеграцию в игру


    def delete_table(self):
        self.kill()
        self.bool_killed_sprite = True

    def dialog_with(self, info): # info = (таблица, столбец) for example: (spider, text_1)d
        self.clear(True)

        def find_who(text_list):

            for i in range(len(text_list)):  # смотрю по первому символу диалога
                first_sumbol = text_list[i][0][0][0]
                if first_sumbol == 'П':
                    self.who.append('Человек Паук')
                if first_sumbol == 'Ж':
                    self.who.append('Железный Человек')
                if first_sumbol == 'Г':
                    self.who.append('Грибной Паук')
                number_emotion = text_list[i][0][0][2:4]
                if number_emotion in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    self.emotion.append(self.data[int(number_emotion[0])])
                if number_emotion in ['10', '12', '13', '14', '15', '16']:
                    self.emotion.append(self.data[int(number_emotion)])

                text_list[i][0][0] = text_list[i][0][0][4:]


        def format_text(text):
            new_text = ''
            count_word = text.split()
            list_text = []
            cow_text = []
            word = 13
            for i in range(len(count_word)):
                cow_text.append(count_word[i])
                if (i+1) % word == 0:
                    list_text.append(cow_text.copy())
                    cow_text.clear()
                if i == len(count_word) -1:
                    list_text.append(cow_text.copy())
                    cow_text.clear()
            assert type(list_text) == type(list())
            return list_text


        db = connect('game.db')
        sql = db.cursor()
        draw = True
        #print('1', info)
        for i in sql.execute(f"SELECT {info[1]} FROM {info[0]}"):
            self.data_text = i[0].split(';')
        for i in self.data_text:
            self.my_phrase.append(format_text(i))
        #print(self.data_text)

        find_who(self.my_phrase)
        self.check(False)
        db.close()


    def clear(self, all=False):
        print('очистка')
        self.phrase = 0
        if all:
            self.data_text = ''
            self.my_phrase.clear()
            self.emotion.clear()
            self.who.clear()
            self.image = load('data\\интерфейс\\диалоговая_полоса.png').convert_alpha()


    def check(self, skip, hero=None):


        if len(self.data) > self.phrase:
            if skip:
                if len(self.who) >= self.phrase:
                    self.phrase += 1
                self.image = load('data\\интерфейс\\диалоговая_полоса.png').convert_alpha()
            draw = True
            white = (255, 255, 255)
            font = Font('pixle_font.ttf', 18)
            who = ''
            my_phrase = []
            if self.phrase == 0:
                my_phrase = ['']
                who = ''
            else:
                if hero != None:  # продолить еблю с окном
                    if self.phrase -1 == len(self.who) and self.phrase -1 != 0:
                        hero.chat = False
                if (self.phrase -1) != len(self.who):
                    who = self.who[self.phrase - 1]
                    my_phrase = self.my_phrase[self.phrase - 1]
                    self.image.blit(self.emotion[self.phrase - 1], (0, 414))
            y = 467

            font2 = Font('pixle_font.ttf', 25)
            txt = font2.render(who, 1, (0, 0, 0))
            self.image.blit(txt, (139, 419))
            font2 = Font('pixle_font.ttf', 25)
            txt = font2.render(who, 1, (80, 200, 120))
            self.image.blit(txt, (140, 420))
            for i in my_phrase:
                txt = font.render((' ').join(i), 1, white)
                self.image.blit(txt, (170, y))
                y += 25

        else:
            draw = False


class Health_tab(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        #set_mode((0, 0), HWSURFACE| DOUBLEBUF| FULLSCREEN)
        self.image = load('data\\интерфейс\\иконки и кнопки\\жизни\\жизни_10.png').convert()
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def new_image(self, helth):
        self.image.fill((0, 0, 0))
        if helth >= 0:
            self.image = load(f'data\\интерфейс\\иконки и кнопки\\жизни\\жизни_{helth}.png').convert()
        else:
            self.image = load(f'data\\интерфейс\\иконки и кнопки\\жизни\\жизни_0.png').convert()

        self.image.set_colorkey((0, 0, 0))

class Cutscene(Sprite):
    def __init__(self, filename, end, name):
        Sprite.__init__(self)
        self.filename = filename
        #self.image = load(filename + '1.png').convert()
        self.image = Surface((960, 1529))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.name = name
        self.end = end
        self.first_end = False
        self.four_end = False
        self.count = 1
        self.animcount = 0
        self.anim = False
        self.lock = 0
        self.not_fast = False

        self.number = 0
        self.animation = []
        for i in add_sprite('data\\катсцены\\1 начало\\начало_4_', 4):
            self.animation.append(load(i).convert())
        self.animation_black = []
        for i in [f'data\\интерфейс\\затенение_{str(j)}.png' for j in range(1, 7)]:
            self.animation_black.append(load(i))

    def upd(self):
        print(self.count)

        if self.count == 1:
            if not self.anim:
                self.image.blit(load(self.filename + '1.png').convert(), (0, 0))
            if self.animcount >= 5:
                self.anim = True
                self.animcount = 0
            if not self.anim:
                self.animcount += 1
                self.image.blit(self.animation_black[self.animcount // 1], (0, 0))
            if self.rect.y + 1528 <= self.end and self.anim:
                self.first_end = True
            else:
                if self.anim:
                    self.rect.y -= 2
        elif self.count == 2:
            self.rect.y = 0
            self.animcount = 0
            self.image = load(self.filename + str(self.count) + '.png').convert()

        elif self.count == 3:
            self.rect.y = 0
            self.animcount = 0
            self.image = load(self.filename + str(self.count) + '.png').convert()
        elif self.count == 4:  #решить проблему со 2 картинкой которую почему то код игнорирует
            self.animcount += 1
            if self.animcount < 48:
                self.image = load(self.filename + str(self.count) + '.png').convert()
            else:
                self.image.blit(self.animation[(self.animcount - 47) // 5], (0, 0))
                if self.animcount - 47 >= 14:
                    self.animcount = 0
                    self.four_end = True
        elif self.count == 5:
            self.rect.y = 0
            self.animcount = 0
            self.image = load(self.filename + str(self.count) + '.png').convert()
        elif self.count == 6:
            self.rect.y = 0
            self.animcount = 0
            self.image = load(self.filename + str(self.count) + '.png').convert()
        elif self.count == 7:
            self.rect.y = 0
            self.animcount = 0
            self.image = load(self.filename + str(self.count) + '.png').convert()

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
        self.START_AUDIO = mixer.Sound(file=r'Sound\start.wav')
        self.USE_AUDIO = mixer.Sound(file=r'Sound\use.wav')
        self.MENU_AUDIO = mixer.Sound(file=r'Sound\menu.wav')
        self.CUTSCENE_AUDIO = mixer.Sound(file=r'Sound\cutscene.wav')
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

    def clear(self):
        # audio
        self.BACK_AUDIO.stop()
        self.START_AUDIO.stop()
        self.USE_AUDIO.stop()
        self.MENU_AUDIO.stop()
        self.CUTSCENE_AUDIO.stop()
        self.FIGHT_AUDIO.stop()
        self.DAMAGE_AUDIO.stop()
        self.STRIKE_AUDIO.stop()
        self.TAKE_AUDIO.stop()
        self.BACK2_AUDIO.stop()
        self.STEP_AUDIO.stop()
        self.STEP2_AUDIO.stop()
        self.BACK_AFTER_WORDS.stop()
        for i in self.SPIDER_AUDIO:
            i.stop()
        self.BUTTON.stop()



class Enemy(Sprite):
    def __init__(self, x, y, sound, width=108, height=110):
        Sprite.__init__(self)
        #self.image = load('data/паук/стоит/паук_стоит_направо_1.png')
        self.image = Surface((width, height))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.SPIDER_AUDIO = sound.SPIDER_AUDIO
        self.rect.x = x
        self.rect.y = y
        self.yvel = 0
        self.xvel = 0
        self.phrase = False
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
        way = 1100
        if not hero.chat:
            if hero.rect.x >= self.rect.x and hero.rect.x > self.rect.x + self.rect.width-1:
                self.update(False, True, platforms)
            elif hero.rect.x <= self.rect.x and hero.rect.x < self.rect.x:
                self.update(True, False, platforms)
            else:
                self.update(False, False, platforms)
        else:
            self.update(False, False, platforms)
        """elif self.damage:
            if hero.rect.x >= self.rect.x and hero.rect.x > self.rect.x + self.rect.width-1:
                self.update(False, True, platforms)
            elif hero.rect.x <= self.rect.x and hero.rect.x < self.rect.x:
                self.update(True, False, platforms)
            else:
                self.update(False, False, platforms)"""


    def update(self, left, right, platforms):
        # лево право
        SPEED = 5
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

class Enemy2(Sprite):
    def __init__(self, x, y, sound, width=80, height=46):
        Sprite.__init__(self)
        #self.image = load('data/паук/стоит/паук_стоит_направо_1.png')
        self.image = Surface((width, height))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.SPIDER_AUDIO = sound.SPIDER_AUDIO
        self.rect.x = x
        self.rect.y = y
        self.yvel = 0
        self.xvel = 0
        self.phrase = False
        self.side = 1
        self.isdie = False
        self.helth = 10
        self.onGround = False
        self.damage = False

        #animation
        self.AnimeEnemyStay = PygAnimation(Work(ANIMATION_ENEMY2_STAY))

        self.AnimeEnemyStay.play()


    def AI(self, hero, platforms):
        # лево право
        self.image.set_colorkey((0, 255, 0))
        self.image.fill((0, 255, 0))

        self.AnimeEnemyStay.blit(self.image, (0, 0))




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
        self.phrase = False
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
    def __init__(self, x, y, side):
        Sprite.__init__(self)
        #self.damage_audio = Sound().DAMAGE_AUDIO
        #set_mode((0, 0), HWSURFACE| DOUBLEBUF| FULLSCREEN)
        if side == 1:
            self.image = load('data\\штуки\\выстрел_паутины_R.png').convert_alpha()
        else:
            self.image = load('data\\штуки\\выстрел_паутины_L.png').convert_alpha()
        #self.image = Surface((10, 10))
        self.rect = self.image.get_rect()
        self.side = side
        self.rect.x = x
        self.rect.y = y
        self.xvel = 0
        self.die = False
        #self.ball =

    def update(self, hero, enemys):
        SPEED = 35
        # лево право
        if self.side == -1:
            self.xvel = -SPEED * 1
        if self.side == 1:
            self.xvel = SPEED * 1

        self.rect.x += self.xvel

class Monster(Sprite):
    def __init__(self, x, y, width=522, height=486):
        Sprite.__init__(self)
        #self.image = load('data/паук/стоит/паук_стоит_направо_1.png')
        self.image = Surface((width, height))
        #self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.yvel = 0
        self.xvel = 0
        self.isdie = False
        self.eat = 0
        self.phrase = False
        self.death = False
        self.animationR = []
        self.animationL = []
        self.animationR_D = []
        self.animationL_D = []

        for i in ANIMATION_ENEMY3_GO_RIGHT:
            #im = load(i).convert_alpha()  # ВТФ почему я не могу конвертировать
            self.animationR.append(load(i))
        for i in ANIMATION_ENEMY3_GO_LEFT:
            #im = load(i).convert_alpha()
            self.animationL.append(load(i))

        for i in ANIMATION_ENEMY3_DIE_LEFT:
            #im = load(i).convert_alpha()  # ВТФ почему я не могу конвертировать
            self.animationR_D.append(load(i))
        for i in ANIMATION_ENEMY3_DIE_RIGHT:
            #im = load(i).convert_alpha()
            self.animationL_D.append(load(i))
        self.animcount = 0

        # coord count
        self.y_go_monster = y - 200
        self.y_stay_monster = y

        self.onGround = False

        #animation
        self.AnimeEnemyStayLeft = PygAnimation(Work(ANIMATION_ENEMY3_STAY_LEFT))
        self.AnimeEnemyStayRight = PygAnimation(Work(ANIMATION_ENEMY3_STAY_RIGHT))
        self.AnimeEnemyDieLeft = PygAnimation(Work(ANIMATION_ENEMY3_DIE_LEFT))
        self.AnimeEnemyDieRight = PygAnimation(Work(ANIMATION_ENEMY3_DIE_RIGHT))

        #on
        self.AnimeEnemyStayLeft.play()
        self.AnimeEnemyStayRight.play()
        self.AnimeEnemyDieLeft.play()
        self.AnimeEnemyDieRight.play()


    def new_coord(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def resize(self, name, hero):
        self.rect.width, self.rect.height = {'Go': (522, 486), 'Stay':(286, 179)}[name]
        if name == 'Go':
            self.rect.y = hero.rect.y - 100   #self.y_go_monster
        else:
            self.rect.y = self.y_stay_monster

    def AI(self, hero):
        self.image.fill((0, 255, 0))
        self.image.set_colorkey((0, 255, 0))
        if not self.death:

            if collide_rect(self, hero):
                end = 63
                if not hero.film:
                    hero.films()
                    hero.moster = True
                    if hero.side == -1:
                        self.rect = self.rect.move(-50, -307)
                    if hero.side == 1:
                        self.rect = self.rect.move(-290, -307)
                if hero.side == -1:
                    self.resize('Go', hero)
                    self.animcount += 1
                    #self.image.fill((0, 255, 0))
                    self.image.blit(self.animationL[self.animcount // 8], (0, 0))
                    self.image.set_colorkey((0, 255, 0))
                    if self.animcount >= end:
                        hero.who_kill.append(self)
                        hero.film = False
                        hero.death = True
                        hero.animcount = 0
                        hero.level = 0
                        hero.helth = 3
                elif hero.side == 1:
                    self.resize('Go', hero)
                    self.animcount += 1
                    #self.image.fill((0, 255, 0))
                    self.image.blit(self.animationR[self.animcount // 8], (0, 0))
                    self.image.set_colorkey((0, 255, 0))
                    if self.animcount >= end:
                        hero.who_kill.append(self)
                        hero.film = False
                        hero.death = True
                        hero.animcount = 0
                        hero.level = 0
                        hero.helth = 3

                else:
                    if hero.side == -1:
                        self.resize('Stay', hero)
                        self.AnimeEnemyStayLeft.blit(self.image, (0, 0))
                    elif hero.side == 1:
                        self.resize('Stay', hero)
                        self.AnimeEnemyRightLeft.blit(self.image, (0, 0))
            else:
                #hero.film = False
                self.resize('Stay', hero)
                self.AnimeEnemyStayLeft.blit(self.image, (0, 0))

        else:
            end = 23
            if hero.side == -1:
                self.resize('Stay', hero)
                self.animcount += 1
                #self.image.fill((0, 255, 0))
                if self.animcount <= end:
                    self.image.blit(self.animationL_D[self.animcount // 8], (0, 0))
                    self.image.set_colorkey((0, 255, 0))
            elif hero.side == 1:
                self.resize('Stay', hero)
                self.animcount += 1
                #self.image.fill((0, 255, 0))
                if self.animcount <= end:
                    self.image.blit(self.animationR_D[self.animcount // 8], (0, 0))
                    self.image.set_colorkey((0, 255, 0))


    def die(self):
        self.isdie = True  # включу запутанного моба
        self.xvel = 0
        self.yvel = 0


class Player(Sprite):
    def __init__(self, x, y, sound, width=105, height=117):
        Sprite.__init__(self)
        self.take_AUDIO = sound.TAKE_AUDIO
        self.step_AUDIO = sound.STEP_AUDIO
        self.step2_AUDIO = sound.STEP2_AUDIO
        self.image = Surface((width, height))
        self.rect = self.image.get_rect()
        self.spawn = '@'
        self.level = 0
        self.bottom = self.rect.bottom
        self.chat = False
        self.rect.move(x, y)
        self.anim = ''
        self.old_anim = ''
        self.film = False
        self.side = 1
        self.yvel = 0
        self.gift = False
        self.audio_step_count = 0
        self.xvel = 0
        self.onGround = False
        self.count = 0
        self.helth = 10
        self.fight = False
        self.jump = False
        self.serf = False
        self.moster = False
        self.y_basic = y
        self.y_take = y + self.rect.height - 140
        self.trees = []
        self.image.set_colorkey((0, 0, 0))
        self.animationR = []
        self.animationL = []
        self.who_kill = []
        self.old_time_on = 0
        self.death = False
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
            'stay': (99, 108),
            'jump': (88, 90),
            'climb': (47, 144),
            'go_strike': (120, 117),
            'die': (127, 109),
            'take': (99, 108)

        }


        self.AnimeGoStrikeRight = PygAnimation(Work(ANIMATION_HERO_GO_STRIKE_RIGHT))
        self.AnimeGoStrikeLeft = PygAnimation(Work(ANIMATION_HERO_GO_STRIKE_LEFT))
        self.AnimeStrikeRight = PygAnimation(Work(ANIMATION_HERO_STRIKE_RIGHT))
        self.AnimeStrikeLeft = PygAnimation(Work(ANIMATION_HERO_STRIKE_LEFT))

        self.AnimeStayLeft = PygAnimation(Work(ANIMATION_HERO_STAY_LEFT, True, 80))
        self.AnimeStayRight = PygAnimation(Work(ANIMATION_HERO_STAY_RIGHT, True, 80))
        self.AnimeGoRight = PygAnimation(Work(ANIMATION_HERO_GO_RIGHT))
        self.AnimeGoLeft = PygAnimation(Work(ANIMATION_HERO_GO_LEFT))
        self.AnimeJumpRight = PygAnimation(Work(ANIMATION_HERO_JUMP_RIGHT))
        self.AnimeJumpLeft = PygAnimation(Work(ANIMATION_HERO_JUMP_LEFT))
        self.AnimeClimbRight = PygAnimation(Work(ANIMATION_HERO_CLIMP_RIGHT))
        self.AnimeClimbLeft = PygAnimation(Work(ANIMATION_HERO_CLIMP_LEFT))
        self.AnimeUseRight = PygAnimation(Work(ANIMATION_HERO_TAKE_RIGHT))
        self.AnimeUseLeft = PygAnimation(Work(ANIMATION_HERO_TAKE_LEFT))

        # on
        self.AnimeUseRight.play()
        self.AnimeUseLeft.play()
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
        #self.x = x
        #self.y = y

    def films(self):
        self.film = True
        self.xvel = 0
        self.yvel = 0

    def change_coord(self, who):
        if who == 'x':
            #self.x += self.xvel
            self.rect = self.rect.move(self.xvel, 0)

        elif who == 'y':
            #self.y += self.yvel
            self.rect = self.rect.move(0, self.yvel)


    def resize(self, name):
        self.image = Surface(self.data_wh[name])
        self.image.set_colorkey((0, 255, 0))
        self.image.fill((0, 255, 0))

    def update(self, left, right, up, platforms, teleports, tree, enemy, use, screen, BOSS, monster, strike, dialog, window_dialog):
        global SPEED

        # animation
        self.image.set_colorkey((0, 255, 0))
        self.image.fill((0, 255, 0))
        # лево право
        if self.helth <= 0:
            self.film = True
        if self.chat:
            self.resize('stay')
            self.xvel = 0
            self.yvel = 0
            if self.side == 1:
                self.AnimeStayRight.blit(self.image, (0, 0))
            if self.side == -1:
                self.AnimeStayLeft.blit(self.image, (0, 0))
        elif window_dialog.phrase == len(window_dialog.who):
            pass
        elif not self.film:
            die_anim = False
            if left or right:
                if self.onGround:
                    self.step_AUDIO.play()
                    self.step2_AUDIO.play()
                elif not self.onGround:
                    self.step_AUDIO.stop()
                    self.step2_AUDIO.stop()
                if left and right:
                    self.xvel = 0
                elif left or right:
                    if left and not self.serf:
                        self.xvel = -SPEED
                        self.side = -1
                    #elif left and self.serf:
                        #self.yvel = -SPEED
                    elif right and not self.serf:
                        self.xvel = SPEED
                        self.side = 1
                    #elif right and self.serf:
                        #self.yvel = SPEED
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
                    elif left and self.serf:
                        self.resize('climb')
                        self.AnimeClimbLeft.blit(self.image, (0, 0))
                    elif right and self.serf:
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
                    elif left and self.onGround and use:
                        self.resize('take')
                        self.AnimeUseLeft.blit(self.image, (0, 0))
                    elif right and self.onGround and use:
                        self.resize('take')
                        self.AnimeUseRight.blit(self.image, (0, 0))
                    elif self.side == 1 and self.onGround and use:
                        self.resize('take')
                        self.AnimeUseLeft.blit(self.image, (0, 0))
                    elif self.side == -1 and self.onGround and use:
                        self.resize('take')
                        self.AnimeUseRight.blit(self.image, (0, 0))
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
                self.audio_step_count = 0
                self.step_AUDIO.stop()
                self.step2_AUDIO.stop()
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
                        if self.side == -1 and self.onGround and use:
                            self.resize('take')
                            self.AnimeUseLeft.blit(self.image, (0, 0))
                        elif self.side == 1 and self.onGround and use:
                            self.resize('take')
                            self.AnimeUseRight.blit(self.image, (0, 0))
                        elif self.side == 1 and not strike:
                            self.resize('stay')
                            self.AnimeStayRight.blit(self.image, (0, 0))
                        elif self.side == -1 and not strike and not use:
                            self.resize('stay')
                            self.AnimeStayLeft.blit(self.image, (0, 0))
                        elif self.side == 1 and strike and not use:
                            self.resize('strike')
                            self.AnimeStrikeRight.blit(self.image, (0, 0))

                        elif self.side == -1 and strike and not use:
                            self.resize('strike')
                            self.AnimeStrikeLeft.blit(self.image, (0, 0))


        else:
            self.xvel = 0
            self.yvel = 0

            if self.moster:
                pass
            else:
                self.resize('die')
                self.animcount += 1
                end = 182
                if self.side == 1:
                    self.image.blit(self.animationR[self.animcount // 8], (0, 0))
                    if self.animcount >= end:
                        self.film = False
                        self.death = True
                        self.animcount = 0
                        self.level = 0
                        self.helth = 10
                elif self.side == -1:
                    self.image.blit(self.animationL[self.animcount // 8], (0, 0))
                    if self.animcount >= end:
                        self.animcount = 0
                        self.film = False
                        self.death = True
                        self.level = 0
                        self.helth = 10

        # прыжок
        if not self.onGround:
            #if self.yvel < 50:
            #self.yvel += GRAVITY
            if not self.serf:
                self.yvel += GRAVITY

            if up and self.count < 1 and self.yvel > 0 and not self.onGround and not self.film and not self.chat:
                self.count += 1
                self.yvel = -(JUMP_POWER - 1)**2

        if up and self.onGround and not self.film and not self.chat:
            self.jump = True
            self.onGround = False
            self.yvel = -JUMP_POWER**2


        self.onGround = False
        #self.serf = False
        self.change_coord('x')
        self.collide(self.xvel, 0, platforms, up)
        self.change_coord('y')
        self.collide(0, self.yvel, platforms, up)

        answer = self.teleport(self.xvel, 0, teleports, BOSS)
        if not answer:
            self.teleport(0, self.yvel, teleports, BOSS)

        self.enemys(enemy)

        self.Boss(BOSS)

        self.monsters(monster, use)

        self.fight_find(enemy)

        self.dialogs(dialog, window_dialog)

        return self.wooden(tree, use, screen)

    def dialogs(self, dialog, window_dialog):
        a = sprite.Group()
        a.add(self)
        pl = sprite.groupcollide(a, dialog, False, True)
        if len(pl) != 0:
            self.chat = True
            #window_dialog.clear(True)
            window_dialog.dialog_with((pl[self][0].name, pl[self][0].dialog))
        pl.clear()

    def monsters(self, monster, use):
        for pl in monster:
            if self.rect.colliderect(Rect(pl.rect.x-100, pl.rect.y-(540-pl.rect.width), 600, 540)) and use and not pl.death:
                try:
                    del self.trees[0]
                    pl.death = True
                except IndexError:
                    continue

    def fight_find(self, enemy):
        for i in enemy:
            if not i.isdie and type(i) != Enemy2:
                if (i.rect.x <= self.rect.x and self.rect.x - i.rect.x <= 900) or (i.rect.x >= self.rect.x and i.rect.x - self.rect.x <= 900):
                    if (i.rect.y <= self.rect.y and self.rect.y - i.rect.y <= 500) or (i.rect.y >= self.rect.y and i.rect.y - self.rect.y <= 500):
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
        self.trees = []

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
                if not pl.isdie and process_time() - self.old_time_on >= 2:
                    self.old_time_on = process_time()
                    self.helth -= 1
                    if self.helth <= 0:
                        self.who_kill.append(pl)
                    break


    def collide(self, xvel, yvel, platforms, UP):
        pl = sprite.spritecollideany(self, platforms, collided = None)
        if pl != None:
            if pl.name == '-':
                #self.serf = True
                if yvel > 0:
                    #self.serf = False
                    self.onGround = True
                    self.count = 0

                    #self.rect.y = pl.rect.top - self.rect.height  # попытки подравнять спрайт take
                    self.rect.bottom = pl.rect.top
                if yvel < 0:
                    self.yvel = 0

                    self.onGround = False
                    self.rect.top = pl.rect.bottom
                if xvel < 0:
                    self.onGround = True
                    self.serf = True
                    self.jump = False
                    self.rect.left = pl.rect.right
                if xvel > 0:
                    self.onGround = True
                    self.serf = True
                    self.jump = False
                    self.rect.right = pl.rect.left  # пытаемся определить состояние когда включить self.serf пока. При нажатии up ничего не меняется
        if UP:
            self.serf = False



    def wooden(self, tree, use, screen):
        for pl in tree:
            if collide_rect(self, pl):  # текст не отобравжается
                if use and not pl.die:
                    pl.use()
                    self.take_AUDIO.play()
                    self.trees.append(pl)
                if pl.die:
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
        self.image = Surface((width, height)).convert()
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
    def __init__(self, x, y, width, height, name, who=None, tag=True, use=False):
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
        self.image.fill((0, 0, 0))
        self.rect.x = x
        self.rect.y = y
        self.number = [str(i) for i in range(1, 13)]
        self.image.set_colorkey((0, 0, 0))
        if self.name in self.number:
            #self.image.blit(load(f'data\\КПК\\1\\ячейки пустые\\ячейка_{self.name}_выкл.png').convert(), (0, 0))
            if self.name == "1":
                self.image.blit(load('data\\КПК\\1\\грибной_паук_выкл.png').convert(), (0, 0))
            elif self.name == "5":
                self.image.blit(load('data\\КПК\\1\\ёж_выкл.png').convert(), (0, 0))
            elif self.name == "3":
                self.image.blit(load('data\\КПК\\1\\щупальцехват_выкл.png').convert(), (0, 0))

            elif self.name == "6":
                self.image.blit(load('data\\КПК\\1\\\ячейки пустые\\ячейка_6_выкл.png').convert(), (0, 0))
            """elif self.name == "2":
                self.image.blit(load('data\\КПК\\1\\текст\\грибная_королева.png').convert(), (0, 0))
            elif self.name == "3":
                self.image.blit(load('data\\КПК\\1\\текст\\овраговый_щупальцехват.png').convert(), (0, 0))
            elif self.name == "4":
                self.image.blit(load('data\\КПК\\1\\текст\\сучий_жук.png').convert(), (0, 0))"""

        elif self.name == 'Exit':
            self.image.blit(load('data\\МЕНЮ\\кнопка_выход_выкл.png').convert(), (0, 0))
        elif self.name == 'Play':
            self.image.blit(load('data\\МЕНЮ\\кнопка_новая_игра_выкл.png').convert(), (0, 0))
        elif self.name == 'Settings':
            self.image.blit(load('data\\МЕНЮ\\кнопка_настройки_выкл.png').convert(), (0, 0))
        elif self.name == 'Shop':
            self.image.blit(load('data\\МЕНЮ\\кнопка_магазин_выкл.png').convert(), (0, 0))
        elif self.name == 'Continue':
            self.image.blit(load('data\\МЕНЮ\\кнопка_продолжить_выкл.png').convert(), (0, 0))
        elif self.name == '0':
            self.image.blit(load('data\\НАСТРОЙКИ\\индикатор_1_выкл.png').convert(), (0, 0))
        elif self.name == '25':
            self.image.blit(load('data\\НАСТРОЙКИ\\индикатор_2_выкл.png').convert(), (0, 0))
        elif self.name == '50':
            self.image.blit(load('data\\НАСТРОЙКИ\\индикатор_3_выкл.png').convert(), (0, 0))
        elif self.name == '75':
            self.image.blit(load('data\\НАСТРОЙКИ\\индикатор_4_выкл.png').convert(), (0, 0))
        elif self.name == '100':
            self.image.blit(load('data\\НАСТРОЙКИ\\индикатор_5_выкл.png').convert(), (0, 0))
        elif self.name == 'назад':
            self.image.blit(load('data\\НАСТРОЙКИ\\назад_выкл.png').convert(), (0, 0))
        elif self.name == 'KPK':
            self.image.blit(load('data\\интерфейс\\иконки и кнопки\\КПК_вкл.png').convert(), (0, 0))
        elif self.name == 'back':
            self.image.blit(load('data\\интерфейс\\иконки и кнопки\\назад_выкл.png').convert(), (0, 0))
        elif self.name == 'menu_ink':
            self.image.blit(load('data\\интерфейс\\иконки и кнопки\\дом_вкл.png').convert(), (0, 0))  # чёт не так с этими кнопками




    def mouse(self, around):
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))

        if around:
            if self.name in self.number:
                #self.image.blit(load(f'data\\КПК\\1\\ячейки пустые\\ячейка_{self.name}_выкл.png').convert(), (0, 0))
                if self.name == "1":
                    self.image.blit(load('data\\КПК\\1\\грибной_паук_выкл.png').convert(), (0, 0))
                elif self.name == "5":
                    self.image.blit(load('data\\КПК\\1\\ёж_выкл.png').convert(), (0, 0))
                elif self.name == "3":
                    self.image.blit(load('data\\КПК\\1\\щупальцехват_выкл.png').convert(), (0, 0))

                elif self.name == "6":
                    self.image.blit(load('data\\КПК\\1\\\ячейки пустые\\ячейка_6_выкл.png').convert(), (0, 0))
                """elif self.name == "2":
                    self.image.blit(load('data\\КПК\\1\\текст\\грибная_королева.png').convert(), (0, 0))
                elif self.name == "3":
                    self.image.blit(load('data\\КПК\\1\\текст\\овраговый_щупальцехват.png').convert(), (0, 0))
                elif self.name == "4":
                    self.image.blit(load('data\\КПК\\1\\текст\\сучий_жук.png').convert(), (0, 0))"""
            elif self.name == 'Exit':
                self.image.blit(load('data\\МЕНЮ\\кнопка_выход_выкл.png').convert(), (0, 0))
            elif self.name == 'Play':
                self.image.blit(load('data\\МЕНЮ\\кнопка_новая_игра_выкл.png').convert(), (0, 0))
            elif self.name == 'Settings':
                self.image.blit(load('data\\МЕНЮ\\кнопка_настройки_выкл.png').convert(), (0, 0))
            elif self.name == 'Shop':
                self.image.blit(load('data\\МЕНЮ\\кнопка_магазин_выкл.png').convert(), (0, 0))
            elif self.name == 'Continue':
                self.image.blit(load('data\\МЕНЮ\\кнопка_продолжить_выкл.png').convert(), (0, 0))
            elif self.name == '0':
                self.image.blit(load('data\\НАСТРОЙКИ\\индикатор_1_выкл.png').convert(), (0, 0))
            elif self.name == '25':
                self.image.blit(load('data\\НАСТРОЙКИ\\индикатор_2_выкл.png').convert(), (0, 0))
            elif self.name == '50':
                self.image.blit(load('data\\НАСТРОЙКИ\\индикатор_3_выкл.png').convert(), (0, 0))
            elif self.name == '75':
                self.image.blit(load('data\\НАСТРОЙКИ\\индикатор_4_выкл.png').convert(), (0, 0))
            elif self.name == '100':
                self.image.blit(load('data\\НАСТРОЙКИ\\индикатор_5_выкл.png').convert(), (0, 0))
            elif self.name == 'назад':
                self.image.blit(load('data\\НАСТРОЙКИ\\назад_выкл.png').convert(), (0, 0))
            elif self.name == 'KPK':
                self.image.blit(load('data\\интерфейс\\иконки и кнопки\\КПК_вкл.png').convert(), (0, 0))
            elif self.name == 'menu_ink':
                self.image.blit(load('data\\интерфейс\\иконки и кнопки\\дом_вкл.png').convert(), (0, 0))
            elif self.name == 'back':
                self.image.blit(load('data\\интерфейс\\иконки и кнопки\\назад_выкл.png').convert(), (0, 0))

            font = Font('pixle_font.ttf', 30)
            txt = font.render(self.name, 1, self.WHITE)
            text_x = self.width // 2 - txt.get_width() // 2
            text_y = self.height // 2 - txt.get_height() // 2
            text_w = txt.get_width()
            text_h = txt.get_height()
            if self.tag:
                self.image.blit(txt, (text_x, text_y))
                rect(self.image, self.WHITE, (self.rect.x+3, self.rect.y+3, self.rect.width-3, self.rect.height-3), 3)
        else:
            if self.name in self.number:
                #self.image.blit(load(f'data\\КПК\\1\\ячейки пустые\\ячейка_{self.name}_вкл.png').convert(), (0, 0))
                if self.name == "1":
                    self.image.blit(load('data\\КПК\\1\\грибной_паук_вкл.png').convert(), (0, 0))
                elif self.name == "5":
                    self.image.blit(load('data\\КПК\\1\\ёж_вкл.png').convert(), (0, 0))
                elif self.name == "3":
                    self.image.blit(load('data\\КПК\\1\\щупальцехват_вкл.png').convert(), (0, 0))
                elif self.name == "6":
                    self.image.blit(load('data\\КПК\\1\\\ячейки пустые\\ячейка_6_вкл.png').convert(), (0, 0))

                """elif self.name == "2":
                    self.image.blit(load('data\\КПК\\1\\текст\\грибная_королева.png').convert(), (0, 0))
                elif self.name == "3":
                    self.image.blit(load('data\\КПК\\1\\текст\\овраговый_щупальцехват.png').convert(), (0, 0))
                elif self.name == "4":
                    self.image.blit(load('data\\КПК\\1\\текст\\сучий_жук.png').convert(), (0, 0))"""
            elif self.name == 'Exit':
                self.image.blit(load('data\\МЕНЮ\\кнопка_выход_вкл.png').convert(), (0, 0))
            elif self.name == 'Play':
                self.image.blit(load('data\\МЕНЮ\\кнопка_новая_игра_вкл.png').convert(), (0, 0))
            elif self.name == 'Settings':
                self.image.blit(load('data\\МЕНЮ\\кнопка_настройки_вкл.png').convert(), (0, 0))
            elif self.name == 'Shop':
                self.image.blit(load('data\\МЕНЮ\\кнопка_магазин_выкл.png').convert(), (0, 0))
            elif self.name == 'Continue':
                self.image.blit(load('data\\МЕНЮ\\кнопка_продолжить_вкл.png').convert(), (0, 0))
            elif self.name == '0':
                self.image.blit(load('data\\НАСТРОЙКИ\\индикатор_1_вкл.png').convert(), (0, 0))
            elif self.name == '25':
                self.image.blit(load('data\\НАСТРОЙКИ\\индикатор_2_вкл.png').convert(), (0, 0))
            elif self.name == '50':
                self.image.blit(load('data\\НАСТРОЙКИ\\индикатор_3_вкл.png').convert(), (0, 0))
            elif self.name == '75':
                self.image.blit(load('data\\НАСТРОЙКИ\\индикатор_4_вкл.png').convert(), (0, 0))
            elif self.name == '100':
                self.image.blit(load('data\\НАСТРОЙКИ\\индикатор_5_вкл.png').convert(), (0, 0))
            elif self.name == 'назад':
                self.image.blit(load('data\\НАСТРОЙКИ\\назад_вкл.png').convert(), (0, 0))
            elif self.name == 'KPK':
                self.image.blit(load('data\\интерфейс\\иконки и кнопки\\КПК_выкл.png').convert(), (0, 0))
            elif self.name == 'menu_ink':
                self.image.blit(load('data\\интерфейс\\иконки и кнопки\\дом_выкл.png').convert(), (0, 0))
            elif self.name == 'back':
                self.image.blit(load('data\\интерфейс\\иконки и кнопки\\назад_вкл.png').convert(), (0, 0))

            font = Font('pixle_font.ttf', 30)
            txt = font.render(self.name, 1, self.WHITE)
            text_x = self.width // 2 - txt.get_width() // 2
            text_y = self.height // 2 - txt.get_height() // 2
            text_w = txt.get_width()
            text_h = txt.get_height()
            if self.tag:
                self.image.blit(txt, (text_x, text_y))
                rect(self.image, self.BLACK, (self.rect.x+3, self.rect.y+3, self.rect.width-3, self.rect.height-3), 3)

class Info(Sprite):
    def __init__(self, name):
        Sprite.__init__(self)
        self.name = name
        self.width = 960
        self.height = 540
        self.image = Surface((self.width, self.height))
        self.rect = self.image.get_rect()

        self.image.fill((255, 255, 255))
        self.rect.x = 0
        self.rect.y = 0
        self.could = True
        self.txt = ''

        try:
            if name == "1":
                self.Anime = PygAnimation(Work(ANIMATION_INFO_SPIDER, True, 500))
            elif name == "2":
                self.Anime = PygAnimation(Work(ANIMATION_INFO_BIGSPIDER, True, 500))
            elif name == "3":
                self.Anime = PygAnimation(Work(ANIMATION_INFO_TENTACLE, True, 500))
            elif name == "4":
                self.Anime = PygAnimation(Work(ANIMATION_INFO_PIDOR, True, 500))
            elif name == "5":
                self.Anime = PygAnimation(Work(ANIMATION_INFO_ESJH, True, 500))
                self.txt = 'data\\КПК\\1\\текст\\ёж.png'
            elif name == "6":
                self.Anime = PygAnimation(Work(ANIMATION_INFO_YELLOW, True, 500))
            elif name == "7":
                self.Anime = PygAnimation(Work(ANIMATION_INFO_BLUE, True, 500))
            elif name == "8":
                self.Anime = PygAnimation(Work(ANIMATION_INFO_LIFE, True, 500))

            self.Anime.play()
        except AttributeError:
            self.could = False


    def life_die(self, live):
        if not self.could:
            live = False
        if live:
            self.Anime.blit(self.image, (0, 0))
            return True
        else:
            self.kill()
            return False
