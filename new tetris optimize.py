import pygame
import random
import os

# Инициализация Pygame
pygame.init()

# Определение размера окна и цвета фона
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
GRID_COLOR = (50, 50, 50)

# Определение размера и цветов для блоков
BLOCK_SIZE = 30

# Определение пути к директории с текстурами
TEXTURE_DIR = os.path.join(os.path.dirname(__file__), "textures")

# Загрузка текстур блоков
BLOCK_TEXTURES = [
    pygame.image.load(os.path.join(TEXTURE_DIR, "tetris_long.png")),
    pygame.image.load(os.path.join(TEXTURE_DIR, "tetris_square.png")),
    pygame.image.load(os.path.join(TEXTURE_DIR, "tetris_s_1.png")),
    pygame.image.load(os.path.join(TEXTURE_DIR, "tetris_s_2.png")),                 # Нужно пофиксить слияние текстур фигур в одну кучу
    pygame.image.load(os.path.join(TEXTURE_DIR, "tetris_l_left.png")),
    pygame.image.load(os.path.join(TEXTURE_DIR, "tetris_l_right.png")),
    pygame.image.load(os.path.join(TEXTURE_DIR, "tetris_t.png")),
]

# Определение форм блоков
SHAPES = [
    [[1, 1, 1, 1]],              # I-форма
    [[1, 1], [1, 1]],            # O-форма
    [[1, 1, 0], [0, 1, 1]],      # Z-форма
    [[0, 1, 1], [1, 1, 0]],      # S-форма
    [[1, 0, 0], [1, 1, 1]],      # L-форма
    [[0, 0, 1], [1, 1, 1]],      # J-форма
    [[1, 1, 1], [0, 1, 0]],      # T-форма
]

# Определение начальной позиции фигуры
START_X = 4
START_Y = -1

# Создание игрового окна
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Тетрис")

clock = pygame.time.Clock()

# Создание класса для блока
class Block:
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color

    def draw(self):
        for row in range(len(self.shape)):
            for col in range(len(self.shape[0])):
                if self.shape[row][col]:
                    window.blit(BLOCK_TEXTURES[self.color], (self.x * BLOCK_SIZE + col * BLOCK_SIZE, self.y * BLOCK_SIZE + row * BLOCK_SIZE))

    def draw_shadow(self, grid):
        shadow_y = self.y
        while not self.check_collision(self.x, shadow_y + 1, self.shape, grid):
            shadow_y += 1

        for row in range(len(self.shape)):
            for col in range(len(self.shape[0])):
                if self.shape[row][col]:
                    window.blit(BLOCK_TEXTURES[0], ((self.x + col) * BLOCK_SIZE, (shadow_y + row) * BLOCK_SIZE))

    def move_down(self):
        self.y += 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def rotate(self):
        self.shape = list(zip(*reversed(self.shape)))

    def check_collision(self, x, y, shape, grid):
        for row in range(len(shape)):
            for col in range(len(shape[0])):
                if shape[row][col]:
                    if (
                        x + col < 0 or
                        x + col >= len(grid[0]) or
                        y + row >= len(grid) or
                        (y + row >= 0 and grid[y + row][x + col] is not None)
                    ):
                        return True
        return False

# Создание класса для игры
class TetrisGame:
    def __init__(self):
        self.grid = [[None] * (WINDOW_WIDTH // BLOCK_SIZE) for _ in range(WINDOW_HEIGHT // BLOCK_SIZE)]
        self.current_block = self.generate_block()
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.fall_speed = 1

    def generate_block(self):
        shape = random.choice(SHAPES)
        color = random.choice(range(1, len(BLOCK_TEXTURES)))
        return Block(START_X, START_Y, shape, color)

    def check_collision(self, x, y, shape):
        for row in range(len(shape)):
            for col in range(len(shape[0])):
                if shape[row][col]:
                    if (
                        x + col < 0 or
                        x + col >= len(self.grid[0]) or
                        y + row >= len(self.grid) or
                        (y + row >= 0 and self.grid[y + row][x + col] is not None)
                    ):
                        return True
        return False

    def place_block(self):
        for row in range(len(self.current_block.shape)):
            for col in range(len(self.current_block.shape[0])):
                if self.current_block.shape[row][col]:
                    self.grid[self.current_block.y + row][self.current_block.x + col] = self.current_block.color

    def clear_lines(self):
        lines_to_clear = []

        for row in range(len(self.grid)):
            if all(self.grid[row]):
                lines_to_clear.append(row)

        for row in lines_to_clear:
            del self.grid[row]
            self.grid.insert(0, [None] * (WINDOW_WIDTH // BLOCK_SIZE))

        return len(lines_to_clear)

    def increase_score(self, lines_cleared):
        self.score += lines_cleared * 100

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        window.blit(score_text, (WINDOW_WIDTH - score_text.get_width() - 10, 10))

    def update(self):
        if not self.check_collision(self.current_block.x, self.current_block.y + 1, self.current_block.shape):
            self.current_block.move_down()
        else:
            self.place_block()
            lines_cleared = self.clear_lines()
            self.increase_score(lines_cleared)

            if any(self.grid[0]):
                self.__init__()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not self.check_collision(self.current_block.x - 1, self.current_block.y, self.current_block.shape):
                        self.current_block.move_left()
                elif event.key == pygame.K_RIGHT:
                    if not self.check_collision(self.current_block.x + 1, self.current_block.y, self.current_block.shape):
                        self.current_block.move_right()
                elif event.key == pygame.K_DOWN:
                    if not self.check_collision(self.current_block.x, self.current_block.y + 1, self.current_block.shape):
                        self.current_block.move_down()
                elif event.key == pygame.K_SPACE:
                    rotated_shape = list(zip(*reversed(self.current_block.shape)))
                    if not self.check_collision(self.current_block.x, self.current_block.y, rotated_shape):
                        self.current_block.rotate()

    def draw_grid(self):
        for row in range(WINDOW_HEIGHT // BLOCK_SIZE):
            pygame.draw.line(window, GRID_COLOR, (0, row * BLOCK_SIZE), (WINDOW_WIDTH, row * BLOCK_SIZE))

        for col in range(WINDOW_WIDTH // BLOCK_SIZE):
            pygame.draw.line(window, GRID_COLOR, (col * BLOCK_SIZE, 0), (col * BLOCK_SIZE, WINDOW_HEIGHT))

    def draw_background(self):
        window.fill(BACKGROUND_COLOR)

    def draw(self):
        self.draw_background()
        self.draw_grid()

        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col]:
                    window.blit(BLOCK_TEXTURES[self.grid[row][col]], (col * BLOCK_SIZE, row * BLOCK_SIZE))

        for row in range(len(self.current_block.shape)):
            for col in range(len(self.current_block.shape[0])):
                if self.current_block.shape[row][col]:
                    if (
                        0 <= self.current_block.y + row < len(self.grid) and
                        0 <= self.current_block.x + col < len(self.grid[0]) and
                        self.grid[self.current_block.y + row][self.current_block.x + col] is None
                    ):
                        window.blit(BLOCK_TEXTURES[self.current_block.color], (self.current_block.x * BLOCK_SIZE + col * BLOCK_SIZE, self.current_block.y * BLOCK_SIZE + row * BLOCK_SIZE))

        self.current_block.draw_shadow(self.grid)
        self.draw_score()

    def run(self):
        while True:
            self.handle_input()
            self.update()
            self.draw()
            pygame.display.update()
            clock.tick(5 * self.fall_speed)

# Запуск игры
if __name__ == "__main__":
    game = TetrisGame()
    game.run()
