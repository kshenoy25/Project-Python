import curses
from curses import wrapper
import queue
import time


maze = [
    ["#", "#", "#", "#", "#", "#", "O", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze, stdscr, path=[]):
    GREEN = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):  # gives the index and the value
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j * 2, "X", RED)
            else:
                stdscr.addstr(i, j * 2, value, GREEN)


def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j

    return None


def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set() # all the positions currently visited

    while not q.empty():
        current_pos, path = q.get() # get the element at the front of the queue
        row, col = current_pos # find neighbors of the position

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col] == end:
            return path

        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor
            if maze[r][c] == "#":
                continue

            new_path = path + [neighbor] # tacking the neighbor on to the current path
            q.put((neighbor, new_path))
            visited.add(neighbor) # to avoid processing multiple times

def find_neighbors(maze, row, col):
    neighbors = []

    if row > 0: # going up
        neighbors.append((row - 1, col))
    if row + 1 < len(maze): # going down
        neighbors.append((row + 1, col))
    if col > 0: # going left
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]): # going right
        neighbors.append((row, col + 1))

    return neighbors


def main(stdscr):

    # initialize color
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    #blue_and_black = curses.color_pair(1)


    find_path(maze, stdscr)
    stdscr.getch() # get character similar to an input statement waiting for the user

wrapper(main) # initializes the curses module