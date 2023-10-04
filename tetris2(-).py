import pygame
import random

pygame.init()

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
WINDOW_TITLE = "Tetris"
BACKGROUND_COLOR = (0, 0, 0)

GRID_WIDTH = 10
GRID_HEIGHT = 20
GRID_SIZE = 30

COLORS = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
]

SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[1, 1, 1], [0, 1, 0]],
]

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_TITLE)

class Tetromino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self):
        self.shape = list(zip(*reversed(self.shape)))

    def draw(self, surface):
        for row in range(len(self.shape)):
            for col in range(len(self.shape[0])):
                if self.shape[row][col]:
                    pygame.draw.rect(
                        surface,
                        self.color,
                        pygame.Rect(
                            (self.x + col) * GRID_SIZE,
                            (self.y + row) * GRID_SIZE,
                            GRID_SIZE,
                            GRID_SIZE,
                        ),
                    )

def check_collision(grid, tetromino):
    for row in range(len(tetromino.shape)):
        for col in range(len(tetromino.shape[0])):
            if tetromino.shape[row][col]:
                if (
                    tetromino.y + row >= GRID_HEIGHT
                    or tetromino.x + col < 0
                    or tetromino.x + col >= GRID_WIDTH
                    or grid[tetromino.y + row][tetromino.x + col]
                ):
                    return True
    return False

def clear_lines(grid):
    full_rows = []
    for row in range(GRID_HEIGHT):
        if all(grid[row]):
            full_rows.append(row)
    for row in full_rows:
        del grid[row]
        grid.insert(0, [0] * GRID_WIDTH)

def main():
    clock = pygame.time.Clock()
    grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    tetromino = Tetromino()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tetromino.move(-1, 0)
                    if check_collision(grid, tetromino):
                        tetromino.move(1, 0)
                if event.key == pygame.K_RIGHT:
                    tetromino.move(1, 0)
                    if check_collision(grid, tetromino):
                        tetromino.move(-1, 0)
                if event.key == pygame.K_DOWN:
                    tetromino.move(0, 1)
                    if check_collision(grid, tetromino):
                        tetromino.move(0, -1)
                if event.key == pygame.K_UP:
                    tetromino.rotate()
                    if check_collision(grid, tetromino):
                        tetromino.rotate()

        tetromino.move(0, 1)
        if check_collision(grid, tetromino):
            tetromino.move(0, -1)
            for row in range(len(tetromino.shape)):
                for col in range(len(tetromino.shape[0])):
                    if tetromino.shape[row][col]:
                        grid[tetromino.y + row][tetromino.x + col] = tetromino.color
            clear_lines(grid)
            tetromino = Tetromino()
            if check_collision(grid, tetromino):
                game_over = True

        window.fill(BACKGROUND_COLOR)
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                pygame.draw.rect(
                    window,
                    grid[row][col],
                    pygame.Rect(col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE),
                )

        tetromino.draw(window)
        pygame.display.flip()
        clock.tick(5)

    pygame.quit()

if __name__ == "__main__":
    main()


# Определение класса для тетромино
class Tetromino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self):
        self.shape = list(zip(*reversed(self.shape)))

    def draw(self, surface):
        for row in range(len(self.shape)):
            for col in range(len(self.shape[0])):
                if self.shape[row][col]:
                    pygame.draw.rect(
                        surface,
                        self.color,
                        pygame.Rect(
                            (self.x + col) * GRID_SIZE,
                            (self.y + row) * GRID_SIZE,
                            GRID_SIZE,
                            GRID_SIZE,
                        ),
                    )

import pygame
import random

pygame.init()

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
WINDOW_TITLE = "Tetris"
BACKGROUND_COLOR = (0, 0, 0)

GRID_WIDTH = 10
GRID_HEIGHT = 20
GRID_SIZE = 30

COLORS = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
]

SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[1, 1, 1], [0, 1, 0]],
]

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_TITLE)

class Tetromino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self):
        self.shape = list(zip(*reversed(self.shape)))

    def draw(self, surface):
        for row in range(len(self.shape)):
            for col in range(len(self.shape[0])):
                if self.shape[row][col]:
                    pygame.draw.rect(
                        surface,
                        self.color,
                        pygame.Rect(
                            (self.x + col) * GRID_SIZE,
                            (self.y + row) * GRID_SIZE,
                            GRID_SIZE,
                            GRID_SIZE,
                        ),
                    )

def check_collision(grid, tetromino):
    for row in range(len(tetromino.shape)):
        for col in range(len(tetromino.shape[0])):
            if tetromino.shape[row][col]:
                if (
                    tetromino.y + row >= GRID_HEIGHT
                    or tetromino.x + col < 0
                    or tetromino.x + col >= GRID_WIDTH
                    or grid[tetromino.y + row][tetromino.x + col]
                ):
                    return True
    return False

def clear_lines(grid):
    full_rows = []
    for row in range(GRID_HEIGHT):
        if all(grid[row]):
            full_rows.append(row)
    for row in full_rows:
        del grid[row]
        grid.insert(0, [0] * GRID_WIDTH)

