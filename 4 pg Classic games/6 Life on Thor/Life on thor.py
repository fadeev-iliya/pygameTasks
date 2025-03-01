import pygame

SIZE = WIDTH, HEIGHT = 1000, 1000


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.cell_size = 25
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
                color = pygame.Color('white') if block else pygame.Color('black')
                pygame.draw.rect(screen, color,
                                 (cell_left, cell_top, self.cell_size, self.cell_size))
                pygame.draw.rect(screen, pygame.Color('white'),
                                 (cell_left, cell_top, self.cell_size, self.cell_size), 1)
                cell_left += self.cell_size
            cell_top += self.cell_size
            cell_left = self.left

    def change(self, xp, yp):
        self.board[yp][xp] = 1 if self.board[yp][xp] == 0 else 0


class Life(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.running = False
        self.speed = 300

    def next_move(self):
        new_board = [[0] * self.width for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                live_neighbors = self.count_live_neighbors_torus(x, y)
                if self.board[y][x] == 1:
                    new_board[y][x] = 1 if live_neighbors in (2, 3) else 0
                else:
                    new_board[y][x] = 1 if live_neighbors == 3 else 0
        self.board = new_board

    def count_live_neighbors_torus(self, x, y):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for dx, dy in directions:
            nx = (x + dx) % self.width
            ny = (y + dy) % self.height
            count += self.board[ny][nx]
        return count

    def toggle_running(self):
        self.running = not self.running

    def adjust_speed(self, delta):
        self.speed = max(50, min(1000, self.speed + delta))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Игра «Жизнь» на торе")
    screen = pygame.display.set_mode(SIZE)

    board = Life(30, 30)
    clock = pygame.time.Clock()

    running = True
    last_move_time = pygame.time.get_ticks()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col = (x - board.left) // board.cell_size
                row = (y - board.top) // board.cell_size
                if 0 <= col <= board.width - 1 and 0 <= row <= board.height - 1:
                    if event.button == 1:
                        board.change(int(col), int(row))
                    elif event.button == 3:
                        board.toggle_running()
                    elif event.button == 4:
                        board.adjust_speed(-50)
                    elif event.button == 5:
                        board.adjust_speed(50)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    board.toggle_running()

        if board.running and pygame.time.get_ticks() - last_move_time >= board.speed:
            board.next_move()
            last_move_time = pygame.time.get_ticks()

        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
