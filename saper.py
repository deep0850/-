import pygame
import random
import time

# Ініціалізація Pygame
pygame.init()

# Константи
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
NUM_MINES = 50
MINE_SIZE = WIDTH // GRID_SIZE

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)

# Ініціалізація екрану
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Сапер")

# Створення полів
field = [[0 for _ in range(MINE_SIZE)] for _ in range(MINE_SIZE)]
revealed = [[False for _ in range(MINE_SIZE)] for _ in range(MINE_SIZE)]

# Розставлення мін
mines = random.sample(range(MINE_SIZE * MINE_SIZE), NUM_MINES)
for mine in mines:
    row = mine // MINE_SIZE
    col = mine % MINE_SIZE
    field[row][col] = -1

# Функція для отримання кількості мін навколо клітинки
def count_mines(row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_row, new_col = row + i, col + j
            if 0 <= new_row < MINE_SIZE and 0 <= new_col < MINE_SIZE and field[new_row][new_col] == -1:
                count += 1
    return count

# Функція для розголошення всіх мін
def reveal_all_mines():
    for mine in mines:
        row = mine // MINE_SIZE
        col = mine % MINE_SIZE
        revealed[row][col] = True

# Головний цикл гри
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouseX, mouseY = event.pos
            row = mouseY // GRID_SIZE
            col = mouseX // GRID_SIZE

            if field[row][col] == -1:
                print("Game Over!")
                reveal_all_mines()  # Reveal all mines when a mine is clicked
                running = False
            else:
                revealed[row][col] = True


    # Відображення клітинок
    screen.fill(WHITE)
    for row in range(MINE_SIZE):
        for col in range(MINE_SIZE):
            rect = pygame.Rect(col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE)

            if revealed[row][col]:
                if field[row][col] == -1:
                    pygame.draw.rect(screen, (255, 0, 0), rect)  # Червона клітина для міни
                else:
                    pygame.draw.rect(screen, GRAY, rect)

                mines_around = count_mines(row, col)
                if mines_around > 0:
                    font = pygame.font.Font(None, 36)
                    text = font.render(str(mines_around), True, BLACK)
                    text_rect = text.get_rect(center=(rect.x + GRID_SIZE // 2, rect.y + GRID_SIZE // 2))
                    screen.blit(text, text_rect)
            else:
                pygame.draw.rect(screen, BLACK, rect)

    pygame.display.flip()

time.sleep(300)
pygame.quit()










