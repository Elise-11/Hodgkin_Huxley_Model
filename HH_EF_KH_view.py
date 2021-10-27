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


#setparam puis sim
#Plot 
def plot():
    #setParam(Cm_val,120,36,0.03,115,-12,10.6)
    #plot_show = hh.plotSimulation()
    canvas = plt.backends.backend_tkagg.FigureCanvasTkAgg(hh.plotSimulation(),master = root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=3,column=1)

#Button
show_button = tk.Button(text ="Show", command= plot)
save_button = tk.Button(text ="Save", command= hh.savePlot)


show_button.grid(row=3,column=2)
save_button.grid(row=3,column=3)

#canvas
empty_canvas = tk.Canvas(root, bg="white", height=400, width=500)
empty_canvas.grid(row=3,column=1)


#Entries and label 
#Cm
Cm_text= tk.StringVar()
Cm_text.set("Cm")
label_CM = tk.Label(root, textvariable=Cm_text, height=4)
label_CM.grid(row=1,column=2)

Cm_var =tk.StringVar()
Cm_entry = tk.Entry(root,textvariable = Cm_var,width=3)
Cm_entry.insert(0, "1")
Cm_entry.grid(row=1,column=3)
Cm_val = int(Cm_entry.get())

#gNa
gNa_text= tk.StringVar()
gNa_text.set("gNa")
label_gNa = tk.Label(root, textvariable=gNa_text, height=4)
label_gNa.grid(row=1,column=4)

gNa_var =tk.StringVar()
gNa_entry = tk.Entry(root,textvariable = gNa_var,width=3)
gNa_entry.insert(0, "120")
gNa_entry.grid(row=1,column=5)
gNa_val = int(gNa_entry.get())

#gK
gK_text= tk.StringVar()
gK_text.set("gK")
label_gK = tk.Label(root, textvariable=gK_text, height=4)
label_gK.grid(row=1,column=6)

gK_var =tk.StringVar()
gK_entry = tk.Entry(root,textvariable = gK_var,width=3)
gK_entry.insert(0, "36")
gK_entry.grid(row=1,column=7)
gK_val = int(gNa_entry.get())

#gLeak
gLeak_text= tk.StringVar()
gLeak_text.set("gLeak")
label_gLeak = tk.Label(root, textvariable=gLeak_text, height=4)
label_gLeak.grid(row=1,column=8)

gLeak_var =tk.StringVar()
gLeak_entry = tk.Entry(root,textvariable = gLeak_var,width=3)
gLeak_entry.insert(0, "0.03")
gLeak_entry.grid(row=1,column=9)
gLeak_val = int(gNa_entry.get())

#ENa
ENa_text= tk.StringVar()
ENa_text.set("ENa")
label_ENa = tk.Label(root, textvariable=ENa_text, height=4)
label_ENa.grid(row=2,column=4)

ENa_var =tk.StringVar()
ENa_entry = tk.Entry(root,textvariable = ENa_var,width=3)
ENa_entry.insert(0, "115")
ENa_entry.grid(row=2,column=5)
ENa_val = int(gNa_entry.get())

#EK
EK_text= tk.StringVar()
EK_text.set("EK")
label_EK = tk.Label(root, textvariable=EK_text, height=4)
label_EK.grid(row=2,column=6)

EK_var =tk.StringVar()
EK_entry = tk.Entry(root,textvariable = EK_var,width=3)
EK_entry.insert(0, "-12")
EK_entry.grid(row=2,column=7)
EK_val = int(gNa_entry.get())


#ELeak
ELeak_text= tk.StringVar()
ELeak_text.set("ELeak")
label_ELeak = tk.Label(root, textvariable=ELeak_text, height=4)
label_ELeak.grid(row=2,column=8)

ELeak_var =tk.StringVar()
ELeak_entry = tk.Entry(root,textvariable = ELeak_var,width=3)
ELeak_entry.insert(0, "10.6")
ELeak_entry.grid(row=2,column=9)
ELeak_val = int(gNa_entry.get())



# def validParam(): 
        
# validate_button = tk.Button(text ="Validate Parameters", command= validParam())
# validate_button.grid(row=4,column=1)

root.mainloop()
root.destroy()