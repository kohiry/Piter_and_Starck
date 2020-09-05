import pygame, sys
from screeninfo import get_monitors
from level import map as MAP
import object
from time import sleep
import time
from pyganim import PygAnimation
from pygame.locals import *



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
after_count = 0
Strike_fast = False
for_strike_count_time_when_we_see_text = 0
jump_x = ((int(get_monitors()[0].width) - WIDTH) // 2)
jump_y = ((int(get_monitors()[0].height) - HEIGHT) // 2)

# состояния
loading = False
start_part = False
menu = False
settings = False
after_words = False
KPK = True

#Start part
#START_PART = object.add_sprite(r'data\катсцены\начало\начало_', 3)
#start_part_animation = PygAnimation(object.Work(START_PART))
#start_part_animation.play()

# map
location = 1
draw_loc = 1

#startet_obj
group_draw = pygame.sprite.Group()
HERO = object.Player(10, 10)
BOSS = object.Boss(10, 10)
BOSS.new_coord(-100, -100)
platforms = []
teleports = []
enemy = []
tree = []
balls = []
monster = []
button = []
x_hero, y_hero = 0, 0
lens = 54




def make_level(level):
    x, y = 0, 0

    def platform(row, col, obj):
        if obj == object.Teleport_BOSS:
            pl = obj(x, y, lens*10, lens)
        else:
            pl = obj(x, y, lens, lens)
        #group_draw.add(pl)
        if object.Platform == obj:
            platforms.append(pl)
        else:
            teleports.append(pl)

    #width =
    for row in level:

        for col in row:
            if col == ' ':
                pass
            else:
                if col in ['-', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f']:
                    if col == 'q':
                        group_draw.add(object.Background(x, y, 'data/фоны/начало.png'))
                    # горизонталь
                    if col == 'w':
                        group_draw.add(object.Background(x, y, 'data/фоны/горизонталь_1.png'))
                    if col == 'e':
                        group_draw.add(object.Background(x, y, 'data/фоны/горизонталь_2.png'))
                    # поворот
                    if col == 'm':
                        group_draw.add(object.Background(x, y, 'data/фоны/начало_старт.png'))
                    if col == 'r':
                        group_draw.add(object.Background(x, y, 'data/фоны/поворот_1.png'))
                    if col == 't':
                        group_draw.add(object.Background(x, y, 'data/фоны/поворот_2.png'))
                    if col == 'y':
                        group_draw.add(object.Background(x, y, 'data/фоны/поворот_3.png'))
                    if col == 'u':
                        group_draw.add(object.Background(x, y, 'data/фоны/поворот_4.png'))
                    if col == 'f':
                        group_draw.add(object.Background(x, y, 'data/фоны/овраг.png'))
                    if col == 'i':
                        group_draw.add(object.Background(x, y, 'data/фоны/вертикаль.png'))
                    if col == 'p':
                        group_draw.add(object.Background(x, y, 'data/фоны/конец.png'))
                    if col == 'a':
                        pl = object.Tree(x, y, 'data/фоны/развилка_вниз.png', 'data/фоны/развилка_вниз_без_ягод.png')
                        group_draw.add(pl)
                        tree.append(pl)
                    if col == 's':
                        pl = object.Tree(x, y, 'data/фоны/развилка_наверх.png', 'data/фоны/развилка_наверх_без_ягод.png')
                        group_draw.add(pl)
                        tree.append(pl)
                    if col == 'd':
                        pl = object.Tree(x, y, 'data/фоны/развилка_направо.png', 'data/фоны/развилка_направо_без_ягод.png')
                        group_draw.add(pl)
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
                    pl = object.Enemy(x, y)
                    enemy.append(pl)
                if col == "$":
                    BOSS.new_coord(x, y)
                    BOSS.isdie = False
                if col == "*":  # тентаклемонстр
                    pl = object.Monster(x, y)
                    group_draw.add(pl)
                    monster.append(pl)

                if col == "_":
                    pass
            x += lens
        y += lens
        x = 0
    for pl in enemy:
        group_draw.add(pl)



#size = width, height = 1080, 720
#window = pygame.display.set_mode(size)
window = pygame.display.set_mode((0, 0), HWSURFACE| DOUBLEBUF| FULLSCREEN)
screen = pygame.Surface(SIZE)
#screen = pygame.Surface((400, 400))
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
total_level_width = len(MAP['level1'][0])*lens
total_level_height = len(MAP['level1'])*lens
camera.new(total_level_width, total_level_height)
make_level(MAP['level1'])
group_draw.add(HERO)

def camera_level(place):
    global Boss_spawn
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
    total_level_width = len(MAP[place][0])*lens
    total_level_height = len(MAP[place])*lens
    camera.new(total_level_width, total_level_height)
    make_level(MAP[place])
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
            camera_level(f'level{str(location)}')

    except KeyError:
        HERO.level = last_level

    camera.update(HERO)
    for e in group_draw:
        coord = camera.apply(e)
        obl = 600

        if pygame.Rect(HERO.rect.topleft[0]-obl, HERO.rect.topleft[1]-obl, 2*obl, 2*obl).colliderect(e.rect):
            screen.blit(e.image, coord)

    if take_barries:
        font = pygame.font.Font('pixle_font.ttf', 20)
        txt = font.render('нажми на ПКМ чтобы собрать плоды', 1, (0, 255, 0))
        screen.blit(txt, (50, 50))
    if Strike_fast:
        font = pygame.font.Font('pixle_font.ttf', 40)
        txt = font.render('Заряжается...', 1, (0, 255, 0))
        rect = HERO.image.get_rect()
        screen.blit(txt, (WIDTH//2, HEIGHT-40))
    font = pygame.font.Font('pixle_font.ttf', 40)
    txt = font.render('SCORE:' + str(len(list(HERO.trees))), 1, (0, 255, 0))
    pygame.display.flip()
    screen.blit(txt, (0, 0)) #WIDTH-200, HEIGHT+100))
    window.blit(screen, ((int(get_monitors()[0].width) - WIDTH) // 2, (int(get_monitors()[0].height) - HEIGHT) // 2))

def create_button():
    button.clear()
    for e in group_draw:
        e.kill()
    w, h = 302, 64
    button.append(object.Button(328, 145, w, h, 'Play', tag=False))
    button.append(object.Button(328, 225, w, h, 'Shop', tag=False))
    button.append(object.Button(328, 315, w, h, 'Settings', tag=False))
    button.append(object.Button(328, 400, w, h, 'Exit', tag=False))
    group_draw.add(object.Background(0, 0, 'data\МЕНЮ\меню_фон.png'))
    for i in button:
        group_draw.add(i)

def create_button_setting():
    button.clear()
    for e in group_draw:
        e.kill()
    w, h = 90, 50
    music = 150
    sound = 400
    name_a = 'music'
    name_b = 'sound'
    name_c = 'menu'
    # music
    button.append(object.Button(100, music, w, h, '0', name_a))
    button.append(object.Button(200, music, w, h, '25', name_a))
    button.append(object.Button(300, music, w, h, '50', name_a))
    button.append(object.Button(400, music, w, h, '75', name_a))
    button.append(object.Button(500, music, w, h, '100', name_a))

    # sound
    button.append(object.Button(100, sound, w, h, '0', name_b))
    button.append(object.Button(200, sound, w, h, '25', name_b))
    button.append(object.Button(300, sound, w, h, '50', name_b))
    button.append(object.Button(400, sound, w, h, '75', name_b))
    button.append(object.Button(500, sound, w, h, '100', name_b))

    # menu
    button.append(object.Button(740, sound, w*2, h*2, 'Exited', name_c))
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
        sound.BACK2_AUDIO.set_volume(level)
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
        sound.DAMAGE_AUDIO.set_volume(level)
        sound.STRIKE_AUDIO.set_volume(level)
        sound.TAKE_AUDIO.set_volume(level)
        sound.BACK2_AUDIO.set_volume(level)
        sound.STEP_AUDIO.set_volume(level)
        sound.STEP2_AUDIO.set_volume(level)
        for i in sound.SPIDER_AUDIO:
            i.set_volume(level)
        sound.BUTTON.set_volume(level)



if start_part:
    start_part_animation.blit(screen, (0, 0))


create_button()


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

running = True
clock = pygame.time.Clock()
pygame.init()

while running:
    #pygame.mouse.set_visible(False)  # скрывает мышь
    if KPK:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEMOTION:
                for i in button:
                    if i.rect.collidepoint((event.pos[0] - jump_x, event.pos[1] - jump_y)):
                        i.mouse(False)
                    else:
                        i.mouse(True)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 or event.button == 2:
                    for i in button:
                        if i.rect.collidepoint((event.pos[0] - jump_x, event.pos[1] - jump_y)):
                            screen.fill((0, 0, 0))
                            if i.name == '1':
                                pass
                            if i.name == '2':
                                pass
                            if i.name == '3':
                                pass
                            if i.name == '4':
                                pass
                            if i.name == '5':
                                pass
                            if i.name == '6':
                                pass
                            if i.name == '7':
                                pass
                            if i.name == '8':
                                pass
                            if i.name == '9':
                                pass
                            if i.name == '10':
                                pass
                            if i.name == '11':
                                pass
                            if i.name == '12':
                                pass


                            pygame.display.flip()
                            sound.BUTTON.play()
                            sleep(2)



        screen.fill((255, 255, 255))
        group_draw.draw(screen)
        window.blit(screen, ((int(get_monitors()[0].width) - WIDTH) // 2, (int(get_monitors()[0].height) - HEIGHT) // 2))
        pygame.display.flip()
        clock.tick(60)

    elif loading:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False



        screen.fill((255, 255, 255))
        if after_count < 2:
            after_count+= 1
            sleep(1)
        else:
            loading = False
        group_draw.draw(screen)
        font = pygame.font.Font('pixle_font.ttf', 72)
        txt = font.render('Типо гружу, да', 1, (0, 0, 0))
        screen.blit(txt, (WIDTH//3, 250))
        window.blit(screen, ((int(get_monitors()[0].width) - WIDTH) // 2, (int(get_monitors()[0].height) - HEIGHT) // 2))
        pygame.display.flip()
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
            sleep(1)
        if not words.update():
            sleep(2)
            running = False
        group_draw.draw(screen)
        window.blit(screen, ((int(get_monitors()[0].width) - WIDTH) // 2, (int(get_monitors()[0].height) - HEIGHT) // 2))
        pygame.display.flip()
        clock.tick(60)

    elif start_part:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEMOTION:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass


        screen.fill((255, 255, 255))
        start_part_animation.blit(screen, (0, 0))
        window.blit(screen, ((int(get_monitors()[0].width) - WIDTH) // 2, (int(get_monitors()[0].height) - HEIGHT) // 2))
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
                    if i.rect.collidepoint((event.pos[0] - jump_x, event.pos[1] - jump_y)):
                        i.mouse(False)
                    else:
                        i.mouse(True)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 or event.button == 2:
                    for i in button:
                        if i.rect.collidepoint((event.pos[0] - jump_x, event.pos[1] - jump_y)):
                            if i.who == 'music' or i.who == 'sound':
                                sound_correct(i.name, i.who)
                            if i.name == 'Exited':
                                menu = True
                                settings = False
                                create_button()
                            sound.BUTTON.play()


        screen.fill((255, 255, 255))
        font = pygame.font.Font('pixle_font.ttf', 72)
        txt = font.render('Music', 1, (0, 0, 0))
        screen.blit(txt, (WIDTH//3 - 120, 50))
        font = pygame.font.Font('pixle_font.ttf', 72)
        txt = font.render('Sound', 1, (0, 0, 0))
        screen.blit(txt, (WIDTH//3 - 120, 300))
        group_draw.draw(screen)
        window.blit(screen, ((int(get_monitors()[0].width) - WIDTH) // 2, (int(get_monitors()[0].height) - HEIGHT) // 2))
        pygame.display.flip()
        clock.tick(60)

    elif menu:
        First_on_audio = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu = False
            if event.type == pygame.MOUSEMOTION:
                for i in button:
                    if i.rect.collidepoint((event.pos[0] - jump_x, event.pos[1] - jump_y)):
                        i.mouse(False)
                    else:
                        i.mouse(True)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 or event.button == 2:
                    for i in button:
                        if i.rect.collidepoint((event.pos[0] - jump_x, event.pos[1] - jump_y)):
                            screen.fill((0, 0, 0))
                            if i.name == 'Play':
                                menu = False
                                loading = True
                                button.clear()
                                after_count = 0
                                for e in group_draw:
                                    e.kill()
                            if i.name == 'Settings':
                                settings = True
                                menu = False
                                create_button_setting()
                            if i.name == 'Exit':
                                running = False

                            pygame.display.flip()
                            sound.BUTTON.play()
                            sleep(2)

        screen.fill((255, 255, 255))
        font = pygame.font.Font('pixle_font.ttf', 72)
        if not loading:
            txt = font.render('Spider Gay', 1, (0, 0, 0))
            screen.blit(txt, (WIDTH//3 -20, 50))
        group_draw.draw(screen)
        window.blit(screen, ((int(get_monitors()[0].width) - WIDTH) // 2, (int(get_monitors()[0].height) - HEIGHT) // 2))
        pygame.display.flip()
        clock.tick(60)

    else:
        ball = 0
        if First_on_audio == 0:
            sound.BACK_AUDIO.play(-1)
            sound.BACK2_AUDIO.play()
            First_on_audio += 1
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

            if event.type == pygame.MOUSEBUTTONDOWN:
                Strike = True
                ball += 1

                """if event.button == 1:
                    if len(balls) < 2:
                        Strike_fast = False
                        first_strike_timer = time.process_time()
                        sound.STRIKE_AUDIO.play()
                        pl = object.Ball(HERO.rect.x, HERO.rect.y + HERO.rect.width // 2, HERO.side)
                        balls.append(pl)
                        group_draw.add(pl)
                    elif int(time.process_time()) - first_strike_timer >= 1:
                        Strike_fast = False
                        first_strike_timer = time.process_time()
                        sound.STRIKE_AUDIO.play()
                        pl = object.Ball(HERO.rect.x, HERO.rect.y + HERO.rect.width // 2, HERO.side)
                        balls.append(pl)
                        group_draw.add(pl)

                    else:
                        Strike_fast = True"""
                if event.button == 2:
                    E = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    UP = False
                if event.key == pygame.K_a:
                    LEFT = False
                if event.key == pygame.K_d:
                    RIGHT = False
                if event.key == pygame.K_f:
                    HERO.film = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    Strike = False
                if event.button == 2:
                    E = False

        keys = pygame.key.get_pressed()  # движения персонажей под зажим\


        """for i in range(ball):
            pl = object.Ball(200, 200, HERO.side)
            #balls.append(pl)
            #group_draw.add(pl) Потом исправлю фигню с фризом, когда создаю объект болл"""
        draw()
        take_barries = HERO.update(LEFT, RIGHT, UP, platforms, teleports, tree, enemy, E, screen, BOSS, monster, Strike)
        if Strike_fast:
            for_strike_count_time_when_we_see_text += 1
        if for_strike_count_time_when_we_see_text >= 5:
            Strike_fast = False
            for_strike_count_time_when_we_see_text = 0

        for i in enemy:
            i.AI(HERO, platforms)
        for i in monster:
            i.AI(HERO)
        if Boss_spawn:
            BOSS.AI(HERO, platforms)
        if HERO.helth <= 0:
            HERO.respawn()
        """for i in balls:
            i.update(platforms, enemy, BOSS)
            if i.die:
                del balls[balls.index(i)]
            i.draw(screen)"""
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
        if keys[pygame.K_ESCAPE]:
            menu = True
            button.clear()
            create_button()


pygame.quit()
quit()
sys.exit()

    # иногда реально ненавижу git hub, снова для нового коммита
