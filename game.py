# game.py

import random
import heapq
import time

# Função de distância de Manhattan para a heurística
def manhattan_distance(puzzle):
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    distance = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0:
                goal_i, goal_j = divmod(puzzle[i][j] - 1, 3)
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

# Função para obter os movimentos válidos para o espaço vazio
def get_valid_moves(i, j):
    valid_moves = []
    if i > 0: valid_moves.append((-1, 0))  # Para cima
    if i < 2: valid_moves.append((1, 0))   # Para baixo
    if j > 0: valid_moves.append((0, -1))  # Para esquerda
    if j < 2: valid_moves.append((0, 1))   # Para direita
    return valid_moves

# Função A* para resolver o puzzle
def a_star_solver(start_puzzle):
    start = tuple(tuple(row) for row in start_puzzle)
    goal = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

    # Fila de prioridade (min-heap)
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start_puzzle), 0, start, None, None))  # (f(n), g(n), state, previous_state, move)
    visited = set()
    visited.add(start)

    came_from = {}
    cost_so_far = {start: 0}

    while open_list:
        _, g, current, previous, move = heapq.heappop(open_list)

        if current == goal:
            # Reconstruir caminho
            path = []
            while current in came_from:
                path.append(came_from[current][1])
                current = came_from[current][0]
            path.reverse()
            return path

        # Encontrar o espaço vazio
        empty_i, empty_j = [(x, y) for x in range(3) for y in range(3) if current[x][y] == 0][0]
        
        # Explorar os movimentos válidos
        for di, dj in get_valid_moves(empty_i, empty_j):
            ni, nj = empty_i + di, empty_j + dj
            new_puzzle = [list(row) for row in current]
            new_puzzle[empty_i][empty_j], new_puzzle[ni][nj] = new_puzzle[ni][nj], new_puzzle[empty_i][empty_j]
            new_puzzle = tuple(tuple(row) for row in new_puzzle)

            if new_puzzle not in visited:
                visited.add(new_puzzle)
                new_g = g + 1
                new_h = manhattan_distance(new_puzzle)
                heapq.heappush(open_list, (new_g + new_h, new_g, new_puzzle, current, (ni, nj)))
                came_from[new_puzzle] = (current, (ni, nj))
                cost_so_far[new_puzzle] = new_g

    return None  # Não há solução

def greedy_solver(start_puzzle):
    start = tuple(tuple(row) for row in start_puzzle)
    goal = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

    # Fila de prioridade (min-heap) baseada na heurística
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start_puzzle), start, None))
    visited = set()
    visited.add(start)

    came_from = {}

    while open_list:
        _, current, move = heapq.heappop(open_list)

        if current == goal:
            # Reconstruir caminho
            path = []
            while current in came_from:
                path.append(came_from[current][1])
                current = came_from[current][0]
            path.reverse()
            return path

        # Encontrar o espaço vazio
        empty_i, empty_j = [(x, y) for x in range(3) for y in range(3) if current[x][y] == 0][0]

        # Explorar os movimentos válidos
        for di, dj in get_valid_moves(empty_i, empty_j):
            ni, nj = empty_i + di, empty_j + dj
            new_puzzle = [list(row) for row in current]
            new_puzzle[empty_i][empty_j], new_puzzle[ni][nj] = new_puzzle[ni][nj], new_puzzle[empty_i][empty_j]
            new_puzzle = tuple(tuple(row) for row in new_puzzle)

            if new_puzzle not in visited:
                visited.add(new_puzzle)
                heapq.heappush(open_list, (manhattan_distance(new_puzzle), new_puzzle, (ni, nj)))
                came_from[new_puzzle] = (current, (ni, nj))

    return None  # Não há solução

def is_solvable(puzzle):
    # Converte o puzzle para uma lista unidimensional
    puzzle_flat = [item for row in puzzle for item in row if item != 0]
    inversions = 0
    
    # Conta o número de inversões
    for i in range(len(puzzle_flat)):
        for j in range(i + 1, len(puzzle_flat)):
            if puzzle_flat[i] > puzzle_flat[j]:
                inversions += 1
    
    # Se o número de inversões for par, o puzzle é resolvível
    return inversions % 2 == 0



# Função para embaralhar o puzzle
def shuffle_puzzle(puzzle):
    while True:
        for _ in range(100):  # Número de movimentos aleatórios
            empty_i, empty_j = [(x, y) for x in range(3) for y in range(3) if puzzle[x][y] == 0][0]
            valid_moves = get_valid_moves(empty_i, empty_j)
            move_i, move_j = random.choice(valid_moves)
            puzzle = move_piece(move_i, move_j, puzzle)
        
        if is_solvable(puzzle):  # Verifique se o puzzle é resolvível
            break
    
    return puzzle


# Função para mover uma peça no puzzle
def move_piece(i, j, puzzle):
    empty_i, empty_j = [(x, y) for x in range(3) for y in range(3) if puzzle[x][y] == 0][0]
    puzzle[empty_i][empty_j], puzzle[i][j] = puzzle[i][j], puzzle[empty_i][empty_j]
    return puzzle

# game.py

# Função para verificar se o puzzle foi resolvido
def check_win(puzzle):
    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    return puzzle == goal
