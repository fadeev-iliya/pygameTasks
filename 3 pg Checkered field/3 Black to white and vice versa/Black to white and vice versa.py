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
            for block in row:
                if block:
                    pygame.draw.rect(screen, pygame.Color('white'),
                                     (cell_left, cell_top, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(screen, pygame.Color('white'),
                                     (cell_left, cell_top, self.cell_size, self.cell_size), 1)
                cell_left += self.cell_size
            cell_top += self.cell_size
            cell_left = self.left

    def change(self, xp, yp):
        invert = lambda a: not a
        self.board[yp][xp] = invert(self.board[yp][xp])
        self.board[yp] = list(map(invert, self.board[yp]))
        for i in range(len(self.board)):
            self.board[i][xp] = invert(self.board[i][xp])


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Чёрное в белое и наоборот")
    screen = pygame.display.set_mode(SIZE)

    board = Board(5, 7)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col = (x - board.left) // board.cell_size
                row = (y - board.top) // board.cell_size
                if 0 <= col <= board.width - 1 and 0 <= row <= board.height - 1:
                    board.change(int(col), int(row))

        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()
