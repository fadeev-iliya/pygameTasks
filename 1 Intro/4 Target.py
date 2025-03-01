import pygame


def is_right_format(text: str):
    data = text.split()
    if len(data) != 2:
        return False

    if data[0].isdigit() and data[1].isdigit():
        return True
    return False


if __name__ == '__main__':
    user_input = input("Введите через пробел сторону окна и кол-во клеток: ")

    if not is_right_format(user_input):
        print("Неправильный формат ввода")
    else:
        arc_width, num = list(map(int, user_input.split()))

        pygame.init()
        pygame.display.set_caption('Мишень')

        size = (2 * num * arc_width, 2 * num * arc_width)
        screen = pygame.display.set_mode(size)

        screen.fill((0, 0, 0))
        colors = ((255, 0, 0), (0, 255, 0), (0, 0, 255))

        for i in range(1, num + 1):
            color = colors[(i - 1) % 3]
            pygame.draw.circle(screen, color, (num * arc_width, num * arc_width), i * arc_width, arc_width)
            pygame.display.flip()

        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
