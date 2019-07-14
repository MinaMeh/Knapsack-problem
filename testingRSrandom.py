import getData
import Greedy
import time
import random
import SimulatedAnnealingVf

# simulatedAnnealing(items,capacity,solinit,samplingSize,temperatureInit,coolingFactor, endingTemperature):
items,nb,capacity = getData.getData()
tempInit=1000
tempFinal=50
samplingSize=5
alpha=0.7
gain_rand,cap_left,solinit=SimulatedAnnealingVf.gen_random_sol(items,nb,capacity)
start1=time.time()

items_sorted,sol,evalu=SimulatedAnnealingVf.simulatedAnnealing(items,capacity,solinit,samplingSize,tempInit,alpha,tempFinal)
end1=time.time()
best_performance=[evalu,end1-start1]
bestParams=[samplingSize,tempInit,alpha,tempFinal]

print(' \n performance initiale ',best_performance,'\t la combinaison de paramtres',bestParams)


while (tempInit > 200 ):
    tempFinal=50
    continue1=1
    while (tempFinal < 500 and continue1==1):
        if (tempInit < tempFinal):
            continue1=0
        else:
            print('\n temp init',tempInit,'\t temp final',tempFinal)

            start1 = time.time()

            items_sorted, sol, evalu = SimulatedAnnealingVf.simulatedAnnealing(items, capacity, solinit, samplingSize, tempInit, alpha, tempFinal)

            end1 = time.time()
            performance = [evalu, end1 - start1]
            if (performance[0] > best_performance[0] or (performance[0]==best_performance[0] and performance[1]< best_performance[1])): ## meilleure performance trouvée
                print(' \n meilleure performance trouvée')
                bestParams = [samplingSize, tempInit, alpha, tempFinal]
                best_performance=performance
            tempFinal=tempFinal+100
    tempInit = tempInit - 100


print(' \n la meilleure performance est ',performance,'  \t la combinaison de parametres ',bestParams)
