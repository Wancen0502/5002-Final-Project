#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 10:01:11 2024

@author: wancenyang
"""
import LogIn
import tkinter as tk
window = tk.Tk()
window.title('Health Management System')
window.geometry("440x600+300+200")
window.resizable(True,True)


button_addFile = tk.Button(window,
                           text="Log in")
button_addFile.place(x = 50,y = 450,
                     width = 120, height = 40)

userName_addFile = tk.Label(window)

userName_addFile.place(x = 20,y = 200,
                     width = 120, height = 40,
                     )

window.mainloop()