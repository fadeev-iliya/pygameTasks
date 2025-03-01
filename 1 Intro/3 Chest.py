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
        pygame.init()
        pygame.display.set_caption('Шахматная клетка')
        side, num = list(map(int, user_input.split()))

        screen = pygame.display.set_mode((side, side))

        screen.fill((0, 0, 0))
        cell = side / num

        colors = [(255, 255, 255), (0, 0, 0)]
        if num % 2:
            colors.reverse()

        for x in range(num):
            for y in range(num):
                color = colors[(x + y) % 2]
                pygame.draw.rect(screen, color, (x * cell, y * cell, cell, cell))

        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
