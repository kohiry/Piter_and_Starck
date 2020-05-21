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
        if self.jumping >= -8:
            if self.jumping >= 0:
                self.xy[1] -= self.jumping ** 2
            else:
                self.xy[1] += self.jumping ** 2
            self.jumping -= 1
        else:
            self.jumping = 8
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

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.xy[0], self.xy[1], self.width, self.height))
        self.damage(screen)
        if self.damages:
            self.hp -= 1


    def damage(self, screen):
        font = pygame.font.Font(None, 40)
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
