#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import curses 

screen = curses.initscr() 
curses.noecho() 
curses.curs_set(0) 
screen.keypad(1) 

screen.addstr("This is a Sample Curses Script\n\n") 
while True: 
    event = screen.getch() 
    if event == ord("q"): break 
    elif event == curses.KEY_UP:
        screen.clear()
        screen.addstr("The user pressed UP")
    elif event == curses.KEY_DOWN:
        screen.clear()
        screen.addstr("The user pressed DOWN")
    
curses.endwin()
