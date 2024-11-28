import pygame
import sys

pygame.init()

WINDOW_SIZE = 900
GRID_SIZE = WINDOW_SIZE // 3
SUBGRID_SIZE = GRID_SIZE // 3
BACKGROUND_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
GRID_COLORS = [[(200,200,200) for _ in range(9)] for _ in range(9)]

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + 100))
pygame.display.set_caption("Number TicTacToe")

# Function to draw the grid lines
def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (i * GRID_SIZE, 0), (i * GRID_SIZE, WINDOW_SIZE), 2)
        pygame.draw.line(screen, LINE_COLOR, (0, i * GRID_SIZE), (WINDOW_SIZE, i * GRID_SIZE), 2)

    for i in range(1, 9):
        if i % 3 == 0:
            continue
        pygame.draw.line(screen, LINE_COLOR, (i * SUBGRID_SIZE, 0), (i * SUBGRID_SIZE, WINDOW_SIZE), 1)
        pygame.draw.line(screen, LINE_COLOR, (0, i * SUBGRID_SIZE), (WINDOW_SIZE, i * SUBGRID_SIZE), 1)

# Function to update selected grids
def update_selected_grid(red, black, blue, gray):
    for i in range(9):
        for j in range(9):
            GRID_COLORS[i][j] = (200, 200, 200)
    for (i, j) in gray:
        GRID_COLORS[i][j] = (150, 150, 150)
    for (i, j) in red:
        GRID_COLORS[i][j] = (255, 127, 127)
    for (i, j) in blue:
        GRID_COLORS[i][j] = (173, 216, 230)
    for (i, j) in black:
        GRID_COLORS[i][j] = (100, 100, 100)

# Function to draw colored grids
def draw_colored_grids():
    for i in range(9):
        for j in range(9):
            pygame.draw.rect(screen, GRID_COLORS[i][j], (j * SUBGRID_SIZE, i * SUBGRID_SIZE, SUBGRID_SIZE, SUBGRID_SIZE))

# Function to draw numbers on the grids
def draw_numbers(grid):
    font = pygame.font.Font(None, 36)
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                text = font.render(str(grid[i][j]), True, (0, 0, 0))
                text_rect = text.get_rect(center=(j * SUBGRID_SIZE + SUBGRID_SIZE // 2, i * SUBGRID_SIZE + SUBGRID_SIZE // 2))
                screen.blit(text, text_rect)

# Function to handle keyboard input
def handle_keyboard_input(event, grid):
    if pygame.K_1 <= event.key <= pygame.K_9:
        row, col = get_selected_cell(pygame.mouse.get_pos())
        val = int(pygame.key.name(event.key))
        return ((row, col), val)
    return (None, 0)

# Function to get selected cell
def get_selected_cell(pos):
    x, y = pos
    row = y // SUBGRID_SIZE
    col = x // SUBGRID_SIZE
    return row, col

# Function to display a text box
def display_text_box(message, x, y, width, height, font_size=30, color=(0, 0, 0)):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(message, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x + width // 2, y + height // 2)
    pygame.draw.rect(screen, BACKGROUND_COLOR, (x, y, width, height))
    screen.blit(text_surface, text_rect)

# Main game loop
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(BACKGROUND_COLOR)

        # Draw the grid lines
        draw_grid()

        # Draw the colored grids
        draw_colored_grids()

        # Draw the numbers
        # Replace `example_grid` with the grid you want to display


        # Display the text box
        display_text_box("This is a text box", 50, 900, 200, 50)

        # Update the display
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
