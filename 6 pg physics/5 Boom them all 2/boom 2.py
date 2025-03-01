import os
import random
import sys

import pygame

size = width, height = 500, 500


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Bomb(pygame.sprite.Sprite):
    bomb_image = load_image("bomb.png")
    boom_image = load_image("boom.png")

    def __init__(self, placed, *group):
        super().__init__(*group)
        self.image = Bomb.bomb_image
        self.rect = self.image.get_rect()
        while True:
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(height - self.rect.height)
            if not any(self.rect.colliderect(p) for p in placed):
                placed.append(self.rect.copy())
                break

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.boom_image


if __name__ == '__main__':
    pygame.init()
    all_sprites = pygame.sprite.Group()

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Boom them all - 2")
    clock = pygame.time.Clock()
    placed = []

    for _ in range(10):
        Bomb(placed, all_sprites)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)

        screen.fill((0, 0, 0))

        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
