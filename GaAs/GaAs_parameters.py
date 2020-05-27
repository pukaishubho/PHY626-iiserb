'''Authors - Elious, Shreya, Subhojit
   Date - 28/2/20
'''
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la

##==============================================================================
'''Parameteres'''
a = float(input('Enter side length : '))                           #Angstrom
Vp = float(input('Enter mettalic energy for cation : '))           #eV
Vm = float(input('Enter mettalic energy for anion : '))            #eV
V2 = float(input('Enter covalent energy : '))                      #eV
V3 = float(input('Enter polar energy : '))                         #eV

##==============================================================================
'''basis coordinates'''
c = {i:[0,0,0] for i in range(4)}
c[4] = [1,1,1] ;c[5] = [-1,-1,1] ;c[6] = [1,-1,-1] ;c[7] = [-1,1,-1]

##==============================================================================
