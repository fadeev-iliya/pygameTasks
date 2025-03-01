import pygame

SIZE = WIDTH, HEIGHT = 200, 200

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('Я слежу за тобой!')

    screen = pygame.display.set_mode(SIZE)

    running = True
    num = 1

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.ACTIVEEVENT and event.state == pygame.APPACTIVE and event.gain == 0:
                num += 1

        screen.fill((0, 0, 0))

        text = pygame.font.Font(None, 100).render(str(num), True, 'red')
        screen.blit(text, (100 - text.get_rect().width / 2, 100 - text.get_rect().height / 2))

        pygame.display.update()
        pygame.display.flip()
    pygame.quit()
