'''Authors - Elious, Shreya, Subhojit
   Date - 28/2/20
'''
from GaAs_dot import *

##==============================================================================
'''The tight-binding hamiltonian matrix elements'''
def element(i,j,k):
    '''Input = ith row, jth column and the k-point
       Output = The H_ij element of the hamiltonian matrix'''
    if i == j and i<4:
        return V3*2
    elif i==j and i>3:
        return 0
    elif abs(i-j) == 4:
        return V2
    elif i<=3 and j <=3:
        return Vp
    elif i>=4 and j >=4:
        cr = [c[j][l]-c[i][l] for l in range(len(c[i]))]
        return Vm*np.exp(1j*dot(k,cr)*a/4)
    else:
        return 0

##==============================================================================
'''Tight-binding hamiltonian matrix'''
def Ham(k):
    '''Input = k-pont
       Output = The 8x8 Tight binding hamiltonian matrix for GaAs'''
    H = np.zeros((8,8),dtype=complex)                  #creating 8x8 null matrix 
    for i in range(8):
        for j in range(8):
            H[i][j] = element(i,j,k)        
    return H

##==============================================================================




