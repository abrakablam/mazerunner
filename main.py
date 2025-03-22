from graphics import Window
from maze import Maze
import sys

def main():
    num_rows = 12
    num_columns = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_columns
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_columns, cell_size_x, cell_size_y, win, 10)
    print("Maze created")

    is_solvable = maze.solve()

    if not is_solvable:
        print("The maze cannot be solved, whoops.")
    else:
        print("Maze has been solved!")
    win.wait_for_close()


if __name__ == "__main__":
    main()

