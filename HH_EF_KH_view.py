#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: fabre
"""
import HH_EF_KH_controller as hh
import tkinter as tk
import matplotlib as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#window
root = tk.Tk()
root.title('Hodgkin_Huxley Model Simulation')
root.geometry('900x700')

#setparam puis sim
#Plot 
def plot():
    #hh.setParam(entries....)
    canvas = plt.backends.backend_tkagg.FigureCanvasTkAgg(hh.plotSimulation(),master = root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=2,column=3)
    
#Button

show_button = tk.Button(text ="Show", command= plot)
save_button = tk.Button(text ="Save", command= hh.savePlot)


show_button.grid(row=4,column=3)
save_button.grid(row=4,column=4)


#canvas
empty_canvas = Canvas(root, bg="white", height=400, width=500)
empty_canvas.grid(row=2,column=3)

#Entries and label 
Cm_text=StringVar()
Cm_text.set("Cm")
label_CM = tk.Label(root, textvariable=Cm_text, height=4)
label_CM.grid(row=1,column=1)

Cm_entry = tk.Entry(root,width=3)
Cm_entry.insert(0, "1")
Cm_entry.grid(row=1,column=2)




root.mainloop()
root.destroy()