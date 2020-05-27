import pygame


def main(screen, width, height, font):

    font = pygame.font.Font(font, 40)
    text = font.render('Прыгать - Space', 25, (255, 0, 0))
    screen.blit(text, (width//2 - 100, height//2 - 90))
    text2 = font.render('Стрелять - F, ЛКМ', 25, (255, 0, 0))
    screen.blit(text2, (width//2 - 100, height//2 - 60))
    text3 = font.render('создавать врагов - E', 25, (255, 0, 0))
    screen.blit(text3, (width//2 - 100, height//2 - 30))
    text4 = font.render('всего "патрон" - 4', 25, (255, 0, 0))
    screen.blit(text4, (width//2 - 100, height//2))


if __name__ == '__main__':
    print('Не на чем, рисовать')
    input('нажми любую кнопку, чтобы выйти')
