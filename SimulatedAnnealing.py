import math
import numpy as np
import Greedy
from getData import getData
import time
import random
# Created by Massina feat Amine
def trier_objet_utility(items ):
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    return items

def get_tab_gain_new(items_sorted, tab_max_nb):
    tab_gain = []
    for i in range(len(tab_max_nb)):
        tab= [items_sorted[i][1]]*tab_max_nb[i]
        tab_gain= tab_gain + tab 
    return tab_gain

def get_tab_poid_new(items_sorted, tab_max_nb):
    tab_poid = []
    for i in range(len(tab_max_nb)):
        tab= [items_sorted[i][0]]*tab_max_nb[i]
        tab_poid= tab_poid + tab 
    return tab_poid

def eval_solution(solution, tab_gain_new):
    gain_total= sum(np.array(solution)* np.array(tab_gain_new))
    return gain_total

def get_max_number_item(items, capacity=0):
    tab_number= [capacity//item[0] for item in items]
    return tab_number, sum(tab_number)

def ntobinary(nsol, max_num_tab):
    bsol=[]
    for i in range(len(max_num_tab)):
        for p in range(nsol[i]):
            bsol.append(1)
        for p in range(nsol[i], max_num_tab[i]):
            bsol.append(0)
    return bsol

def binaryToNsolution(solution, tab_max_nb):
    solN= []
    indMin=0
    for i in range(len(tab_max_nb)):
        indMax= indMin+tab_max_nb[i]
        solN.append(sum(solution[indMin:indMax]))
        indMin = indMax
    return solN

def cool(temprature, coolingFactor):
    return temprature* coolingFactor

def  getNeighbour(solution,taille, tab_poids_new, capacity):
    caprest=capacity-sum(np.array(solution)*np.array(tab_poids_new))
    np.random.seed()
    loop= True
    sol= solution
    while(loop):
        x = np.random.randint(taille)
        if sol[x] == 1:
            sol[x]=0
            caprest=caprest+tab_poids_new[x]
        else:
            if (tab_poids_new[x] < caprest ):
                sol[x]=1
        if sum(np.array(solution)*np.array(tab_poids_new)) <= capacity :
            loop= False
        else:
            sol= solution
    return sol



def getNextState( solution,taille,tab_poids_new, tab_gain_new, capacity, temperature):
        newSolution = getNeighbour(solution, taille, tab_poids_new, capacity);
        evalNewSol= eval_solution(newSolution,tab_gain_new)
        evalOldSol= eval_solution(solution,tab_gain_new)
        delta = evalNewSol - evalOldSol
        if (delta > 0):
            return newSolution
        else :
            x = np.random.rand()
            if (x < math.exp(delta / temperature)) :
                return newSolution
            else :
                return solution

def simulatedAnnealing(items,capacity,solinit,samplingSize,temperatureInit,coolingFactor, endingTemperature):
    for i in range(len(items)):
        items[i].append(solinit[i])
    items_sorted=trier_objet_utility(items)
   # print(items_sorted)
    solinitsorted=[]
    for i in range(len(items_sorted)):
        solinitsorted.append(items_sorted[i][2])
   # print(solinitsorted)
    tab_max_nb,taille= get_max_number_item(items_sorted, capacity)
    tab_poids_new= get_tab_poid_new(items_sorted, tab_max_nb)
    tab_gain_new= get_tab_gain_new(items_sorted,tab_max_nb)
    solCurrent= ntobinary(solinitsorted, tab_max_nb)
    evalsol= eval_solution(solCurrent,tab_gain_new)
        #print('eval sol de solution initale',evalsol)
    temperature= temperatureInit
    bestSol= solCurrent.copy()
    bestEval= evalsol
    while (temperature > endingTemperature):
        for i in range(samplingSize):

            #print('avant get nEXT state')
            solCurrent = getNextState(solCurrent,taille,tab_poids_new, tab_gain_new, capacity, temperature)
            #print('apres get next state')
            evalCurrent=eval_solution(solCurrent, tab_gain_new);
           # print('current_sol',solCurrent,binaryToNsolution(solCurrent,tab_max_nb),evalCurrent, 'best eval',bestEval, bestSol)
    
            if evalCurrent > bestEval:
                bestSol= solCurrent.copy()
                bestEval=evalCurrent
        temperature= cool(temperature, coolingFactor)
    #print(bestSol)
    Nsol= binaryToNsolution(bestSol, tab_max_nb)
    return items_sorted, Nsol, bestEval

#test
#items= [[3, 10], [5, 3],[3,5]]
#items= [[2,5],[3,2],[5,10],[7,20]]

#capacity=13
#nb=len(items)
#capacity = 13
#solinit=[2,0,1]

items,nb,capacity = getData()

start = time.time()
tab,gain,used=Greedy.greedy(items,capacity)
tab2=tab.copy()
end=time.time()
solinit=Greedy.greedyToInitRs(tab)
print('la solution initiale Greedy est ',solinit,'\n son gain est ',gain,'\t temps d execution',end -start)



#print('Gain Calculé dans le test est de \n ',gainTest)



items,nb,capacity = getData()
items= [[2,5],[3,2],[5,10],[7,20]]

capacity=20

start2=time.time()
items_sorted,sol,evalu=simulatedAnnealing(items,capacity,solinit,5,10,0.9,5)
end2=time.time()
print('Solution du RS ',sol,'\n son gain selon l algo :',evalu,' \t son temps d execution \n',end2 -start2)
gainTest=0
for i in range(0,nb):
    gainTest=gainTest + sol[i] *tab2[i][1]
print('le nouveau gain est ',gainTest)

def gen_random_sol(tab,n,capacity):
    weight=[]
    profits=[]
    capacityleft=capacity
    sol=[]
    gain=0
    for k in range(0,n):
        sol.append(0)
    for i in range(0, n):
        weight.append(tab[i][0])
        profits.append(tab[i][1])
    j=0
    while(j<n and capacityleft>0):
        index=random.randint(0,n-1)
        maxQuantity = int(capacityleft / weight[index]) + 1
        nbItems=random.randint(0,maxQuantity)
        sol[index]=nbItems
        capacityleft=capacityleft-weight[index]
        gain= gain + profits[index]
        j=j+1

    return gain,capacityleft,sol

#items= [[2,5],[3,2],[5,10],[7,20]]
#nb=len(items)
#cap=20
#gain,cap_left,solution=gen_random_sol(items,nb,cap)
#print('solution aléatoire :',solution,'capacite restante',cap_left,'gain = ',gain)