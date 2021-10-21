#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 18:23:37 2021

@author: fabre
"""

"""
The HHModel tracks conductances of 3 channels, depending on time and voltage, 
while keeping Vm at a fixed valu. 

The 3 channels are : 
    - Potassium channel 
    - Sodium channel 
    - leak channel
    
NA = sodium 
K = potassium 
L = Leak (leakage current ions)
"""

"""
The SquidModel class contains the differentiel equation of 
the Hodgkin and Huxley model and parameters. 
Default parameters are those taken from the original article
"""

import scipy as sp
import pylab as plt
from scipy.integrate import odeint

class SquidModel : 
    #membrane capacitance
    C_m  =   1
    
    #maximum conductances ms/cm^2
    g_Na = 120
    g_K  =  36
    g_L  =   0
    
    #potential in mV
    E_Na =  115
    E_K  = -12
    E_L  = 10.613
    
    #time 
    t = sp.arange(0.0, 450.0, 0.01)
    
    V = -65
    m = 0.05
    h = 0.6
    n = 0.32
        
     
    #voltage-dependent channel opening kinetics
    #equations from the initial paper (+cst)
    #sodium channels
    def alpha_n(self, V):
        return 0.01*(V+55.0)/(1.0 - sp.exp(-(V+55.0) / 10.0))
    
    #potassium chanel 
    def alpha_m(self, V):
        return 0.1*(V+40.0)/(1.0 - sp.exp(-(V+40.0) / 10.0))
    
    #potassium channel
    def alpha_h(self, V):
        return 0.07*sp.exp(-(V+65.0) / 20.0)
    
    
    #voltage-dependent channel closure kinetics
    def beta_n(self, V):
        return 0.125*sp.exp(-(V+65) / 80.0)
    
    def beta_m(self, V):
        return 4.0*sp.exp(-(V+65.0) / 18.0)

    def beta_h(self, V):
        return 1.0/(1.0 + sp.exp(-(V+35.0) / 10.0))
    
    #Sodium potential
    def Na_potential (self):
        gNa = self.g_Na * self.m **3 * self.h 
        return gNa
    
    #Sodium current
    def Na_current(self, V, m, h):
        gNa = self.Na_potential()
        I_Na = gNa * (V- self.E_Na)
        return I_Na
 
    #potassium potential
    def K_potential (self):
        gK = self.g_K * self.n**4 
        return gK
 
    #Potassium current 
    def K_current(self, V, n):
        gK = self.K_potential()
        I_K = gK * (V - self.E_K)
        return I_K
        
    #Leak current
    def Leak_current(self, V):
        I_L = self.g_L * (V - self.E_L)
        return I_L
    
    #??? 
    def I_inj(self, t):
        return 10*(t>100) - 10*(t>200) + 35*(t>300) - 35*(t>400)
    
    def total_current(self): 
        I_tot = self.K_current(self.V,self.n)+ self.Na_current(self.V, self.m,self.h)+ self.Leak_current(self.V)
        return I_tot 

    
    #activation equations 
    def dfdt(V, m, h, n , t, self):
        dVdt = (self.I_inj(t)-self.Na_current(V, m, h) - self.K_current(V, n) - self.Leak_current(V)) / self.C_m
        #sodium activation 
        dmdt = self.alpha_m(V)*(1-m) - self.beta_m(V)*m
        #sodium inactivation 
        dhdt = self.alpha_h(V)*(1-h) - self.beta_h(V)*h
        #potassium activation
        dndt = self.alpha_n(V)*(1-n) - self.beta_n(V)*n
        
        return dVdt, dmdt, dhdt, dndt

    def Main(self):
        #résoudre équation pour t varie ... (et avec h, m, n définits dans main)
        ina = self.Na_current(self.V, self.m, self.h)
        ik = self.K_current(self.V, self.n)
        il = self.Leak_current(self.V)
        
        #plot V 
        #plot conductances g 
        #plot courants I
        #plot I tot 


if __name__ == '__main__':
    runner = SquidModel()
    runner.Main()


    
"""
The ModelSimulation contains functions to test the model on different 
values by varying the values ​​for certain parameters.
"""
#class TestModel : 
    
#fct main de démo 
#différents cas variations des paramètres 
#
    