import pygame
from screeninfo import get_monitors
from pygame import mixer
mixer.init()
pygame.init()


SIZE = WIDTH, HEIGHT = 1080, 700
window = pygame.display.set_mode((0, 0), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
screen = pygame.Surface(SIZE)
#screen = pygame.Surface((400, 400))
pygame.display.set_caption('Gay game')
BACK_AUDIO = mixer.Sound(file='audio/basicback.ogg')


running = True
BACK_AUDIO.play()
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((255, 255, 255))
    pygame.display.flip()
    pygame.time.Clock().tick(60)
