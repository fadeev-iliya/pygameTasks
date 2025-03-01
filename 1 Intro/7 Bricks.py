import pygame

SIZE = WIDTH, HEIGHT = 300, 200

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Кирпичи')

    screen = pygame.display.set_mode(SIZE)
    screen.fill((255, 255, 255))

    for y in range(0, HEIGHT, 17):
        for x in range(0, WIDTH, 32):
            if y % 2 == 0:
                x -= 15
            pygame.draw.rect(screen, pygame.Color('red'), (x, y, 30, 15))

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
