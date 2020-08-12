import pygame
from screeninfo import get_monitors
pygame.init()


SIZE = WIDTH, HEIGHT = 1080, 700
window = pygame.display.set_mode((0, 0), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
screen = pygame.Surface(SIZE)
#screen = pygame.Surface((400, 400))
pygame.display.set_caption('Gay game')



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEMOTION:
            for i in button:
                print(event.pos, (i.rect.x, i.rect.y))
                if Rect(*event.pos, 2, 2).colliderect(i.image.rect):
                    i.mouse(False)
                else:
                    i.mouse(True)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 or event.button == 2:
                pass

    screen.fill((255, 255, 255))
    font = pygame.font.Font('pixle_font.ttf', 72)
    txt = font.render('Spider Gay', 1, (0, 0, 0))
    screen.blit(txt, (WIDTH//3, 100))
    group_draw.draw(screen)
    window.blit(screen, ((int(get_monitors()[0].width) - WIDTH) // 2, (int(get_monitors()[0].height) - HEIGHT) // 2))
    pygame.display.flip()
    pygame.time.Clock().tick(60)
