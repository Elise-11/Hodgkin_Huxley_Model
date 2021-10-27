#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 09:54:21 2021

@author: fabre
"""
import HH_EF_KH_controller as hh
import tkinter as tk
import matplotlib as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Plot 
def plot():
    canvas = plt.backends.backend_tkagg.FigureCanvasTkAgg(hh.plotSimulation(),master = root)
    canvas.draw()
    canvas.get_tk_widget().pack()


root = tk.Tk()
root.title('Hodgkin_Huxley Model Simulation')
root.geometry('700x500')

#Button
show_button = tk.Button(text ="Show", command= plot)
save_button = tk.Button(text ="Save", command= hh.savePlot)

show_button.pack(side='bottom')
save_button.pack(side='bottom')


Cm_txt = int()
Cm_var = Entry(root, textvariable = Cm_txt, width=30)
ligne_texte.pack(side = "top")


#Param
# Cm_slider_axis = plt.axes([0.1, 0.15, 0.65, 0.03], facecolor=axis_color)
# Cm_slider = Slider(I_slider_axis, '$I_{ext}$ ', 0.0, 7., valinit=I_init)

# gNa_slider_axis = plt.axes([0.1, 0.1, 0.17, 0.03], facecolor=axis_color)
# gNa_slider = Slider(
# gNa_slider_axis, '$g_{Na}$ ', 80., 160., valinit=g_Na_init)

# gK_slider_axis = plt.axes([0.34, 0.1, 0.17, 0.03], facecolor=axis_color)
# gK_slider = Slider(gK_slider_axis, '$g_{K}$ ', 0., 70., valinit=g_K_init)

# gLeak_slider_axis = plt.axes([0.58, 0.1, 0.17, 0.03], facecolor=axis_color)
# gLeak_slider = Slider(
# gLeak_slider_axis, '$g_{Leak}$ ', 0., 1., valinit=g_Leak_init)

# ENa_slider_axis = plt.axes([0.1, 0.05, 0.17, 0.03], facecolor=axis_color)
# ENa_slider = Slider(
# ENa_slider_axis, '$E_{Na}$ ', 20., 80., valinit=E_Na_init)

# EK_slider_axis = plt.axes([0.34, 0.05, 0.17, 0.03], facecolor=axis_color)
# EK_slider = Slider(
# EK_slider_axis, '$E_{K}$ ', -100., -50., valinit=E_K_init)

# ELeak_slider_axis = plt.axes(
# [0.58, 0.05, 0.17, 0.03], facecolor=axis_color)
# ELeak_slider = Slider(
# ELeak_slider_axis, '$E_{Leak}$ ', -70, -40, valinit=E_Leak_init)

root.mainloop()
root.destroy()