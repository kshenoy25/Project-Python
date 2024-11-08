import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("Hello, world!")
    stdscr.refresh()

wrapper(main)