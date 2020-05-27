'''Authors - Elious, Shreya, Subhojit
   Date - 28/2/20
'''
from GaAs_parameters import *

##==============================================================================
def kpath(ini , fin , n):
    '''Input = ini-initial point of k-path, fin-final point of k-path,
               n = number of k-points required
       Output =  straight line starting from ini->fin kpoints in a dicionary'''
    r = [fin[i]-ini[i] for i in range(len(ini))]    #Generating vector Rf-Ri
    l = np.linspace(0,1,n)                  #uniformly spaced array from 0 to 1
    p = []                                  #empty array to store the k-points                
    for j in range(len(l)):
        p.append([ini[i] + l[j]*r[i] for i in range(len(ini))]) 
    return p

##==============================================================================
'''k-point paths'''
n = 501                                 #number of k-ponits required in the path
D = kpath([0,0,0], [2*np.pi/a,0,0], n)              #Generating the path Gamma-X
L = kpath([0,0,0], [np.pi/a,np.pi/a,np.pi/a], n)    #Generating the path Gamma-L

##==============================================================================

