import pygame

SIZE = WIDTH, HEIGHT = 500, 500


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.cell_size = 50
        self.left = WIDTH / 2 - width / 2 * self.cell_size
        self.top = HEIGHT / 2 - height / 2 * self.cell_size

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        cell_top = self.top
        cell_left = self.left
        for row in self.board:
            for _ in row:
                pygame.draw.rect(screen, pygame.Color('white'), (cell_left, cell_top, self.cell_size, self.cell_size),
                                 1)
                cell_left += self.cell_size
            cell_top += self.cell_size
            cell_left = self.left


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Инициализация игры")
    screen = pygame.display.set_mode(SIZE)

    board = Board(5, 7)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()

    pygame.quit()
