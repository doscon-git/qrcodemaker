# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 10:08:27 2023

@author: AleksanderHykkerud
"""

import qrcode
import tkinter as tk
import os

BASE_PATH = os.path.dirname(__file__)
if not os.path.exists(os.path.join(BASE_PATH,"QRcodes")):
    os.mkdir(os.path.join(BASE_PATH,"QRcodes"))
# link = r""
# img = qrcode.make(link)
# img.save("safety_folder.png")

def create_qr_code(event):
    link = entryfield.get()
    filename = filenamefield.get()
    if filename == "" or link == "":
        print("Empty fields. Please enter link and filename")
        return False
    img = qrcode.make(link)
    if filename.split(".")[-1] != "png":
        filename += ".png"
    filepath = os.path.join(BASE_PATH,"QRcodes",filename)
    print("Saved to",filepath)
    img.save(filepath)
    entryfield.delete("0","end")
    filenamefield.delete("0","end")
    
mainwindow = tk.Tk()
tk.Label(text="Enter link: ").pack()
entryfield = tk.Entry(width=150)
entryfield.pack()
tk.Label(text="Enter image name: ").pack()
filenamefield = tk.Entry(width=100)
filenamefield.pack()
button = tk.Button(text="Create qrcode")
button.pack()
button.bind("<Button-1>",create_qr_code)

mainwindow.mainloop()



