import pygame


class Hero:
    def __init__(self, xy, width, height, speed):
        self.xy = xy
        self.width = width
        self.height = height
        self.colour = (0, 0, 0)
        self.speed = speed
        self.jumping = 13
        self.front = 1

    def check(self, screen):
        font = pygame.font.Font("pixle_font.ttf", 40)
        text = font.render("Картинка чутья", 25, (255, 0, 0))
        screen.blit(text, (self.xy[0] - self.width, self.xy[1] - 40))

    def rect(self):
        return pygame.Rect((self.xy[0], self.xy[1]), (self.width, self.height))

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.xy[0], self.xy[1], self.width, self.height))

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
