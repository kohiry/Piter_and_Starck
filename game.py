import pygame
pygame.init()
from screeninfo import get_monitors
from level import level1
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

#startet_obj
group_draw = pygame.sprite.Group()
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



#size = width, height = 1000, 1000
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

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def camera_func(camera, target_rect):
    l = -target_rect.x + SIZE[0]/2
    t = -target_rect.x + SIZE[1]/2
    w, h = camera.width, camera.height

    l = min(0, l)
    l = max(-(camera.width - SIZE[0], l))
    t = max(-(camera.height-SIZE[1]), ts)
    t = min(0, t)
    return pygame.Rect(l, t, w, h)

total_level_width = len(level1[0]*43)


def draw():
    screen.fill(GREEN)
    group_draw.draw(screen)
    window.blit(screen, ((int(get_monitors()[0].width) - WIDTH) // 2, (int(get_monitors()[0].height) - HEIGHT) // 2))


running = True
while running:
    #starter_obj.enemy.damages = False

    pygame.mouse.set_visible(True)  # скрывает мышь
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

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                UP = False
            if event.key == pygame.K_LEFT:
                LEFT = False
            if event.key == pygame.K_RIGHT:
                RIGHT = False

    keys = pygame.key.get_pressed()  # движения персонажей под зажим\
    if keys[pygame.K_ESCAPE]:
        running = False

    HERO.update(LEFT, RIGHT, UP, platforms)
    draw()
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()

# иногда реально ненавижу git hub, снова для нового коммита
