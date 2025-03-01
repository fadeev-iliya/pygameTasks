import pygame

FPS = 60
SIZE = WIDTH, HEIGHT = 800, 600

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Вентилятор")
    clock = pygame.time.Clock()

    rects = []
    is_drawing = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    is_drawing = True
                    rects.append([*event.pos, *event.pos])
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    is_drawing = False

            if event.type == pygame.KEYDOWN:
                mods = pygame.key.get_mods()
                if event.key == pygame.K_z and (mods & pygame.KMOD_CTRL) and rects:
                    rects.pop(-1)

        screen.fill((0, 0, 0))

        if is_drawing:
            pos = pygame.mouse.get_pos()
            rects[-1] = [rects[-1][0], rects[-1][1], *pos]

        for x1, y1, x2, y2 in rects:
            width = min(x2 - x1, -10) if x2 - x1 < 0 else max(x2 - x1, 10)
            height = min(y2 - y1, -10) if y2 - y1 < 0 else max(y2 - y1, 10)
            pygame.draw.rect(screen, pygame.Color('white'), pygame.Rect(x1, y1, width, height), width=5,
                             border_radius=5)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
