import random
import time
import numpy as np

from getData import getData
# Created by Massina feat Amine


def generator(quantity, weight_range, value_range):
    tab = [[0 for x in range(2)] for y in range(quantity)]
    for j in range(0, quantity):
        tab[j][0] = random.randint(1, weight_range)
        tab[j][1] = random.randint(1, value_range)
    return tab


def greedy(tab, capacity=0):
    for i in range(0, len(tab)):
        tab[i].append(round(tab[i][1] / tab[i][0], 4))
    tab.sort(key=lambda x: x[2], reverse=True)
    #print(tab)
    used_capacity = 0
    new_tab = []
    while tab != []:
        nb = 0
        while used_capacity + tab[0][0] <= capacity:
            used_capacity += tab[0][0]
            nb += 1
        tab[0].append(nb)
        new_tab.append(tab[0])
        tab.pop(0)
    sol=[]
    gain_total = 0
    for i in range(0, len(new_tab)):
        new_tab[i].pop(2)
        gain_total += new_tab[i][1] * new_tab[i][2]
        if (new_tab[i][2]!=0):
            sol.append(new_tab[i])

    objects, solution=getObjectsSolution(tab, new_tab)
    return sol,new_tab, gain_total, used_capacity

def getObjectsSolution(items,solution):
    objects = []
    sol=[]
    for i in range(len(items)):
        if solution[i] != 0:
            objects.append(items[i])
            sol.append(solution[i])
    return objects, sol
def greedyH2(tab, capacity=0):
    for i in range(0, len(tab)):
        tab[i].append(round(tab[i][1] / tab[i][0], 4))
    tab.sort(key=lambda x: x[2], reverse=True)
    tab_couple = [];
    for i in range(len(tab) - 1):
        tab_couple.append([tab[i], tab[i + 1]])

   # print(tab_couple)
    used_capacity = 0
    new_tab = []
    tab_nb = np.zeros(len(tab))
    i = 0
    gain_total = 0
    objects=[]
    solutions=[]
    while tab_couple != [] and used_capacity < capacity:
        while (used_capacity + tab_couple[0][0][0] + tab_couple[0][1][0] <= capacity):
            used_capacity = used_capacity + tab_couple[0][0][0] + tab_couple[0][1][0]
            gain_total = gain_total + tab_couple[0][0][1] + tab_couple[0][1][1]
            tab_nb[i] += 1
            objects.append(tab_couple[0][0])
            objects.append(tab_couple[0][1])
            solutions.append(tab_nb[i])
            tab_nb[i + 1] += 1
            solutions.append(tab_nb[i+1])

        tab_couple.pop(0)
        i += 1

    return objects,solutions, gain_total, used_capacity
'''
NAME, WEIGHT, VALUE = range(3)

capacity= int(input("Donnez la capacité du sac à dos: "))
nbr= int(input("Donnez le nombre d'objets: "))
items= []
for i in range(nbr):
    weight=int(input("poids de l\'objet: "))
    value=int(input("valeur de l\'objet: "))
    items.append([weight,value])

print(items)
print (greedyH2(items,capacity))
'''


def greedyToInitRs(tab):
    result = []
    for items in tab:
        result.append(items[2])

    return result
## TEST
'''
#items,nb,cap= getData()
items= [[3, 10], [5, 3],[3,5]]
cap = 13
nb=len(items)
start = time.time()
tab,gain,used=greedy(items,cap)
end = time.time()
print(gain,"\t temps :",end-start)
print('tab solution de greedy est ',tab)
res=greedyToInitRs(tab)
print('le résultat formaté est',res)

'''
