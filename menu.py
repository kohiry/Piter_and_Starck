import pygame
from screeninfo import get_monitors
pygame.init()


SIZE = WIDTH, HEIGHT = 1080, 700
window = pygame.display.set_mode((0, 0), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
screen = pygame.Surface(SIZE)
#screen = pygame.Surface((400, 400))
pygame.display.set_caption('Gay game')



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            run = False

    screen.fill((0, 0, 0))
    font = pygame.font.Font('pixle_font.ttf', 72)
    txt = font.render('Spider Gay', 1, (255, 255, 255))
    screen.blit(txt, (WIDTH//2, 100))
    window.blit(screen, ((int(get_monitors()[0].width) - WIDTH) // 2, (int(get_monitors()[0].height) - HEIGHT) // 2))
    pygame.display.flip()
