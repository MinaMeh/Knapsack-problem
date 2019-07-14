
import numpy as np
from getData import getData
# Created by Massina feat Amine
def totalvalue(items, capacity):
    cap= capacity
    sol= np.zeros(len(items), dtype=int)
    tmp= np.zeros(len(items),dtype=int )
    gain=0
    while (cap>0 ):
        for i in range(len(items)):
            tmp[i]= items[i][1] * (cap // items[i][0])
        print(tmp)
        if np.array_equal(tmp,np.zeros(len(items))):
            break;
        indmax= np.argmax(tmp)
        print('indmax', indmax)
        gain= tmp[indmax]+gain
        if(sol[indmax] == 0):
            sol[indmax]= cap // items[indmax][0]
            cap= cap- sol[indmax]* items[indmax][0]
        print('solution',sol)
    return items, sol,gain
#test
test=getData("test.txt")
items, sol , gain =totalvalue(test[0],test[2])
print(items)
print(sol)
print(gain)

