'''Authors - Elious, Shreya, Subhojit
   Date - 29/2/20-1/3/20
'''
from GaAs_Hamiltonian import *

##==============================================================================
'''Finding the eigenvalues along the k-paths'''
hd = []    #Empty list to store eigenvalues of the H-matrix along Gamma-X path
ED = {}    #Empty dictionry to store eigenvalues of each band along Gamma-X path
for d in D:
    '''Finding the eigenvalues along Gamma-X path'''
    hd.append(sorted(la.eig(Ham(d))[0].real))
for j in range(len(hd[0])):
    '''Categorising the different eigenvalues into different bands'''
    ED[j] = []
    for i in hd:
        ED[j].append(i[j])
        
hl = []   #Empty list to store eigenvalues of the H-matrix along Gamma-L path
EL = {}   #Empty dictionry to store eigenvalues of each band along Gamma-L path
for l in L:
    '''Finding the eigenvalues along Gamma-L path'''
    hl.append(sorted(la.eig(Ham(l))[0].real))
for j in range(len(hl[0])):
    '''Categorising the different eigenvalues into different bands'''
    EL[j] = []
    for i in hl:
        EL[j].append(i[j])

EB ={}  ##Empty dictionry to combine eigenvalues to give band along L-Gamma-X path
for i in range(len(ED.keys())):
    r = EL[i]
    r.reverse()
    EB[i] = r + ED[i]

##==============================================================================
'''Ploting the band structure'''    
xl = [-200,0,200]
my_xticks = ['L',r'$\Gamma$','x']
plt.figure()
plt.title('GaAs band-structure')
for i in range(len(ED.keys())):
    plt.plot([j for j in range(-len(hd),len(hd))],list(EB[i]))
plt.ylabel('Energy (eV) ----->')
plt.xlabel('K-path ----->')
plt.xticks(xl, my_xticks)
plt.show()

##==============================================================================
