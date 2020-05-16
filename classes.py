import pygame


class Hero:
    def __init__(self, xy, width, height, speed):
        self.xy = xy
        self.width = width
        self.height = height
        self.colour = (0, 0, 0)
        self.speed = speed
        self.jumping = 7

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.xy[0], self.xy[1], self.width, self.height))

    def move_x_a(self):
        self.xy[0] -= self.speed

    def move_x_d(self):
        self.xy[0] += self.speed

    def jump(self):
        if self.jumping >= -7:
            if self.jumping >= 0:
                self.xy[1] -= self.jumping ** 2
            else:
                self.xy[1] += self.jumping ** 2
            self.jumping -= 1
        else:
            self.jumping = 7
            return 'End'
