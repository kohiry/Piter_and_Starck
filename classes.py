import pygame
import starter_obj


def backs(width, height):
    pos, end = 'data/фоны/', '.png'
    sprite = {
        'границы': [pygame.image.load(pos + 'начало' + end), pygame.image.load(pos + 'конец' + end)],
        'центр': [pygame.image.load(pos + 'горизонталь_1' + end), pygame.image.load(pos + 'горизонталь_2' + end)]
    }
    list_key = sprite.keys()
    for i in list_key:
        for j in sprite[i]:
            sprite[i][sprite[i].index(j)] = pygame.transform.scale(j, (height, height))
    return sprite


def maps(width, height, map):
    sprites = backs(width, height)
    if map == 1:
        return [sprites['границы'][0], sprites['центр'][0], sprites['центр'][0], sprites['центр'][0]]

class Map:
    def __init__(self, width, height, speed):
        self.sprite = maps(width, height, 1)

    def draw(self, screen, width):
        for i in self.sprite:
            screen.blit(i, ((width-200) * self.sprite.index(i), 0))


'''
class Count:
    def __init__(self):
        self.count = 0
        self.flag = False

    def use(self):
        self.count += 1
        self.flag = True

    def give(self):
        return self.count

    def clear(self):
        self.count = 0

    def flags(self):
        return self.flag

    def dont_use(self):
        self.flag = False

def group():
    return {
        'прыжок_лево': Count(),
        'прыжок_право': Count(),
        'бег_лево': Count(),
        'бег_право': Count(),
        'стойка_лево': Count(),
        'стойка_право': Count()
    }

class Sprites_hero:
    def __init__(self):
        self.groups = group()

    def give_sprites(self):
        stand = 'data/паук/стоит/'
        run = "data/паук/бежит/"
        strike = "data/паук/стреляет/"
        jump = "data/паук/прыжок/"
        loading = pygame.image.load
        end = '.png'
        return {
            "прыжок": {'влево':[
                            self.groups['прыжок_лево'],  # слежка за спрайтами anim_count
                            loading(jump + "прыжок_налево_1" + end),
                            loading(jump + "прыжок_налево_2" + end),
                            loading(jump + "прыжок_налево_3" + end),
                            loading(jump + "прыжок_налево_4" + end),
                            loading(jump + "прыжок_налево_5" + end)
                                ],
                        'вправо':[
                                self.groups['прыжок_право'],  # слежка за спрайтами anim_count
                                loading(jump + "прыжок_направо_1" + end),
                                loading(jump + "прыжок_направо_2" + end),
                                loading(jump + "прыжок_направо_3" + end),
                                loading(jump + "прыжок_направо_4" + end),
                                loading(jump + "прыжок_направо_5" + end)
                            ]
                      },

            'стойка': {'влево': [
                            self.groups['стойка_лево'],  # слежка за спрайтами anim_count
                            loading(stand + "паук_стоит_налево_1" + end),
                            loading(stand + "паук_стоит_налево_2" + end)
                        ],
                       'вправо': [
                            self.groups['стойка_право'],  # слежка за спрайтами anim_count
                            loading(stand + "паук_стоит_направо_1" + end),
                            loading(stand + "паук_стоит_направо_2" + end)
                            ]
                      },
            'бег': {'влево': [
                        self.groups['бег_лево'],  # слежка за спрайтами anim_count
                        loading(run + "паук_бежит_налево_1" + end),
                        loading(run + "паук_бежит_налево_2" + end),
                        loading(run + "паук_бежит_налево_3" + end),
                        loading(run + "паук_бежит_налево_4" + end)
                    ],
                    'вправо':[
                        self.groups['бег_право'],  # слежка за спрайтами anim_count
                        loading(run + "паук_бежит_направо_1" + end),
                        loading(run + "паук_бежит_направо_2" + end),
                        loading(run + "паук_бежит_направо_3" + end),
                        loading(run + "паук_бежит_направо_4" + end)
                    ]}
        }

'''
class Hero:
    def __init__(self, xy, width, height, speed):
        self.xy = xy
        self.width = width
        self.height = height
        self.colour = (255, 255, 255)
        self.speed = speed
        self.old_speed = speed
        self.jumping = 15
        self.front = 1  # 1-вправо -1-влево
        self.move = 0  # 0-стойка 1-бег влево 2-вправо 3-прыжок влево 4-прыжок вправо
        # 5-прыжок с паутиной влево 6-прыжок с паутиной вправо 7-выстрел вправо 8- выстрел влево
        # 9 - лезет справа 10 - лезет слева 11- лесез вправо по верху 12-лезетвлево по верху

        #self.sprite = starter_obj.sprite_hero.give_sprites()
        self.anim_count = 0
        self.action = False
        self.count = 0
        self.wall = 0  # -1 - слева стена; 0 - стен нет; 1 - справа стена
        self.fall = False  # False - на платформе; True - падает
        self.speed_fall = 0

    def clear_speed(self):
        self.speed = 0

    def rewrite_speed(self):
        self.speed = self.old_speed

    def check(self, screen):
        font = pygame.font.Font("pixle_font.ttf", 40)
        text = font.render("Картинка чутья", 25, (255, 0, 0))
        screen.blit(text, (self.xy[0] - self.width, self.xy[1]))

    def rect(self):
        return pygame.Rect((self.xy[0], self.xy[1]), (self.width, self.height))

    def move_x_a(self):
        if self.wall != -1:
            self.xy[0] -= self.speed
            self.front = -1

    def move_x_d(self):
        if self.wall != 1:
            self.xy[0] += self.speed
            self.front = 1

    def action_jump(self):  # может быть когда-нибудь рализую двойной прыжок
        pass

    def jump(self):
        if self.jumping >= -15:
            if self.jumping >= 0:
                self.xy[1] -= (self.jumping) ** 2 // 5
            else:
                self.xy[1] += (self.jumping) ** 2 // 5
            self.jumping -= 1
        else:
            self.jumping = 15
            return 'End'

    def respawn(self, xy):
        self.speed_fall = 0
        self.xy[1] = (xy[1] // 10) * 10
        self.xy[0] = (xy[0] // 10) * 10

    def falling(self):
        if self.fall:
            self.xy[1] += self.speed_fall
            self.speed_fall += 1
        else:
            self.speed_fall = 0

    def animation(self, list_anim, screen, maxx, speed):
        if list_anim[0].give() + 1 >= maxx:
            list_anim[0].clear()
        img = list_anim[1:len(list_anim)][list_anim[0].give() // speed]
        img = pygame.transform.scale(img, (self.width, self.height))
        screen.blit(img, tuple(self.xy))
        list_anim[0].use()
        for i in starter_obj.sprite_hero.groups.keys():
            obj = starter_obj.sprite_hero.groups[i]
            if obj != list_anim[0] and obj.flags() is True:
                obj.dont_use()
                obj.clear()

    def touch(self, answer, jump):
        self.fall = True
        print(self.xy[1], '|', self.speed_fall)
        if 'down' in answer:
            if jump:
                self.jumping = 15
                starter_obj.is_jump = False
        elif 'up' in answer:
            self.xy[1] = answer[0].y - self.height
            self.fall = False
            if jump:
                self.jumping = 15
                starter_obj.is_jump = False
        elif 'right' in answer:
            self.wall = 1
        elif 'left' in answer:
            self.wall = -1
        else:
            self.wall = 0
        self.falling()


    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.xy[0], self.xy[1], self.width, self.height))
        '''
        if starter_obj.is_jump:
            if self.front > 0:  #вправо
                self.animation(self.sprite['прыжок']['вправо'], screen, 40, 10)
            else:
                self.animation(self.sprite['прыжок']['влево'], screen, 40, 10)
        elif self.action:  #двигается ли он
            if self.front > 0:  #вправо
                self.animation(self.sprite['бег']['вправо'], screen, 20, 5)
            else:
                self.animation(self.sprite['бег']['влево'], screen, 20, 5)
        else:
            if self.front > 0:  #вправо
                self.animation(self.sprite['стойка']['вправо'], screen, 10, 5)
            else:
                self.animation(self.sprite['стойка']['влево'], screen, 10, 5)
        '''


class Platform:
    def __init__(self, x, y, width=150, height=50, speed=10):
        self.rect = pygame.Rect((x, y), (width, height))
        self.speed = speed
        self.height = height
        self.width = width
        self.x, self.y = x, y

    def move(self, x, y, width, height):
        self.rect.move(self.x + self.speed * front, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)

    def touch(self, x, y, width, height):
        print(self.y)
        left    = pygame.Rect((x, y), (2, height))
        right   = pygame.Rect((x + width-1, y), (2, height))
        up      = pygame.Rect((x, y + height - 1), (width, 10))
        down    = pygame.Rect((x, y), (width, 2))

        self_left   = pygame.Rect((self.x, self.y), (2, self.height))
        self_right  = pygame.Rect((self.x + self.width-1, self.y), (2, self.height))
        self_up     = pygame.Rect((self.x, self.y + self.height - 1), (self.width, height//2))
        self_down   = pygame.Rect((self.x, self.y), (self.width, height//2))
        answer      = []
        if self_down.colliderect(up):
            answer.append('up')
        elif self_up.colliderect(down):
            answer.append('down')
        elif self_right.colliderect(left):
            answer.append('left')
        elif self_left.colliderect(right):
            answer.append('right')

        return [self] + answer

class Enemy:
    def __init__(self, xy, width, height, speed):
        self.xy = xy
        self.width = width
        self.height = height
        self.colour = (0, 0, 0)
        self.speed = speed
        self.old_speed = speed
        self.hp = 3
        self.damages = False
        self.around = 300

    def rewrite_speed(self, speed):
        self.speed = speed

    def return_speed(self):
        self.speed = self.old_speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.xy[0], self.xy[1], self.width, self.height))
        self.damage(screen)
        if self.damages:
            self.hp -= 1
            self.damages = False
            self.around = 1000

    def AI(self, hero):  # искусственный интеллект бота
        dont_move = 50
        if 0 <= hero.xy[0] - self.xy[0] <= dont_move:
            pass
        elif 0 <= hero.xy[0] - self.xy[0] <= self.around - (hero.width + 10):  # используем коорды бота и игрока
            self.move_x_d()
        elif 0 <= self.xy[0] - hero.xy[0] <= self.around:  # используем коорды бота и игрока
            self.move_x_a()


    def damage(self, screen):
        font = pygame.font.Font("pixle_font.ttf", 40)
        text = font.render(str(self.hp), 25, (255, 0, 0))
        screen.blit(text, (self.xy[0] + self.width//2, self.xy[1] - 40))


    def rect(self):
        return pygame.Rect((self.xy[0], self.xy[1]), (self.width, self.height))

    def move_x_a(self):
        self.xy[0] -= self.speed

    def move_x_d(self):
        self.xy[0] += self.speed


class Attack:
    def __init__(self, xy, radius, speed, front):
        self.xy = xy.copy()
        self.radius = radius
        self.colour = (125, 125, 125)
        self.speed = speed
        self.old_speed = speed
        self.jumping = 7
        self.front = front

    def rewrite_speed(self, speed):
        self.speed = speed

    def return_speed(self):
        self.speed = self.old_speed

    def rect(self):
        return pygame.Rect((self.xy[0], self.xy[1]), (self.radius, self.radius))

    def move(self):
        self.xy[0] += self.speed * self.front

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (self.xy[0], self.xy[1]), self.radius)


'''
class Background:
    def __init__(self, name):
        self.image = pygame.image.load(name)

    def move(self):
        pass

    def give_art(self):
        return self.image

if __name__ == '__main__':
    print('Файл с классами')
    input('нажми любую кнопку, чтобы выйти')
'''


class Button:
    def __init__(self, x, y, text):
        self.x, self.y = x, y
        font = pygame.font.Font("pixle_font.ttf", 50)
        self.text = font.render(text, 1, (50, 255, 50))
        self.width = self.text.get_width()
        self.height = self.text.get_height()

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen, click):
        screen.blit(self.text, (self.x, self.y))
        if click:
            pygame.draw.rect(screen, (0, 150, 0), (self.x - 10, self.y - 10,
                                                   self.width + 20, self.height + 20), 10)
            return False

        else:
            pygame.draw.rect(screen, (200, 255, 200), (self.x - 10, self.y - 10,
                                                   self.width + 20, self.height + 20), 10)
            return True
