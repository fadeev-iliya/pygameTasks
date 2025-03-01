import pygame

SIZE = WIDTH, HEIGHT = 501, 501

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('К щелчку')

    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    running = True
    x, y = WIDTH // 2, HEIGHT // 2
    x_targ, y_targ = x, y

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_targ, y_targ = event.pos

        dif_x, dif_y = x - x_targ, y - y_targ

        x -= dif_x / abs(dif_x) if dif_x != 0 else 0
        y -= dif_y / abs(dif_y) if dif_y != 0 else 0

        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 20)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
