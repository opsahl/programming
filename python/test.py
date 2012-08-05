import curses

myscreen = curses.initscr()

myscreen.border(0)
myscreen.addstr(22, 70, "Python curses in action!")
myscreen.refresh()
myscreen.getch()

curses.endwin()
