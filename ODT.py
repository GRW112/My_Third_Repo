#!/usr/bin/env python
# coding: utf-8

# In[96]:


# Hello Repository!!! It's me again!

import numpy as np
import math as m
from qutip import *
import matplotlib.pyplot as plt

class atomTrap:
    def __init__(self,m,ω1,ω2,Γ1,Γ2,ΔFS,P,w0):
       
        c = 3*10**8
        λ = (1070*10**-9)
        ωtrap = 2*np.pi*c/λ
        
        self.mass = m
        self.resfreq = (ω1 + 2*ω2)/3
        self.detuning = ωtrap - ((ω1 + 2*ω2)/3)
        self.line = (Γ1 + Γ2)/2
        self.FSsplit = ΔFS
        
        self.TrapPower = P
        self.TrapWaist = w0

        
    
    def gaussianbeam(self,x,x0,σ):
        c = 3*10**8
        Intensity = (2*self.TrapPower)/(m.pi*self.TrapWaist**2)
        U0 = (np.pi*c**2*self.line)/(2*self.resfreq**2*self.detuning)
        return U0*Intensity*np.exp(-(x-x0)**2 / (2*σ**2)) 


# In[97]:


Rbm = 1.44316*10**-25
Rbω1 = 2*m.pi*377.107463380*10**12
Rbω2 = 2*m.pi*384.2304844685*10**12
RbΓ1 = 2*m.pi*5.75*10**6
RbΓ2 = 2*m.pi*6.0666*10**6
RbΔFS = 2*m.pi*7.1230210885*10**12
Pwr = 1
waist = 100*10**-6


RbTrap_param = np.array([Rbm,Rbω1,Rbω2,RbΓ1,RbΓ2,RbΔFS,Pwr,waist])
RbTrap = atomTrap(Rbm,Rbω1,Rbω2,RbΓ1,RbΓ2,RbΔFS,Pwr,waist)


# In[59]:


#list([RbTrapparam[x] for x in list(range(0,len(RbTrap_param)))])


# In[60]:


#list([RbTrapparam[x] for x in list(range(0,len(RbTrap_param)))])


# In[101]:


xx = np.linspace(-10,10,100)
yvals = RbTrap.gaussianbeam(xx,0,3)
plt.plot(xx,yvals)


# In[76]:


RbTrap.mass


# In[ ]:
