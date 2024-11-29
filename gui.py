import tkinter as tk
from tkinter import messagebox
import random
from puzzle_game import move_piece, check_win

# Função para embaralhar o puzzle
def shuffle_puzzle(puzzle):
    for _ in range(100):  # Número de movimentos aleatórios
        empty_i, empty_j = [(x, y) for x in range(3) for y in range(3) if puzzle[x][y] == 0][0]
        i, j = empty_i, empty_j
        # Gerar um movimento aleatório para mover uma peça
        valid_moves = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]  # Movimentos para baixo, cima, direita e esquerda
        valid_moves = [(x, y) for x, y in valid_moves if 0 <= x < 3 and 0 <= y < 3]
        move_i, move_j = random.choice(valid_moves)
        puzzle = move_piece(move_i, move_j, puzzle)
    return puzzle

# Função para atualizar a interface gráfica com o estado atual do puzzle
def update_puzzle(puzzle, buttons):
    for i in range(3):
        for j in range(3):
            value = puzzle[i][j]
            buttons[i][j].config(text=str(value) if value != 0 else "", state="normal" if value != 0 else "disabled")

# Função principal para criar a interface gráfica
def create_gui(puzzle):
    root = tk.Tk()
    root.title("8-Puzzle Game")
    
    buttons = [[None for _ in range(3)] for _ in range(3)]
    
    # Criar botões para cada peça
    for i in range(3):
        for j in range(3):
            value = puzzle[i][j]
            buttons[i][j] = tk.Button(root, text=str(value) if value != 0 else "", width=10, height=3,
                                      command=lambda i=i, j=j: update_and_move(i, j, puzzle, buttons))
            buttons[i][j].grid(row=i, column=j)

    # Botão "Começar" / "Recomeçar"
    start_button = tk.Button(root, text="Começar", width=10, height=2, command=lambda: start_game(puzzle, buttons, start_button))
    start_button.grid(row=3, column=1)

    root.mainloop()

# Função que inicia o jogo (embaralha e altera o texto do botão)
def start_game(puzzle, buttons, start_button):
    puzzle = shuffle_puzzle(puzzle)
    update_puzzle(puzzle, buttons)
    start_button.config(text="Recomeçar", command=lambda: reset_game(puzzle, buttons, start_button))

# Função que reinicia o jogo (reseta o puzzle para o estado inicial)
def reset_game(puzzle, buttons, start_button):
    puzzle = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    update_puzzle(puzzle, buttons)
    start_button.config(text="Recomeçar", command=lambda: start_game(puzzle, buttons, start_button))

def update_and_move(i, j, puzzle, buttons):
    puzzle = move_piece(i, j, puzzle)
    update_puzzle(puzzle, buttons)
    if check_win(puzzle):
        messagebox.showinfo("You Win!", "Congratulations, you've solved the puzzle!")

# Estado inicial do puzzle
puzzle = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

create_gui(puzzle)
