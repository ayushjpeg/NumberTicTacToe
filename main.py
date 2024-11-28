from Graphics import (screen, BACKGROUND_COLOR, get_selected_cell, handle_keyboard_input, draw_grid, draw_numbers, draw_colored_grids,
                      update_selected_grid, display_text_box, show_popup_message)
from tictactoe import valid_move, check_winner, check_final_winner
import pygame, sys

grid = [[-1000 for _ in range(9)] for _ in range(9)]
winner_list = [[None, None, None],[None, None, None],[None, None, None]]

x_grids = []
o_grids = []
X = 'X'
gray = []
black =[]
running = True
move = (-1,-1)
previous_move = (-1,-1)
Message = "Welcome"
stop = False
t = None
while running:
    screen.fill(BACKGROUND_COLOR)
    display_text_box(Message, 300, 900, 300, 100,color=(100,100,220))
    display_text_box(str('Turn : '+X), 600, 900, 300, 100,color=(220,100,100))
    # pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:  # Left mouse button
                row, col = get_selected_cell(pygame.mouse.get_pos())
                print("Clicked on grid:", row, col)
                t = (row,col)
                black = [(row,col)]
                update_selected_grid(x_grids,black,o_grids,gray)
        elif event.type == pygame.KEYDOWN and not stop:
            val = handle_keyboard_input(event)
            if val is not None and t is not None:
                move = t
                flag, grid = valid_move(move,grid, X, previous_move,val,winner_list)
                if flag:
                    Message = 'Valid Move'
                    previous_move = move
                    flag2, winner_list = check_winner(winner_list,move, grid,X)
                    tx = move[0] % 3
                    ty = move[1] % 3
                    if winner_list[tx][ty] is None:
                        tx *= 3
                        ty *= 3
                        gray = [(tx,ty),(tx+1,ty),(tx+2,ty),(tx,ty+1),(tx+1,ty+1),(tx+2,ty+1),(tx,ty+2),(tx+1,ty+2),(tx+2,ty+2)]
                    else:
                        gray = []


                    if flag2:
                        tx = move[0]//3 * 3
                        ty = move[1]//3 * 3
                        Message = X + ' Won '+ str(tx//3+1) + ',' + str(ty//3+1) + ' Grid'
                        if X == 'X':
                            x_grids.append((tx,ty))
                            x_grids.append((tx+1, ty+1))
                            x_grids.append((tx+2, ty))
                            x_grids.append((tx, ty+2))
                            x_grids.append((tx+2, ty+2))
                        else:

                            o_grids.append((tx, ty))
                            o_grids.append((tx + 1, ty))
                            o_grids.append((tx + 2, ty))
                            o_grids.append((tx, ty + 2))
                            o_grids.append((tx + 1, ty + 2))
                            o_grids.append((tx + 2, ty + 2))
                            o_grids.append((tx, ty + 1))
                            o_grids.append((tx + 2, ty + 1))

                    update_selected_grid(x_grids, black, o_grids, gray)
                    if check_final_winner(winner_list):
                        show_popup_message('Game Over ' + X + ' Won')
                        stop = True
                    else:
                        for i in winner_list:
                            if None in i:
                                break
                        else:
                            show_popup_message('Draw')
                            stop = True
                    if X == 'X':
                        X = 'O'
                    else:
                        X = 'X'
                else:
                    Message = "Invalid Move"







    draw_colored_grids()
    draw_grid()
    draw_numbers(grid)

    pygame.display.flip()
pygame.quit()
sys.exit()