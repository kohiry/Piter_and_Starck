import pygame


class Hero:
    def __init__(self, xy, width, height, speed):
        self.xy = xy
        self.width = width
        self.height = height
        self.colour = (0, 0, 0)
        self.speed = speed
        self.jumping = 8
        self.front = 1

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
        if self.jumping >= -8:
            if self.jumping >= 0:
                self.xy[1] -= self.jumping ** 2
            else:
                self.xy[1] += self.jumping ** 2
            self.jumping -= 1
        else:
            self.jumping = 8
            return 'End'



class Attack:  # ПОСМОТРЕТЬ РОЛИК НА ЮТЬЮБЕ
    def __init__(self, xy, radius, speed, front):
        self.xy = xy.copy()
        self.radius = radius
        self.colour = (125, 125, 125)
        self.speed = speed
        self.jumping = 7
        self.front = front

    def move(self):
        self.xy[0] += self.speed * self.front

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (self.xy[0], self.xy[1]), self.radius)
