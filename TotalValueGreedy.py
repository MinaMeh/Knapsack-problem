import numpy as np
from getData import getData
# Created by Massina feat Amine
def totalvalue(items, capacity):
    cap= capacity
    sol= np.zeros(len(items), dtype='int64')
    tmp= np.zeros(len(items),dtype='int64' )
    gain=0
    objects=[]
    solution=[]
    while (cap>0 ):
        for i in range(len(items)):
            tmp[i]= items[i][1] * (cap // items[i][0])
        #print(tmp)
        if np.array_equal(tmp,np.zeros(len(items))):
            break;
        indmax= np.argmax(tmp)
        #print('indmax', indmax)
        gain= tmp[indmax]+gain
        if(sol[indmax] == 0):
            sol[indmax]= cap // items[indmax][0]
            if (sol[indmax]!=0):
                solution.append(sol[indmax])
                objects.append(items[indmax])
            cap= cap- sol[indmax]* items[indmax][0]
    return objects,solution, gain,capacity-cap,sol
'''#test
test=getData("test.txt")
items, sol , gain =totalvalue(test[0],test[2])
print(items)
print(sol)
print(gain)

'''