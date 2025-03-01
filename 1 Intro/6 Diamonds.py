import pygame

SIZE = WIDTH, HEIGHT = 300, 300

if __name__ == '__main__':
    user_input = input("Введите диагональ ромбиков: ")

    if not user_input.isdigit():
        print("Неправильный формат ввода")
    else:
        n = int(user_input)

        pygame.init()
        pygame.display.set_caption('Ромбики')

        screen = pygame.display.set_mode(SIZE)

        screen.fill(pygame.Color('yellow'))
        for x in range(WIDTH // n):
            for y in range(HEIGHT // n):
                pygame.draw.polygon(screen, pygame.Color('orange'), (
                    (x * n + n / 2, y * n), (x * n, y * n + n / 2), (x * n + n / 2, y * n + n),
                    (x * n + n, y * n + n / 2))
                                    )

        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
