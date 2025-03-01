import os
import sys

import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    size = width, height = 800, 600

    pygame.init()
    pygame.mouse.set_visible(False)

    cursor_image = load_image("arrow.png")
    cursor_rect = cursor_image.get_rect()

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Свой курсор мыши")

    while pygame.event.wait().type != pygame.QUIT:
        screen.fill((0, 0, 0))

        if pygame.mouse.get_focused():
            cursor_rect.topleft = pygame.mouse.get_pos()
            screen.blit(cursor_image, cursor_rect)

        pygame.display.flip()
    pygame.quit()
