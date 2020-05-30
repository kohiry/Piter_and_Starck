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


class Sprites_hero:
    def __init__(self):
        self.count_jump1 = 0
        self.count_jump2 = 0
        self.count_stand1 = 0
        self.count_stand2 = 0
        self.count_strike1 = 0
        self.count_strike2 = 0
        self.count_run1 = 0
        self.count_run2 = 0

    def clear_data(self):  # придумать как красиво подчищать не используемые каунты
        self.count_jump1 = 0
        self.count_jump2 = 0
        self.count_stand1 = 0
        self.count_stand2 = 0
        self.count_strike1 = 0
        self.count_strike2 = 0
        self.count_run1 = 0
        self.count_run2 = 0

    def give_sprites(self):
        stand = 'data/паук/стоит/'
        run = "data/паук/бежит/"
        strike = "data/паук/стреляет/"
        jump = "data/паук/прыжок/"
        loading = pygame.image.load
        end = '.png'
        return {
            "прыжок": {'влево':[
                            self.count_jump1,  # слежка за спрайтами anim_count
                            loading(jump + "прыжок_налево_1" + end),
                            loading(jump + "прыжок_налево_2" + end),
                            loading(jump + "прыжок_налево_3" + end),
                            loading(jump + "прыжок_налево_4" + end),
                            loading(jump + "прыжок_налево_5" + end)
                                ],
                        'вправо':[
                                self.count_jump2,  # слежка за спрайтами anim_count
                                loading(jump + "прыжок_направо_1" + end),
                                loading(jump + "прыжок_направо_2" + end),
                                loading(jump + "прыжок_направо_3" + end),
                                loading(jump + "прыжок_направо_4" + end),
                                loading(jump + "прыжок_направо_5" + end)
                            ]
                      },

            'стойка': {'влево': [
                            self.count_stand1,  # слежка за спрайтами anim_count
                            loading(stand + "паук_стоит_налево_1" + end),
                            loading(stand + "паук_стоит_налево_2" + end)
                        ],
                       'вправо': [
                            self.count_stand2,  # слежка за спрайтами anim_count
                            loading(stand + "паук_стоит_направо_1" + end),
                            loading(stand + "паук_стоит_направо_2" + end)
                            ]
                      },
            'бег': {'влево': [
                        self.count_run1,  # слежка за спрайтами anim_count
                        loading(run + "паук_бежит_налево_1" + end),
                        loading(run + "паук_бежит_налево_2" + end),
                        loading(run + "паук_бежит_налево_3" + end),
                        loading(run + "паук_бежит_налево_4" + end)
                    ],
                    'вправо':[
                        self.count_run1,  # слежка за спрайтами anim_count
                        loading(run + "паук_бежит_направо_1" + end),
                        loading(run + "паук_бежит_направо_2" + end),
                        loading(run + "паук_бежит_направо_3" + end),
                        loading(run + "паук_бежит_направо_4" + end)
                    ]}
        }
