# gui.py

import tkinter as tk
from tkinter import messagebox
import time
from game import shuffle_puzzle, move_piece, a_star_solver, manhattan_distance, check_win

# Função para atualizar a interface gráfica com o estado atual do puzzle
def update_puzzle(puzzle, buttons):
    for i in range(3):
        for j in range(3):
            value = puzzle[i][j]
            buttons[i][j].config(text=str(value) if value != 0 else "", state="normal" if value != 0 else "disabled")

# Função para mostrar as peças sendo movidas uma por vez
def show_solution(path, puzzle, buttons):
    for move in path:
        time.sleep(0.5)  # Pausa para mostrar cada movimento
        puzzle = move_piece(move[0], move[1], puzzle)
        update_puzzle(puzzle, buttons)  # Atualiza a interface a cada movimento

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

    # Botão "Resolver"
    solve_button = tk.Button(root, text="Resolver", width=10, height=2, command=lambda: solve_game(puzzle, buttons))
    solve_button.grid(row=3, column=0)

    root.mainloop()

# Função para resolver o puzzle
def solve_game(puzzle, buttons):
    path = a_star_solver(puzzle)
    if path:
        show_solution(path, puzzle, buttons)
    else:
        messagebox.showinfo("Não é possível resolver", "Não há solução para o puzzle!")

# Função para iniciar o jogo e embaralhar o puzzle
def start_game(puzzle, buttons, start_button):
    puzzle = shuffle_puzzle(puzzle)
    update_puzzle(puzzle, buttons)
    start_button.config(text="Recomeçar", command=lambda: start_game(puzzle, buttons, start_button))

def update_and_move(i, j, puzzle, buttons):
    puzzle = move_piece(i, j, puzzle)
    update_puzzle(puzzle, buttons)
    if check_win(puzzle):
        messagebox.showinfo("Você Ganhou!", "Parabéns, você resolveu o puzzle!")
