# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 10:23:25 2025

@author: CB.EN.U4ECE24016
"""

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,100,1000)
t=np.linspace(-1,1,1000)

def sin(x,t):
    x1=np.sin(x)
    plt.plot(t,x1)
    plt.title("sin(x)")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
def cos(x,t):
    x1=np.cos(x)
    plt.plot(t,x1)
    plt.title("cos(x)")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
def exp(x,t):
    x1=np.exp(-x)
    plt.plot(t,x1)
    plt.title("exp(-x)")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
def x2(x,t):
    x1=x**2
    plt.plot(t,x1)
    plt.title("x^2")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    
plt.subplot(221)
sin(x,t)
plt.subplot(222)
cos(x,t)
plt.subplot(223)
exp(x,t)
plt.subplot(224)
x2(x,t)

plt.tight_layout()
plt.show()