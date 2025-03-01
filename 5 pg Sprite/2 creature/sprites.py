import os
import sys

import pygame

STEP = 10


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    size = width, height = 300, 300

    pygame.init()

    creature_image = load_image("creature.png")
    creature_rect = creature_image.get_rect(topleft=(0, 0))

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Герой двигается!")

    while pygame.event.wait().type != pygame.QUIT:
        screen.fill((255, 255, 255))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            creature_rect.x -= STEP
        if keys[pygame.K_RIGHT]:
            creature_rect.x += STEP
        if keys[pygame.K_UP]:
            creature_rect.y -= STEP
        if keys[pygame.K_DOWN]:
            creature_rect.y += STEP

        screen.blit(creature_image, creature_rect)
        pygame.display.flip()
    pygame.quit()
