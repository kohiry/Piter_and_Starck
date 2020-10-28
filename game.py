import pygame, sys
from screeninfo import get_monitors
from level import map as MAP
import object
import time
from pyganim import PygAnimation
from pygame.locals import *
import asyncio


pygame.init()

# audio
sound = object.Sound()
#setting
fight = False
SIZE = WIDTH, HEIGHT = 960, 540
BACK_SIZE = int(1080/1.5)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)

FONT = "pixle_font.ttf"
UP = False
ball = 0
LEFT = False
RIGHT = False
E = False
F = False
take_barries = False
Boss_spawn = False
First_on_audio = 0
count_audio = 0
Strike = False
first_strike_timer = 0
black_count = 0
after_count = 0
Strike_fast = False
for_strike_count_time_when_we_see_text = 0
jump_x = ((int(get_monitors()[0].width) - WIDTH) // 2)
jump_y = ((int(get_monitors()[0].height) - HEIGHT) // 2)

# состояния
start_game = True
loading = False
start_part = False
menu = False
map = False
scene_enemy = False
scene_enemy3 = False
settings = False
after_words = False
KPK = False
scene_enemy2 = False

# map
location = 1
draw_loc = 1

#startet_obj
group_draw = pygame.sprite.Group()
group_interface = pygame.sprite.Group()
group_platform = pygame.sprite.Group()
batton_in_KPK = pygame.sprite.Group()
start_game_gr = pygame.sprite.Group()
HERO = object.Player(10, 10, sound)
BOSS = object.Boss(10, 10)
health_tab = object.Health_tab(415, 10)
#dialog_tab = object.Dialog_Tab(0, 0)
BOSS.new_coord(-100, -100)
StartScene = object.Start()
start_game_gr.add(StartScene)
platforms = []
teleports = []
enemy = []
all_obj = []
matrix = []
tree = []
balls = []
game = []
monster = []
info = []
button = []
x_hero, y_hero = 0, 0
lens = 54

animation_balck = []
# затемнение для катсцен
for i in [f'data\\интерфейс\\затенение_{str(j)}.png' for j in range(1, 7)]:
    animation_balck.append(pygame.image.load(i))




def make_level(level):
    global all_obj
    x, y = 0, 0

    def platform(row, col, obj):
        global all_obj
        if obj == object.Teleport_BOSS:
            pl = obj(x, y, lens*10, lens)
            game.append(pl)
        else:
            pl = obj(x, y, lens, lens)
            game.append(pl)
        #group_draw.add(pl)
        if object.Platform == obj:
            group_platform.add(pl)
            platforms.append(pl)
            game.append(pl)
        else:
            teleports.append(pl)
            game.append(pl)

    #width =
    for row in level:
        for col in row:
            if col == ' ':
                all_obj.append('')
            else:
                if col in ['-', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'l']:
                    if col == 'q':
                        pl = object.Background(x, y, 'data/фоны/начало.png')
                        group_draw.add(pl)
                        game.append(pl)
                    # горизонталь
                    if col == 'w':
                        pl = object.Background(x, y, 'data/фоны/горизонталь_1.png')
                        group_draw.add(pl)
                        game.append(pl)
                    if col == 'e':
                        pl = object.Background(x, y, 'data/фоны/горизонталь_2.png')
                        group_draw.add(pl)
                        game.append(pl)
                    if col == 'l':
                        pl = object.Background(x, y, 'data/фоны/началостарт.png')
                        group_draw.add(pl)
                        game.append(pl)
                    # поворот
                    if col == 'r':
                        pl = object.Background(x, y, 'data/фоны/поворот_1.png')
                        group_draw.add(pl)
                        game.append(pl)
                    if col == 't':
                        pl = object.Background(x, y, 'data/фоны/поворот_2.png')
                        group_draw.add(pl)
                        game.append(pl)
                    if col == 'y':
                        pl = object.Background(x, y, 'data/фоны/поворот_3.png')
                        group_draw.add(pl)
                        game.append(pl)
                    if col == 'u':
                        pl = object.Background(x, y, 'data/фоны/поворот_4.png')
                        group_draw.add(pl)
                        game.append(pl)
                    if col == 'f':
                        pl = object.Background(x, y, 'data/фоны/овраг.png')
                        group_draw.add(pl)
                        game.append(pl)
                        pl2 = object.Monster(x+lens*3, y+lens*6)
                        game.append(pl2)
                        group_draw.add(pl2)
                        monster.append(pl2)
                    if col == 'i':
                        pl = object.Background(x, y, 'data/фоны/вертикаль.png')
                        group_draw.add(pl)
                        game.append(pl)
                    if col == 'p':
                        pl = object.Background(x, y, 'data/фоны/конец.png')
                        group_draw.add(pl)
                        game.append(pl)
                    if col == 'a':
                        pl = object.Tree(x, y, 'data/фоны/развилка_вниз.png', 'data/фоны/развилка_вниз_без_ягод.png')
                        group_draw.add(pl)
                        tree.append(pl)
                        game.append(pl)
                    if col == 's':
                        pl = object.Tree(x, y, 'data/фоны/развилка_наверх.png', 'data/фоны/развилка_наверх_без_ягод.png')
                        group_draw.add(pl)
                        game.append(pl)
                        tree.append(pl)
                    if col == 'd':
                        pl = object.Tree(x, y, 'data/фоны/развилка_направо.png', 'data/фоны/развилка_направо_без_ягод.png')
                        group_draw.add(pl)
                        game.append(pl)
                        tree.append(pl)
                    platform(row, col, object.Platform)

                if (col == '@' and HERO.spawn == '@') or (col == '#' and HERO.spawn == '#') or (col == '%' and HERO.spawn == '%'):
                    HERO.new_coord(x, y)
                if col == "^":
                    platform(row, col, object.Teleport_A)
                if col == "v":
                    platform(row, col, object.Teleport_B)
                if col == "!":
                    platform(row, col, object.Teleport_BOSS)
                if col == "?":
                    platform(row, col, object.Teleport_COME)
                if col == "&":
                    pl = object.Enemy(x, y, sound)
                    enemy.append(pl)
                    game.append(pl)
                if col == "$":
                    pl = object.Enemy2(x, y, sound)
                    enemy.append(pl)
                    game.append(pl)
                if col == "$":
                    BOSS.new_coord(x, y)
                    BOSS.isdie = False
                if col == "_":
                    pass

            x += lens
        y += lens
        x = 0
    for pl in enemy:
        group_draw.add(pl)
    game.reverse()


middle = ((int(get_monitors()[0].width) - WIDTH)//2, (int(get_monitors()[0].height) - HEIGHT)//2)
#middle = ((1080 - WIDTH)//2, (720 - HEIGHT)//2)
#size = width, height = 1080, 720
#window = pygame.display.set_mode(size)
window = pygame.display.set_mode((0, 0), HWSURFACE| DOUBLEBUF| FULLSCREEN)
screen = pygame.Surface(SIZE)
pygame.display.set_caption('Gay game')


#camera
class Camera:
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def new(self, width, height):
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def camera_func(camera, target_rect):
    l = -target_rect.x + SIZE[0]//2
    t = -target_rect.y + SIZE[1]//2
    w, h = camera.width, camera.height

    l = min(0, l)
    l = max(-(camera.width - SIZE[0]), l)
    t = max(-(camera.height - SIZE[1]), t)
    t = min(0, t)
    return pygame.Rect(l, t, w, h)


camera = Camera(camera_func, 1, 1)

def camera_level(place):
    global Boss_spawn
    for e in group_draw:
        e.kill()
    for e in group_interface:
        e.kill()
    platforms.clear()
    teleports.clear()
    enemy.clear()
    tree.clear()
    monster.clear()
    button.clear()
    BOSS.isdie = True
    Boss_spawn = False
    total_level_width = len(MAP[place][0])*lens
    total_level_height = len(MAP[place])*lens
    camera.new(total_level_width, total_level_height)
    make_level(MAP[place])
    MAP.clear()
    if place == 'level69':
        group_draw.add(BOSS)
        Boss_spawn = True
    group_draw.add(HERO)

def draw():
    global draw_loc, location
    screen.fill((0, 0, 0))
    last_level = location
    location = HERO.level
    try:
        if draw_loc != location:
            draw_loc = location
            #camera_level(f'level{str(location)}')

    except KeyError:
        HERO.level = last_level

    camera.update(HERO)
    for e in group_draw:
        coord = camera.apply(e)
        obl = 600

        if pygame.Rect(HERO.rect.topleft[0]-obl, HERO.rect.topleft[1]-obl, 2*obl, 2*obl).colliderect(e.rect):
            screen.blit(e.image, coord)

    white = (255, 255, 255)
    if take_barries:
        font = pygame.font.Font('pixle_font.ttf', 20)
        txt = font.render('нажми на ПКМ чтобы собрать плоды', 1, white)
        screen.blit(txt, (50, 50))
    if Strike_fast:
        font = pygame.font.Font('pixle_font.ttf', 40)
        txt = font.render('Заряжается...', 1, white)
        rect = HERO.image.get_rect()
        screen.blit(txt, (WIDTH//2, HEIGHT-40))
    group_interface.draw(screen)
    pygame.display.flip()
    window.blit(screen, middle)

def create_button():
    button.clear()
    for e in group_draw:
        e.kill()
    for e in group_interface:
        e.kill()
    w, h = 302, 64
    button.append(object.Button(328, 145, w, h, 'Play', tag=False))
    button.append(object.Button(328, 230, w, h, 'Shop', tag=False))
    button.append(object.Button(328, 315, w, h, 'Settings', tag=False))
    button.append(object.Button(328, 400, w, h, 'Exit', tag=False))
    group_draw.add(object.Background(0, 0, 'data\МЕНЮ\меню_фон.png'))
    for i in button:
        group_draw.add(i)

def create_button_2():
    button.clear()
    for e in group_draw:
        e.kill()
    for e in group_interface:
        e.kill()
    w, h = 302, 64
    button.append(object.Button(328, 145, w, h, 'Continue', tag=False))
    button.append(object.Button(328, 225, w, h, 'Shop', tag=False))
    button.append(object.Button(328, 315, w, h, 'Settings', tag=False))
    button.append(object.Button(328, 400, w, h, 'Exit', tag=False))
    group_draw.add(object.Background(0, 0, 'data\МЕНЮ\меню_фон.png'))
    for i in button:
        group_draw.add(i)


def create_button_map():
    button.clear()
    for e in group_draw:
        e.kill()
    for e in group_interface:
        e.kill()
    w, h = 46, 46
    button.append(object.Button(20, 10, w, h, 'back', tag=False))
    for i in button:
        group_draw.add(i)

def create_button_setting():
    button.clear()
    for e in group_draw:
        e.kill()
    for e in group_interface:
        e.kill()
    w, h = 113, 59
    music = 100
    sound = 350
    name_a = 'music'
    name_b = 'sound'
    name_c = 'menu'
    # music
    button.append(object.Button(70, music, w, h, '0', name_a))
    button.append(object.Button(183, music, w, h, '25', name_a))
    button.append(object.Button(293, music, w, h, '50', name_a))
    button.append(object.Button(402, music, w, h, '75', name_a))
    button.append(object.Button(512, music, w, h, '100', name_a))

    # sound
    button.append(object.Button(70, sound, w, h, '0', name_b))
    button.append(object.Button(183, sound, w, h, '25', name_b))
    button.append(object.Button(293, sound, w, h, '50', name_b))
    button.append(object.Button(402, sound, w, h, '75', name_b))
    button.append(object.Button(512, sound, w, h, '100', name_b))

    # menu
    button.append(object.Button(760, 420, 135, 68, 'назад', name_c, False))
    group_draw.add(object.Background(0, 0, 'data\\НАСТРОЙКИ\\фон.png'))
    for i in button:
        group_draw.add(i)

def sound_correct(number, name):
    level = 0
    if name == "music":
        if number == '0':
            level = 0
        if number == '25':
            level = 0.10
        if number == '50':
            level = 0.25
        if number == '75':
            level = 0.45
        if number == '100':
            level = 0.5
        sound.BACK_AUDIO.set_volume(level)
        sound.START_AUDIO.set_volume(level)
        sound.CUTSCENE_AUDIO.set_volume(level)
        sound.BACK2_AUDIO.set_volume(level)
        sound.MENU_AUDIO.set_volume(level)
        sound.FIGHT_AUDIO.set_volume(level)
        sound.BACK_AFTER_WORDS.set_volume(level)
    elif name == "sound":
        if number == '0':
            level = 0
        if number == '25':
            level = 0.10
        if number == '50':
            level = 0.25
        if number == '75':
            level = 0.45
        if number == '100':
            level = 0.5
        sound.USE_AUDIO.set_volume(level)
        sound.DAMAGE_AUDIO.set_volume(level)
        sound.STRIKE_AUDIO.set_volume(level)
        sound.TAKE_AUDIO.set_volume(level)
        sound.BACK2_AUDIO.set_volume(level)
        sound.STEP_AUDIO.set_volume(level)
        sound.STEP2_AUDIO.set_volume(level)
        HERO.step_AUDIO.set_volume(level)
        HERO.step2_AUDIO.set_volume(level)
        for i in sound.SPIDER_AUDIO:
            i.set_volume(level)
        sound.BUTTON.set_volume(level)


if menu:
    create_button()
    sound.MENU_AUDIO.play(-1)


if after_words:
    for e in group_draw:
        e.kill()
    button.clear()
    words = object.After_words(HEIGHT)
    words.play(sound.BACK_AFTER_WORDS)
    group_draw.add(words)

if KPK:
    x_1 = 64
    x_2 = 364
    x_3 = 664
    w, h = 234, 64
    for e in group_draw:
        e.kill()
    button.clear()
    button.append(object.Button(x_1, 140, w, h, '1', tag=False))
    button.append(object.Button(x_1, 230, w, h, '2', tag=False))
    button.append(object.Button(x_1, 320, w, h, '3', tag=False))
    button.append(object.Button(x_1, 408, w, h, '4', tag=False))
    button.append(object.Button(x_2, 140, w, h, '5', tag=False))
    button.append(object.Button(x_2, 230, w, h, '6', tag=False))
    button.append(object.Button(x_2, 320, w, h, '7', tag=False))
    button.append(object.Button(x_2, 408, w, h, '8', tag=False))
    button.append(object.Button(x_3, 140, w, h, '9', tag=False))
    button.append(object.Button(x_3, 230, w, h, '10', tag=False))
    button.append(object.Button(x_3, 320, w, h, '11', tag=False))
    button.append(object.Button(x_3, 408, w, h, '12', tag=False))
    group_draw.add(object.Background(0, 0, r'data\КПК\1\фон.png'))
    for i in button:
        group_draw.add(i)

def KPK_create():
    x_1 = 64
    x_2 = 364
    x_3 = 664
    w, h = 234, 64
    for e in group_draw:
        e.kill()
    for e in group_interface:
        e.kill()
    button.clear()
    button.append(object.Button(x_1, 140, w, h, '1', tag=False))
    button.append(object.Button(x_1, 230, w, h, '2', tag=False))
    button.append(object.Button(x_1, 320, w, h, '3', tag=False))
    button.append(object.Button(x_1, 408, w, h, '4', tag=False))
    button.append(object.Button(x_2, 140, w, h, '5', tag=False))
    button.append(object.Button(x_2, 230, w, h, '6', tag=False))
    button.append(object.Button(x_2, 320, w, h, '7', tag=False))
    button.append(object.Button(x_2, 408, w, h, '8', tag=False))
    button.append(object.Button(x_3, 140, w, h, '9', tag=False))
    button.append(object.Button(x_3, 230, w, h, '10', tag=False))
    button.append(object.Button(x_3, 320, w, h, '11', tag=False))
    button.append(object.Button(x_3, 408, w, h, '12', tag=False))
    pl = object.Button(20, 10, 48, 48, 'back', tag=False)
    batton_in_KPK.add(pl)
    button.append(pl)
    group_draw.add(object.Background(0, 0, r'data\КПК\1\фон.png'))
    for i in button:
        if i.name != 'back':
            group_draw.add(i)

if start_part:
    sound.START_AUDIO.play(-1)
    for e in group_draw:
        e.kill()
    button.clear()
    Scene = object.Cutscene('data\\катсцены\\1 начало\\начало_', HEIGHT, 'spawn')
    group_draw.add(Scene)

def scene_enemy_def():
    for e in group_draw:
        e.kill()
    platforms.clear()
    teleports.clear()
    enemy.clear()
    tree.clear()
    monster.clear()
    button.clear()
    BOSS.isdie = True
    Boss_spawn = False
    button.clear()
    #Scene = object.Cutscene('data\\катсцены\\5 грибной паук\\грибной_паук_проигрыш.png', HEIGHT, 'enemy')
    #group_draw.add(Scene)

def scene_moster():
    for e in group_draw:
        e.kill()
    platforms.clear()
    teleports.clear()
    enemy.clear()
    tree.clear()
    monster.clear()
    button.clear()
    BOSS.isdie = True
    Boss_spawn = False
    button.clear()
    #Scene = object.Cutscene('data\\катсцены\\5 грибной паук\\грибной_паук_проигрыш.png', HEIGHT, 'enemy')
    #group_draw.add(Scene)

def interface_bytton():
    pl = object.Button(kpk_width, all_height, 46, 39, 'KPK', tag=False)
    pl2 = object.Button(menu_width, all_height, 47, 46, 'menu_ink', tag=False)
    button.append(pl)
    button.append(pl2)
    group_interface.add(pl)
    group_interface.add(pl2)
    group_interface.add(health_tab)
    #group_interface.add(dialog_tab)
    group_draw.add(HERO)

if start_game:
    StartScene.time = time.process_time()

running = True
clock = pygame.time.Clock()
pygame.init()

while running:
    #pygame.mouse.set_visible(False)  # скрывает мышь
    if start_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if StartScene.change:
                        StartScene.change = False
                    elif not StartScene.change:
                        start_game = False
                        start_part = True
                        sound.START_AUDIO.play(-1)
                        for e in group_draw:
                            e.kill()
                        button.clear()
                        Scene = object.Cutscene('data\\катсцены\\1 начало\\начало_', HEIGHT, 'spawn')
                        group_draw.add(Scene)

        screen.fill((255, 255, 255))
        if (time.process_time() - StartScene.time) <= 4 and StartScene.change != False:
            StartScene.upd(True)
        elif (time.process_time() - StartScene.time) <= 4 and StartScene.change == False:
            #start_part = True
            StartScene.upd(False)

        elif (time.process_time() - StartScene.time) > 4 and StartScene.change == False:
            start_game = False
            start_part = True
            sound.START_AUDIO.play(-1)
            for e in group_draw:
                e.kill()
            button.clear()
            Scene = object.Cutscene('data\\катсцены\\1 начало\\начало_', HEIGHT, 'spawn')
            group_draw.add(Scene)
        else:
            if StartScene.change != False:
                StartScene.change = False
                StartScene.time = time.process_time()
        if start_game:
            start_game_gr.draw(screen)
            window.blit(screen, middle)
            pygame.display.flip()
            clock.tick(60)




    elif KPK:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    KPK = False
                    loading = True
                    sound.MENU_AUDIO.stop()
                    button.clear()
                    after_count = 0
                    for e in group_draw:
                        e.kill()
                    for e in group_interface:
                        e.kill()
                if event.key == pygame.K_k:
                    KPK = False
                    loading = True
                    sound.MENU_AUDIO.stop()
                    button.clear()
                    after_count = 0
                    for e in group_draw:
                        e.kill()
                    for e in group_interface:
                        e.kill()
            if event.type == pygame.MOUSEMOTION:
                for i in button:
                    if i.rect.collidepoint((event.pos[0] - jump_x, event.pos[1] - jump_y)):
                        i.mouse(False)
                    else:
                        i.mouse(True)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    if len(info) == 0:
                        for i in button:
                            if i.rect.collidepoint((event.pos[0] - jump_x, event.pos[1] - jump_y)):
                                if i.name != 'back':
                                    pl = object.Info(i.name)
                                    info.append(pl)
                                    group_draw.add(pl)
                                else:
                                    KPK = False
                                    loading = True
                                    sound.MENU_AUDIO.stop()
                                    button.clear()
                                    after_count = 0
                                    for e in group_draw:
                                        e.kill()
                                    for e in group_interface:
                                        e.kill()
                                    i.kill()
                    else:
                        for i in batton_in_KPK:
                            if i.rect.collidepoint((event.pos[0] - jump_x, event.pos[1] - jump_y)):
                                if len(info) > 0:
                                    info[0].life_die(False)
                                info.clear()


                if event.button == 3:
                    if len(info) > 0:
                        info[0].life_die(False)
                    info.clear()


        screen.fill((255, 255, 255))
        if len(info) > 0:
            if not info[0].life_die(True):
                info.clear()
        group_draw.draw(screen)
        batton_in_KPK.draw(screen)
        window.blit(screen, middle)
        pygame.display.flip()
        clock.tick(60)

    elif loading:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        group_draw.draw(screen)
        kpk_width = 910
        menu_width = 10
        all_height = 10
        start_game_gr.draw(screen)
        window.blit(screen, middle)
        pygame.display.flip()
        if (time.process_time() - StartScene.time) <= 4:
            StartScene.upd(True)
        else:
            loading = False
            menu = False
            camera_level('level1')
            interface_bytton()
        clock.tick(60)

    elif after_words:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False



        screen.fill((255, 255, 255))
        if after_count < 2:
            after_count+= 1
        if not words.update():
            running = False
        group_draw.draw(screen)
        window.blit(screen, middle)
        pygame.display.flip()
        clock.tick(60)

    elif scene_enemy:
        inf = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEMOTION:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and black_count > 47:
                    running = False
                    #inf = True



        screen.fill((255, 255, 255))
        screen.blit(pygame.image.load('data\\катсцены\\5 грибной паук\\грибной_паук_проигрыш.png').convert(),(0, 0))
        #group_draw.draw(screen)
        black_count += 1
        if black_count <= 47:
            screen.blit(animation_balck[black_count // 8], (0, 0))
        window.blit(screen, middle)
        #Scene.upd()

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    elif scene_enemy2:
        inf = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEMOTION:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and black_count > 47:
                    running = False
                    #inf = True



        screen.fill((255, 255, 255))
        screen.blit(pygame.image.load('data\\катсцены\\6 ёж\\ёж_проигрыш.png').convert(),(0, 0))
        black_count += 1
        if black_count <= 47:
            screen.blit(animation_balck[black_count // 8], (0, 0))
        group_draw.draw(screen)
        window.blit(screen, middle)
        #Scene.upd()

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    elif scene_enemy3:
        inf = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEMOTION:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and black_count > 47:
                    running = False
                    #inf = True




        screen.fill((255, 255, 255))

        screen.blit(pygame.image.load('data\\катсцены\\2 тентакли\\тентакли.png').convert(), (0, 0))
        black_count += 1
        if black_count <= 47:
            screen.blit(animation_balck[black_count // 8], (0, 0))
        #group_draw.draw(screen)
        window.blit(screen, middle)
        #Scene.upd()

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    elif start_part:
        inf = False
        skip = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    skip = True
                if event.key == pygame.K_a:
                    if Scene.count != 1:
                        Scene.count = 1
                        Scene.lock = 0
                        Scene.anim = False
                        Scene.animcount = 0
                        Scene.image = pygame.image.load('data\\катсцены\\1 начало\\начало_1.png').convert()
                        Scene.image.fill((0,0,0))
                if event.key == pygame.K_d:
                    Scene.lock = 1
                    inf = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Scene.lock = 1
                    inf = True

        if skip:
            sound.START_AUDIO.stop()
            menu = True
            start_part = False
            create_button()
            sound.MENU_AUDIO.play(-1)
        else:
            screen.fill((255, 255, 255))
            group_draw.draw(screen)
            window.blit(screen, middle)
            if inf:
                if Scene.upd():
                    sound.START_AUDIO.stop()
                    menu = True
                    start_part = False
                    create_button()
                    sound.MENU_AUDIO.play(-1)
            if Scene.count in [1, 4]:
                Scene.upd()

            pygame.display.flip()
            pygame.time.Clock().tick(60)

    elif settings:
        First_on_audio = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEMOTION:
                for i in button:
                    if i.rect.collidepoint((event.pos[0] - jump_x, event.pos[1] - jump_y)):  # добавить залипание выбранной кнопки звука
                        i.mouse(False)
                    else:
                        i.mouse(True)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 or event.button == 3:
                    for i in button:
                        if i.rect.collidepoint((event.pos[0] - jump_x, event.pos[1] - jump_y)):
                            if i.who == 'music' or i.who == 'sound':
                                sound_correct(i.name, i.who)
                            if i.name == 'назад':
                                menu = True
                                settings = False
                                if len(game) != 0:
                                    create_button_2()
                                else:
                                    create_button()
                            sound.BUTTON.play()


        screen.fill((255, 255, 255))
        group_draw.draw(screen)
        font = pygame.font.Font('pixle_font.ttf', 50)
        txt = font.render('Music', 1, (255, 255, 255))
        screen.blit(txt, (WIDTH//3 - 250, 20))
        font = pygame.font.Font('pixle_font.ttf', 50)
        txt = font.render('Sound', 1, (255, 255, 255))
        screen.blit(txt, (WIDTH//3 - 250, 270))

        window.blit(screen, middle)
        pygame.display.flip()
        clock.tick(60)

    elif menu:
        First_on_audio = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if len(game) != 0:
                        menu = False
                        button.clear()
                        for e in group_draw:
                            e.kill()
                        for e in group_interface:
                            e.kill()
                        for e in enemy:
                            e.kill()
                        for i in game:
                            if type(i) != object.Platform:  # не понятный баг с исчезновение пауков
                                group_draw.add(i)
                        for i in enemy:
                            i.kill()
                            group_draw.add(i)
                        interface_bytton()
                        break
            if event.type == pygame.MOUSEMOTION:
                for i in button:
                    if i.rect.collidepoint((event.pos[0] - jump_x, event.pos[1] - jump_y)):
                        i.mouse(False)
                    else:
                        i.mouse(True)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 or event.button == 3:
                    for i in button:
                        if i.rect.collidepoint((event.pos[0] - jump_x, event.pos[1] - jump_y)):
                            if i.name == 'Play':
                                menu = False
                                loading = True
                                sound.MENU_AUDIO.stop()
                                button.clear()
                                after_count = 0
                                StartScene.change = True
                                StartScene.time = time.process_time()
                                for e in group_draw:
                                    e.kill()
                                break

                            if i.name == 'Settings':
                                settings = True
                                menu = False
                                create_button_setting()
                                break
                            if i.name == 'Exit':
                                running = False
                                break

                            if i.name == 'Continue':
                                menu = False
                                button.clear()
                                for e in group_draw:
                                    e.kill()
                                for e in group_interface:
                                    e.kill()
                                for e in enemy:
                                    e.kill()
                                for i in game:
                                    if type(i) != object.Platform:  # не понятный баг с исчезновение пауков
                                        group_draw.add(i)
                                for i in enemy:
                                    i.kill()
                                    group_draw.add(i)
                                interface_bytton()
                                break
                            if i.name != 'Shop':
                                sound.BUTTON.play()
                                break
        if menu:
            screen.fill((0, 0, 0))
            group_draw.draw(screen)
            window.blit(screen, middle)
            pygame.display.flip()
            clock.tick(60)
        else:
            if not settings:
                sound.MENU_AUDIO.stop()
                sound.BACK_AUDIO.play(-1)
                sound.BACK2_AUDIO.play(-1)


    elif map:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_m:
                    if len(game) != 0:
                        map = False
                        button.clear()
                        for e in group_draw:
                            e.kill()
                        for e in group_interface:
                            e.kill()
                        for e in enemy:
                            e.kill()
                        for i in game:
                            if type(i) != object.Platform:  # не понятный баг с исчезновение пауков
                                group_draw.add(i)
                        for i in enemy:
                            i.kill()
                            group_draw.add(i)
                        interface_bytton()
                        break

            if event.type == pygame.MOUSEMOTION:
                for i in button:
                    if i.rect.collidepoint((event.pos[0] - jump_x, event.pos[1] - jump_y)):
                        i.mouse(False)
                    else:
                        i.mouse(True)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 or event.button == 3:
                    for i in button:
                        if i.rect.collidepoint((event.pos[0] - jump_x, event.pos[1] - jump_y)):
                            screen.fill((0, 0, 0))
                            if i.name == 'back':
                                if len(game) != 0:
                                    map = False
                                    loading = True
                                    sound.MENU_AUDIO.stop()
                                    button.clear()
                                    after_count = 0
                                    for e in group_draw:
                                        e.kill()

                            pygame.display.flip()
                            sound.BUTTON.play()



        screen.fill((255, 255, 255))
        screen.blit(pygame.image.load('data\\МИНИКАРТА\\миникарта.png').convert(), (0, 0))
        group_draw.draw(screen)
        window.blit(screen, middle)
        pygame.display.flip()
        clock.tick(60)

    else:
        ball = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    UP = True
                if event.key == pygame.K_a:
                    LEFT = True
                if event.key == pygame.K_d:
                    RIGHT = True
                if event.key == pygame.K_ESCAPE:
                    menu = True
                    button.clear()
                    create_button_2()
                    sound.BACK_AUDIO.stop()
                    sound.BACK2_AUDIO.stop()
                    sound.FIGHT_AUDIO.stop()
                    sound.BACK_AFTER_WORDS.stop()
                    sound.MENU_AUDIO.play(-1)
                if event.key == pygame.K_m:
                    map = True
                    button.clear()
                    create_button_map()
                    sound.BACK_AUDIO.stop()
                    sound.BACK2_AUDIO.stop()
                    sound.FIGHT_AUDIO.stop()
                    sound.BACK_AFTER_WORDS.stop()
                    sound.MENU_AUDIO.play(-1)

                if event.key == pygame.K_k:
                    KPK = True
                    button.clear()
                    KPK_create()
                    sound.BACK_AUDIO.stop()
                    sound.BACK2_AUDIO.stop()
                    sound.FIGHT_AUDIO.stop()
                    sound.BACK_AFTER_WORDS.stop()
                    sound.MENU_AUDIO.play(-1)


            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Strike = True
                    ball += 1

                    if int(time.process_time()) - first_strike_timer >= 1:
                        Strike_fast = False
                        first_strike_timer = time.process_time()
                        sound.STRIKE_AUDIO.play()
                        if HERO.side == 1:
                            coord_x = HERO.rect.x + HERO.rect.width
                        if HERO.side == -1:
                            coord_x = HERO.rect.x
                        pl = object.Ball(coord_x, HERO.rect.y + 20, HERO.side)
                        balls.append(pl)
                        group_draw.add(pl)

                    else:
                        Strike_fast = True
                if event.button == 3:
                    sound.USE_AUDIO.play()
                    E = True
                    Strike = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    UP = False
                if event.key == pygame.K_a:
                    LEFT = False
                if event.key == pygame.K_d:
                    RIGHT = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    Strike = False
                if event.button == 3:
                    E = False

            if event.type == pygame.MOUSEMOTION:
                for i in button:
                    if i.rect.collidepoint((event.pos[0] - jump_x, event.pos[1] - jump_y)):
                        i.mouse(False)
                    else:
                        i.mouse(True)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 or event.button == 3:
                    for i in button:
                        if i.rect.collidepoint((event.pos[0] - jump_x, event.pos[1] - jump_y)):
                            screen.fill((0, 0, 0))
                            if i.name == 'KPK':
                                KPK = True
                                button.clear()
                                KPK_create()
                                sound.BACK_AUDIO.stop()
                                sound.BACK2_AUDIO.stop()
                                sound.FIGHT_AUDIO.stop()
                                sound.BACK_AFTER_WORDS.stop()
                                sound.MENU_AUDIO.play(-1)
                            if i.name == 'menu_ink':
                                menu = True
                                Strike = False
                                button.clear()
                                create_button_2()
                                sound.BACK_AUDIO.stop()
                                sound.BACK2_AUDIO.stop()
                                sound.FIGHT_AUDIO.stop()
                                sound.BACK_AFTER_WORDS.stop()
                                sound.MENU_AUDIO.play(-1)

                            pygame.display.flip()
                            sound.BUTTON.play()
        keys = pygame.key.get_pressed()  # движения персонажей под зажим\


        """for i in range(ball):
            pl = object.Ball(200, 200, HERO.side)
            #balls.append(pl)
            #group_draw.add(pl) Потом исправлю фигню с фризом, когда создаю объект болл"""
        draw()
        take_barries = HERO.update(LEFT, RIGHT, UP, group_platform, teleports, tree, enemy, E, screen, BOSS, monster, Strike)
        health_tab.new_image(HERO.helth)
        #dialog_tab.check(enemy, HERO)
        if Strike_fast:
            for_strike_count_time_when_we_see_text += 1
        if for_strike_count_time_when_we_see_text >= 5:
            Strike_fast = False
            for_strike_count_time_when_we_see_text = 0
        way = 1000
        list_collide = lambda x: [Rect(i.rect.x - 500, i.rect.y-250, way, way//2) for i in x]
        b = list_collide(enemy)
        d = list_collide(monster)
        #b.reverse()
        a = HERO.rect.collidelistall(b)
        for i in a:
            enemy[i].AI(HERO, platforms)
        q = HERO.rect.collidelistall(d)
        for i in q:
            monster[i].AI(HERO)

        '''for i in enemy:
            i.AI(HERO, platforms)

        for i in monster:
            i.AI(HERO)'''
        if Boss_spawn:
            BOSS.AI(HERO, platforms)
        if HERO.helth <= 0:
            HERO.respawn()
        for i in balls:
            i.update(platforms, enemy, BOSS)
            if i.die:
                del balls[balls.index(i)]
        if HERO.fight and not fight:
            fight = True
            sound.BACK_AUDIO.stop()
            sound.FIGHT_AUDIO.play(-1)
            sound.BACK2_AUDIO.stop()
        elif not HERO.fight and fight:
            fight = False
            sound.BACK2_AUDIO.play(-1)
            sound.BACK_AUDIO.play(-1)
            sound.FIGHT_AUDIO.stop()


        pygame.display.flip()
        clock.tick(60)

        if HERO.death:
            sound.BACK_AUDIO.stop()
            sound.BACK2_AUDIO.stop()
            sound.FIGHT_AUDIO.stop()
            sound.BACK_AFTER_WORDS.stop()
            sound.MENU_AUDIO.stop()
            sound.CUTSCENE_AUDIO.play(-1)
            black_count = 0
            if len(HERO.who_kill) != 0:
                if type(HERO.who_kill[0]) == object.Enemy:
                    scene_enemy = True
                elif type(HERO.who_kill[0]) == object.Enemy2:
                    scene_enemy2 = True
                    scene_enemy_def()
                elif type(HERO.who_kill[0]) == object.Monster:
                    scene_enemy3 = True
                    scene_moster()


pygame.quit()
quit()
sys.exit()

    # иногда реально ненавижу git hub, снова для нового коммита
