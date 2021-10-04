from tkinter import *
import numpy as np
from numpy.lib.function_base import append, place, select
import pygame
import sys, math
from connect4 import *
from connect4_with_ai import *

root = Tk()


root.title("Connect-4 Game")
root.geometry("700x800")

top_frame = Frame(root, width=max, height= 200)
top_frame.pack(side="top")

middel_frame = Frame(root, width= max, height= 600)
middel_frame.pack(side="top", pady=50)

title_labl = Label(top_frame, text="Connect 4 Game", fg="black", justify=CENTER, font=("Arial", 60))
title_labl.pack()

one_players_btn = Button(middel_frame, font=("Arial", 30), text="Single Player", command= lambda: single_player(var.get()), bg= "red", cursor= "arrow"
)
one_players_btn.pack()

two_players_btn = Button(middel_frame, font=("Arial", 30), text="Two Players", command= two_player, bg= "red", cursor= "arrow"
)
two_players_btn.pack()

var = IntVar()

R1 = Radiobutton(middel_frame, text="Easy", variable=var, value=1, font=("Arial", 30), justify= CENTER)
R1.select()
R1.pack( anchor = W)

R2 = Radiobutton(middel_frame, text="Normal", variable=var, value=3, font=("Arial", 30), justify= CENTER)
R2.deselect()
R2.pack( anchor = W)

R3 = Radiobutton(middel_frame, text="Hard", variable=var, value=5, font=("Arial", 30), justify= CENTER)
R3.deselect()
R3.pack( anchor = W)
Checkbutton.size= 30
root.mainloop()