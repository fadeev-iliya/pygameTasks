import random

import pygame

SIZE = WIDTH, HEIGHT = 500, 500
FPS = 60
IND = 5


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:
            self.add(ver_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(hor_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.radius = radius

        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"), (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)

        self.vel_x = random.randint(-5, 5)
        self.vel_y = random.randrange(-5, 5)

    def update(self):
        self.rect = self.rect.move(self.vel_x, self.vel_y)
        if pygame.sprite.spritecollideany(self, hor_borders):
            self.vel_y = -self.vel_y
        if pygame.sprite.spritecollideany(self, ver_borders):
            self.vel_x = -self.vel_x


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Столкновение шариков")
    screen = pygame.display.set_mode(SIZE)

    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    hor_borders = pygame.sprite.Group()
    ver_borders = pygame.sprite.Group()

    for i in range(10):
        Ball(20, HEIGHT // 2, WIDTH // 2)

    Border(IND, IND, WIDTH - IND, IND)
    Border(IND, IND, IND, HEIGHT - IND)

    Border(IND, HEIGHT - IND, WIDTH - IND, HEIGHT - IND)
    Border(WIDTH - IND, IND, WIDTH - IND, HEIGHT - IND)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(pygame.Color('white'))

        all_sprites.draw(screen)
        all_sprites.update()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
