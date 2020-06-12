from starter_obj import hero
import pygame
import starter_obj


class Camera:
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)  #длина уровня

    def update(self, target):  # опр camera_func
        self.state = self.camera_func(self.state, target.rect)

    def apply(self.target):  # передвижение объектов уровня
        return target.rect.move(self.state.topleft)

def camera_func(camera, target_rect, width, height):
    l = -hero.xy[0] + width//2
    t = -hero.xy[1] + height//2
    w, h = camera.width, camera.height

    l = min(0, l)
    l = max(-(level.width - screen.width), l)

    return pygame.Rect(l, t, w, h)


total_level_width = starter_obj.width_window * 3
total_level_height = starter_obj.height_window

camera = Camera(camera_func, total_level_width, total_level_height)
