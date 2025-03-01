import pygame

SIZE = WIDTH, HEIGHT = 300, 300


def is_right_format(text: str):
    data = text.split()
    if len(data) != 2:
        return False
    if not (data[0].isdigit() and data[1].isdigit()):
        return False

    side, hue = map(int, data)
    if side % 4 != 0 or side > 100 or 0 > hue or hue > 360:
        return False
    return True


if __name__ == '__main__':
    user_input = input("Введите через пробел сторону куба и hue: ")

    if not is_right_format(user_input):
        print("Неправильный формат ввода")
    else:
        side, hue = map(int, user_input.split())

        pygame.init()
        pygame.display.set_caption('Куб')
        screen = pygame.display.set_mode(SIZE)

        x = 150 - side * 0.75
        y = 150 - side / 4
        half_side = side / 2

        color_front = pygame.Color('white')
        color_upper = pygame.Color('white')
        color_side = pygame.Color('white')
        hsv = pygame.Color('white').hsva

        color_front.hsva = (hue, hsv[1] + 100, hsv[2] - 25, hsv[3])
        color_upper.hsva = (hue, hsv[1] + 100, hsv[2], hsv[3])
        color_side.hsva = (hue, hsv[1] + 100, hsv[2] - 50, hsv[3])

        pygame.draw.polygon(screen, color_front, ((x, y), (x + side, y), (x + side, y + side), (x, y + side)))
        pygame.draw.polygon(screen, color_upper, (
            (x + half_side, y - half_side), (x + half_side + side, y - half_side), (x + side, y), (x, y)))
        pygame.draw.polygon(screen, color_side, (
            (x + side, y), (x + half_side + side, y - half_side), (x + half_side + side, y + half_side),
            (x + side, y + side)))

        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
