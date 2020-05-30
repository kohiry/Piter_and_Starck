import pygame
import sprites
import starter_obj


class Hero:
    def __init__(self, xy, width, height, speed):
        self.xy = xy
        self.width = width
        self.height = height
        self.colour = (255, 255, 255)
        self.speed = speed
        self.jumping = 13
        self.front = 1  # 1-вправо -1-влево
        self.move = 0  # 0-стойка 1-бег влево 2-вправо 3-прыжок влево 4-прыжок вправо
        # 5-прыжок с паутиной влево 6-прыжок с паутиной вправо 7-выстрел вправо 8- выстрел влево
        # 9 - лезет справа 10 - лезет слева 11- лесез вправо по верху 12-лезетвлево по верху

        self.sprite = starter_obj.sprite_hero.give_sprites()
        self.anim_count = 0
        self.action = False
        self.count = 0

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
        #pygame.draw.rect(screen, self.colour, (self.xy[0], self.xy[1], self.width, self.height))
        if starter_obj.is_jump:
            if self.front > 0:  #вправо
                self.animation(self.sprite['прыжок']['вправо'], screen, 40, 10)
            else:
                self.animation(self.sprite['прыжок']['влево'], screen, 40, 10)
        elif self.action:  #двигается ли он
            if self.front > 0:  #вправо
                self.animation(self.sprite['стойка']['вправо'], screen, 20, 10)
            else:
                self.animation(self.sprite['стойка']['влево'], screen, 20, 10)
        else:
            if self.front > 0:  #вправо
                self.animation(self.sprite['бег']['вправо'], screen, 10, 5)
            else:
                self.animation(self.sprite['бег']['влево'], screen, 10, 5)




class Enemy:
    def __init__(self, xy, width, height, speed):
        self.xy = xy
        self.width = width
        self.height = height
        self.colour = (0, 0, 0)
        self.speed = speed
        self.hp = 3
        self.damages = False
        self.around = 300

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
        self.jumping = 7
        self.front = front

    def rect(self):
        return pygame.Rect((self.xy[0], self.xy[1]), (self.radius, self.radius))

    def move(self):
        self.xy[0] += self.speed * self.front

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (self.xy[0], self.xy[1]), self.radius)


if __name__ == '__main__':
    print('Файл с классами')
    input('нажми любую кнопку, чтобы выйти')
