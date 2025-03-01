import pygame

def is_right_format(text: str):
    data = text.split()
    if len(data) != 2:
        return False

    if data[0].isdigit() and data[1].isdigit():
        return True
    return False

if __name__ == '__main__':
    user_input = input("Введите через пробел ширину и высоту окна: ")

    if not is_right_format(user_input):
        print("Неправильный формат ввода")
    else:
        size = width, height = list(map(int, user_input.split()))

        pygame.init()
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Крест")
        screen.fill((0, 0, 0))

        pygame.draw.line(screen, (255, 255, 255), (0, 0), size, width=5)
        pygame.draw.line(screen, (255, 255, 255), (0, height), (width, 0), width=5)

        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()