import pygame

pygame.init()


WINDOW_SIZE = 900
GRID_SIZE = WINDOW_SIZE // 3
SUBGRID_SIZE = GRID_SIZE // 3
BACKGROUND_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
GRID_COLORS = [[(200,200,200) for _ in range(9)] for _ in range(9)]

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + 100))
pygame.display.set_caption("Number TicTacToe")


def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (i * GRID_SIZE, 0), (i * GRID_SIZE, WINDOW_SIZE), 2)
        pygame.draw.line(screen, LINE_COLOR, (0, i * GRID_SIZE), (WINDOW_SIZE, i * GRID_SIZE), 2)

    for i in range(1, 9):
        if i % 3 == 0:
            continue
        pygame.draw.line(screen, LINE_COLOR, (i * SUBGRID_SIZE, 0), (i * SUBGRID_SIZE, WINDOW_SIZE), 1)
        pygame.draw.line(screen, LINE_COLOR, (0, i * SUBGRID_SIZE), (WINDOW_SIZE, i * SUBGRID_SIZE), 1)

def update_selected_grid(red,black,blue,gray):
    for i in range(9):
        for j in range(9):
            GRID_COLORS[i][j] = (200,200,200)
    for (i,j) in gray:
        GRID_COLORS[i][j] = (150, 150, 150)
    for (i,j) in red:
        GRID_COLORS[i][j] = (255, 127, 127)
    for (i,j) in blue:
        GRID_COLORS[i][j] = (173, 216, 255)
    for (i,j) in black:
        GRID_COLORS[i][j] = (100, 100, 100)


def draw_colored_grids():
    for i in range(9):
        for j in range(9):
            pygame.draw.rect(screen, GRID_COLORS[i][j], (j * SUBGRID_SIZE, i * SUBGRID_SIZE, SUBGRID_SIZE, SUBGRID_SIZE))


def draw_numbers(grid):
    font = pygame.font.Font(None, 36)
    for i in range(9):
        for j in range(9):
            if grid[i][j] != -1000:
                text = font.render(str(grid[i][j]), True, (0, 0, 0))
                text_rect = text.get_rect(center=(j * SUBGRID_SIZE + SUBGRID_SIZE // 2, i * SUBGRID_SIZE + SUBGRID_SIZE // 2))
                screen.blit(text, text_rect)


def handle_keyboard_input(event):
    if pygame.K_1 <= event.key <= pygame.K_9 :
        val = int(pygame.key.name(event.key))
        return val
    elif pygame.K_KP1 <= event.key <= pygame.K_KP9:
        return int(pygame.key.name(event.key)[1])
    return None


def get_selected_cell(pos):
    x, y = pos
    row = y // SUBGRID_SIZE
    col = x // SUBGRID_SIZE
    return row, col


def display_text_box(message, x, y, width, height, font_size=60, color=(0, 0, 0)):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(message, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x + width // 2, y + height // 2)
    pygame.draw.rect(screen, BACKGROUND_COLOR, (x, y, width, height))
    screen.blit(text_surface, text_rect)



def show_popup_message(message):
    # Create a font
    font = pygame.font.Font(None, 72)

    # Create a surface and render the message on it
    popup_surface = font.render(message, True, (0, 0,0))
    popup_rect = popup_surface.get_rect(center=(900 // 2, 900 // 2))

    # Blit the message surface onto the screen
    screen.blit(popup_surface, popup_rect)

    # Update the display
    pygame.display.update()

    # Wait for a few seconds
    pygame.time.wait(6000)