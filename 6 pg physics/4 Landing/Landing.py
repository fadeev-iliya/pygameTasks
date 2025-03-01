import os
import sys

import pygame

SIZE = WIDTH, HEIGHT = 750, 500
FPS = 60

pygame.init()
pygame.display.set_caption("Десант")
screen = pygame.display.set_mode(SIZE)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()

    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Landing(pygame.sprite.Sprite):
    image = load_image("pt.png")

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = Landing.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if not pygame.sprite.collide_mask(self, mountain):
            self.rect = self.rect.move(0, 1)


class Mountain(pygame.sprite.Sprite):
    image = load_image("mountains.png")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = HEIGHT


if __name__ == '__main__':
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    mountain = Mountain()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                Landing(*event.pos)

        screen.fill(pygame.Color('black'))

        all_sprites.draw(screen)
        all_sprites.update()

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
