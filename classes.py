import pygame
import starter_obj


class Background:
    def __init__(self, width, height, x, y):
        pos, end = 'data/фоны/', '.png'
        self.x, self.y = x, y
        self.sprite = {
            'границы': [pygame.image.load(pos + 'начало' + end), pygame.image.load(pos + 'конец' + end)],
            'центр': [pygame.image.load(pos + 'горизонталь_1' + end), pygame.image.load(pos + 'горизонталь_2' + end)]
        }
        for i in self.sprite.keys():
            for j in self.sprite[i]:
                self.sprite[i][self.sprite[i].index(j)] = pygame.transform.scale(j, (height, height))
        self.width, self.height = width, height

    def rect_left(self):
        return pygame.Rect((self.x, self.y), (self.height, self.height))

    def rect_right(self):
        return pygame.Rect((self.x + self.width, self.y), (self.height, self.height))

    def move(self, front, speed, hero):
        if self.rect_left().colliderect(hero.rect()) == 0 or self.rect_right().colliderect(hero.rect()) == 0:
            self.x += speed * front
        else:
            hero.rewrite_speed()
            print(self.rect_left().colliderect(hero.rect()), self.rect_right().colliderect(hero.rect()))

    def draw(self, screen):
        screen.blit(self.sprite['границы'][0], (self.x, self.y))
        screen.blit(self.sprite['границы'][1], (self.x + self.width, self.y))
        screen.blit(self.sprite['центр'][0], (self.x + self.width//2, self.y))
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
        self.jumping = 13
        self.front = 1  # 1-вправо -1-влево
        self.move = 0  # 0-стойка 1-бег влево 2-вправо 3-прыжок влево 4-прыжок вправо
        # 5-прыжок с паутиной влево 6-прыжок с паутиной вправо 7-выстрел вправо 8- выстрел влево
        # 9 - лезет справа 10 - лезет слева 11- лесез вправо по верху 12-лезетвлево по верху

        #self.sprite = starter_obj.sprite_hero.give_sprites()
        self.anim_count = 0
        self.action = False
        self.count = 0

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
        self.xy[0] -= self.speed
        self.front = -1

    def move_x_d(self):
        self.xy[0] += self.speed
        self.front = 1

    def action_jump(self):  # может быть когда-нибудь рализую двойной прыжок
        pass

    def jump(self):
        if self.jumping >= -13:
            if self.jumping >= 0:
                self.xy[1] -= (self.jumping) ** 2 // 4
            else:
                self.xy[1] += (self.jumping) ** 2 // 4
            self.jumping -= 1
        else:
            self.jumping = 13
            return 'End'

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
