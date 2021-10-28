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
root.geometry('1000x700')


#Entry 

Cm_var =tk.StringVar()
gNa_var =tk.StringVar()
gK_var =tk.StringVar()
gLeak_var =tk.StringVar()
ENa_var =tk.StringVar()
EK_var=tk.StringVar()
ELeak_var=tk.StringVar()

def validate():
    ELeak_val=float(ELeak_var.get())
    EK_val = int(EK_var.get())
    ENa_val = int(ENa_var.get())
    gLeak_val = float(gLeak_var.get())
    gK_val = int(gK_var.get())
    gNa_val = int(gNa_var.get())
    Cm_val = int(Cm_var.get())
    hh.setParam(Cm_val,gNa_val,gK_val,gLeak_val,ENa_val,EK_val,ELeak_val)
    simPlot = hh.plotSimulation()
    canvas = plt.backends.backend_tkagg.FigureCanvasTkAgg(simPlot,master = root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=3,column=1)
    
#Cm
Cm_label = tk.Label(root, text = 'Cm')
Cm_label.grid(row=1,column=2)

Cm_var.set("1")
Cm_entry = tk.Entry(root,textvariable = Cm_var,width=3)
Cm_entry.grid(row=1,column=3)

#gNa
gNa_label = tk.Label(root, text = 'gNa')
gNa_label.grid(row=1,column=4)

gNa_var.set("120")
gNa_entry = tk.Entry(root,textvariable = gNa_var,width=3)
gNa_entry.grid(row=1,column=5)

#gK
gK_label = tk.Label(root, text = 'gK')
gK_label.grid(row=1,column=6)

gK_var.set("36")
gK_entry = tk.Entry(root,textvariable = gK_var,width=3)
gK_entry.grid(row=1,column=7)


#gLeak
gLeak_label = tk.Label(root, text = 'gLeak')
gLeak_label.grid(row=1,column=8)

gLeak_var.set("0.03")
gLeak_entry = tk.Entry(root,textvariable = gLeak_var,width=3)
gLeak_entry.grid(row=1,column=9)

#ENa
ENa_label = tk.Label(root, text = 'ENa')
ENa_label.grid(row=2,column=4)

ENa_var.set("115")
ENa_entry = tk.Entry(root,textvariable = ENa_var,width=3)
ENa_entry.grid(row=2,column=5)

#EK
EK_label = tk.Label(root, text = 'EK')
EK_label.grid(row=2,column=6)

EK_var.set("-12")
EK_entry = tk.Entry(root,textvariable = EK_var,width=3)
EK_entry.grid(row=2,column=7)

#ELeak
ELeak_label = tk.Label(root, text = 'ELeak')
ELeak_label.grid(row=2,column=8)

ELeak_var.set("10.6")
ELeak_entry = tk.Entry(root,textvariable = ELeak_var,width=3)
ELeak_entry.grid(row=2,column=9)

#Button
val_button = tk.Button(text ="Plot", command= validate)
save_button = tk.Button(text ="Save Plot", command= hh.savePlot)

val_button.grid(row=3,column=3)
save_button.grid(row=3,column=4)

#canvas
empty_canvas = tk.Canvas(root, bg="white", height=400, width=500)
empty_canvas.grid(row=3,column=1)

root.mainloop()
root.destroy()
