'''Authors - Elious, Shreya, Subhojit
   Date - 28/2/20
'''
from GaAs_kpath import *

##==============================================================================
def dot(i,j):
    '''Input - Two vectors i and j as lists or tuples
       Output - Dot product of the vectors'''
    s = 0
    for e in range(len(i)):
        s = s + i[e]*j[e]
    return s

##==============================================================================
