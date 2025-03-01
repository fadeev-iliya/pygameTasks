import pygame

if __name__ == '__main__':
    user_input = input("Введите кол-во эллипсов: ")

    if not user_input.isdigit():
        print("Неправильный формат ввода")
    else:
        n = int(user_input)

        pygame.init()
        pygame.display.set_caption('Сфера')
        screen = pygame.display.set_mode((300, 300))

        screen.fill((0, 0, 0))
        step = 150 // n
        for a in range(0, n):
            pygame.draw.ellipse(screen, (255, 255, 255), (a * step, 0, 300 - a * 2 * step, 300), 1)
            pygame.draw.ellipse(screen, (255, 255, 255), (0, a * step, 300, 300 - a * 2 * step), 1)

        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()