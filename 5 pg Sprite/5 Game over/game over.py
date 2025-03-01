import os
import sys

import pygame

FPS = 60
SPEED = 200


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    size = width, height = 600, 300

    pygame.init()

    game_over_image = load_image("gameover.png")
    game_over_rect = game_over_image.get_rect(topright=(0, 0))

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Game over")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(pygame.Color('blue'))
        if game_over_rect.x < 0:
            game_over_rect.x += SPEED // FPS

        screen.blit(game_over_image, game_over_rect)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
