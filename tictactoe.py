def valid_move(move,grid,player,previous_move,val,winner_list):
    if grid[move[0]][move[1]] != -1000:
        print('Invalid Move')
        return (False, grid)
    check_grid = [[set() for i in range(3)] for i in range(3)]

    for i in range(9):
        for j in range(9):
            check_grid[i//3][j//3].add(grid[i][j])

    x = move[0] // 3
    y = move[1] // 3
    if winner_list[x][y] is not None:
        print('Invalid Move')
        return (False, grid)

    px = previous_move[0] % 3
    py = previous_move[1] % 3

    if winner_list[px][py] is not None:
        previous_move = (-1,-1)

    if (x == px and y == py) or (previous_move[0] == -1):
        if val not in check_grid[x][y]:
            print('Valid Move')
            grid[move[0]][move[1]] = val
            return (True, grid)

    print('Invalid Move')
    return (False, grid)

def check_winner(winner_list, move, grid, player):
    x = move[0] // 3
    y = move[1] // 3
    x = x * 3
    y = y * 3
    flag = 0
    for j in range(3):
        s = 0
        for i in range(3):
            s += grid[x+j][y+i]
        if s == 15:
            winner_list[x//3][y//3] = player
            return (True, winner_list)
        if s < 0:
            flag = 1

    if flag == 0:
        winner_list[x // 3][y // 3] = -1
        return (False, winner_list)

    for i in range(3):
        s = 0
        for j in range(3):
            s += grid[x+j][y+i]
        if s == 15:
            winner_list[x//3][y//3] = player
            return (True, winner_list)
    if grid[x][y] + grid[x+1][y+1] + grid[x+2][y+2] == 15 or grid[x+2][y] + grid[x+1][y+1] + grid[x][y+2] == 15:
        winner_list[x//3][y//3] = player
        return (True, winner_list)
    return (False, winner_list)


def check_final_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None and board[i][0] != -1:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None and board[0][i] != -1:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None and board[0][0] != -1:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None  and board[0][2] != -1:
        return board[0][2]
