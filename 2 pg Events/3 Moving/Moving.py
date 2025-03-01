import pygame

SIZE = WIDTH, HEIGHT = 300, 300
SIDE = 100

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Перетаскивание')

    screen = pygame.display.set_mode(SIZE)

    running = True
    is_pressed = False
    x, y = 0, 0
    x_old, y_old = 0, 0
    x_rel, y_rel = 0, 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x < event.pos[0] < x + SIDE and y < event.pos[1] < y + SIDE:
                    is_pressed = True

            if event.type == pygame.MOUSEMOTION:
                if is_pressed:
                    x_rel, y_rel = event.rel
                    x += x_rel
                    y += y_rel

            if event.type == pygame.MOUSEBUTTONUP:
                is_pressed = False

        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, 'green', (x, y, SIDE, SIDE))
        pygame.display.flip()
    pygame.quit()
