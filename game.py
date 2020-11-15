import pygame, sys
from screeninfo import get_monitors
from level import map as MAP
import object
import time
from pyganim import PygAnimation
from pygame.locals import *
#import asyncio
import threading
import add_info_into_config

#pygame.locals()
pygame.init()

class Game:
    '''My game about Spider man. Wrote this cod - kohiry (PinkyGully). Artist - Hiku'''
    def __init__(self):
        print('Game is switch on, my congratulations!')

        self.SIZE = self.WIDTH, self.HEIGHT = 960, 540
        #camera
        class Camera:
            def __init__(cam_self, width, height):
                cam_self.state = pygame.Rect(0, 0, width, height)

            def new(cam_self, width, height):
                cam_self.state = pygame.Rect(0, 0, width, height)

            def apply(cam_self, target):
                return target.rect.move(cam_self.state.topleft)

            def update(cam_self, target):
                cam_self.state = cam_self.camera_func(cam_self.state, target.rect)

            def camera_func(cam_self, camera, target_rect):
                l = -target_rect.x + self.SIZE[0]//2-30
                t = -target_rect.y + self.SIZE[1]//2
                w, h = camera.width, camera.height

                l = min(0, l)
                l = max(-(camera.width - self.SIZE[0]), l)
                t = max(-(camera.height - self.SIZE[1]), t)
                t = min(0, t)
                return pygame.Rect(l, t, w, h)


        self.camera = Camera(1, 1)

        # audio
        self.sound = object.Sound()
        self.count_dialog = 0
        self.count_audio = 0
        #startet_obj
        self.group_draw = pygame.sprite.Group()
        self.group_interface = pygame.sprite.Group()
        self.group_platform = pygame.sprite.Group()
        self.batton_in_KPK = pygame.sprite.Group()
        self.start_game_gr = pygame.sprite.Group()
        self.Bullet = pygame.sprite.Group()
        self.dialog = pygame.sprite.Group()
        self.HERO = object.Player(10, 10, self.sound)
        self.BOSS = object.Boss(10, 10)
        self.health_tab = object.Health_tab(415, 10)
        self.black_theme = object.BlackTheme()
        self.dialog_tab = object.Dialog_Tab(0, 0)
        self.BOSS.new_coord(-100, -100)
        self.StartScene = object.Start()
        self.start_game_gr.add(self.StartScene)
        self.teleports = []
        self.enemy = []
        self.all_obj = []
        self.matrix = []
        self.tree = []
        self.balls = []
        self.game = []
        self.monster = []
        self.info = []
        self.button = []
        self.x_hero, y_hero = 0, 0
        self.lens = 54

        self.animation_balck = []
        # затемнение для катсцен
        for i in [f'data\\интерфейс\\затенение_{str(j)}.png' for j in range(1, 7)]:
            self.animation_balck.append(pygame.image.load(i))
        self.clock = pygame.time.Clock()
        #setting
        self.fight = False

        self.BACK_SIZE = int(1080/1.5)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 200, 0)

        self.FONT = "pixle_font.ttf"
        self.VERSION = 'V0.6.9a'
        self.UP = False
        self.ball = 0
        self.dialog_start_part = 1
        self.LEFT = False
        self.RIGHT = False
        self.E = False
        self.F = False
        self.take_barries = False
        self.Boss_spawn = False
        self.First_on_audio = 0
        self.Strike = False
        self.first_strike_timer = 0
        self.black_count = 0
        self.after_count = 0
        self.Strike_fast = False
        self.for_strike_count_time_when_we_see_text = 0
        self.jump_x = ((int(get_monitors()[0].width) - self.WIDTH) // 2)
        self.jump_y = ((int(get_monitors()[0].height) - self.HEIGHT) // 2)

        # состояния
        self.start_game = True
        self.loading = False
        self.start_part = False
        self.menu = False
        self.map = False
        self.GAME = False
        self.scene_enemy = False
        self.scene_enemy3 = False
        self.settings = False
        self.after_words = False
        self.KPK = False
        self.scene_enemy2 = False
        self.pre_alpha_scene = False
        self.die_end = False
        #Thread
        self.updai_bool = True
        self.updBullet_ai = True
        self.updHERO_ai = True

        # map
        self.location = 1
        self.draw_loc = 1

        if self.start_game:
            self.StartScene.time = time.process_time()


        # Window
        #self.middle = ((int(get_monitors()[0].width) - self.WIDTH)//2, (int(get_monitors()[0].height) - self.HEIGHT)//2)
        self.middle = ((1080 - self.WIDTH)//2, (720 - self.HEIGHT)//2)
        self.size = width, height = 1080, 720
        self.window = pygame.display.set_mode(self.size)
        #self.window = pygame.display.set_mode((0, 0), HWSURFACE| DOUBLEBUF| FULLSCREEN)
        self.screen = pygame.Surface(self.SIZE)
        pygame.display.set_caption('Gay game')


        self.running = True

    def game_cycle(self):
        while self.running:
            #pygame.mouse.set_visible(False)  # скрывает мышь
            if self.start_game:

                self.GAME = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            if self.StartScene.change:
                                self.StartScene.change = False
                            elif not self.StartScene.change:
                                self.start_game = False
                                self.start_part = True
                                self.sound.START_AUDIO.play(-1)
                                for e in self.group_draw:
                                    e.kill()
                                self.button.clear()
                                #self.dialog_tab.clear(True)
                                self.dialog_tab.dialog_with(('FirstCutscene', 'text_1'))
                                self.Scene = object.Cutscene('data\\катсцены\\1 начало\\начало_', self.HEIGHT, 'spawn')
                                self.group_draw.add(self.Scene)

                self.screen.fill((255, 255, 255))
                if (time.process_time() - self.StartScene.time) <= 5 and self.StartScene.change != False:
                    self.StartScene.upd(True)
                elif (time.process_time() - self.StartScene.time) <= 3 and self.StartScene.change == False:
                    #start_part = True
                    self.StartScene.upd(False)

                elif (time.process_time() - self.StartScene.time) > 3 and self.StartScene.change == False:
                    self.start_game = False
                    self.start_part = True
                    self.sound.START_AUDIO.play(-1)
                    for e in self.group_draw:
                        e.kill()
                    self.button.clear()
                    self.Scene = object.Cutscene('data\\катсцены\\1 начало\\начало_', self.HEIGHT, 'spawn')
                    #self.dialog_tab.clear(True)
                    self.dialog_tab.dialog_with(('FirstCutscene', 'text_1'))
                    self.group_draw.add(self.Scene)
                else:
                    if self.StartScene.change != False:
                        self.StartScene.change = False
                        self.StartScene.time = time.process_time()
                if self.start_game:
                    self.start_game_gr.draw(self.screen)

                    self.window.blit(self.screen, self.middle)
                    pygame.display.flip()
                    self.clock.tick(60)






            elif self.KPK:

                self.GAME = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            if len(self.game) != 0:
                                self.KPK = False
                                self.button.clear()
                                for e in self.group_draw:
                                    e.kill()
                                for e in self.group_interface:
                                    e.kill()
                                for e in self.enemy:
                                    e.kill()
                                for e in self.batton_in_KPK:
                                    e.kill()
                                for i in game:
                                    if type(i) != object.Platform:  # не понятный баг с исчезновение пауков
                                        self.group_draw.add(i)
                                for i in self.enemy:
                                    i.kill()
                                    self.group_draw.add(i)
                                self.interface_bytton()
                                break
                        if event.key == pygame.K_k:
                            if len(game) != 0:
                                self.KPK = False
                                self.button.clear()
                                for e in self.group_draw:
                                    e.kill()
                                for e in self.group_interface:
                                    e.kill()
                                for e in self.batton_in_KPK:
                                    e.kill()
                                for e in self.enemy:
                                    e.kill()
                                for i in self.game:
                                    if type(i) != object.Platform:  # не понятный баг с исчезновение пауков
                                        self.group_draw.add(i)
                                for i in self.enemy:
                                    i.kill()
                                    self.group_draw.add(i)
                                interface_bytton()
                                break
                    if event.type == pygame.MOUSEMOTION:
                        for i in self.button:
                            if i.rect.collidepoint((event.pos[0] - self.jump_x, event.pos[1] - self.jump_y)):
                                i.mouse(False)
                            else:
                                i.mouse(True)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if len(self.info) == 0:
                                for i in self.button:
                                    if i.rect.collidepoint((event.pos[0] - self.jump_x, event.pos[1] - self.jump_y)):
                                        if i.name != 'back':
                                            pl = object.Info(i.name)
                                            self.info.append(pl)
                                            self.group_draw.add(pl)
                                        else:
                                            if len(self.game) != 0:
                                                self.KPK = False
                                                self.button.clear()
                                                for e in self.group_draw:
                                                    e.kill()
                                                for e in self.group_interface:
                                                    e.kill()
                                                for e in self.batton_in_KPK:
                                                    e.kill()
                                                for e in self.enemy:
                                                    e.kill()
                                                for i in self.game:
                                                    if type(i) != object.Platform:  # не понятный баг с исчезновение пауков
                                                        self.group_draw.add(i)
                                                for i in self.enemy:
                                                    i.kill()
                                                    self.group_draw.add(i)
                                                self.interface_bytton()
                                                break
                            else:
                                for i in self.batton_in_KPK:
                                    if i.rect.collidepoint((event.pos[0] - self.jump_x, event.pos[1] - self.jump_y)):
                                        if len(self.info) > 0:
                                            self.info[0].life_die(False)
                                        self.info.clear()


                        if event.button == 3:
                            if len(self.info) > 0:
                                self.info[0].life_die(False)
                            self.info.clear()

                if self.KPK:
                    self.screen.fill((255, 255, 255))
                    if len(self.info) > 0:
                        if not self.info[0].life_die(True):
                            self.info.clear()
                    self.group_draw.draw(self.screen)
                    self.batton_in_KPK.draw(self.screen)
                    self.window.blit(self.screen, self.middle)
                    pygame.display.flip()
                    self.clock.tick(60)
                else:
                    if len(self.info) > 0:
                        self.info[0].life_die(False)
                    self.info.clear()
                    self.sound.clear()

            elif self.loading:
                self.GAME = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False

                self.screen.fill((255, 255, 255))

                self.group_draw.draw(self.screen)
                self.kpk_width = 904
                self.menu_width = 10
                self.all_height = 10
                self.start_game_gr.draw(self.screen)
                font = pygame.font.Font('pixle_font.ttf', 15)
                txt = font.render('Чтобы   пройти   щупальцехвата,   киньте   в   него   ягодой,   на   ПКМ', 1, (255, 255, 255))
                self.screen.blit(txt, (245, 500))
                self.window.blit(self.screen, self.middle)
                pygame.display.flip()
                if (time.process_time() - self.StartScene.time) <= 4:
                    self.StartScene.upd(True)
                else:
                    self.loading = False
                    self.menu = False
                    self.camera_level('level1')
                    self.interface_bytton()
                self.clock.tick(60)

            elif self.after_words:
                GAME = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False



                screen.fill((255, 255, 255))
                if after_count < 2:
                    after_count+= 1
                if not words.update():
                    running = False
                group_draw.draw(screen)
                window.blit(screen, middle)
                pygame.display.flip()
                clock.tick(60)

            elif self.pre_alpha_scene:
                GAME = False
                inf = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEMOTION:
                        pass
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            sound.clear()
                            menu = True
                            pre_alpha_scene = False
                            game.clear()
                            for e in group_draw:
                                e.kill()
                            for e in group_interface:
                                e.kill()
                            teleports.clear()
                            enemy.clear()
                            tree.clear()
                            monster.clear()
                            button.clear()
                            HERO.who_kill.clear()
                            create_button()
                            HERO.helth = 10
                            HERO.death = False
                            sound.clear()
                            sound.MENU_AUDIO.play(-1)

                            #inf = True



                screen.fill((255, 255, 255))
                screen.blit(pygame.image.load('end_phrase.jpg').convert(),(0, 0))
                black_theme.draw(screen)
                window.blit(screen, middle)
                #group_draw.draw(screen)
                #Scene.upd()

                pygame.display.flip()
                pygame.time.Clock().tick(60)

            elif self.die_end:
                GAME = False
                inf = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEMOTION:
                        pass
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            #sound.clear()
                            pre_alpha_scene = True
                            die_end = False
                            game.clear()
                            for e in group_draw:
                                e.kill()
                            for e in group_interface:
                                e.kill()
                            teleports.clear()
                            enemy.clear()
                            tree.clear()
                            monster.clear()
                            button.clear()
                            HERO.who_kill.clear()
                            create_button()
                            HERO.helth = 10
                            HERO.death = False
                            #sound.clear()
                            #sound.MENU_AUDIO.play(-1)

                            #inf = True



                screen.fill((255, 255, 255))
                screen.blit(pygame.image.load('data\катсцены\экран_проигрыш_вы_всрали.png').convert(),(0, 0))
                black_theme.draw(screen)
                window.blit(screen, middle)
                #group_draw.draw(screen)
                #Scene.upd()

                pygame.display.flip()
                pygame.time.Clock().tick(60)

            elif self.scene_enemy:
                GAME = False
                inf = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEMOTION:
                        pass
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            die_end = True
                            scene_enemy = False
                            black_count = 0
                            black_theme.zero()
                            #inf = True



                screen.fill((255, 255, 255))
                screen.blit(pygame.image.load('data\\катсцены\\5 грибной паук\\грибной_паук_проигрыш.png').convert(),(0, 0))
                black_theme.draw(screen)
                window.blit(screen, middle)
                #group_draw.draw(screen)
                #Scene.upd()

                pygame.display.flip()
                clock.tick(60)

            elif self.scene_enemy2:
                GAME = False
                inf = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEMOTION:
                        pass
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            die_end = True
                            scene_enemy2 = False
                            black_theme.zero()
                            #inf = True



                screen.fill((255, 255, 255))
                screen.blit(pygame.image.load('data\\катсцены\\6 ёж\\ёж_проигрыш.png').convert(),(0, 0))
                black_theme.draw(screen)
                window.blit(screen, middle)
                #group_draw.draw(screen)
                #Scene.upd()

                pygame.display.flip()
                pygame.time.Clock().tick(60)

            elif self.scene_enemy3:
                GAME = False
                inf = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEMOTION:
                        pass
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            die_end = True
                            scene_enemy3 = False
                            black_count = 0




                screen.fill((255, 255, 255))

                screen.blit(pygame.image.load('data\\катсцены\\2 тентакли\\тентакли.png').convert(), (0, 0))
                black_theme.draw(screen)
                window.blit(screen, middle)
                #group_draw.draw(screen)
                #Scene.upd()

                pygame.display.flip()
                pygame.time.Clock().tick(60)

            elif self.start_part:
                self.GAME = False
                inf = False
                skip = False
                self.next_dialog = False

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            skip = True
                        if event.key == pygame.K_a:
                            if self.Scene.count != 1:
                                self.Scene.count = 1
                                self.Scene.lock = 0
                                self.Scene.anim = False
                                self.Scene.animcount = 0
                                self.Scene.image = pygame.image.load('data\\катсцены\\1 начало\\начало_1.png').convert()
                                self.Scene.image.fill((0,0,0))
                        if event.key == pygame.K_d:
                            self.Scene.lock = 1
                            inf = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.Scene.lock = 1
                            inf = True
                        if event.button == 3:
                            self.next_dialog = True

                if skip:
                    self.sound.clear()
                    #self.dialog_tab.clear(True)
                    self.menu = True
                    self.start_part = False
                    self.create_button()
                    self.sound.MENU_AUDIO.play(-1)
                else:
                    self.screen.fill((255, 255, 255))
                    if (self.Scene.count == 3 or self.Scene.count == 4 or self.Scene.count == 5) and self.next_dialog:
                        pass
                    self.group_draw.draw(self.screen)
                    if self.dialog_tab.draw:
                        self.screen.blit(self.dialog_tab.image, (0, 0))
                    self.window.blit(self.screen, self.middle)
                    if inf:
                        if self.Scene.count not in [1] and (self.dialog_start_part < 5 and self.Scene.count != 3):
                            self.dialog_tab.check(True)
                        #if Scene.count == 4:
                            #dialog_tab.check(True)
                        if self.Scene.count == 5:
                            self.dialog_tab.check(True)
                        #if Scene.count == 6:
                        #    dialog_tab.check(True)
                        if self.dialog_start_part < 5 and self.Scene.count == 3:
                            self.dialog_start_part += 1
                            self.dialog_tab.check(True)
                        else:
                            if self.Scene.upd():
                                self.sound.clear()
                                self.menu = True
                                self.start_part = False
                                self.create_button()
                                self.sound.MENU_AUDIO.play(-1)
                    if self.Scene.count in [1, 4]:
                        self.Scene.upd()
                        #if Scene.count == 5:
                            #dialog_tab.check(True)

                    pygame.display.flip()
                    pygame.time.Clock().tick(60)

            elif self.settings:
                self.GAME = False
                First_on_audio = 0
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.menu = True
                            self.settings = False
                            if len(self.game) != 0:
                                self.create_button_2()
                            else:
                                self.create_button()
                    if event.type == pygame.MOUSEMOTION:
                        for i in self.button:
                            if i.rect.collidepoint((event.pos[0] - self.jump_x, event.pos[1] - self.jump_y)):  # добавить залипание выбранной кнопки звука
                                i.mouse(False)
                            else:
                                i.mouse(True)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1 or event.button == 3:
                            for i in self.button:
                                if i.rect.collidepoint((event.pos[0] - self.jump_x, event.pos[1] - self.jump_y)):
                                    if i.who == 'music' or i.who == 'sound':
                                        self.sound_correct(i.name, i.who)
                                    if i.name == 'назад':
                                        self.menu = True
                                        self.settings = False
                                        if len(self.game) != 0:
                                            self.create_button_2()
                                        else:
                                            self.create_button()
                                    self.sound.BUTTON.play()


                self.screen.fill((255, 255, 255))
                self.group_draw.draw(self.screen)
                font = pygame.font.Font('pixle_font.ttf', 30)
                txt = font.render('Музыка', 1, (255, 255, 255))
                self.screen.blit(txt, (self.WIDTH//3 - 140, 65))
                font = pygame.font.Font('pixle_font.ttf', 30)
                txt = font.render('Звуки', 1, (255, 255, 255))
                self.screen.blit(txt, (self.WIDTH//3 - 140, 285))

                self.window.blit(self.screen, self.middle)
                pygame.display.flip()
                self.clock.tick(60)

            elif self.menu:
                self.GAME = False
                self.First_on_audio = 0
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            if len(self.game) != 0:
                                self.menu = False
                                self.button.clear()
                                #self.dialog_tab.clear(True)
                                for e in self.group_draw:
                                    e.kill()
                                for e in self.group_interface:
                                    e.kill()
                                for e in self.enemy:
                                    e.kill()
                                for i in self.game:
                                    if type(i) != object.Platform:  # не понятный баг с исчезновение пауков
                                        self.group_draw.add(i)
                                for i in self.enemy:
                                    i.kill()
                                    self.group_draw.add(i)
                                self.interface_bytton()
                                break
                    if event.type == pygame.MOUSEMOTION:
                        for i in self.button:
                            if i.rect.collidepoint((event.pos[0] - self.jump_x, event.pos[1] - self.jump_y)):
                                i.mouse(False)
                            else:
                                i.mouse(True)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1 or event.button == 3:
                            for i in self.button:
                                if i.rect.collidepoint((event.pos[0] - self.jump_x, event.pos[1] - self.jump_y)):
                                    if i.name == 'Play':
                                        self.menu = False
                                        self.loading = True
                                        self.sound.clear()
                                        self.button.clear()
                                        #self.dialog_tab.clear(True)
                                        self.after_count = 0
                                        self.StartScene.change = True
                                        self.StartScene.time = time.process_time()
                                        for e in self.group_draw:
                                            e.kill()
                                        self.processing_start()
                                        break

                                    if i.name == 'Settings':
                                        self.settings = True
                                        self.menu = False
                                        self.create_button_setting()
                                        break
                                    if i.name == 'Exit':
                                        self.running = False
                                        break

                                    if i.name == 'Continue':
                                        self.menu = False
                                        self.button.clear()
                                        #self.dialog_tab.clear(True)
                                        for e in self.group_draw:
                                            e.kill()
                                        for e in self.group_interface:
                                            e.kill()
                                        for e in self.enemy:
                                            e.kill()
                                        for i in self.game:
                                            if type(i) != object.Platform:  # не понятный баг с исчезновение пауков
                                                self.group_draw.add(i)
                                        for i in self.enemy:
                                            i.kill()
                                            self.group_draw.add(i)
                                        self.interface_bytton()
                                        break
                                    if i.name != 'Shop':
                                        self.sound.BUTTON.play()
                                        break
                if self.menu:
                    self.screen.fill((0, 0, 0))
                    self.group_draw.draw(self.screen)
                    font = pygame.font.Font('pixle_font.ttf', 10)
                    txt = font.render(self.VERSION, 1, (255, 255, 255))
                    self.screen.blit(txt, (35, 10))
                    self.window.blit(self.screen, self.middle)
                    pygame.display.flip()
                    self.clock.tick(60)


            elif self.map:
                GAME = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE or event.key == pygame.K_m:
                            if len(game) != 0:
                                sound.clear()
                                map = False
                                button.clear()
                                for e in group_draw:
                                    e.kill()
                                for e in group_interface:
                                    e.kill()
                                for e in enemy:
                                    e.kill()
                                for i in game:
                                    if type(i) != object.Platform:  # не понятный баг с исчезновение пауков
                                        group_draw.add(i)
                                for i in enemy:
                                    i.kill()
                                    group_draw.add(i)
                                interface_bytton()
                                break

                    if event.type == pygame.MOUSEMOTION:
                        for i in button:
                            if i.rect.collidepoint((event.pos[0] - jump_x, event.pos[1] - jump_y)):
                                i.mouse(False)
                            else:
                                i.mouse(True)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1 or event.button == 3:
                            for i in button:
                                if i.rect.collidepoint((event.pos[0] - jump_x, event.pos[1] - jump_y)):
                                    screen.fill((0, 0, 0))
                                    if i.name == 'back':
                                        if len(game) != 0:
                                            sound.clear()
                                            #sound.BACK_AUDIO.play(-1)
                                            #sound.BACK2_AUDIO.play(-1)
                                            map = False
                                            button.clear()
                                            for e in group_draw:
                                                e.kill()
                                            for e in group_interface:
                                                e.kill()
                                            for e in enemy:
                                                e.kill()
                                            for i in game:
                                                if type(i) != object.Platform:  # не понятный баг с исчезновение пауков
                                                    group_draw.add(i)
                                            for i in enemy:
                                                i.kill()
                                                group_draw.add(i)
                                            interface_bytton()

                                    pygame.display.flip()
                                    sound.BUTTON.play()



                screen.fill((255, 255, 255))
                screen.blit(pygame.image.load('data\\МИНИКАРТА\\миникарта.png').convert(), (0, 0))
                group_draw.draw(screen)
                window.blit(screen, middle)
                pygame.display.flip()
                clock.tick(60)

            else:
                self.GAME = True
                self.ball = 0
                if not self.HERO.chat:
                    self.dialog_tab.kill()
                else:
                    self.group_interface.add(self.dialog_tab)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.UP = True
                        if event.key == pygame.K_a:
                            self.LEFT = True
                        if event.key == pygame.K_d:
                            self.RIGHT = True
                        if event.key == pygame.K_ESCAPE:
                            self.menu = True
                            self.Strike = False
                            self.UP = False
                            self.LEFT = False
                            self.RIGHT = False
                            self.E = False
                            self.button.clear()
                            self.create_button_2()
                            self.sound.clear()
                            self.sound.MENU_AUDIO.play(-1)
                        if event.key == pygame.K_m:
                            self.map = True

                            self.Strike = False
                            self.UP = False
                            self.LEFT = False
                            self.RIGHT = False
                            self.E = False
                            self.sound.clear()
                            self.button.clear()
                            self.create_button_map()
                            self.sound.MENU_AUDIO.play(-1)

                        if event.key == pygame.K_k:
                            self.KPK = True

                            self.Strike = False
                            self.UP = False
                            self.LEFT = False
                            self.RIGHT = False
                            self.E = False
                            self.button.clear()
                            self.KPK_create()
                            self.sound.clear()
                            self.sound.MENU_AUDIO.play(-1)


                    if event.type == pygame.MOUSEMOTION:
                        for i in self.button:
                            if i.rect.collidepoint((event.pos[0] - self.jump_x, event.pos[1] - self.jump_y)):
                                i.mouse(False)
                            else:
                                i.mouse(True)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1 or event.button == 3:
                            for i in self.button:
                                if i.rect.collidepoint((event.pos[0] - self.jump_x, event.pos[1] - self.jump_y)):
                                    self.screen.fill((0, 0, 0))
                                    if i.name == 'KPK':
                                        self.KPK = True
                                        self.Strike = False
                                        self.UP = False
                                        self.LEFT = False
                                        self.RIGHT = False
                                        self.E = False
                                        self.button.clear()
                                        self.KPK_create()
                                        self.sound.clear()
                                        self.sound.MENU_AUDIO.play(-1)
                                    if i.name == 'menu_ink':
                                        self.menu = True
                                        self.Strike = False
                                        self.UP = False
                                        self.LEFT = False
                                        self.RIGHT = False
                                        self.E = False
                                        self.button.clear()
                                        self.create_button_2()
                                        self.sound.clear()
                                        self.sound.MENU_AUDIO.play(-1)

                                    pygame.display.flip()
                                    self.sound.BUTTON.play()
                            else:
                                if event.button == 1:
                                    self.Strike = True
                                    self.E = False
                                    #first_strike_timer = time.process_time()
                                    if self.HERO.side == 1:
                                        self.coord_x = self.HERO.rect.x + self.HERO.rect.width
                                    elif self.HERO.side == -1:
                                        self.coord_x = self.HERO.rect.x
                                    if self.HERO.fight:
                                        pl = object.Ball(self.coord_x, self.HERO.rect.y + 20, self.HERO.side)
                                        self.Bullet.add(pl)
                                        self.group_draw.add(pl)
                                        self.sound.STRIKE_AUDIO.play()
                                if event.button == 3:
                                    if self.HERO.chat:
                                        self.dialog_tab.check(True, self.HERO)
                                    else:
                                        self.sound.USE_AUDIO.play()
                                        self.E = True
                                        self.Strike = False

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:
                            self.UP = False
                        if event.key == pygame.K_a:
                            self.LEFT = False
                        if event.key == pygame.K_d:
                            self.RIGHT = False
                    if event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                            self.Strike = False
                        if event.button == 3:
                            self.E = False

                # состояния
                self.game_or_not = (not self.menu and not self.map and not self.scene_enemy and not self.scene_enemy2 and not self.scene_enemy3 and not self.settings and not self.KPK and not self.pre_alpha_scene)
                self.take_barries = self.HERO.update(self.LEFT, self.RIGHT, self.UP, self.group_platform,
                                                     self.teleports, self.tree, self.enemy, self.E, self.screen,
                                                     self.BOSS, self.monster, self.Strike, self.dialog, self.dialog_tab)
                self.draw()
                self.health_tab.new_image(self.HERO.helth)

                if self.HERO.helth <= 0:
                    self.HERO.respawn()
                if self.HERO.fight and not self.fight and self.game_or_not:
                    self.fight = True
                    self.sound.clear()
                    self.sound.BACK2_AUDIO.stop()
                    self.sound.BACK_AUDIO.stop()
                    self.sound.FIGHT_AUDIO.play(-1)
                elif not self.HERO.fight and self.fight and self.game_or_not:
                    self.fight = False
                    self.sound.clear()
                    self.sound.FIGHT_AUDIO.stop()
                    self.sound.BACK2_AUDIO.play(-1)
                    self.sound.BACK_AUDIO.play(-1)
                elif not self.HERO.fight and not self.fight:
                    if (self.sound.BACK_AUDIO.get_num_channels() <= 0 or self.sound.BACK2_AUDIO.get_num_channels() <= 0) and self.game_or_not:
                        self.sound.FIGHT_AUDIO.stop()
                        self.sound.clear()
                        self.sound.BACK2_AUDIO.play(-1)
                        self.sound.BACK_AUDIO.play(-1)
                if (self.sound.BACK_AUDIO.get_num_channels() <= 0 or self.sound.BACK2_AUDIO.get_num_channels() <= 0) and self.sound.FIGHT_AUDIO.get_num_channels() <= 0 and self.game_or_not:
                    self.sound.FIGHT_AUDIO.stop()
                    self.sound.clear()
                    self.sound.BACK2_AUDIO.play(-1)
                    self.sound.BACK_AUDIO.play(-1)

                pygame.display.flip()
                self.clock.tick(60)

                if self.HERO.death:
                    self.sound.clear()
                    self.sound.CUTSCENE_AUDIO.play(-1)
                    self.black_count = 0
                    if len(self.HERO.who_kill) != 0:
                        if type(self.HERO.who_kill[0]) == object.Enemy:
                            self.scene_enemy = True
                        elif type(self.HERO.who_kill[0]) == object.Enemy2:
                            self.scene_enemy2 = True
                            self.scene_enemy_def()
                        elif type(self.HERO.who_kill[0]) == object.Monster:
                            self.scene_enemy3 = True
                            self.scene_moster()

        for i in self.group_draw:
            i.kill()
        for i in self.group_interface:
            i.kill()
        for i in self.group_platform:
            i.kill()
        for i in self.batton_in_KPK:
            i.kill()
        for i in self.start_game_gr:
            i.kill()
        for i in self.Bullet:
            i.kill()

        self.teleports.clear()
        self.enemy.clear()
        self.all_obj.clear()
        self.matrix.clear()
        self.tree.clear()
        self.balls.clear()
        self.game.clear()
        self.monster.clear()
        self.info.clear()
        self.button.clear()
        self.animation_balck.clear()
        self.updai_bool = False
        self.updBullet_ai = False
        self.updHERO_ai = False
        import delete_trash
        pygame.quit()
        quit()
        sys.exit()


    def create_button(self):
        self.button.clear()
        for e in self.group_draw:
            e.kill()
        for e in self.group_interface:
            e.kill()
        w, h = 302, 64
        self.button.append(object.Button(328, 145, w, h, 'Play', tag=False))
        self.button.append(object.Button(328, 230, w, h, 'Shop', tag=False))
        self.button.append(object.Button(328, 315, w, h, 'Settings', tag=False))
        self.button.append(object.Button(328, 400, w, h, 'Exit', tag=False))
        self.group_draw.add(object.Background(0, 0, 'data\МЕНЮ\меню_фон.png'))
        for i in self.button:
            self.group_draw.add(i)

    def create_button_2(self):
        self.button.clear()

        for e in self.group_draw:
            e.kill()
        for e in self.group_interface:
            e.kill()
        w, h = 302, 64
        self.button.append(object.Button(328, 145, w, h, 'Continue', tag=False))
        self.button.append(object.Button(328, 225, w, h, 'Shop', tag=False))
        self.button.append(object.Button(328, 315, w, h, 'Settings', tag=False))
        self.button.append(object.Button(328, 400, w, h, 'Exit', tag=False))
        self.group_draw.add(object.Background(0, 0, 'data\МЕНЮ\меню_фон.png'))
        for i in self.button:
            self.group_draw.add(i)

    def create_button_setting(self):
        self.button.clear()
        for e in self.group_draw:
            e.kill()
        for e in self.group_interface:
            e.kill()
        w, h = 113, 59
        music = 130
        sound = 350
        name_a = 'music'
        name_b = 'sound'
        name_c = 'menu'
        # music
        self.button.append(object.Button(70, music, w, h, '0', name_a))
        self.button.append(object.Button(183, music, w, h, '25', name_a))
        self.button.append(object.Button(293, music, w, h, '50', name_a))
        self.button.append(object.Button(402, music, w, h, '75', name_a))
        self.button.append(object.Button(512, music, w, h, '100', name_a))

        # sound
        self.button.append(object.Button(70, sound, w, h, '0', name_b))
        self.button.append(object.Button(183, sound, w, h, '25', name_b))
        self.button.append(object.Button(293, sound, w, h, '50', name_b))
        self.button.append(object.Button(402, sound, w, h, '75', name_b))
        self.button.append(object.Button(512, sound, w, h, '100', name_b))

        # menu
        self.button.append(object.Button(760, 420, 135, 68, 'назад', name_c, False))
        self.group_draw.add(object.Background(0, 0, 'data\\НАСТРОЙКИ\\фон.png'))
        for i in self.button:
            self.group_draw.add(i)

    def sound_correct(self, number, name):
        level = 0
        if name == "music":
            if number == '0':
                level = 0
            if number == '25':
                level = 0.10
            if number == '50':
                level = 0.25
            if number == '75':
                level = 0.45
            if number == '100':
                level = 0.5
            self.sound.BACK_AUDIO.set_volume(level)
            self.sound.START_AUDIO.set_volume(level)
            self.sound.CUTSCENE_AUDIO.set_volume(level)
            self.sound.BACK2_AUDIO.set_volume(level)
            self.sound.MENU_AUDIO.set_volume(level)
            self.sound.FIGHT_AUDIO.set_volume(level)
            self.sound.BACK_AFTER_WORDS.set_volume(level)
        elif name == "sound":
            if number == '0':
                level = 0
            if number == '25':
                level = 0.10
            if number == '50':
                level = 0.25
            if number == '75':
                level = 0.45
            if number == '100':
                level = 0.5
            self.sound.USE_AUDIO.set_volume(level)
            self.sound.DAMAGE_AUDIO.set_volume(level)
            self.sound.STRIKE_AUDIO.set_volume(level)
            self.sound.TAKE_AUDIO.set_volume(level)
            self.sound.BACK2_AUDIO.set_volume(level)
            self.sound.STEP_AUDIO.set_volume(level)
            self.sound.STEP2_AUDIO.set_volume(level)
            self.HERO.step_AUDIO.set_volume(level)
            self.HERO.step2_AUDIO.set_volume(level)
            for i in self.sound.SPIDER_AUDIO:
                i.set_volume(level)
            self.sound.BUTTON.set_volume(level)

    def make_level(self, level):
        x, y = 0, 0

        def platform(row, col, obj):
            if obj == object.Teleport_BOSS:
                pl = obj(x, y, self.lens*10, self.lens)
                self.game.append(pl)
            else:
                pl = obj(x, y, self.lens, self.lens)
                self.game.append(pl)
            #group_draw.add(pl)
            if object.Platform == obj:
                self.group_platform.add(pl)
                self.game.append(pl)
            else:
                self.teleports.append(pl)
                self.game.append(pl)

        #width =
        for row in level:
            for col in row:
                if col == ' ':
                    self.all_obj.append('')
                else:
                    if col in ['-', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'l', 'b']:
                        if col == 'q':
                            pl = object.Background(x, y, 'data/фоны/начало.png')
                            self.group_draw.add(pl)
                            self.game.append(pl)
                        # горизонталь
                        if col == 'w':
                            pl = object.Background(x, y, 'data/фоны/горизонталь_1.png')
                            self.group_draw.add(pl)
                            self.game.append(pl)
                        if col == 'e':
                            pl = object.Background(x, y, 'data/фоны/горизонталь_2.png')
                            self.group_draw.add(pl)
                            self.game.append(pl)
                        if col == "b":
                            pl = object.Background(x, y + 180, 'end_phrase.jpg')
                            self.group_draw.add(pl)
                            self.game.append(pl)
                        if col == 'l':
                            pl = object.Background(x, y, 'data/фоны/началостарт.png')
                            self.group_draw.add(pl)
                            self.game.append(pl)
                        # поворот
                        if col == 'r':
                            pl = object.Background(x, y, 'data/фоны/поворот_1.png')
                            self.group_draw.add(pl)
                            self.game.append(pl)
                        if col == 't':
                            pl = object.Background(x, y, 'data/фоны/поворот_2.png')
                            self.group_draw.add(pl)
                            self.game.append(pl)
                        if col == 'y':
                            pl = object.Background(x, y, 'data/фоны/поворот_3.png')
                            self.group_draw.add(pl)
                            self.game.append(pl)
                        if col == 'u':
                            pl = object.Background(x, y, 'data/фоны/поворот_4.png')
                            self.group_draw.add(pl)
                            self.game.append(pl)
                        if col == 'f':
                            pl = object.Background(x, y, 'data/фоны/овраг.png')
                            self.group_draw.add(pl)
                            self.game.append(pl)
                            pl2 = object.Monster(x+self.lens*3, y+self.lens*6)
                            self.game.append(pl2)
                            self.group_draw.add(pl2)
                            self.monster.append(pl2)
                        if col == 'i':
                            pl = object.Background(x, y, 'data/фоны/вертикаль.png')
                            self.group_draw.add(pl)
                            self.game.append(pl)
                        if col == 'p':
                            pl = object.Background(x, y, 'data/фоны/конец.png')
                            self.group_draw.add(pl)
                            self.game.append(pl)
                        if col == 'a':
                            pl = object.Tree(x, y, 'data/фоны/развилка_вниз.png', 'data/фоны/развилка_вниз_без_ягод.png')
                            self.group_draw.add(pl)
                            self.tree.append(pl)
                            self.game.append(pl)
                        if col == 's':
                            pl = object.Tree(x, y, 'data/фоны/развилка_наверх.png', 'data/фоны/развилка_наверх_без_ягод.png')
                            self.group_draw.add(pl)
                            self.game.append(pl)
                            self.tree.append(pl)
                        if col == 'd':
                            pl = object.Tree(x, y, 'data/фоны/развилка_направо.png', 'data/фоны/развилка_направо_без_ягод.png')
                            self.group_draw.add(pl)
                            self.game.append(pl)
                            self.tree.append(pl)
                        platform(row, col, object.Platform)

                    if (col == '@' and self.HERO.spawn == '@') or (col == '#' and self.HERO.spawn == '#') or (col == '%' and self.HERO.spawn == '%'):
                        self.HERO.new_coord(x, y)
                    if col == "^":
                        self.dialog.add(object.DialogWindowSpawner(x, y, self.count_dialog))
                        self.count_dialog += 1
                    if col == "v":
                        platform(row, col, object.Teleport_B)
                    if col == "!":
                        platform(row, col, object.Teleport_BOSS)
                    if col == "?":
                        platform(row, col, object.Teleport_COME)
                    if col == "&":
                        pl = object.Enemy(x, y, self.sound)
                        self.enemy.append(pl)
                        self.game.append(pl)
                    if col == "$":
                        pl = object.Enemy2(x, y, self.sound)
                        self.enemy.append(pl)
                        self.game.append(pl)
                    if col == "$":
                        self.BOSS.new_coord(x, y)
                        self.BOSS.isdie = False
                    if col == "_":
                        pass

                x += self.lens
            y += self.lens
            x = 0
        for pl in self.enemy:
            self.group_draw.add(pl)
        self.game.reverse()

    def camera_level(self, place):
        for e in self.group_draw:
            e.kill()
        for e in self.group_interface:
            e.kill()
        self.teleports.clear()
        self.enemy.clear()
        self.tree.clear()
        self.monster.clear()
        self.button.clear()
        self.BOSS.isdie = True
        self.Boss_spawn = False
        self.total_level_width = len(MAP[place][0])*self.lens
        self.total_level_height = len(MAP[place])*self.lens
        self.camera.new(self.total_level_width, self.total_level_height)
        self.make_level(MAP[place])
        if place == 'level69':
            self.group_draw.add(BOSS)
            self.Boss_spawn = True
        self.HERO.kill()
        self.group_draw.add(self.HERO)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.last_level = self.location
        self.location = self.HERO.level
        try:
            if self.draw_loc != self.location:
                self.draw_loc = self.location
                #camera_level(f'level{str(location)}')

        except KeyError:
            self.HERO.level = self.last_level

        self.camera.update(self.HERO)
        for e in self.group_draw:
            coord = self.camera.apply(e)
            obl = 600
            if pygame.Rect(self.HERO.rect.topleft[0]-obl, self.HERO.rect.topleft[1]-obl, 2*obl, 2*obl).colliderect(e.rect):
                self.screen.blit(e.image, coord)

        white = (255, 255, 255)
        if self.HERO.chat:
            if self.dialog_tab.phrase == 0:
                 self.dialog_tab.phrase += 1
                 self.dialog_tab.check(False)
        if not self.HERO.chat and not self.dialog_tab.bool_killed_sprite:
            self.dialog_tab.delete_table()
        elif self.HERO.chat and self.dialog_tab.bool_killed_sprite:
            self.group_interface.add(self.dialog_tab)
            self.dialog_tab.bool_killed_sprite = False
        self.group_interface.draw(self.screen)
        #Bullet.draw(screen)
        if self.take_barries:
            font = pygame.font.Font('pixle_font.ttf', 22)
            txt = font.render('ПКМ - собрать\бросить плоды', 1, white)
            self.screen.blit(txt, (365, 500))
        self.window.blit(self.screen, self.middle)
        pygame.display.flip()

    def create_button_map(self):
        self.button.clear()
        for e in self.group_draw:
            e.kill()
        for e in self.group_interface:
            e.kill()
        w, h = 46, 46
        self.button.append(object.Button(20, 10, w, h, 'back', tag=False))
        for i in self.button:
            self.group_draw.add(i)

    '''
    if after_words:
        for e in group_draw:
            e.kill()
        button.clear()
        words = object.After_words(HEIGHT)
        words.play(sound.BACK_AFTER_WORDS)
        group_draw.add(words)
    '''

    def KPK_create(self):
        x_1 = 64
        x_2 = 364
        x_3 = 664
        w, h = 234, 64
        for e in self.group_draw:
            e.kill()
        for e in self.group_interface:
            e.kill()
        self.button.clear()
        self.button.append(object.Button(x_1, 140, w, h, '1', tag=False))
        #"""button.append(object.Button(x_1, 230, w, h, '2', tag=False))
        self.button.append(object.Button(x_1, 320, w, h, '3', tag=False))
        #button.append(object.Button(x_1, 408, w, h, '4', tag=False))"""
        self.button.append(object.Button(x_1, 230, w, h, '5', tag=False))
        self.button.append(object.Button(x_2, 230, w, h, '6', tag=False))
        #button.append(object.Button(x_2, 320, w, h, '7', tag=False))
        #button.append(object.Button(x_2, 408, w, h, '8', tag=False))
        #button.append(object.Button(x_3, 140, w, h, '9', tag=False))
        #button.append(object.Button(x_3, 230, w, h, '10', tag=False))
        #button.append(object.Button(x_3, 320, w, h, '11', tag=False))
        #button.append(object.Button(x_3, 408, w, h, '12', tag=False))"""
        pl = object.Button(20, 10, 48, 48, 'back', tag=False)
        self.batton_in_KPK.add(pl)
        self.button.append(pl)
        self.group_draw.add(object.Background(0, 0, r'data\КПК\1\фон.png'))
        for i in self.button:
            if i.name != 'back':
                self.group_draw.add(i)

    def scene_enemy_def(self):
        for e in self.group_draw:
            e.kill()
        self.teleports.clear()
        self.enemy.clear()
        self.tree.clear()
        self.monster.clear()
        self.button.clear()
        self.BOSS.isdie = True
        self.Boss_spawn = False
        self.button.clear()
        #Scene = object.Cutscene('data\\катсцены\\5 грибной паук\\грибной_паук_проигрыш.png', HEIGHT, 'enemy')
        #group_draw.add(Scene)

    def scene_moster(self):
        for e in self.group_draw:
            e.kill()
        self.teleports.clear()
        self.enemy.clear()
        self.tree.clear()
        self.monster.clear()
        self.button.clear()
        self.BOSS.isdie = True
        self.Boss_spawn = False
        self.button.clear()
        #Scene = object.Cutscene('data\\катсцены\\5 грибной паук\\грибной_паук_проигрыш.png', HEIGHT, 'enemy')
        #group_draw.add(Scene)

    def interface_bytton(self):
        pl = object.Button(self.kpk_width, self.all_height, 46, 39, 'KPK', tag=False)
        pl2 = object.Button(self.menu_width, self.all_height, 47, 46, 'menu_ink', tag=False)
        self.button.append(pl)
        self.button.append(pl2)
        self.group_interface.add(pl)
        self.group_interface.add(pl2)
        self.group_interface.add(self.health_tab)
        self.group_interface.add(self.dialog_tab)
        #self.HERO.kill()
        self.group_draw.add(self.HERO)




    # Потоки
    def damage(self):
        while self.updBullet_ai:
            try:
                if self.GAME:
                    info = pygame.sprite.groupcollide(self.Bullet, self.enemy, True, False)
                    keys_bullet = info.keys()
                    pygame.sprite.groupcollide(self.Bullet, self.group_platform, True, False)
                    self.Bullet.update(self.HERO, self.enemy)
                    for i in keys_bullet:
                        for j in info[i]:
                            self.sound.DAMAGE_AUDIO.play()
                            j.helth -= 1
                            j.damage = True
                            j.hit()
                            if j.helth < 0:
                                j.die()
                            break
                    self.clock.tick(60)
            except Exception as e:
                add_info_into_config.main('Third Thread: ' + str(e))
        print('Third Thread end.')



    def UpdAI(self):
        way = 1200
        while self.updai_bool:
            try:
                if self.GAME:
                    list_collide = lambda x: [Rect(i.rect.x - 500, i.rect.y-250, way, 500) for i in x]
                    b = list_collide(self.enemy)
                    a = self.HERO.rect.collidelistall(b)
                    for i in a:
                        self.enemy[i].AI(self.HERO, self.group_platform)
                    d = list_collide(self.monster)
                    q = self.HERO.rect.collidelistall(d)
                    for i in q:
                        self.monster[i].AI(self.HERO)
                    if self.Boss_spawn:
                        self.BOSS.AI(self.HERO, self.group_platform)
                    self.clock.tick(60)
            except Exception as e:
                add_info_into_config.main('Second Thread: ' + str(e))
        print('Second Thread end.')


    def updHERO_ai(self):
        while self.updHERO_ai:
            try:
                if self.GAME:
                    take_barries = self.HERO.update(self.LEFT, self.RIGHT, self.UP, self.group_platform,
                                                    self.teleports, self.tree, self.enemy, self.E, self.screen,
                                                    self.BOSS, self.monster, self.Strike)
                    self.clock.tick(60)
            except Exception as e:
                add_info_into_config.main('First Thread: ' + str(e))
        print('First Thread end.')

    def processing_start(self):
        self.updai_bool = True
        self.updBullet_ai = True
        self.updHERO_ai = True
        self.process_one = threading.Thread(target=self.UpdAI)
        self.process_two = threading.Thread(target=self.damage)
        self.process_one.start()
        self.process_two.start()
        #threading.Thread(target=self.updHERO_ai).start()








def main():
    My_Games = Game()

    My_Games.game_cycle()



if __name__ == '__main__':
    main()


    # иногда реально ненавижу git hub, снова для нового коммита
