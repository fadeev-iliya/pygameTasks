import pygame

FPS = 60
SIZE = WIDTH, HEIGHT = 501, 501


def scale_points(points, center, scale_factor):
    x_c, y_c = center

    scaled_points = []
    for x, y in points:
        new_x = (x - x_c) * scale_factor + x_c
        new_y = (y - y_c) * scale_factor + y_c
        scaled_points.append((new_x, new_y))

    return scaled_points


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Вентилятор")
    clock = pygame.time.Clock()

    with open("points.txt", "r") as file:
        data = map(lambda x: str.replace(x, ",", "."), file.read().split(", "))
        points = list(map(lambda x: list(map(float, x[1:-1].split(";"))), data))
    points = list(map(lambda x: [x[0] + WIDTH // 2, (-x[1]) + HEIGHT // 2], points))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                    points = scale_points(points, (WIDTH // 2, HEIGHT // 2), 1.1)
                elif event.y < 0:
                    points = scale_points(points, (WIDTH // 2, HEIGHT // 2), 0.9)

        screen.fill((0, 0, 0))
        pygame.draw.polygon(screen, pygame.Color('white'), points, width=1)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
