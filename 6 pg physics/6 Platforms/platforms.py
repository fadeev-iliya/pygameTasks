import pygame

SIZE = WIDTH, HEIGHT = 500, 500
FPS = 60


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 50

    def update(self, *args):
        self.rect.y += self.speed / FPS
        if pygame.sprite.spritecollideany(self, platforms):
            self.rect.y -= self.speed / FPS

    def move(self, dx):
        self.rect.x += dx
        if pygame.sprite.spritecollideany(self, platforms):
            self.rect.x -= dx


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.Surface((50, 10))
        self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect(topleft=(x, y))


if __name__ == '__main__':
    pygame.init()

    player = None
    platforms = pygame.sprite.Group()

    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Платформы")
    clock = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    platforms.add(Platform(*event.pos))
                elif event.button == 3:
                    player = Player(*event.pos)
            elif event.type == pygame.KEYDOWN and player:
                if event.key == pygame.K_LEFT:
                    player.move(-10)
                elif event.key == pygame.K_RIGHT:
                    player.move(10)

        screen.fill((0, 0, 0))
        if player:
            player.update()
            screen.blit(player.image, player.rect)
        platforms.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