def main():
    clock = pygame.time.Clock()
    grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    tetromino = Tetromino()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tetromino.move(-1, 0)
                    if check_collision(grid, tetromino):
                        tetromino.move(1, 0)
                if event.key == pygame.K_RIGHT:
                    tetromino.move(1, 0)
                    if check_collision(grid, tetromino):
                        tetromino.move(-1, 0)
                if event.key == pygame.K_DOWN:
                    tetromino.move(0, 1)
                    if check_collision(grid, tetromino):
                        tetromino.move(0, -1)
                if event.key == pygame.K_UP:
                    tetromino.rotate()
                    if check_collision(grid, tetromino):
                        tetromino.rotate()

        tetromino.move(0, 1)
        if check_collision(grid, tetromino):
            tetromino.move(0, -1)
            for row in range(len(tetromino.shape)):
                for col in range(len(tetromino.shape[0])):
                    if tetromino.shape[row][col]:
                        grid[tetromino.y + row][tetromino.x + col] = tetromino.color
            clear_lines(grid)
            tetromino = Tetromino()
            if check_collision(grid, tetromino):
                game_over = True

        window.fill(BACKGROUND_COLOR)
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                pygame.draw.rect(
                    window,
                    grid[row][col],
                    pygame.Rect(col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE),
                )

        tetromino.draw(window)
        pygame.display.flip()
        clock.tick(5)

    pygame.quit()

if __name__ == "__main__":
    main()



def draw_score_and_level(surface, score, level):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))
    surface.blit(score_text, (10, 10))
    surface.blit(level_text, (10, 50))

import pygame
import random

pygame.init()

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
WINDOW_TITLE = "Tetris"
BACKGROUND_COLOR = (0, 0, 0)

GRID_WIDTH = 10
GRID_HEIGHT = 20
GRID_SIZE = 30

COLORS = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
]

SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[1, 1, 1], [0, 1, 0]],
]

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_TITLE)

class Tetromino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self):
        self.shape = list(zip(*reversed(self.shape)))

    def draw(self, surface):
        for row in range(len(self.shape)):
            for col in range(len(self.shape[0])):
                if self.shape[row][col]:
                    pygame.draw.rect(
                        surface,
                        self.color,
                        pygame.Rect(
                            (self.x + col) * GRID_SIZE,
                            (self.y + row) * GRID_SIZE,
                            GRID_SIZE,
                            GRID_SIZE,
                        ),
                    )

def check_collision(grid, tetromino):
    for row in range(len(tetromino.shape)):
        for col in range(len(tetromino.shape[0])):
            if tetromino.shape[row][col]:
                if (
                    tetromino.y + row >= GRID_HEIGHT
                    or tetromino.x + col < 0
                    or tetromino.x + col >= GRID_WIDTH
                    or grid[tetromino.y + row][tetromino.x + col]
                ):
                    return True
    return False

def clear_lines(grid):
    full_rows = []
    for row in range(GRID_HEIGHT):
        if all(grid[row]):
            full_rows.append(row)
    for row in full_rows:
        del grid[row]
        grid.insert(0, [0] * GRID_WIDTH)

def main():
    clock = pygame.time.Clock()
    grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    tetromino = Tetromino()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tetromino.move(-1, 0)
                    if check_collision(grid, tetromino):
                        tetromino.move(1, 0)
                if event.key == pygame.K_RIGHT:
                    tetromino.move(1, 0)
                    if check_collision(grid, tetromino):
                        tetromino.move(-1, 0)
                if event.key == pygame.K_DOWN:
                    tetromino.move(0, 1)
                    if check_collision(grid, tetromino):
                        tetromino.move(0, -1)
                if event.key == pygame.K_UP:
                    tetromino.rotate()
                    if check_collision(grid, tetromino):
                        tetromino.rotate()

        tetromino.move(0, 1)
        if check_collision(grid, tetromino):
            tetromino.move(0, -1)
            for row in range(len(tetromino.shape)):
                for col in range(len(tetromino.shape[0])):
                    if tetromino.shape[row][col]:
                        grid[tetromino.y + row][tetromino.x + col] = tetromino.color
            clear_lines(grid)
            tetromino = Tetromino()
            if check_collision(grid, tetromino):
                game_over = True

        window.fill(BACKGROUND_COLOR)
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                pygame.draw.rect(
                    window,
                    grid[row][col],
                    pygame.Rect(col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE),
                )

        tetromino.draw(window)
        pygame.display.flip()
        clock.tick(5)

    pygame.quit()

if __name__ == "__main__":
    main()



def main():
    clock = pygame.time.Clock()
    grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    tetromino = Tetromino()
    game_over = False
    score = 0
    level = 1

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tetromino.move(-1, 0)
                    if check_collision(grid, tetromino):
                        tetromino.move(1, 0)
                if event.key == pygame.K_RIGHT:
                    tetromino.move(1, 0)
                    if check_collision(grid, tetromino):
                        tetromino.move(-1, 0)
                if event.key == pygame.K_DOWN:
                    tetromino.move(0, 1)
                    if check_collision(grid, tetromino):
                        tetromino.move(0, -1)
                if event.key == pygame.K_UP:
                    tetromino.rotate()
                    if check_collision(grid, tetromino):
                        tetromino.rotate()

        tetromino.move(0, 1)
        if check_collision(grid, tetromino):
            tetromino.move(0, -1)
            for row in range(len(tetromino.shape)):
                for col in range(len(tetromino.shape[0])):
                    if tetromino.shape[row][col]:
                        grid[tetromino.y + row][tetromino.x + col] = tetromino.color
            clear_lines(grid)
            tetromino = Tetromino()
            if check_collision(grid, tetromino):
                game_over = True

            # Увеличиваем счет и уровень
            score += 10
            if score % 100 == 0:
                level += 1

        window.fill(BACKGROUND_COLOR)
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                pygame.draw.rect(
                    window,
                    grid[row][col],
                    pygame.Rect(col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE),
                )

        tetromino.draw(window)
        draw_score_and_level(window, score, level)
        pygame.display.flip()
        clock.tick(level * 2)

    pygame.quit()

if __name__ == "__main__":
    main()
