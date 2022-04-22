#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 20:50:20 2022

@author: priyankadas
"""

from tkinter import *
from tkmacosx import *

root = Tk()
root.title("ASCII")
root.geometry("400x400")

root.configure(background = "gold")
wrod = Entry(root) 
wrod.place(relx = 0.5, rely = 0.2, anchor = CENTER)
name = Label(root, text = "Text in ASCII \n", bg = "orange", fg = "black")
name.place(relx = 0.5, rely = 0.7, anchor = CENTER)
name1 = Label(root, text = "Encrypted Text \n", bg = "red", fg = "black")
name1.place(relx = 0.5, rely = 0.8, anchor = CENTER)


def converter():
    input = wrod.get()
    for i in input:
        name["text"] += str(ord(i)) + " "
        name1["text"] += chr(ord(i) + 1)
   
        
btn = Button(root, text = "Convert to ASCII", command = converter, fg = "black")
btn.place(relx = 0.5, rely = 0.4, anchor = CENTER)


root.mainloop()

#8.6/10