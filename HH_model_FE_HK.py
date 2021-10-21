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
    g_Na = 120.0
    g_K  =  36.0
    g_L  =   0.3
    
    #potential in mV
    E_Na =  115
    E_K  = -12
    E_L  = 10.613
    
     
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


#tous les I 
#equa diff

    
"""
The ModelSimulation contains functions to test the model on different 
values by varying the values ​​for certain parameters.
"""
class TestModel : 
    
#fct main de démo 
#différents cas variations des paramètres 
#+
    