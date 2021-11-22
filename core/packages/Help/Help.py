import curses
from curses import wrapper
import time
import random

class Help:
    def __init__(self):
        """ Help Manual """

        wrapper(self.Help_Manual)
    
    def Help_Manual(self, stdscr):
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

        self.Display_Data(stdscr)

    def Display_Data(self, stdscr):
        stdscr.clear()
        stdscr.addstr("Welcome to the Seven Help Manual")
        stdscr.addstr("\nPress any key to begin!")
        stdscr.refresh()
        stdscr.getkey()

        print()

help = Help()