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
        pygame.display.set_caption("Прямоугольник")
        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, pygame.Color('red'), pygame.Rect(1, 1, width - 2, height - 2))

        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()