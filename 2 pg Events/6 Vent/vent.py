import math

import pygame

FPS = 60
SIZE = WIDTH, HEIGHT = 201, 201
ACCELERATION = 50 / FPS

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Вентилятор")
    clock = pygame.time.Clock()

    angle = -90
    running = True
    speed = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                 if event.button == 1:
                     speed -= ACCELERATION
                 elif event.button == 3:
                     speed += ACCELERATION

        screen.fill((0, 0, 0))
        angle += speed

        for flap_ang in range(0, 360, 120):
            left_angle = (angle - 15 + flap_ang) * math.pi / 180
            right_angle = (angle + 15 + flap_ang) * math.pi / 180

            xl = WIDTH // 2 + 70 * math.cos(left_angle)
            yl = HEIGHT // 2 + 70 * math.sin(left_angle)

            xr = WIDTH // 2 + 70 * math.cos(right_angle)
            yr = HEIGHT // 2 + 70 * math.sin(right_angle)

            pygame.draw.polygon(screen, pygame.Color('white'), ((WIDTH // 2, HEIGHT // 2), (xl, yl), (xr, yr)))

        pygame.draw.circle(screen, pygame.Color('white'), (WIDTH // 2, HEIGHT // 2), 10)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
