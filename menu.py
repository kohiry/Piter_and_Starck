import pygame


def main(screen, width, height):
    font = pygame.font.Font(None, 40)
    text = font.render('Прыгать - Space', 25, (255, 0, 0))
    screen.blit(text, (width//2 - 100, height//2 - 90))
    text = font.render('Стрелять - F', 25, (255, 0, 0))
    screen.blit(text, (width//2 - 100, height//2 - 60))
    text = font.render('создавать врагов - E', 25, (255, 0, 0))
    screen.blit(text, (width//2 - 100, height//2 - 30))
    text = font.render('всего "патрон" - 4', 25, (255, 0, 0))
    screen.blit(text, (width//2 - 100, height//2))


if __name__ == '__main__':
    print('Не на чем, рисовать')
    input('нажми любую кнопку, чтобы выйти')
