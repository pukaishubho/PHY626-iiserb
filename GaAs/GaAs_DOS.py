'''Authors - Elious, Shreya, Subhojit
   Date - 4/4/20'''

from GaAs_eigen_2 import *

##==============================================================================
Ev = []  #Empty list to store energy values at which the DOS is to be calculated
el = -13
while el<=6:
    Ev.append(el)
    el = el + 0.5

##==============================================================================
def Neigen(l,a,b):
    '''Takes in a list of eigenvalues and gives the number of eigenvalues
    within aeV and beV'''
    s = 0
    for i in l:
        if i < b and i>=a :
            s = s + 1
        else:
            continue
    return s

##==============================================================================
'''Finding the DOS'''
EBv = []  #Empty list to store the band index as in EB.keys() in GaAs_eigen_2.py
for i in list(EB.keys()):
    EBv = EBv + EB[i]
    
NEv = [Neigen(EBv,i-0.5,i) for i in Ev] #Finding the DOS at each energy in Ev

##==============================================================================
'''Plotting the DOS'''
plt.figure()
plt.title('GaAs DOS')
plt.plot(NEv,Ev)
plt.xlabel('DOS----->')
plt.ylabel('E(eV)----->')
plt.show()

##==============================================================================
    
