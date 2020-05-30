import pygame


class Background:
    def __init__(self, width, height):
        pos, end = 'data/фоны/', '.png'
        self.sprite = {
            'границы': [pygame.image.load(pos + 'начало' + end), pygame.image.load(pos + 'конец' + end)]
        }
        for i in self.sprite.keys():
            for j in self.sprite[i]:
                self.sprite[i][self.sprite[i].index(j)] = pygame.transform.scale(j, (width, height))

    def draw(self, screen):
        screen.blit(self.sprite['границы'][0], (0, 0))

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
                            #loading(jump + "прыжок_налево_1" + end),
                            loading(jump + "прыжок_налево_2" + end),
                            loading(jump + "прыжок_налево_3" + end),
                            loading(jump + "прыжок_налево_4" + end),
                            loading(jump + "прыжок_налево_5" + end)
                                ],
                        'вправо':[
                                self.groups['прыжок_право'],  # слежка за спрайтами anim_count
                                #loading(jump + "прыжок_направо_1" + end),
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
