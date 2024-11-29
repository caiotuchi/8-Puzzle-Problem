def check_win(puzzle):
    correct = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return puzzle == correct

def move_piece(i, j, puzzle):
    empty_i, empty_j = [(x, y) for x in range(3) for y in range(3) if puzzle[x][y] == 0][0]
    if (abs(empty_i - i) == 1 and empty_j == j) or (abs(empty_j - j) == 1 and empty_i == i):
        puzzle[empty_i][empty_j], puzzle[i][j] = puzzle[i][j], puzzle[empty_i][empty_j]
    return puzzle
