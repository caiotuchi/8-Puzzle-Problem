# main.py

from gui import create_gui

# Estado inicial do puzzle
puzzle = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Chama a interface gráfica
create_gui(puzzle)
