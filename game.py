import pygame
pygame.init()
from screeninfo import get_monitors
from level import map as MAP
import object

#setting
SIZE = WIDTH, HEIGHT = 1080, 700
BACK_SIZE = int(1080/1.5)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
FONT = "pixle_font.ttf"
UP = False
LEFT = False
RIGHT = False
E = False

# map
location = 1
draw_loc = 1

#startet_obj
group_draw = pygame.sprite.Group()
HERO = object.Player(10, 10)
platforms = []
teleports = []
enemy = []
tree = []
x_hero, y_hero = 0, 0
lens = 45

def make_level(level):
    x, y = 0, 0

    def platform(row, col, obj):
        pl = obj(x, y, lens, lens)
        group_draw.add(pl)
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
                    pl = object.Enemy(x, y, lens, lens)
                    group_draw.add(pl)
                    enemy.append(pl)
                if col == "_":
                    pass
            x += lens
        y += lens
        x = 0




#size = width, height = 1080, 720
#window = pygame.display.set_mode(size)
window = pygame.display.set_mode((0, 0), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
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
    for e in group_draw:
        e.kill()
    platforms.clear()
    teleports.clear()
    enemy.clear()
    tree.clear()
    total_level_width = len(MAP[place][0])*lens
    total_level_height = len(MAP[place])*lens
    camera.new(total_level_width, total_level_height)
    make_level(MAP[place])
    group_draw.add(HERO)

def draw():
    global draw_loc, location
    screen.fill((0, 0, 25))
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
        screen.blit(e.image, camera.apply(e))
    window.blit(screen, ((int(get_monitors()[0].width) - WIDTH) // 2, (int(get_monitors()[0].height) - HEIGHT) // 2))


running = True
while running:
    pygame.mouse.set_visible(False)  # скрывает мышь
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                UP = True
            if event.key == pygame.K_LEFT:
                LEFT = True
            if event.key == pygame.K_RIGHT:
                RIGHT = True
            if event.key == pygame.K_e:
                E = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                UP = False
            if event.key == pygame.K_LEFT:
                LEFT = False
            if event.key == pygame.K_RIGHT:
                RIGHT = False
            if event.key == pygame.K_e:
                E = False

    keys = pygame.key.get_pressed()  # движения персонажей под зажим\
    if keys[pygame.K_ESCAPE]:
        running = False

    HERO.update(LEFT, RIGHT, UP, platforms, teleports, tree, E, screen)
    for i in enemy:
        i.AI(HERO, platforms)
    draw()
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()

# иногда реально ненавижу git hub, снова для нового коммита
